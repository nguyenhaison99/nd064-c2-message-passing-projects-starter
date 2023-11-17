# Use the official Node.js 14.8.0 image based on Alpine Linux 3.12
FROM node:14.8.0-alpine

# Set the working directory in the container to the root directory
WORKDIR .

# Copy package.json and package-lock.json to the container's root directory
COPY package.json ./
COPY package-lock.json ./

# Install Node.js dependencies from package.json
RUN npm install

# Install React Scripts globally in the container
RUN npm install react-scripts@3.4.3 -g

# Copy the entire project directory into the container's root directory
COPY . ./

# Expose port 3000 for the application
EXPOSE 3000

# Start the application using "npm start" when the container runs
CMD ["npm", "start"]

