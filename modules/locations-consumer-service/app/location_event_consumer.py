import json
import logging
import os

from kafka import KafkaConsumer
from sqlalchemy import create_engine

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_environment_variable(variable_name):
    """Get an environment variable with error handling."""
    try:
        return os.environ[variable_name]
    except KeyError:
        logger.error(f"Environment variable '{variable_name}' is not set.")
        raise


# Get database and Kafka configuration from environment variables
DB_USERNAME = get_environment_variable("DB_USERNAME")
DB_PASSWORD = get_environment_variable("DB_PASSWORD")
DB_HOST = get_environment_variable("DB_HOST")
DB_PORT = get_environment_variable("DB_PORT")
DB_NAME = get_environment_variable("DB_NAME")
KAFKA_URL = get_environment_variable("KAFKA_URL")
KAFKA_TOPIC = get_environment_variable("KAFKA_TOPIC")


def connect_to_kafka_consumer():
    """Create and return a KafkaConsumer instance."""
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=[KAFKA_URL],
        group_id=None,  # Use None for unique consumers
        auto_offset_reset='earliest'
    )
    return consumer


def write_location_to_db(location):
    """Write location data to the database."""
    engine = create_engine(f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo=True)
    with engine.connect() as conn:
        person_id = int(location["personId"])
        latitude, longitude = float(location["latitude"]), float(location["longitude"])

        insert_query = "INSERT INTO location (person_id, coordinate) VALUES (%s, ST_Point(%s, %s))"
        conn.execute(insert_query, (person_id, latitude, longitude))


if __name__ == "__main__":
    try:
        # Connect to Kafka
        consumer = connect_to_kafka_consumer()

        # Process Kafka messages
        for location_message in consumer:
            message = location_message.value.decode('utf-8')
            location_data = json.loads(message)
            write_location_to_db(location_data)
            logger.info("Location data written to the database.")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise
