require 'bacon'

RSpec.describe Bacon do
  it "it editable" do
    expect(Bacon.new.editable?).to be(true)
  end

  it "can expire" do
    bacon = Bacon.new
    bacon.expired!
    expect(bacon).not_to be_editable
  end

end
