class PageController < ApplicationController
  def home
  end

  def about_us
  end

  def contact_us
  end

  def products
  end

  def newsletter
  end

  def blog
  end

  def calendar
    @time = Time.now()
    @year = params["year"].to_i
    @month = params["month"].to_i

    if @year <= 0
      @year = @time.strftime("%Y").to_i
    end

    if @month < 1 || @month > 12
      @month = @time.strftime("%m").to_i
    end


  end

  def articles
  end

  def login
  end
end
