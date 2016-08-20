import datetime

default_names = ["Justin", "john", "Emilee", "Jim", "Ron", "Sandra", "veronica", "Whitney"]
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

unf_message = """
Hi {name}!
Thank you for the purchase on {date}.
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!
Team CFE
"""


print(unf_message)


def make_messages(names, amounts):
    messages = []
    if len(names) == len(amounts):
        i = 0
        today = datetime.date.today()
        day_format = '{}/{}/{}'.format(today.year, today.month, today.day)
        amount = amounts[i]
        for name is names:
            new_msg = unf_message.format(
                name=name,
                date=day_format,
                total=amount
            )
            i += 1
            
