# Dockerfile
FROM python:3.10-slim

# Set working directory
WORKDIR /app

RUN apt-get update && apt-get install -y \
    git \
    ffmpeg \
    && apt-get clean

# Copy source
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

RUN python -m grpc_tools.protoc -I=app/proto --python_out=app/proto --grpc_python_out=app/proto  app/proto/story.proto

# Expose gRPC port
EXPOSE 50051

# Run gRPC server
CMD ["python", "app/main.py"]

