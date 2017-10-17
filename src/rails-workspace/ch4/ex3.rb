test = :test
puts test


lang_hash = {
  'one': 'uno',
  'two': 'dos',
  'three': 'tres'
}

p lang_hash


lang_hash.each do | key, value |
  puts "#{key} in spanish is #{value}"
end


# https://www.upwork.com/i/interview-questions/ruby-on-rails/
