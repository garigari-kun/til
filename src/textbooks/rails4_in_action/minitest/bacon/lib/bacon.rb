class Bacon
  attr_accessor :expired

  def editable?
    return !expired
  end

  def expired!
    self.expired = true
  end


end
