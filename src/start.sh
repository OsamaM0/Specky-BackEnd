#!/bin/bash

# Start Qdrant
docker run -d -p 6333:6333 qdrant/qdrant

# Wait for Qdrant to be ready
while ! nc -z localhost 6333; do
  echo "Waiting for Qdrant to be ready..."
  sleep 5
done


# Start the uvicorn server
exec uvicorn main:app --port 8000 --host 0.0.0.0