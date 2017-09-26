"""

6kyu
Rainfall

data and data1 are two strings with rainfall
records of a few cities for months from January to December.
The records of towns are separated by \n.
The name of each town is followed by:.

data and towns can be seen in "Your Test Cases:".

Task:

- function: mean(town, strng) should return the average of rainfall
for the city `town` and the `strng` `data` or `data1`.
- function: variance(town, strng) should return the variance of rainfall
for the city `town` and the `strng` `data` or `data1`.


Examples:

mean("London", data), 51.19(9999999999996)
variance("London", data), 57.42(833333333374)
Notes:

- if functions `mean`or `variance` have as parameter `town` a city
which has no records return `-1`
- Don't truncate or round: the tests will pass
if `abs(your_result - test_result) <= 1e-2`.
- <http://www.mathsisfun.com/data/standard-deviation.html>
- `data` and `data1` are adapted from <http://www.worldclimate.c


"""

def mean(town, strng):
    formatted_str = format_data(strng)
    if not town in formatted_str.keys():
        return -1
    if formatted_str[town]:
        data_str = formatted_str[town]
        months, records = sep_month_and_record(data_str)
        record_in_num = [float(record) for record in records]
        return sum(record_in_num) / len(record_in_num)

    else:
        return -1


def variance(town, strng):
    formatted_str = format_data(strng)
    if not town in formatted_str.keys():
        return -1
    if formatted_str[town]:
        data_str = formatted_str[town]
        months, records = sep_month_and_record(data_str)
        record_in_num = [float(record) for record in records]
        r_mean = sum(record_in_num) / len(record_in_num)
        record_for_var = [(record - r_mean) ** 2 for record in record_in_num]
        return sum(record_for_var) / len(record_for_var)

    else:
        return -1

def format_data(string):
    sep_string = string.split('\n')
    map_data = {}
    for data in sep_string:
        town, records = data.split(':')
        map_data[town] = records
    return map_data

def sep_month_and_record(data_str):
    months = []
    records = []
    sep_data_str = data_str.split(',')
    for data in sep_data_str:
        month, record = data.split(' ')
        months.append(month)
        records.append(record)
    return months, records


"""
Clever and clean solution that I found from the github
"""

def get_towndata(town, strng):
    for line in strng.split('\n'):
        s_town, s_data = line.split(':')
        if s_town == town:
            return [s.split(' ') for s in s_data.split(',')]
    return None

def mean(town, strng):
    data = get_towndata(town, strng)
    if data is not None:
        return sum([float(x) for m, x in data]) / len(data)
    else:
        return -1

def variance(town, strng):
    data = get_town_data(town.strng)
    if data is not None:
        mean = sum([float(x) for m, x in data]) / len(data)
        return sum([(float(x) - mean) ** 2 for m, x in data]) / len(data)
    else:
        return -1
