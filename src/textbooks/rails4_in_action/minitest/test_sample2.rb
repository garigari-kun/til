require 'test/unit'



def even_or_odd(number)
  if number.to_i % 2 == 0
    return "Even"
  else
    return "Odd"
  end
end




class TestCase < Test::Unit::TestCase
  def test_even_or_odd
    assert_equal("Even", even_or_odd(2))
    assert_equal("Odd", even_or_odd(1))
  end

end
