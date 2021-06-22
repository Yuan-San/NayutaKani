import time
import random
from replit import db
import pandas as pd
import discord
import csv

#Replit Keys
db["KDRoom1Local"] = 0
db["KDRoom2Local"] = 0
db["KDRoom3Local"] = 0
db["KDRoom4Local"] = 0
db["KDRoom5Local"] = 0
db["KDRoom1LocalPW"] = 0
db["KDRoom2LocalPW"] = 0
db["KDRoom3LocalPW"] = 0
db["KDRoom4LocalPW"] = 0
db["KDRoom5LocalPW"] = 0
db["KDRoom1LocalHost"] = 0
db["KDRoom2LocalHost"] = 0
db["KDRoom3LocalHost"] = 0
db["KDRoom4LocalHost"] = 0
db["KDRoom5LocalHost"] = 0

def kingdom_local_createroom(name, password):
  id1 = db["KDRoom1Local"]
  id2 = db["KDRoom2Local"]
  id3 = db["KDRoom3Local"]
  id4 = db["KDRoom4Local"]
  id5 = db["KDRoom5Local"]
  if id1 == 0:
    with open('players.csv', 'a', newline='') as fd:
            fdw = csv.writer(fd)
            fdw.writerow([id1, password, name, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    newid1 = random.randint(100, 999)
    db["KDRoom1Local"] = newid1
    db["KDRoom1LocalHost"] = name
    if password == int:
      db["KDRoom1LocalPW"] = password
      fmt = 'Your Room was Successfully Created! Room ID: {} | Password: {}.'
      return fmt.format(newid1, password)
    elif password is None:
      fmt = 'Your Room was Successfully Created! Room ID: {} | No Password.'
      return fmt.format(newid1)
  elif id2 == 0:
    with open('players.csv', 'a', newline='') as fd:
            fdw = csv.writer(fd)
            fdw.writerow([id2, password, name, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    newid2 = random.randint(100, 999)
    db["KDRoom2Local"] = newid2
    db["KDRoom2LocalHost"] = name
    if password == int:
     db["KDRoom2LocalPW"] = password
     fmt = 'Your Room was Successfully Created! Room ID: {} | Password: {}.'
     return fmt.format(newid2, password)
    elif password is None:
      fmt = 'Your Room was Successfully Created! Room ID: {} | No Password.'
      return fmt.format(newid2)
  elif id3 == 0:
   with open('players.csv', 'a', newline='') as fd:
            fdw = csv.writer(fd)
            fdw.writerow([id3, password, name, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
   newid3 = random.randint(100, 999)
   db["KDRoom3Local"] = newid3
   db["KDRoom3LocalHost"] = name
   if password == int:
      db["KDRoom3LocalPW"] = password
      fmt = 'Your Room was Successfully Created! Room ID: {} | Password: {}.'
      return fmt.format(newid3, password)
   elif password is None:
      fmt = 'Your Room was Successfully Created! Room ID: {} | No Password.'
      return fmt.format(newid3)
  elif id4 == 0:
   with open('players.csv', 'a', newline='') as fd:
            fdw = csv.writer(fd)
            fdw.writerow([id4, password, name, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
   newid4 = random.randint(100, 999)
   db["KDRoom4Local"] = newid4
   db["KDRoom4LocalHost"] = name
   if password == int:
      db["KDRoom4LocalPW"] = password
      fmt = 'Your Room was Successfully Created! Room ID: {} | Password: {}.'
      return fmt.format(newid4, password)
   elif password is None:
      fmt = 'Your Room was Successfully Created! Room ID: {} | No Password.'
      return fmt.format(newid4)
  elif id5 == 0:
   with open('players.csv', 'a', newline='') as fd:
            fdw = csv.writer(fd)
            fdw.writerow([id5, password, name, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
   newid5 = random.randint(100, 999)
   db["KDRoom5Local"] = newid5
   db["KDRoom5LocalHost"] = name
   if password == int:
      db["KDRoom5LocalPW"] = password
      fmt = 'Your Room was Successfully Created! Room ID: {} | Password: {}.'
      return fmt.format(newid5, password)
   elif password is None:
      fmt = 'Your Room was Successfully Created! Room ID: {} | No Password.'
      return fmt.format(newid5)
  else:
   return "Rooms are full right now, Please try again later!"

def kingdom_local_endroom(name, password):
  host1 = db["KDRoom1LocalHost"]
  host2 = db["KDRoom2LocalHost"]
  host3 = db["KDRoom3LocalHost"]
  host4 = db["KDRoom4LocalHost"]
  host5 = db["KDRoom5LocalHost"]
  if host1 != 0:
    if name == host1:
      db["KDRoom1Local"] = 0
      db["KDRoom1LocalPW"] = 0
      db["KDRoom1LocalHost"] = 0
      return "Room 1 was Ended. Resetting and Cleaning up Room... "
  elif host2 != 0:
    if name == host2:
      db["KDRoom2Local"] = 0
      db["KDRoom2LocalPW"] = 0
      db["KDRoom2LocalHost"] = 0
      return "Room 2 was Ended. Resetting and Cleaning up Room... "
  elif host3 != 0:
    if name == host3:
      db["KDRoom3Local"] = 0
      db["KDRoom3LocalPW"] = 0
      db["KDRoom3LocalHost"] = 0
      return "Room 3 was Ended. Resetting and Cleaning up Room... "
  elif host4 != 0:
    if name == host4:
      db["KDRoom4Local"] = 0
      db["KDRoom4LocalPW"] = 0
      db["KDRoom4LocalHost"] = 0
      return "Room 4 was Ended. Resetting and Cleaning up Room... "
  elif host5 != 0:
    if name == host5:
      db["KDRoom5Local"] = 0
      db["KDRoom5LocalPW"] = 0
      db["KDRoom5LocalHost"] = 0
      return "Room 5 was Ended. Resetting and Cleaning up Room... "

def kingdom_local_joinroom(name, id, password):
  id1 = db["KDRoom1Local"]
  id2 = db["KDRoom2Local"]
  id3 = db["KDRoom3Local"]
  id4 = db["KDRoom4Local"]
  id5 = db["KDRoom5Local"]
  pw1 = db["KDRoom1LocalPW"]
  pw2 = db["KDRoom2LocalPW"]
  pw3 = db["KDRoom3LocalPW"]
  pw4 = db["KDRoom4LocalPW"]
  pw5 = db["KDRoom5LocalPW"]