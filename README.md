# Quiz Service

An interactive web application for knowledge quizzes with a FastAPI backend and React frontend. Challenge yourself to guess scientific concepts, historical events, and famous personalities based on progressive hints.

## Overview

This full-stack application provides an engaging quiz experience across three specialized categories. Players receive five sequential hints and must deduce the correct answer before reaching the final clue. The application features a modern React interface backed by a robust FastAPI backend.

## Features

- 🧪 **Science Quiz** (`/nature`) - Test your scientific knowledge with advanced topics
- 📚 **History Quiz** (`/old`) - Challenge your historical expertise with complex events
- ⭐ **Celebrity Quiz** (`/fame`) - Identify brilliant minds and influential figures
- 💡 **Progressive Hints System** - 5 strategic hints per question
- 🎨 **Modern React UI** - Responsive and intuitive user interface
- 📖 **Interactive API Documentation** - Built-in Swagger UI
- 🔥 **Advanced Difficulty** - Challenging questions for serious quiz enthusiasts

## Architecture

```
Quiz Service
├── Backend (FastAPI)
│   ├── /nature    - Science Quiz Endpoint
│   ├── /old       - History Quiz Endpoint
│   └── /fame      - Celebrity Quiz Endpoint
└── Frontend (React)
    └── Interactive Quiz Interface
```

## Technology Stack

**Backend:**

- Python 3.7+
- FastAPI
- Uvicorn

**Frontend:**

- React
- Node.js & npm

## Endpoints

### 1. `/nature` - Science Quiz

**Description:** Advanced quizzes on scientific concepts, theories, and breakthroughs  
**Category:** Science  
**Difficulty:** Advanced  
**Topics Include:** Quantum Field Theory, Entropy, General Relativity, Cosmology, and more  
**Challenge:** Guess the scientific term or concept in 5 hints

### 2. `/old` - History Quiz

**Description:** Complex quizzes on historical events, movements, and significant moments  
**Category:** History  
**Difficulty:** Advanced  
**Topics Include:** Napoleonic Wars, Renaissance, Encomienda System, Peace of Westphalia, and more  
**Challenge:** Identify the historical event in 5 hints

### 3. `/fame` - Celebrity Quiz

**Description:** Challenging quizzes on brilliant minds, scientists, and influential figures  
**Category:** Celebrity  
**Difficulty:** Advanced  
**Topics Include:** Stephen Hawking, Frank Herbert, John Williams, Alan Turing, and more  
**Challenge:** Recognize the person based on 5 hints

## How It Works

1. **Select a Quiz:** Choose from Science, History, or Celebrity categories
2. **Receive Hints:** Get 5 progressive hints, starting from broad to specific
3. **Make Your Guess:** Submit your answer using the hints provided
4. **Learn:** Discover the correct answer and expand your knowledge

The hint progression typically follows this pattern:

- **Hint 1:** General category/background information
- **Hint 2:** Additional context or related facts
- **Hint 3:** More specific identifying characteristics
- **Hint 4:** Stronger clues pointing toward the answer
- **Hint 5:** Final, most direct clue

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Node.js 14+ and npm
- Git

### Backend Setup

1. **Navigate to backend directory:**

   ```bash
   cd backend
   ```

2. **Create a Python virtual environment (recommended):**

   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Python dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Start the FastAPI server:**

   ```bash
   uvicorn app.main:app --reload --port 8000
   ```

   The backend API will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory:**

   ```bash
   cd app/frontend
   ```

2. **Install dependencies:**

   ```bash
   npm install
   ```

3. **Start the React development server:**

   ```bash
   npm run dev
   ```

   The frontend will be available at `http://localhost:5173`

## API Documentation

Interactive API documentation is available when the backend is running:

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

## Project Structure

```
.
├── README.md                    # This file
├── backend/                     # FastAPI backend
│   ├── app/
│   │   ├── main.py              # FastAPI application and endpoints
│   │   ├── science_quizzes.py   # Science quiz questions (8 advanced quizzes)
│   │   ├── history_quizzes.py   # History quiz questions (8 advanced quizzes)
│   │   ├── celebrity_quizzes.py # Celebrity quiz questions (8 advanced quizzes)
│   │   └── __init__.py
│   ├── requirements.txt          # Python dependencies
│   └── .gitignore               # Git ignore rules
└── app/                         # Frontend application
    └── frontend/                # React application (Vite)
        ├── src/
        │   ├── components/       # React components
        │   │   ├── Home.jsx      # Home page with category selection
        │   │   ├── Quiz.jsx      # Quiz interface with hints system
        │   │   ├── Loading.jsx   # Loading component
        │   │   └── Error.jsx     # Error component
        │   ├── styles/           # CSS stylesheets
        │   │   ├── globals.css   # Global styles and animations
        │   │   ├── Home.css      # Home page styles
        │   │   ├── Quiz.css      # Quiz interface styles
        │   │   ├── Loading.css   # Loading component styles
        │   │   └── Error.css     # Error component styles
        │   ├── App.jsx           # Main App component
        │   ├── main.jsx          # Entry point
        │   ├── App.css           # App styles
        │   └── index.css         # Global CSS
        ├── public/               # Static files
        ├── package.json          # npm dependencies
        ├── vite.config.js        # Vite configuration
        └── index.html            # HTML template
```

## Development

### Backend Development

- API changes are hot-reloaded with `--reload` flag
- Refer to [FastAPI documentation](https://fastapi.tiangolo.com/) for framework details
- Interactive API documentation available at `http://localhost:8000/docs`

### Frontend Development

- React hot-reloading is enabled by default
- Refer to [React documentation](https://react.dev/) for framework details
- Modern responsive design with Tailwind-inspired styling
- Built-in error handling and loading states
- Progressive hints system with smooth animations

### Frontend Features

- **Modern UI**: Beautiful dark-themed interface with gradient accents
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Smooth Animations**: Fade-in, slide-in, and pulse animations for better UX
- **Progressive Hints**: Reveals hints one by one as you guess
- **Real-time Validation**: Instant feedback on answer submission
- **Error Handling**: Graceful error display with dismissal option
- **Loading States**: Spinner animation while fetching quizzes
- **Category Selection**: Beautiful card-based interface for choosing quiz categories

### Backend Quiz Data Structure

The quiz questions are organized into three separate modules for maintainability:

- **science_quizzes.py**: 8 advanced science quizzes covering quantum mechanics, thermodynamics, astrophysics, etc.
- **history_quizzes.py**: 8 advanced history quizzes covering historical events, treaties, and movements
- **celebrity_quizzes.py**: 8 advanced quizzes on brilliant minds and influential figures

Each quiz contains:

- **Hints**: 5 progressive hints (general → specific)
- **Answer**: The correct answer string

**Adding New Quizzes:**

1. Open the relevant quiz file (e.g., `backend/app/science_quizzes.py`)
2. Create a new `QuizData` object with 5 hints and an answer
3. Append it to the respective `*_QUIZZES` list
4. The API will automatically randomize questions from the expanded pool

## Troubleshooting

- **Port 8000 already in use:** Change the port with `--port` flag
- **Port 5173 already in use:** Vite will automatically use the next available port, or you can set it manually in `vite.config.js`
- **CORS issues:** Ensure backend is running on port 8000 and frontend on port 5173

## Support

For issues or questions, please [create an issue](https://github.com/yourrepo/issues) or contact the development team.

---

## Project Credits

**Project Maintainer**: Prakhar Arora

- Email: [shri.prakhar.arora@gmail.com](mailto:shri.prakhar.arora@gmail.com)
- GitHub: [@Prakhar-Arora](https://github.com/Prakhar-Arora)

**Built with ❤️**

*Last Updated: May 2026*
