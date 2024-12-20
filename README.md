# Specky

This is a RAG model for question answering.

# Speaky - Mini-RAG Project Documentation

## Project Overview
**Speaky** is a Mini-RAG (Retrieval-Augmented Generation) project designed to enable efficient interaction with documentation using advanced natural language processing techniques. It leverages FastAPI for API development, MongoDB for data storage, and vector databases for semantic search. The project architecture follows a modular and scalable design, ensuring flexibility and maintainability.

This document explains the project's directory structure and describes the workflow to help contributors understand the flow of data and functionality.

---

## Directory Structure and Workflow

Below is a detailed breakdown of the directories and their roles within the project, along with an explanation of how the code flows from one module to another.

---

### **1. assets/**
This directory contains auxiliary files for project setup and testing:
- **`.gitignore`**: Excludes unnecessary files from Git tracking.
- **`.gitkeep`**: Preserves empty directories in version control.
- **`mini-rag-app.postman_collection.json`**: A collection of API endpoints for testing via Postman.

### **How it fits in the workflow:**
This directory does not directly impact the runtime of the application but supports development and testing. The Postman collection, for instance, is critical for verifying API functionality during and after development.

---

### **2. controllers/**
This folder contains the **controllers**, which act as intermediaries between the API routes and the underlying logic (models, helpers, etc.). Each controller is responsible for a specific part of the application.

- **`BaseController.py`**: A shared base for all controllers, providing reusable methods and structures.
- **`DataController.py`**: Handles data-related operations, such as storing and retrieving files or data records.
- **`NLPController.py`**: Manages natural language processing tasks, including query understanding and semantic search.
- **`ProcessController.py`**: Oversees the file processing pipeline, splitting documents into manageable chunks.
- **`ProjectController.py`**: Coordinates project-wide operations and provides endpoints for higher-level functionalities.
- **`__init__.py`**: Initializes the package.

### **Workflow:**
1. **Routes** call the respective **controller** to handle incoming requests.
2. Controllers orchestrate calls to **helpers**, **models**, or external services (e.g., vector DB or LLMs).
3. Controllers prepare the response to be sent back to the API routes.

---

### **3. helpers/**
The **helpers** folder provides utility scripts and configuration settings that are reused across the project.

- **`config.py`**: Centralized configuration for environment variables, database connections, and other settings.
- **`__init__.py`**: Initializes the helpers package.

### **Workflow:**
Helpers are accessed by **controllers** or other components to:
1. Load configurations dynamically (e.g., API keys, database URLs).
2. Provide reusable utility functions.

---

### **4. models/**
This directory defines the **data models** and schemas used throughout the application. These models are critical for data validation, transformation, and storage.

- **`AssetModel.py`**: Represents files and related metadata stored in the database.
- **`BaseDataModel.py`**: A base class for other models, ensuring consistency and reusability.
- **`ChunkModel.py`**: Defines how text is split into smaller pieces (chunks) for efficient processing.
- **`db_schemes/`**: Contains database schema definitions for MongoDB collections.
- **`enums/`**: Provides enumerations for standardizing fixed values (e.g., file types, statuses).
- **`ProjectModel.py`**: Manages project-specific data models, such as project settings or configurations.
- **`__init__.py`**: Initializes the models package.

### **Workflow:**
1. **Controllers** call models to validate data or interact with the database.
2. Models handle schema definition, database operations, and data consistency.

---

### **5. routes/**
Defines the API endpoints and maps them to their respective controllers. This folder organizes the API logic for modularity and scalability.

- **`base.py`**: Defines basic endpoints for general-purpose use.
- **`data.py`**: Handles endpoints for uploading, downloading, and retrieving data.
- **`nlp.py`**: Provides endpoints for semantic search and NLP-related tasks.
- **`schemes/`**: Contains Pydantic schemas for validating API request and response payloads.
- **`__init__.py`**: Initializes the routes package.

### **Workflow:**
1. A client sends an HTTP request to an endpoint defined in **routes**.
2. The route invokes the corresponding **controller** method.
3. After processing, a response is sent back to the client.

---

### **6. stores/**
The **stores** directory contains components for managing external integrations, specifically LLMs (Large Language Models) and vector databases.

- **`llm/`**: Manages the integration and usage of LLMs, such as GPT models.
- **`vectordb/`**: Handles operations on the vector database (e.g., QDrant), enabling semantic search and retrieval.

### **Workflow:**
1. **Controllers** interact with **stores** to process complex tasks.
   - For instance, the **NLPController** may query the **vectordb** to retrieve relevant document chunks based on a user query.
2. Results are processed and returned to the **controller** for further action.

---

## Application Workflow

The following steps explain the typical workflow in the application:

### 1. **Uploading a File**
- **Routes (data.py)**: The `/upload` endpoint receives the file.
- **DataController.py**: Validates and stores the file in the database via the **AssetModel**.
- **ProcessController.py**: Processes the file into text chunks using **ChunkModel**, stores the chunks in the **vectordb**, and updates metadata in the database.

### 2. **Semantic Search**
- **Routes (nlp.py)**: The `/search` endpoint receives a user query.
- **NLPController.py**: Processes the query using an LLM from the **stores/llm/** and retrieves relevant chunks from **stores/vectordb/**.
- **Response**: Combines the LLM output with retrieved data chunks to generate an augmented answer.

### 3. **Project Management**
- **Routes (base.py or project-specific)**: Provides project-level configurations and summaries.
- **ProjectController.py**: Coordinates project-wide operations like fetching stats or configuring settings.



## Requirements

- Python 3.8 or later

#### Install Python using MiniConda

1) Download and install MiniConda from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)
2) Create a new environment using the following command:
```bash
$ conda create -n mini-rag python=3.8
```
3) Activate the environment:
```bash
$ conda activate mini-rag
```

### (Optional) Setup you command line interface for better readability

```bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```


## Installation

### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.

## Run Docker Compose Services

```bash
$ cd docker
$ cp .env.example .env
```

- update `.env` with your credentials



```bash
$ cd docker
$ sudo docker compose up -d
```

## Run the FastAPI server

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

## POSTMAN Collection

Download the POSTMAN collection from [/assets/mini-rag-app.postman_collection.json](/assets/mini-rag-app.postman_collection.json)

---

## Conclusion

The **Speaky** project is a scalable, modular implementation of a Mini-RAG system. By following the directory structure and understanding the workflow, developers can easily extend and customize the application for various use cases, such as document retrieval, FAQ systems, and more.


