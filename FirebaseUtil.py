# -*- coding: utf-8 -*-

import json
import requests

SUCCESS = 100
PARTIAL = 200
FAILURE = 400
ENCODING = "UTF-8"
FIREBASE_SERVER = "https://fcm.googleapis.com/fcm/send"
FIREBASE_SERVER_KEY = "FIREBASE-SERVER-KEY"

def send (token, title, body, link = None) :
    status = FAILURE

    try :
        response = exec (token, title, body, link)
        success = int (json.loads (response) ["success"])
        check = 1
        if not isinstance (token, str) : check = len (token)
        if 0 == success : status = FAILURE
        if check == success : status = SUCCESS
        if 0 < success and check > success : status = PARTIAL

    except Exception as e :
        print (str (e))

    return status

def exec (token, title, body, link = None) :
    response = ""

    try :
        request = {}
        if (isinstance (token, str)) :
            request ["to"] = token
        else :
            request ["registration_ids"] = token 
        notification = {}
        notification ["title"] = title
        notification ["body"] = body
        notification ["icon"] = "default"
        notification ["sound"] = "default"
        request ["notification"] = notification
        if (link is not None) :
            data = {}
            data ["link"] = link
            request ["data"] = data
        response = post (json.dumps (request))

    except Exception as e :
        print (str (e))

    return response

def post (data) :
    response = ""

    try :
        headers = {
            "Accept-Charset" : "{}".format (ENCODING)
            , "Authorization" : "key={}".format (FIREBASE_SERVER_KEY)
            , "Content-Type" : "application/json; Charset={}".format (ENCODING)
        }
        response = requests.post (FIREBASE_SERVER, data = data, headers = headers).text

    except Exception as e :
        print (str (e))

    return response
