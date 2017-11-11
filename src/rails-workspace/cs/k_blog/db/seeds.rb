# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)


# t.string   "name"
# t.string   "director"
# t.text     "description"
# t.integer  "year"
# t.decimal  "length"
# t.string   "format"
# t.datetime "created_at"
# t.datetime "updated_at"
# t.string   "image"
# t.string   "thumbnail"

# require "faker"
# include Faker

formats = ["Beta", "VHS", "IMAX", "HD", "SuperHD", "4K", "DVD", "BlueRay"]

images = ["skies.jpg", "boots.jpg", "poles.jpg"]


Movie.destroy_all()


100.times do

  movie = Movie.create(
    :name => Faker::Company.bs,
    :director => Faker::Name.name,
    :description => Faker::Lorem.paragraphs.join('<br />'),
    :year => rand(1940..2017),
    :length => rand(20..240),
    :format => formats[rand(formats.length)],
    :image => images[rand(images.length)],
    :thumbnail => images[rand(images.length)]
  )

  puts movie.inspect

end
