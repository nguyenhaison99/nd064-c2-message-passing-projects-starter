# main.py
import json
import logging
import time
from concurrent import futures

import grpc
from kafka import KafkaProducer
from kafka.errors import KafkaError

import LocationEvent_pb2
import LocationEvent_pb2_grpc

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LocationEventServicer(LocationEvent_pb2_grpc.ItemServiceServicer):

    def Create(self, request, context):
        request_value = {
            "personId": request.personId,
            "latitude": request.latitude,
            "longitude": request.longitude,
        }
        logger.info('Processing entity: %s', request_value)

        # Insertion to Kafka broker
        producer = KafkaProducer(
            bootstrap_servers=['kafka-headless:9092'],
            api_version=(0, 10, 0),
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

        future = producer.send('sampe', request_value)
        producer.flush()

        try:
            record_metadata = future.get(timeout=10)
            logger.info('Record metadata: %s', record_metadata)
        except KafkaError as e:
            logger.error('Kafka Exception: %s', e)

        return LocationEvent_pb2.LocationEventMessage(**request_value)


# Initialize gRPC server
def run_grpc_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    LocationEvent_pb2_grpc.add_ItemServiceServicer_to_server(LocationEventServicer(), server)
    logger.info("gRPC Server listening on port 5005...")
    server.add_insecure_port("[::]:5005")
    server.start()

    try:
        while True:
            time.sleep(400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    run_grpc_server()
