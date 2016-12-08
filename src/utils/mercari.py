from selenium import webdriver


driver = webdriver.Chrome('/Users/macuser/Documents/webapp/til/selenium/webdriver/chromedriver')
driver.get('https://www.mercari.com/jp/sell/')
product_name_field = driver.find_element_by_class('input-default')
product_name_field.send_keys('ライダース')
