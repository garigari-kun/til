"""

Your task is to write function findSum.

Upto and including n, this function will return the sum of all multiples of 3 and 5.

For example:

findSum(5) should return 8 (3 + 5)

findSum(10) should return 33 (3 + 5 + 6 + 9 + 10)



"""


def find(n)
  num_array = []
  counter = 1
  m_of_three = 1
  m_of_five = 1
  while m_of_three < n
    m_of_three = 3 * counter
    num_array << m_of_three if m_of_three <= n
    counter += 1
  end
  counter = 1
  while m_of_five < n
    m_of_five = 5 * counter
    num_array << m_of_five if m_of_five <= n
    counter += 1
  end
  return num_array.inject { |sum, x| sum + x }
end


describe "find" do
  context "given 5" do
    it "returns 8" do
      expect(find(5)).to eq(8)
    end
  end

  context "given 10" do
    it "returns 33" do
      expect(find(10)).to eq(33)
    end
  end

end
