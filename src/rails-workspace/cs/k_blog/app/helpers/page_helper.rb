module PageHelper



  def calendar(year, month)
    weekday = 7
    last = 0
    first_date = Date.new(year, month, 1)
    first_day_of_week = first_date.strftime("%w").to_i()

    next_month_first_date = first_date + 1.month
    last_date = next_month_first_date - 1
    sp_last_date = last_date.to_s().split("-")

    sel_month = first_date.strftime("%B")
    sel_year = first_date.strftime("%Y")

    prev_year = year
    prev_month = month - 1

    next_year = year
    next_month = month + 1

    if prev_month <= 0
      prev_month = 12
      prev_year -= 1
    end

    if next_month > 12
      next_month = 1
      next_year += 1
    end


    cal = ""
    cal += "#{ sel_month }, #{ sel_year }<br />"
    # cal += link_to("Prev", "/page/calendar?year=#{ prev_year }&month=#{ prev_month }")
    cal += link_to("Prev", page_calendar_path(:month => prev_year, :year => prev_month))
    cal += "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
    # cal += link_to("Next", "/page/calendar?year=#{ next_year }&month=#{ next_month }")
    cal += link_to("Next", page_calendar_path(:month => next_month, :year => next_year))
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    cal += "<table class='table'><tr>"
    # Rendering week header
    days.each do | day |
      cal += "<td>#{ day }</td>"
    end
    cal += "</tr>"

    # Rendering first week of the month
    cal += "<tr>"
    first_day_of_week.times do | day |
      cal += "<td>&nbsp;</td>"
    end
    (weekday - first_day_of_week).times do | day |
      cal += "<td>#{ day + 1 }</td>"
      last = day + 1
    end


    # Rendering between first and last
    cal += "<tr>"
    beg = weekday - first_day_of_week + 1
    last = weekday - first_day_of_week + weekday
    (beg..last).each do | day |
      cal += "<td>#{ day }</td>"
    end
    cal += "</tr>"


    cal += "<tr>"
    beg = last + 1
    last = last + weekday
    (beg..last).each do | day |
      cal += "<td>#{ day }</td>"
    end
    cal += "</tr>"


    cal += "<tr>"
    beg = last + 1
    last = last + weekday
    (beg..last).each do | day |
      cal += "<td>#{ day }</td>"
    end
    cal += "</tr>"


    # Rendering last week of the month
    cal += "<tr>"
    beg = last + 1
    last = last + weekday
    (beg..last).each do | day |
      if day.to_i <= sp_last_date[2].to_i
        cal += "<td>#{ day }</td>"
      else
        cal += "<td>&nbsp;</td>"
      end
    end
    cal += "</tr>"


    cal += "</table>"
    return cal
  end



end
