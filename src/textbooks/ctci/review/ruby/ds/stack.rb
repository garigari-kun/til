class Stack

  def initialize
    @items = []
  end

  def push(value)
    @items << value
  end

  def pop
    return @items.pop()
  end

  def peek
    return @items[-1]
  end

  def size
    return @items.length
  end

  def is_empty
    return @items.empty?
  end

end



stack = Stack.new()
puts stack.is_empty()
stack.push(4)
stack.push(8)
stack.push(15)
stack.pop()
puts stack.size()
puts stack.is_empty()
puts stack.inspect
