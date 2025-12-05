import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s → %(message)s",
    datefmt="%H:%M:%S"
)

logger = logging.getLogger("SalesAnalysis")
