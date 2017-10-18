class String

  def palindrome?
    return self == self.reverse
  end

end




class User

  attr_accessor :name, :email

  def initialize(attributes={})
    @name = attributes[:name]
    @email = attributes[:email]
  end

  def formatted_email
    return "#{@name} <#{@email}>"
  end




end
