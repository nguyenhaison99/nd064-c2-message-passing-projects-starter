import grpc

import LocationEvent_pb2
import LocationEvent_pb2_grpc


# Sample implementation of a gRPC client for sending data

def send_sample_payload():
    print("Sending sample payload...")

    channel = grpc.insecure_channel("localhost:5005")
    stub = LocationEvent_pb2_grpc.ItemServiceStub(channel)

    # Update this with desired payload
    location = LocationEvent_pb2.LocationEventMessage(
        personId=1222,
        latitude=100,
        longitude=200
    )

    _ = stub.Create(location)


if __name__ == "__main__":
    send_sample_payload()
