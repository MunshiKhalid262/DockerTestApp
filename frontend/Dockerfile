# Use Node.js base image
FROM node:16-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json /app/
RUN npm install

# Copy the application code
COPY . /app/

# Expose the port the app runs on
EXPOSE 3000

# Command to run the application
CMD ["npm", "start"]
