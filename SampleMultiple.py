# -*- coding: utf-8 -*-

import FirebaseUtil
from datetime import datetime

token = []
token.append ("FIREBASE-DEVICE-TOKEN #1")
token.append ("FIREBASE-DEVICE-TOKEN #2")
token.append ("FIREBASE-DEVICE-TOKEN #3")

date = datetime.today ()
title = "DEMO {}".format (date.strftime ("%Y-%m-%d %H:%M:%S #%f"))
body = "DEMO Some message here!"
link = "https://github.com/cafewill?{}".format (date.strftime ("%Y%m%d%H%M%S%f"))

response = FirebaseUtil.exec (token, title, body)
# response = FirebaseUtil.send (token, title, body)
# response = FirebaseUtil.exec (token, title, body, link)
# response = FirebaseUtil.send (token, title, body, link)

print ("title : {}".format (title))
print ("body : {}".format (body))
print ("link : {}".format (link))
print ("response : {}".format (response))
