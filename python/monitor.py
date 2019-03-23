#!/bin/env python
#conding:utf-8


import json, urllib2, sys

  
def http_get():
        url='http://api.somesite.com/someapi/index.php'
        response = urllib2.urlopen(url)
        return response.read()

api_get = http_get()
apijson = json.loads(api_get)
apistatus = apijson['status']




if apistatus == 1:
        print "OK - status is %s api service is fine." % apistatus
        sys.exit(0)
else:
        print "CRITICAL - api service is down."
        sys.exit(1)