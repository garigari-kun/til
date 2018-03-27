"""

Create a function that takes a string and an integer (n).

The function should return a string that repeats the input string n number of times.

If anything other than a string is passed in you should return 'Not a string'

Example
'Hi', 2 --> 'HiHi'
1234, 5 --> 'Not a string'


"""


def repeat_it(string,n)
  if string.instance_of? String
    return string * n
  else
    return 'Not a string'
  end
end


# more ruby way
def repeat_it_better(string,n)
  string.class==String ? string*n : "Not a string"
end


describe "repeat_it" do

  context "given 'Hello', 2" do
    it "returns 'HelloHello'" do
      expect(repeat_it('Hello', 2)).to eql('HelloHello')
    end
  end

  context "given 'Hello', 1" do
    it "returns 'Hello'" do
      expect(repeat_it('Hello', 1)).to eql('Hello')
    end
  end

  context "given 1234, 5" do
    it "returns 'Not a string'" do
      expect(repeat_it(1234, 5)).to eql('Not a string')
    end
  end



end
