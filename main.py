from src.Kidney_Disease_Classification import logger
from src.Kidney_Disease_Classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME="Data Ingestion Stage"

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        
    except Exception as e:
        logger.exception(e)
        raise e