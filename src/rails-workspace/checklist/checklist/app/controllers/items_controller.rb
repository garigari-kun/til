class ItemsController < ApplicationController

  before_action :find_item, only: [:show, :edit, :update, :destroy]

  def index
    if user_signed_in?
      @items = Item.where(:user_id => current_user.id)
    end
  end

  def show
  end

  def new
    # @item = Item.new
    @item = current_user.items.build()
  end

  def create
    # @item = Item.new(item_params)
    @item = current_user.items.build(item_params)
    if @item.save
      redirect_to root_path(@item)
    else
      render 'new'
    end
  end

  def edit
  end

  def update
    if @item.update(item_params)
      redirect_to item_path(@item)
    else
      render 'edit'
    end
  end

  def destroy
    if @item.destroy
      redirect_to root_path
    end
  end

  private

    def item_params
      return params.require(:item).permit(:title, :description)
    end

    def find_item
      return @item = Item.find(params[:id])
    end


end
