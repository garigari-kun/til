
def monkey_count(n)
  counting_array = []
  (1..n).each { |i| counting_array << i }
  return counting_array
end


# rspec test
describe "monkey_count" do
  it "returns [1, 2, 3] it the number is 3" do
    expect(monkey_count(3)).to eq [1, 2, 3]
  end

  it "returns [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if the number is 10" do
    expect(monkey_count(10)).to eq [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
  end
end
