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
    @year = 2017
    @month = 11
  end

  def articles
  end

  def login
  end
end
