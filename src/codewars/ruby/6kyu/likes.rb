'''

You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:

likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
For 4 or more names, the number in and 2 others simply increases.




'''


def likes(names)
  if names.empty?
    return 'no one likes this'
  elsif names.length == 1
    return "#{names[0]} likes this"
  elsif names.length == 2
    return "#{names[0]} and #{names[1]} like this"
  elsif names.length == 3
    return "#{names[0]}, #{names[1]} and #{names[2]} like this"
  elsif names.length >= 4
    return "#{names[0]}, #{names[1]} and #{names.length - 2} others like this"
  end
end


describe "likes" do

  context "given []" do
    it "returns 'no one likes this'" do
      expect(likes([])).to eql('no one likes this')
    end
  end

  context 'given ["Peter"]' do
    it 'returns "Peter likes this"' do
      expect(likes(['Peter'])).to eql('Peter likes this')
    end
  end

  context 'given ["Peter", "Alex"]' do
    it 'returns "Peter and Alex like this"' do
      expect(likes(['Peter', 'Alex'])).to eql('Peter and Alex like this')
    end
  end

  context 'given ["Peter", "Alex", "Max"]' do
    it 'returns "Peter, Alex and Max like this"' do
      expect(likes(['Peter', 'Alex', 'Max'])).to eql('Peter, Alex and Max like this')
    end
  end

  context 'given ["Peter", "Alex", "Max", "Keisuke"]' do
    it 'returns "Peter, Alex and 2 others like this"' do
      expect(likes(['Peter', 'Alex', 'Max', 'Keisuke'])).to eql('Peter, Alex and 2 others like this')
    end
  end

end
