# Dockerfile for MinIO (Object Storage, compatible con S3)
FROM minio/minio:latest

# Set environment variables for MinIO
ENV MINIO_ACCESS_KEY=minioaccesskey
ENV MINIO_SECRET_KEY=miniosecretkey

# Expose port 9000 for MinIO
EXPOSE 9000

# Default command to run MinIO
CMD ["server", "/data"]
