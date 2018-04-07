require "rails_helper"

RSpec.feature "Users can view tickets" do
  before do
    sublime = FactoryGirl.create(:project, name: "Sublime Text3")
    FactoryGirl.create(:ticket, name: "Make it shiney!",
                         description: "Gradients.hahahahaha",
                         project: sublime)

    ie = FactoryGirl.create(:project, name: "Internet Explorer")
    FactoryGirl.create(:ticket, name: "Standars",
                         description: "Isn't a joke.hahahahaha",
                         project: ie)

    visit "/"
  end

  scenario "for a given project" do
    click_link "Sublime Text3"

    expect(page).to have_content "Make it shiney!"
    expect(page).to have_no_content "Standars"

    click_link "Make it shiney!"
    within("#ticket h2") do
      expect(page).to have_content "Make it shiney!"
    end
    expect(page).to have_content "Gradients.hahahahaha"
  end


end
