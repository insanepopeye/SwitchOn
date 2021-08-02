# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 13:47:50 2021

@author: Gourav
"""
import pymongo
#from bson import ObjectId

connection = pymongo.MongoClient("localhost", 27017)

database = connection['SwitchOn']

collection = database['SwitchOn']
print("Database connected")


def get_multiple_data():
    
    "Fetching All the Data"
    
    data = collection.find({})
    return list(data)

def get_multiple_good_data():
    
    "Fetching Only Good Data"
    
    data = collection.find({"Status":"Good"})
    return list(data)

def get_multiple_bad_data():
    
    "Fetching Only Bad Data"
    
    data = collection.find({"Status":"Bad"})
    return list(data)

#Closing Connection
connection.close()
