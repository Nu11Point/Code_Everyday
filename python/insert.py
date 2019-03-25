#!/bin/env python

import sys
import MySQLdb
import time

try:
    import MySQLdb
except Exception, e:
    print "--[FAIL][%s] Import MySQLdb lib failed. %s" %(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), e)
    sys.exit()


class connDB:
 def __init__(self,host = None, port = None, user = None, password = None, db = None, charset = None):
  self.__host = host
  self.__port = port
  self.__user = user
  self.__password = password
  self.__db = db
  self.__charset = charset
 def connect(self,host = None, port = None, user = None, password = None, db = None, charset = None):
  if host and len(host) > 0:
      self.__host = host
  if port and port > 0:
      self.__port = port
  if user and len(user) > 0:
      self.__user = user
  if password and len(password) > 0:
      self.__password = password
  if db and len(db) > 0:
      self.__db = db
  if charset and len(charset) > 0:
      self.__charset = charset
  try:
   conn = MySQLdb.connect(
    host = self.__host,
    port = int(self.__port),
    user = self.__user,
    password = self.__password,
    db = self.__db,
    charset = self.__charset,
    connect_timeout = 200)
  except Exception, e:
   print "[FAIL][%s] Connect MySQL failed  host:%s,user:%s,port:%s,password:%s,Details:%s" %(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),self.__host,self.__user,self.__port,self.__password,e)
   return None
  return conn
 def disconnect(self,conn):
  if conn:
   conn.close()
   return None
 def excute(self,conn,sql,flag = 0):
  curs = conn.cursor()
  result = None
  try:
   print "[DEBUG] sql: %s" %(sql)
   result = cursor(sql)
   conn.commit()
   if flag:
    result = curs.fetchall()
  except Exception, e:
   print "[FAIL][%s] Excute sql : %s failed. detail: %s" %(time.strftime("%Y-%m-%d %H:%M:%S"),time.localtime,sql,e)
   curs.close()
   return None
  curs.close()
  return result
  
  
if __name__ == '__main__':
 in1 = connDB(host = sys.argv[1], port = sys.argv[2], user = sys.argv[3], password = str(sys.argv[4]), db = sys.argv[5], charset = 'utf8')
 in1.excute(in1.connect(),'select * from test;',0)
 in1.close()
 
