from app.core.config import load_config
from app.core.logging import setup_logger


def main():
    config = load_config()
    logger = setup_logger(config["logging"]["level"])

    logger.info("Bootstrapping existing stock data...")
    logger.info(f"Raw data path: {config['paths']['raw_data']}")


if __name__ == "__main__":
    main()
