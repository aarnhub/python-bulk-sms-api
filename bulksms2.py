import urllib
import time
# Proovl SMS API settings www.proovl.com / Script for Python 2
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
for x in numbers:
  messagesSent += 1
  params = {
  "user": user,       
  "token": token,
  "from": from1,
  "text": text,
  "to": x}
  query_string = urllib.urlencode(params)   
  http_req = host + query_string
  f = urllib.urlopen(http_req)
  txt = (f.read().decode('utf-8'))
  z = txt.split(";")
  time.sleep(0.5)
  print("Progress: {}/{}") .format(messagesSent, len(numbers)), (x), (z[0])
if z[0] == "Error":
  print("== Error. Text messages not sent ==")
else:
  print("== Message has been sent! ==")
