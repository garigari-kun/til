=begin

When provided with a number between 0-9, return it in words.

Input :: 1

Output :: "One".

Try using "Switch" statements.

This kata is meant for beginners. Rank and upvote to bring it out of beta

=end


def switch_it_up(number)
  word_hash = {
    1 => "One",
    2 => "Two",
    3 => "Three",
    4 => "Four",
    5 => "Five",
    6 => "Six",
    7 => "Seven",
    8 => "Eight",
    9 => "Nine"
  }
  if word_hash.key?(number)
    return word_hash[number]
  else
    return number
  end
end


# rspec test
describe "switch_it_up" do
  it "return One if the number is 1" do
    expect(switch_it_up(1)).to eq "One"
  end

  it "returns Nine if the number is 9" do
    expect(switch_it_up(9)).to eq "Nine"
  end

  it "returns 100 if the number is 100" do
    expect(switch_it_up(100)).to eq 100
  end
end
