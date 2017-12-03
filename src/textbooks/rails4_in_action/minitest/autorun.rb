require 'minitest/autorun'


class Bacon
  def self.saved?
    return true
  end

end


class TestCase < Minitest::Test
  def test_saved
    assert Bacon.saved?, 'Our bacon was not saved.'
  end

end
