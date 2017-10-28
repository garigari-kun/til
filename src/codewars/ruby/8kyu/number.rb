def number(bus_stops)
  number_of_people = 0
  bus_stops.each do |bus_stop|
    number_of_people += bus_stop[0] - bus_stop[1]
  end

  if number_of_people >= 0
    return number_of_people
  else
    return 0
  end
end





 number([[10, 0], [3, 5], [5, 8]])
