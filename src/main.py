import argparse
from src.data.prepareLanguages import prepareData
#from src.models.train import train_model
#from src.models.evaluate import evaluate_model
#from src.models.predict import make_predictions
from src.utils.logger import setup_logger



def main():
    # Set up logger
    logger = setup_logger()
    logger.info("Starting the AI project...")

    parser = argparse.ArgumentParser(description="AI Project Workflow")
    parser.add_argument("--mode", type=str, required=True,
                        choices=["train", "evaluate", "predict"],
                        help="Specify the mode: train, evaluate, or predict.")
    args = parser.parse_args()
    mode = args.mode

    logger.info("Preparing data.")
    input_lang, output_lang, pairs = prepareData('eng', 'fra', True)
    print(input_lang)
    
    """
    # Step 3: Workflow based on mode
    if mode == "train":
        logger.info("Training mode selected.")
        model = train_model(data)
        logger.info("Model training completed.")

    elif mode == "evaluate":
        logger.info("Evaluation mode selected.")
        evaluation_results = evaluate_model(data)
        logger.info(f"Evaluation results: {evaluation_results}")

    elif mode == "predict":
        logger.info("Prediction mode selected.")
        predictions = make_predictions(data)
        logger.info(f"Predictions: {predictions}")

    else:
        logger.error("Invalid mode selected.")
        raise ValueError("Invalid mode. Choose from 'train', 'evaluate', or 'predict'.")
    """
    logger.info("AI project completed.")

if __name__ == "__main__":
    main()
