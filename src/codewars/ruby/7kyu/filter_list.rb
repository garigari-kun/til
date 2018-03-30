"""

In this kata you will create a function that takes a list of non-negative integers
and strings and returns a new list with the strings filtered out.

Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]


"""

def filter_list(l)
  return l.select { |el| el.is_a? Integer }
end

describe "filter_list" do

  context "given [1,2,'a','b']" do
    it "returns [1, 2]" do
      expect(filter_list([1,2,'a','b'])).to eq([1, 2])
    end
  end

  context "given [1,'a','b',0,15]" do
    it "returns [1,0,15]" do
      expect(filter_list([1,'a','b',0,15])).to eq([1,0,15])
    end
  end

  context "given [1,2,'aasf','1','123',123]" do
    it "returns [1,2,123]" do
      expect(filter_list([1,2,'aasf','1','123',123])).to eq([1,2,123])
    end
  end




end
