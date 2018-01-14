class CommentsController < ApplicationController

  before_action :find_message, only: [:create]
  before_action :find_comment, only: [:create]

  def create
    @comment.user_id = current_user.id
    if @comment.save()
      redirect_to message_path(@message.id)
    else
      render 'new'
    end
  end


  private

    def comment_params
      return params.require(:comment).permit(:content)
    end

    def find_message
      return @message = Message.find(params[:message_id])
    end

    def find_comment
      return @comment = @message.comments.create(comment_params)
    end

end
