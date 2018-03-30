"""

Write simple .camelCase method (camel_case function in PHP or CamelCase in C#) for strings.
All words must have their first letter capitalized without spaces.

For instance:

'hello case'.camelcase => HelloCase
'camel case word'.camelcase => CamelCaseWord


"""


class String

  # def camelcase
  #   camel = ''
  #   splited = self.split(' ')
  #   splited.map { |word| camel += word.capitalize }
  #   return camel
  # end

  # refactored version
  def camelcase
    self.split.map { |word| word.capitalize }.join
  end



end


describe String do

  describe ".camelcase" do

    context "given 'hello case'" do
      it "returns 'HelloCase'" do
        expect("hello case".camelcase).to eq("HelloCase")
      end
    end

    context "given 'came case word'" do
      it "returns 'CamelCaseWord'" do
        expect('camel case word'.camelcase).to eq('CamelCaseWord')
      end
    end

  end

end
