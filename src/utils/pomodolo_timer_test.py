from datetime import datetime, timedelta
from time import sleep


def simple_timer():
    now = datetime.now()
    after_work = now + timedelta(seconds = 5)
    is_finished = False
    while not is_finished:
        is_finished = timer(after_work)
        sleep(1)
    if is_finished:
        print('Well Done! You have 5 minitues of break time! Enjoy!')
        break_time()

def select_choices():
    print('You have 3 options.')
    print('b: Take a breaktime')
    print('s: Start working again without breaktime')

def break_time():
    print('break time')
    is_finished = False
    now = datetime.now()
    after_break = now + timedelta(seconds = 5)
    while not is_finished:
        is_finished = start_breaktime(after_break)
        sleep(1)
    if is_finished:
        choice = input("Start working?[y/n]: ")
        if choice == 'y':
            simple_timer()
        else:
            print('Thank you')
            return

def start_breaktime(after_break):
    is_finished = False
    moment = datetime.now()
    print("break: {}".format(moment))
    if moment >= after_break:
        is_finished = True

    return is_finished

def timer(after_work):
    is_finished = False
    moment = datetime.now()
    print("work: {}".format(moment))
    if moment >= after_work:
        is_finished = True

    return is_finished


if __name__ == '__main__':
    whether_start = input('Start working? Press Enter!')
    print(whether_start)
    #simple_timer()
    if not len(whether_start):
        simple_timer()
