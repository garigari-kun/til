
word_list = "foo bar    bax".split()
p word_list


puts word_list.join()
puts word_list.join(" ")
puts word_list.join(", ")

a = (0..9).to_a()
p a


(1..5).each { |i| puts 2 * i }


(1..5).each do |i|
  puts 2 * i
end



puts "-----------------------------"
(0..16).each do |i|
  puts i ** 2
end





def yeller(arr)
  new_arr = []
  arr.each do |ch|
    new_arr.push(ch.upcase())
  end
  return new_arr.join()
end


new_arr = yeller(['0', 'l', 'd'])
p new_arr


def random_subdomain()
  return (a..z).to_a.shuffle[0..7].join()
end  
