"""

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.

The input string will only consist of lower case letters and/or spaces.


"""


def getCount(inputStr)
  return inputStr.count('aeiou')
end



describe "getCount" do
  context "given 'abcde'" do
    it "returns 2" do
      expect(getCount("abcde")).to eql(2)
    end
  end
end
