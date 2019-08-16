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
