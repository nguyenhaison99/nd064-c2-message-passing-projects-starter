# Use the official Python 3.8 image as the base image
FROM python:3.8

# Set the working directory in the container to the root directory
WORKDIR .

# Copy all files from the host into the container's root directory
COPY . .

# Install Python dependencies from the requirements.txt file
RUN pip install -r requirements.txt

# Set the entry point for the container to run the location_event_consumer.py script
ENTRYPOINT ["python", "app/location_event_consumer.py"]
