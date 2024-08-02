import pandas as pd
from src.data.data_loading import load_data
from src.model.train_evaluate_model import train_silhouette_model, train_elbow_model
from src.utils.utils import setup_logging

def main():
    logger = setup_logging()  
    try:
        
        logger.info('Starting Unsupervised Clustering Solution Model')

        data = load_data('data/mall_customers.csv')
        logger.info("Data loaded") 

        score = train_elbow_model(data)
        logger.info(f"Model Elblow Score: {score}")
        
        score = train_silhouette_model(data)
        logger.info(f"Model Silhouette Score: {score}")


    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
