require "Set"

# def num_jewels_in_stones(j, s)
#   unique_j = j.split.uniq.join
#   return s.count(unique_j)
# end


# def num_jewels_in_stones(j, s)
#   s.chars.count { |c| j.include?(c) }
# end

def num_jewels_in_stones(j, s)
  count = 0
  s.split("").each do |c|
    if j.include?(c)
      count += 1
    end
  end
  return count
end


RSpec.describe do
  describe "num_jewels_in_stones" do
    it "returns 3" do
      expect(num_jewels_in_stones("aA", "aAAbbbb")).to eq(3)
    end

    it "returns 0" do
      expect(num_jewels_in_stones("z", "ZZ")).to eq(0)
    end
  end
end
