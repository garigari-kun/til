class MessagesController < ApplicationController

  before_action :find_message, only: [:show, :edit, :update, :destroy]

  def index
    @messages = Message.all.order('title DESC')
  end

  def show
    @comment = @message.comments.build()
  end

  def new
    @message = current_user.messages.build()
  end

  def create
    @message = current_user.messages.build(message_params)
    if @message.save()
      redirect_to root_path
    else
      render 'new'
    end
  end

  def edit
  end

  def update
    if @message.update(message_params)
      redirect_to message_path(@message.id)
    else
      render 'edit'
    end
  end

  def destroy
    if @message.destroy()
      redirect_to root_path
    end
  end


  private

    def find_message
      return @message = Message.find(params[:id])
    end

    def message_params
      return params.require(:message).permit(:title, :description)
    end

end
