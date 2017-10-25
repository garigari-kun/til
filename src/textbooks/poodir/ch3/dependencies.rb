class Gear
  attr_reader :chainring, :cog, :rim, :tire

  def initialize(chainring, cog, rim, tire)
    @chainring = chainring
    @cog = cog
    @rim = rim
    @tire = tire
  end

  def ratio
    return chainring / cog.to_f
  end

  def gear_inches
    return ratio() * Wheel.new(rim, tire).diameter()
  end


end



class Wheel

  attr_reader :rim, :tire

  def initialize(rim, tire)
    @rim = rim
    @tire = tire
  end

  def diameter
    return rim + (tire * 2)
  end


end
