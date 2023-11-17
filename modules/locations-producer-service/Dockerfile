# Use the official Python 3.8 image as the base image
FROM python:3.8

# Set the working directory in the container to the root directory
WORKDIR .

# Copy all files from the host into the container's root directory
COPY . .

# Install Python dependencies from the requirements.txt file
RUN pip install -r requirements.txt

# Expose port 5005 for the application (for potential network access)
EXPOSE 5005

# Set the entry point for the container to run the main.py script
ENTRYPOINT ["python", "app/main.py"]
