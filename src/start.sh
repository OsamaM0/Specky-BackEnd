#!/bin/bash

# Start Qdrant
docker run -d -p 6333:6333 qdrant/qdrant

# Wait for Qdrant to be ready
while ! nc -z localhost 6333; do
  echo "Waiting for Qdrant to be ready..."
  sleep 1
done

# Get the port from environment variable, default to 8000 if not set
PORT="${PORT:-8000}"

# Start the uvicorn server
exec uvicorn main:app --port $PORT --host 0.0.0.0