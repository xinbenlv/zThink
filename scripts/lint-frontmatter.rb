#!/usr/bin/env ruby
require 'yaml'
require 'date'

def validate_cover_image(file, data)
  cover_image = data['cover_image']
  return [] if cover_image.nil?

  errors = []
  unless cover_image.is_a?(Hash)
    return ["cover_image must be a mapping with src, x, y, and size"]
  end

  %w[src x y size].each do |key|
    errors << "cover_image.#{key} is required" unless cover_image.key?(key)
  end
  return errors unless errors.empty?

  unless cover_image['src'].is_a?(String) && !cover_image['src'].strip.empty?
    errors << "cover_image.src must be a non-empty string"
  end

  %w[x y size].each do |key|
    value = cover_image[key]
    unless value.is_a?(Integer)
      errors << "cover_image.#{key} must be an integer"
      next
    end
    if value < 0
      errors << "cover_image.#{key} must be >= 0"
    end
  end

  if cover_image['size'].is_a?(Integer) && cover_image['size'] <= 0
    errors << "cover_image.size must be > 0"
  end

  if cover_image['src'].is_a?(String) && cover_image['src'].start_with?('/assets/')
    asset_path = File.join(Dir.pwd, cover_image['src'].sub(%r{\A/}, ''))
    errors << "cover_image.src asset does not exist: #{cover_image['src']}" unless File.exist?(asset_path)
  end

  errors
end

exit_code = 0

ARGV.each do |file|
  next unless File.file?(file)
  
  content = File.read(file)
  # Check if file has YAML front matter
  if content =~ /\A(---\s*\n.*?\n?)^((---|\.\.\.)\s*$\n?)/m
    front_matter = $1
    begin
      data = YAML.safe_load(front_matter, permitted_classes: [Date, Time], aliases: true) || {}
      validate_cover_image(file, data).each do |error|
        puts "❌ Front matter validation failed in #{file}:"
        puts "   #{error}"
        exit_code = 1
      end
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
