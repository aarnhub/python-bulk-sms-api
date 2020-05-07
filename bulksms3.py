import urllib
import urllib.parse
import urllib.request
import time
from urllib import request as urlrequest
import ssl
# Proovl SMS API settings www.proovl.com / Script for Python 3+
user = "***********"   # change ***** to your Proovl user ID
token = "***********"   # change ***** to your Proovl token
from1 = "***********"  # change ***** to your Proovl SMS number
text = "Hello World"   # text
# Add numbers: format "44755555555" / one per line
numbers = [
"44755555555",
"44755555555",
"44755555555",
"44755555555"
]
messagesSent = 0
host = "https://www.proovl.com/api/send.php?"
hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
for x in numbers:
  messagesSent += 1
  params = {
  "user": user,       
  "token": token,
  "from": from1,
  "text": text,
  "to": x}
  try:
    _create_unverified_https_context = ssl._create_unverified_context
  except AttributeError:
    pass
  else:
    ssl._create_default_https_context = _create_unverified_https_context
  query_string = urllib.parse.urlencode(params)   
  http_req = host + query_string
  req = urllib.request.Request(http_req, headers=hdr)
  f = urllib.request.urlopen(req)
  txt = (f.read().decode('utf-8'))
  z = txt.split(";")
  time.sleep(0.5)
  print("Progress: {}/{}".format(messagesSent, len(numbers)), (x), (z[1]))
if z[0] == "Error":
  print("== Error. Text messages not sent ==")
else:
  print("== Message has been sent! ==")
