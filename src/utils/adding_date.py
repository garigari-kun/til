from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.today()
print('Not formatted: {}'.format(today))
print('Formatted: {}'.format(today.strftime('%Y/%m/%d')))
date_after_month = today + relativedelta(months = 1)
date_after_six_months = today + relativedelta(months = 6)
date_after_year = today + relativedelta(years = 1)
print('After One month: {}'.format(date_after_month.strftime('%Y/%m/%d')))
print('After Six months: {}'.format(date_after_six_months.strftime('%Y/%m/%d')))
print('After One year: {}'.format(date_after_year.strftime('%Y/%m/%d')))
