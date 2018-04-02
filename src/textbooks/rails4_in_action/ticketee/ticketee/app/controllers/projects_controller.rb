class ProjectsController < ApplicationController

  def index
  end

  def show
    @project = Project.find(params[:id])
  end

  def new
    @project = Project.new
  end

  def create
    @project = Project.new(project_params)

    if @project.save
      flash[:notice] = "Project has been created."
      redirect_to project_path(@project.id)
    else
      # rerender new
    end
  end

  private

  def project_params
    return params.require(:project).permit(:name, :description)
  end


end
