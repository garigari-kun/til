import logging

LOG_FILENAME = 'loggin_example.out'
logging.basicConfig(filename = LOG_FILENAME, level = logging.DEBUG)
logging.debug('This message will go to log file.')

f = open(LOG_FILENAME, 'rt')
try:
    body = f.read()
finally:
    f.close()

print('FILE: ')
print(body)
