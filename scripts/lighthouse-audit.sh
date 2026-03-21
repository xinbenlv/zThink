#!/bin/sh
set -eu

host="127.0.0.1"
port="${LIGHTHOUSE_PORT:-4179}"
strategy="mobile"
performance_threshold="${LIGHTHOUSE_PERFORMANCE_THRESHOLD:-70}"
quality_threshold="${LIGHTHOUSE_QUALITY_THRESHOLD:-100}"

for arg in "$@"; do
  case "$arg" in
    --strategy=*)
      strategy="${arg#*=}"
      ;;
  esac
done

repo_root="$(CDPATH= cd -- "$(dirname "$0")/.." && pwd)"
report_dir="$repo_root/tmp/ttl=7d"
budget_path="$repo_root/budget.json"
timestamp="$(date -u +"%Y-%m-%dT%H-%M-%S")"
report_path="$report_dir/lighthouse-$strategy-$timestamp.json"
summary_path="$report_dir/lighthouse-summary-$timestamp.json"
server_pid=""

cleanup() {
  if [ -n "$server_pid" ] && kill -0 "$server_pid" >/dev/null 2>&1; then
    kill "$server_pid" >/dev/null 2>&1 || true
    wait "$server_pid" 2>/dev/null || true
  fi
}

trap cleanup EXIT INT TERM

echo "Lighthouse Audit (local)" >&2
echo "Performance threshold: $performance_threshold" >&2
echo "Quality threshold (a11y/BP/SEO): $quality_threshold" >&2
echo "Strategies: $strategy" >&2
if [ -f "$budget_path" ]; then
  echo "Budget: $(basename "$budget_path")" >&2
fi

if ! command -v curl >/dev/null 2>&1; then
  echo "Audit failed: curl is required" >&2
  exit 1
fi

mkdir -p "$report_dir"

echo "Building site..." >&2
pages_repo_nwo="$(git config --get remote.origin.url 2>/dev/null | sed -E 's#.*github.com[:/]([^/]+/[^/.]+)(\\.git)?#\1#' || true)"
if [ -n "$pages_repo_nwo" ]; then
  export PAGES_REPO_NWO="$pages_repo_nwo"
fi
JEKYLL_ENV=production bundle exec jekyll build

(
  cd "$repo_root/_site"
  python3 -m http.server "$port" --bind "$host" >/tmp/zthink-lighthouse-server.log 2>&1
) &
server_pid="$!"

ready=0
for _ in $(seq 1 60); do
  if curl -fsS "http://$host:$port/" >/dev/null 2>&1; then
    ready=1
    break
  fi
  sleep 0.25
done

if [ "$ready" -ne 1 ]; then
  echo "Audit failed: static server did not become ready" >&2
  exit 1
fi

echo "Running Lighthouse ($strategy) against http://$host:$port/ ..." >&2

set -- \
  --yes \
  lighthouse \
  "http://$host:$port/" \
  --quiet \
  --output=json \
  "--output-path=$report_path" \
  --chrome-flags=--headless=new \
  --chrome-flags=--no-sandbox \
  --chrome-flags=--disable-gpu

if [ "$strategy" = "desktop" ]; then
  set -- "$@" --preset=desktop
fi

if [ -f "$budget_path" ]; then
  set -- "$@" "--budget-path=$budget_path"
fi

npx "$@"

LIGHTHOUSE_STRATEGY_LABEL="$(printf '%s' "$strategy" | tr '[:lower:]' '[:upper:]')" ruby - "$report_path" "$summary_path" "$performance_threshold" "$quality_threshold" "$budget_path" <<'RUBY'
require "json"

report_path, summary_path, perf_threshold, quality_threshold, budget_path = ARGV
report = JSON.parse(File.read(report_path))

summary = {
  "performance" => report.dig("categories", "performance", "score"),
  "accessibility" => report.dig("categories", "accessibility", "score"),
  "best-practices" => report.dig("categories", "best-practices", "score"),
  "seo" => report.dig("categories", "seo", "score"),
  "metrics" => {
    "fcp" => report.dig("audits", "first-contentful-paint", "numericValue"),
    "lcp" => report.dig("audits", "largest-contentful-paint", "numericValue"),
    "tbt" => report.dig("audits", "total-blocking-time", "numericValue"),
    "cls" => report.dig("audits", "cumulative-layout-shift", "numericValue"),
    "si" => report.dig("audits", "speed-index", "numericValue")
  }
}

File.write(summary_path, JSON.pretty_generate(summary))

def fmt_score(score)
  "#{(score.to_f * 100).round}/100"
end

puts
puts "  #{ENV.fetch("LIGHTHOUSE_STRATEGY_LABEL", "MOBILE")}:"
%w[performance accessibility best-practices seo].each do |key|
  score = summary[key]
  threshold = key == "performance" ? perf_threshold.to_i : quality_threshold.to_i
  pass = (score.to_f * 100).round >= threshold
  puts "  #{pass ? "✅" : "❌"} #{key.ljust(16)} #{fmt_score(score)} (threshold: #{threshold})"
end
puts
puts "  FCP #{summary.dig("metrics", "fcp").to_f.round}ms"
puts "  LCP #{summary.dig("metrics", "lcp").to_f.round}ms"
puts "  TBT #{summary.dig("metrics", "tbt").to_f.round}ms"
puts format("  CLS %.3f", summary.dig("metrics", "cls").to_f)
puts "  SI  #{summary.dig("metrics", "si").to_f.round}ms"
puts "  Report: #{report_path}"
puts "  Summary: #{summary_path}"

failures = []
%w[performance accessibility best-practices seo].each do |key|
  threshold = key == "performance" ? perf_threshold.to_i : quality_threshold.to_i
  failures << "#{key} #{fmt_score(summary[key])} < #{threshold}" if (summary[key].to_f * 100).round < threshold
end

if File.exist?(budget_path)
  budget = JSON.parse(File.read(budget_path))
  timings = budget.is_a?(Array) ? budget[0]["timings"] : budget["timings"]
  audit_map = {
    "first-contentful-paint" => summary.dig("metrics", "fcp"),
    "largest-contentful-paint" => summary.dig("metrics", "lcp"),
    "total-blocking-time" => summary.dig("metrics", "tbt"),
    "speed-index" => summary.dig("metrics", "si")
  }
  Array(timings).each do |item|
    actual = audit_map[item["metric"]]
    next unless actual
    failures << "#{item["metric"]} #{actual.round}ms > #{item["budget"]}ms budget" if actual > item["budget"].to_f
  end
end

if failures.empty?
  puts
  puts "✅ PASS"
else
  warn
  warn "❌ FAIL:"
  failures.each { |failure| warn "   - #{failure}" }
  exit 1
end
RUBY
