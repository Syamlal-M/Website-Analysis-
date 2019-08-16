# Checking the return status code from the website 

Requests is a Python module that you can use to send all kinds of HTTP requests. It is an easy-to-use library with a lot of features 
ranging from passing parameters in URLs to sending custom headers and SSL Verification. Here I am using the requests module fetch the status
code using python.

## Task

The above code is used to fetch the staus code of the websites and the time taken to execute the code. Here i am using requests and time module to do this operation.
```python

import requests
import time

start = time.time()

urls = [
  'https://freevideolectures.com',
  'https://www.guru99.com/',
  'https://linuxjourney.com',
  'https://www.quora.com',
  'https://www.tecmint.com',
  'https://linuxsurvival.com',
  'https://www.tutorialspoint.com',
  'https://www.computerworld.com',
  'https://hackernoon.com',
  'https://www.howtoforge.com',
  'https://www.ubuntupit.com/',
  'https://www.techworm.net',
  'https://www.2daygeek.com/',
  'https://www.linux.org',
  'https://linuxacademy.com',
  'https://www.cyberciti.biz',
  'https://itsfoss.com',
  'https://blog.feedspot.com',
  'https://www.techradar.com'
]


statusDict = {}

def fetchStatus(url):

  information = requests.get(url,timeout=2)
  statusDict[url] = information.status_code


for url in urls:
  fetchStatus(url)


for url in statusDict:
  status = statusDict[url]

  print('{:4} : {}'.format(status,url))

end = time.time()

print()
print (f'Total Time Taken : {end-start}')
```
## Result

```bash
ubuntu@/:~$ python3 reqcode.py
 403 : https://freevideolectures.com
 200 : https://www.guru99.com/
 200 : https://linuxjourney.com
 200 : https://www.quora.com
 200 : https://www.tecmint.com
 200 : https://linuxsurvival.com
 200 : https://www.tutorialspoint.com
 200 : https://www.computerworld.com
 200 : https://hackernoon.com
 200 : https://www.howtoforge.com
 200 : https://www.ubuntupit.com/
 200 : https://www.techworm.net
 403 : https://www.2daygeek.com/
 200 : https://www.linux.org
 200 : https://linuxacademy.com
 200 : https://www.cyberciti.biz
 200 : https://itsfoss.com
 200 : https://blog.feedspot.com
 200 : https://www.techradar.com

Total Time Taken : 14.835082530975342
ubuntu@/:~$
```
