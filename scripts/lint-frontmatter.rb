#!/usr/bin/env ruby
require 'yaml'
require 'date'

exit_code = 0

ARGV.each do |file|
  next unless File.file?(file)
  
  content = File.read(file)
  # Check if file has YAML front matter
  if content =~ /\A(---\s*\n.*?\n?)^((---|\.\.\.)\s*$\n?)/m
    front_matter = $1
    begin
      YAML.safe_load(front_matter, permitted_classes: [Date, Time], aliases: true)
    rescue => e
      puts "❌ Error parsing YAML front matter in #{file}:"
      puts "   #{e.message}"
      exit_code = 1
    end
  end
end

if exit_code == 0
  puts "✅ All markdown files have valid YAML front matter."
end

exit exit_code
