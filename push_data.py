import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL= os.getenv("MONGO_DB_URL")

print(MONGO_DB_URL)

import certifi  ##to establish the secure http connection 
ca=certifi.where()  ## retrieves the path to the certificates which are stored in the certified authorities

import pandas as pd
import numpy as np
import pymongo
from NetworkSecurity.logging import logger
from NetworkSecurity.exception.exception import NetworkSecurityException

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def csv_to_json_convertor(self, file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)


            ##maing the csv data to key value pair 1. we transpost the data then we convert it to json its a in to out approach
            
            records=list(json.loads(data.T.to_json()).values())

            return records

        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def insert_data_to_mongodb(self, records , database ,collection):
        try:
            self.database= database
            self.collection = collection
            self.records= records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL ,tlsCAFile=ca)
            self.database = self.mongo_client[self.database]


            self.collection =  self.database[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))


        except Exception as e:
            raise NetworkSecurityException(e,sys)

if __name__=='__main__':
    File_path="network_data\phisingData.csv"
    DATABSE="Phishing"
    Collection= "NetworkData"
    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json_convertor(file_path=File_path)
    no_of_records=networkobj.insert_data_to_mongodb(records , DATABSE , Collection)

    print(no_of_records)

