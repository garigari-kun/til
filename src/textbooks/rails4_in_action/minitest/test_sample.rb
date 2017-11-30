require 'test/unit'


def greeting
  return "Hello, world!"
end


class TestCase < Test::Unit::TestCase
  def test_greeting
    assert_equal 'Hello, world!', greeting
  end
end
