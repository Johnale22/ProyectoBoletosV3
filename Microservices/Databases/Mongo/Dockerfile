# Dockerfile for MongoDB
FROM mongo:4.4

# Set environment variables for MongoDB
ENV MONGO_INITDB_ROOT_USERNAME=root
ENV MONGO_INITDB_ROOT_PASSWORD=1234
ENV MONGO_INITDB_DATABASE=mongodb

# Expose port 27017 for MongoDB
EXPOSE 27017

# Default command to run MongoDB
CMD ["mongod"]
