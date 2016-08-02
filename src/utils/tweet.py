from datetime import datetime
from getpass import getpass

from selenium import webdriver

import time


"""
Ask a username or email and password
Try to login using these information
Type a tweet and send it
print something

"""


def get_username_and_password():
    name = input('Username: ')
    password = getpass('Password: ')
    return name, password

def open_browser():
    driver = webdriver.Firefox()
    return driver


def login_twitter(driver, name, password):
    twitter_url = 'https://twitter.com/?lang=en'
    driver.get(twitter_url)

    username_field = driver.find_element_by_id('signin-email')
    password_field = driver.find_element_by_id('signin-password')
    username_field.send_keys(name)
    password_field.send_keys(password)
    password_field.submit()

    return True


def post_tweet(driver):
    current_date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    post_body = driver.find_element_by_id('tweet-box-home-timeline')
    post_body.send_keys('自動投稿テスト {}'.format(current_date))
    try:
        post_button = driver.find_element_by_css_selector('button.tweet-action')
        post_button.click()
        print('Success')
    except:
        print('Failed')







if __name__ == '__main__':
    name, password = get_username_and_password()
    driver = open_browser()
    print('open a browser')
    time.sleep(1)
    success = login_twitter(driver, name, password)
    if success:
        print('Login success')
        time.sleep(3)
        post_tweet(driver)
        print('Done tweeting')
