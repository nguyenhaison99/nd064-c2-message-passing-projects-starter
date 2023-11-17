# Use the official Python 3.7 image based on Alpine Linux
FROM python:3.7-alpine

# Set the working directory in the container to the root directory
WORKDIR .

# Install necessary system packages and libraries
RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev

# Copy the Python requirements file to the container
COPY requirements.txt requirements.txt

# Install Python dependencies from requirements.txt
RUN pip install -r requirements.txt

# Expose port 5000 for the Flask application
EXPOSE 5000

# Copy the entire project directory into the container's root directory
COPY . .

# Define the command to run the Flask application with host binding to 0.0.0.0
CMD ["flask", "run", "--host", "0.0.0.0"]
