class BooksController < ApplicationController

  before_action :find_book, only: [:show, :edit, :update, :destroy]

  def index
    if params[:category].blank?
      @books = Book.all.order("created_at DESC")
    else
      @category_id = Category.find_by(:name => params[:category])
      @books = Book.where(:category_id => @category_id).order("created_at DESC")
    end
  end

  def show
  end

  def new
    @book = current_user.books.build()
    @categories = Category.all.map { |c| [c.name, c.id] }
  end

  def create
    @book = current_user.books.build(book_params)
    @book.category_id = params[:category_id]

    if @book.save
      redirect_to root_path
    else
      render 'new'
    end
  end

  def edit
    @categories = Category.all.map { |c| [c.name, c.id] }
  end

  def update
    @book.category_id = params[:book][:category_id]
    if @book.update(book_params)
      redirect_to book_path(@book.id)
    else
      render 'edit'
    end
  end

  def destroy
    if @book.destroy
      redirect_to root_path
    end
  end

  private

    def book_params
      return params.require(:book).permit(:title, :description, :author)
    end

    def find_book
      return @book = Book.find(params[:id])
    end


end
