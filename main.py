from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.logging.logger import logging
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig  ,DataValidationConfig  

import sys
if __name__ == "__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        logging.info("data ingestion started")
        data_ingestion = DataIngestion(dataingestionconfig)
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
        logging.info("data ingestion completed")
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        # data_validation = DataValidation(dataingestionartifact,data_validation_config)
        data_validation = DataValidation(data_validation_config, dataingestionartifact)
        logging.info("initiate the data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data validation completed")
        print(data_validation_artifact)

    except Exception as e:
        raise NetworkSecurityException(e, sys)