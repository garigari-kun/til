from datetime import datetime, timedelta
from time import sleep

# minutes
POMODORO_WORK_TIME = 3

# minutes
POMODORO_SHORT_BREAK_TIME = 3
POMODORO_LONG_BREAK_TIME = 3

# main
# Run pomodoro function from here
def main():
    is_started = False
    while not is_started:
        check = input('Start working? Type "start": ')
        if check == 'start':
            is_started = True
            # Call timer function
            trigger_pomodoro_timer()
        else:
            is_started = False

#
def trigger_pomodoro_timer():
    now = datetime.now()
    after_work = now + timedelta(seconds = POMODORO_WORK_TIME)
    is_finished = False

    while not is_finished:
        is_finished = timer(after_work)
        sleep(1)
    if is_finished:
        is_chosen = False
        while not is_chosen:
            print('Well Done!')
            bt_kind = input('Short break or Long break?[short/long]: ')
            if bt_kind == 'short':
                is_chosen = True
                trigger_short_break()
            elif bt_kind == 'long':
                is_chosen = True
                trigger_long_break()
            else:
                is_chosen = False
                print('Error. Choose again')

#
def trigger_short_break():
    print('short break')
    is_finished = False
    now = datetime.now()
    after_break = now + timedelta(seconds = POMODORO_SHORT_BREAK_TIME)
    while not is_finished:
        is_finished = breaktimer(after_break)
        sleep(1)

    if is_finished:
        choice = input("Start working? [y/n]: ")
        if choice == 'y':
            trigger_pomodoro_timer()
        else:
            print('Good job.')
            return

#
def trigger_long_break():
    print('long break')
    is_finished = False
    now = datetime.now()
    after_break = now + timedelta(seconds = POMODORO_LONG_BREAK_TIME)
    while not is_finished:
        is_finished = breaktimer(after_break)
        sleep(1)

    if is_finished:
        choice = input("Start working? [y/n]: ")
        if choice == 'y':
            trigger_pomodoro_timer()
        else:
            print('Good job.')
            return

#
def breaktimer(after_break):
    is_finished = False
    moment = datetime.now()
    print("break: {}".format(moment))
    if moment >= after_break:
        is_finished = True

    return is_finished

#
def timer(after_work):
    is_finished = False
    moment = datetime.now()
    print("work: {}".format(moment))
    if moment >= after_work:
        is_finished = True

    return is_finished


if __name__ == '__main__':
    main()
