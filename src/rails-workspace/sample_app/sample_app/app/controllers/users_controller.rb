class UsersController < ApplicationController

  def show
    @user = User.find(params[:id])
    # debugger()
  end

  def new
    @user = User.new
  end

  def create
    @user = User.new(user_params)
    if @user.save
      # after saving
      flash[:success] = "Welcome to the sample app!!!"
      redirect_to user_url(@user)
    else
      render "new"
    end
  end

  # private methods
  private

    def user_params
      return params.require(:user).permit(:name, :email, :password, :password_confirmation)
    end


end
