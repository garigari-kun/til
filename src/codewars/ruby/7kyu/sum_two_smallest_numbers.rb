"""

Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 integers.
 No floats or empty arrays will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.

Hint: Do not modify the original array.



"""


def sum_two_smallest_numbers(numbers)
  sorted_numbers = numbers.sort
  return sorted_numbers[0] + sorted_numbers[1]
end


describe "sum_two_smallest_numbers" do

  context "given [19, 5, 42, 2, 77]" do
    it "returns 7" do
      expect(sum_two_smallest_numbers([19, 5, 42, 2, 77])).to eql(7)
    end
  end

  context "given [10, 343445353, 3453445, 3453545353453]" do
    it "returns 3453455" do
      expect(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453])).to eql(3453455)
    end
  end

end
