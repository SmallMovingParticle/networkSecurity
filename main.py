from NetworkSecurity.components.data_ingestion import DataIngestion

from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.logging.logger import logging

from NetworkSecurity.entity.config_entity import DataIngestionConfig
from NetworkSecurity.entity.config_entity import DataTransformationConfig

from NetworkSecurity.entity.config_entity import TrainingPipelineConfig
import sys
from NetworkSecurity.components.data_validation import DataValidation , DataValidationConfig
from NetworkSecurity.components.data_transformation import DataTransformation

if __name__=="__main__":
    try:
        trainingpipelineconfig= TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion= DataIngestion(dataingestionconfig)
        logging.info("initiate the data ingestion")
        dataingestionartifact= data_ingestion.initiate_data__ingestion()
        logging.info("data initiation completed")
        print (dataingestionartifact)
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation=  DataValidation(dataingestionartifact , data_validation_config)
        logging.info("initiate data validation")
        data_validation_Artifact=data_validation.initiate_data_validation()
        logging.info("initiate data validation completed")
        print("data validation artifacts")
        data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
        data_transformation=DataTransformation(data_validation_Artifact , data_transformation_config)
        data_transformation_artifact= data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)

    except Exception as e:
        raise NetworkSecurityException(e,sys)