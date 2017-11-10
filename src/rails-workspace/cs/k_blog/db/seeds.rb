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


movie = Movie.create(
  :name => "Machine",
  :director => "Johnson",
  :description => "Something about machine",
  :year => 2017,
  :length => 120,
  :format => "HD",
)
