"""

Create a combat function that takes the player's current health and the amount of damage recieved,
and returns the player's new health. Health can't be less than 0.

"""


require 'test/unit'


def combat(health, damage)
  rest = health - damage
  if rest > 0
    return rest
  else
    return 0
  end
end


class TestCase < Test::Unit::TestCase
  def test_combat()
    assert_equal(95, combat(100, 5))
    assert_equal(10, combat(30, 20))
    assert_equal(0, combat(100, 200))
  end

end
