@echo off
color a
docker run -d -p 6333:6333 qdrant/qdrant
uvicorn main:app --port 8000 --host 0.0.0.0