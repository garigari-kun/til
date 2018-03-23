class SessionsController < ApplicationController
  def new
  end

  def create
    user = User.find_by(email: params[:session][:email].downcase)
    if user && user.authenticate(params[:session][:password])
      # login action
      login user
      redirect_to user_url(user.id)
    else
      # authentication error
      flash.now[:danger] = "Invalid email/password combination."
      render "new"
    end
  end
end
