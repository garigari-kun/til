class People < ActiveRecord::Base

  def full_name()
    return "#{first_name} #{last_name}"
  end

  def describe()
    return "The name is #{first_name} #{last_name}"
  end


end
