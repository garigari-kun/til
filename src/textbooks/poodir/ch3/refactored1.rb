class Gear
  attr_reader :chainring, :cog, :wheel

  def initialize(chainring, cog, wheel)
    @chainring = chainring
    @cog = cog
    @wheel = wheel
  end

  def ratio
    return chainring / cog.to_f
  end

  def gear_inches
    return ratio() * wheel.diamter()
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
