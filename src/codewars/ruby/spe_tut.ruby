


def fizz_buzz(number)
  if number % 3 == 0 and number % 5 == 0
    return "fizzbuzz"
  elsif number % 5 == 0
    return "buzz"
  elsif number % 3 == 0
    return "fizz"
  else
    return number
  end
end






# rspec test
describe "fizz_buzz" do
  it "returns 1 if number is 1" do
    expect(fizz_buzz(1)).to eq 1
  end

  it "returns fizz if number is 3" do
    expect(fizz_buzz(3)).to eq "fizz"
  end

  it "returns buzz if number is 5" do
    expect(fizz_buzz(5)).to eq "buzz"
  end

  it "returns fizzbuzz if number is 15" do
    expect(fizz_buzz(15)).to eq "fizzbuzz"
  end
end
