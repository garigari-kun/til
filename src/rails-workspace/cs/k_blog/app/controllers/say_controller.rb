class SayController < ApplicationController
  def hello
    @yo = 'Yo'
    @now = Time.now
  end
end
