require "rails_helper"


RSpec.feature "Users can edit existing projects" do

  before do
    project = FactoryGirl.create(:project, name: "Sublime Text3")

    visit "/"
    click_link "Sublime Text3"
    click_link "Edit Project"
  end

  scenario "with valid attributes" do
    fill_in "Name", with: "Sublime Text4 beta"
    click_button "Update Project"

    expect(page).to have_content "Project has been updated."
    expect(page).to have_content "Sublime Text4 beta"
  end

  scenario "when providing invalid attributes" do
    fill_in "Name", with: ""
    click_button "Update Project"

    expect(page).to have_content "Project has not been updated."
  end
end
