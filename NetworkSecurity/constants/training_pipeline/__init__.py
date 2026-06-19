## to define all the info with regard to data

import os
import sys
import numpy as np
import pandas as pd


"""
defining common constants variable for the training pipeline
"""

TARGET_COLUMN= "Result"
PIPELINE_NAME: str= "NetworkSecurity"
ARTIFACT_DIR: str= "Artifacts"
FILE_NAME:str= "PhisingData.csv"

TRAIN_FILE_NAME:str= "train.csv"
TEST_FILE_NAME:str = "test.csv"

SCHEMA_FILE_PATH = os.path.join("NetworkSecurity", "data_schema", "schema.yaml")

"""
data ingestion related constants start with DATA_INGESTION variable name
"""

DATA_INGESTION_COLLECTION_NAME: str = "NetworkData"
DATA_INGESTION_DATABASE_NAME: str = "devyansh"
DATA_INGESTION_DIR_NAME: str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str ="feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2


"""
data validation related constants start with DATA_VALIDATION ver name
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_INVALID_DIR: str="invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drinft_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str= "report.yaml"