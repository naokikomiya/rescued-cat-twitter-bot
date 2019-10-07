import os
from os.path import join
from os.path import dirname


CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')

print('#'*15)
print(GOOGLE_CHROME_SHIM)
print('#'*15)
print(CONSUMER_KEY)
print(CONSUMER_SECRET)
print(ACCESS_TOKEN)
print(ACCESS_TOKEN_SECRET)

print(os.environ.get('HOME'))
