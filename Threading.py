
import requests
import time
import threading

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
  
  response = requests.get(url,timeout=2)
  statusDict[url] = response.status_code
  

threadList = []
  
for url in urls:
  
  t = threading.Thread(target=fetchStatus,args=(url,))
  t.start()
  
  threadList.append(t)
  
for t in threadList:
  
  t.join()
  

end = time.time()



with open('result.txt','w') as fh:

  for url in statusDict:
    
    status = statusDict[url]
    fh.write('{:4} : {}\n'.format(status,url))
  
  fh.write('\n\n')
  fh.write(f'Total Time Taken : {end - start}\n')
  fh.write('\n\n')
  
