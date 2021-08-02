# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 21:16:29 2021

@author: Gourav
"""
from mongoengine import  fields, connect, Document
import glob
connect(db="SwitchOn", host="localhost",port=27017)

class User(Document):
    "Setting Up MongoDb Param"
    
    meta = {"collection":"SwitchOn"}
    SKU_ID = fields.StringField(required=True)
    U_ID = fields.StringField(required=True)
    Status = fields.StringField(required=True)
    Photo = fields.ImageField(thumbnail_size=(150,150, False))

def Insertdata():
    "Inserting Data In MongoDb"
    images=glob.glob("*.jpg")
    flag=1
    sflag=1
    for image in images:
        if flag == 5 or flag == 10 or flag == 15 or flag == 25 or flag == 35 or flag == 45 or flag == 55 or flag == 65 or flag == 75 or flag == 85 or flag == 95 :
            img = open(image,'rb')
            if flag == 20 or flag == 40 or flag == 60 or flag == 80:
                sflag = sflag +1
            sid = "P"+str(sflag)
            uid= "u"+str(flag)
            status = "Bad"   
            Popeye = User(SKU_ID=sid, U_ID=uid,Status=status)
            Popeye.Photo.replace(img)
            Popeye.save()
        else:
            img = open(image,'rb')
            if flag == 20 or flag == 40 or flag == 60 or flag == 80:
                sflag = sflag +1       
            sid = "P"+str(sflag)
            uid= "u"+str(flag)
            status = "Good"   
            Popeye = User(SKU_ID=sid, U_ID=uid,Status=status)
            Popeye.Photo.replace(img)
            Popeye.save()
        flag = flag+1

Insertdata()

