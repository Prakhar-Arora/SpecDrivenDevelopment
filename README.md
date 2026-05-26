# Quiz Service API

A FastAPI-based quiz service that challenges users to guess words, events, and people based on five progressive hints.

## Overview

This application provides an interactive quiz experience with three specialized quiz categories. Players receive five hints and must guess the correct answer for each round.

## Endpoints

### 1. `/nature` - Science Quiz

Test your knowledge of scientific concepts, natural phenomena, and scientific breakthroughs.

- **Category**: Science
- **Task**: Guess the scientific word or concept
- **Hints**: 5 progressive hints to guide you

### 2. `/old` - History Quiz

Challenge yourself with historical events, dates, and significant moments in history.

- **Category**: History
- **Task**: Guess the historical event
- **Hints**: 5 progressive hints from broad to specific

### 3. `/fame` - Celebrity Quiz

Identify notable personalities, celebrities, and famous figures.

- **Category**: Celebrity
- **Task**: Guess the person's identity
- **Hints**: 5 progressive hints about the person

## How It Works

Each quiz endpoint presents the user with 5 sequential hints. Players must use these hints to deduce the correct answer:

1. First hint: Broad/General information
2. Second hint: Additional context
3. Third hint: More specific details
4. Fourth hint: Closer to the answer
5. Fifth hint: Final clue

## Getting Started

### Requirements

- Python 3.7+
- FastAPI
- Uvicorn

### Installation

```bash
# Install dependencies
pip install fastapi uvicorn

# Run the server
uvicorn main:app --reload
```

The server will start at `http://localhost:8000`

## Usage

### Example Request

```bash
# Access the Nature quiz
curl http://localhost:8000/nature

# Access the History quiz
curl http://localhost:8000/old

# Access the Celebrity quiz
curl http://localhost:8000/fame
```

### Example Response

Each endpoint returns quiz data with 5 hints and expects the user to provide their guess.

## API Documentation

Once the server is running, visit:

- **Interactive docs**: `http://localhost:8000/docs` (Swagger UI)
- **Alternative docs**: `http://localhost:8000/redoc` (ReDoc)

## Project Structure

```
.
├── main.py              # FastAPI application and endpoint definitions
├── README.md            # This file
└── requirements.txt     # Python dependencies (optional)
```

## Features

✓ Three specialized quiz categories  
✓ Progressive hint system  
✓ Interactive API documentation  
✓ RESTful endpoint design  
---

## Project Credits

**Project Maintainer**: Prakhar Arora

- Email: [shri.prakhar.arora@gmail.com](mailto:shri.prakhar.arora@gmail.com)
- GitHub: [@Prakhar-Arora](https://github.com/Prakhar-Arora)


**Built with ❤️**

*Last Updated: May 2026*
