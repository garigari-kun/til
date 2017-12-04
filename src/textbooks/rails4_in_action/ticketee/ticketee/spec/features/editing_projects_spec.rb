require "rails_helper"

RSpec.feature "Uses can edit existing projects" do

  before do
    FactoryGirl.create(:project, name: "Sublime Text3")
    visit "/"
    click_link "Sublime Text3"
    click_link "Edit Project"
  end

  scenario "with valid attributes" do
    fill_in "Name", with: "Sublime Text 4 beta"
    click_button "Update Project"

    expect(page).to have_content "Project has been updated"
    expect(page).to have_content "Sublime Text 4 beta"
  end

  scenario "when providing invalid attributes" do
    fill_in "Name", with: ""
    click_button "Update Project"

    expect(page).to have_content "Project has not been updated."
  end

end
