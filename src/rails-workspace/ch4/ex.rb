

# Returns the full title on a per-page basis
def full_title(page_title='')
  puts 'test'
end


full_title()
puts 17 + 42
puts ''
puts 'foo'
puts 'foo' + 'bar'

first_name = 'Tsukamoto'
puts first_name
puts "#{first_name} Keisuke"


city = 'Niigata city'
state = 'Niigata pref'
puts "#{city}, #{state}"


puts first_name.length
puts first_name.empty?

if first_name.empty?
  puts "The string is empty"
else
  puts "The string is not empty"
end


def string_message(str = "")
  if str.empty?
    return "It's an empty string!"
  else
    return "It's an not empty string"
  end
end



puts string_message("foobar")
puts string_message("")



def palindrome_tester(s)
  if s == s.reverse
    puts 'The string is palindrome'
  else
    puts 'The string is not palindrom'
  end
end


palindrome_tester("arc")
palindrome_tester("ara")


# https://www.railstutorial.org/book/rails_flavored_ruby
# http://ruby-for-beginners.rubymonstas.org/index.html
