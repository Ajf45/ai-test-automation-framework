import logging

def get_logger():
    logger = logging.getLogger("TestLogger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.FileHandler("reports/test.log")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    return logger