"""
Quiz Service Backend - FastAPI Application
A modern backend for interactive quizzes with progressive hints system.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
from typing import List

# Initialize FastAPI app
app = FastAPI(
    title="Quiz Service API",
    description="Interactive Quiz Service with Progressive Hints",
    version="1.0.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Quiz Data Structure
class QuizData:
    def __init__(self, hints: List[str], answer: str):
        self.hints = hints
        self.answer = answer

    def to_dict(self):
        return {"hints": self.hints, "answer": self.answer}


# Science Quiz Data
SCIENCE_QUIZZES = [
    QuizData(
        hints=[
            "I am a force that attracts all objects with mass.",
            "I slow down objects thrown upward.",
            "I am responsible for keeping planets in orbit.",
            "Without me, you would float off Earth.",
            "Isaac Newton discovered the laws governing me.",
        ],
        answer="Gravity",
    ),
    QuizData(
        hints=[
            "I am the smallest unit of matter.",
            "I am made of protons, neutrons, and electrons.",
            "I have a nucleus at my center.",
            "I combine with other atoms to form molecules.",
            "Hydrogen is the simplest type of me.",
        ],
        answer="Atom",
    ),
    QuizData(
        hints=[
            "I am the study of living organisms.",
            "I try to understand how life evolves.",
            "Charles Darwin developed theories about me.",
            "I examine cells, genetics, and ecosystems.",
            "I am one of the three major sciences.",
        ],
        answer="Biology",
    ),
    QuizData(
        hints=[
            "I am a state of matter, like ice or water vapor.",
            "I flow and take the shape of my container.",
            "Most of me on Earth is salty.",
            "I cover about 70% of Earth's surface.",
            "I am essential for all known life.",
        ],
        answer="Water",
    ),
    QuizData(
        hints=[
            "I am the process plants use to make food.",
            "I use sunlight, water, and carbon dioxide.",
            "I produce oxygen as a byproduct.",
            "I am the reason plants are green.",
            "Without me, most life on Earth couldn't exist.",
        ],
        answer="Photosynthesis",
    ),
]

# History Quiz Data
HISTORY_QUIZZES = [
    QuizData(
        hints=[
            "I am a year that changed world history.",
            "World War II started in this year.",
            "A German leader invaded Poland.",
            "This year led to millions of deaths.",
            "I am 1939.",
        ],
        answer="1939",
    ),
    QuizData(
        hints=[
            "I am a famous document.",
            "I was written in 1776.",
            "American colonies used me to declare independence.",
            "I begin with 'We hold these truths to be self-evident.'",
            "I am the Declaration of Independence.",
        ],
        answer="Declaration of Independence",
    ),
    QuizData(
        hints=[
            "I am an ancient wonder.",
            "I was built as a tomb.",
            "I am located in Egypt.",
            "I have triangular sides.",
            "I am the Great Pyramid of Giza.",
        ],
        answer="Great Pyramid of Giza",
    ),
    QuizData(
        hints=[
            "I am a famous wall that no longer divides.",
            "I split a city and a country.",
            "I fell in 1989.",
            "I separated East and West.",
            "I am the Berlin Wall.",
        ],
        answer="Berlin Wall",
    ),
    QuizData(
        hints=[
            "I am a period of human history.",
            "I followed the Middle Ages.",
            "Great artists and thinkers lived during me.",
            "Leonardo da Vinci was born during me.",
            "I am the Renaissance.",
        ],
        answer="Renaissance",
    ),
]

# Celebrity Quiz Data
CELEBRITY_QUIZZES = [
    QuizData(
        hints=[
            "I am an actress and filmmaker.",
            "I am known for action and sci-fi movies.",
            "I starred in a franchise involving blue aliens.",
            "My name starts with Z.",
            "I am Zoe Saldana.",
        ],
        answer="Zoe Saldana",
    ),
    QuizData(
        hints=[
            "I am a singer and entrepreneur.",
            "I revolutionized the music industry.",
            "I am known for my influence on fashion.",
            "My real name is Beyoncé Knowles.",
            "I am Beyoncé.",
        ],
        answer="Beyoncé",
    ),
    QuizData(
        hints=[
            "I am a filmmaker and producer.",
            "I have won multiple Academy Awards.",
            "I directed films about space and the deep ocean.",
            "My name is James.",
            "I am James Cameron.",
        ],
        answer="James Cameron",
    ),
    QuizData(
        hints=[
            "I am a tech entrepreneur.",
            "I founded one of the world's largest companies.",
            "I stepped down as CEO in 2014.",
            "I am known for Windows and Microsoft.",
            "I am Bill Gates.",
        ],
        answer="Bill Gates",
    ),
    QuizData(
        hints=[
            "I am a soccer player.",
            "I am known as one of the greatest of all time.",
            "I have won multiple international titles.",
            "My first name is Cristiano.",
            "I am Cristiano Ronaldo.",
        ],
        answer="Cristiano Ronaldo",
    ),
]


# Endpoints
@app.get("/", tags=["Health"])
async def root():
    """Root endpoint - Health check"""
    return {
        "status": "ok",
        "message": "Quiz Service API is running",
        "version": "1.0.0",
    }


@app.get("/nature", tags=["Quizzes"])
async def nature_quiz():
    """
    Science Quiz Endpoint
    Returns a random science quiz with 5 progressive hints.

    Returns:
        - hints: List of 5 hints from general to specific
        - answer: The correct answer
    """
    quiz = random.choice(SCIENCE_QUIZZES)
    return quiz.to_dict()


@app.get("/old", tags=["Quizzes"])
async def history_quiz():
    """
    History Quiz Endpoint
    Returns a random history quiz with 5 progressive hints.

    Returns:
        - hints: List of 5 hints from general to specific
        - answer: The correct answer
    """
    quiz = random.choice(HISTORY_QUIZZES)
    return quiz.to_dict()


@app.get("/fame", tags=["Quizzes"])
async def celebrity_quiz():
    """
    Celebrity Quiz Endpoint
    Returns a random celebrity quiz with 5 progressive hints.

    Returns:
        - hints: List of 5 hints from general to specific
        - answer: The correct answer
    """
    quiz = random.choice(CELEBRITY_QUIZZES)
    return quiz.to_dict()


# Additional endpoints for documentation
@app.get("/quizzes/all", tags=["Documentation"])
async def get_all_quizzes():
    """Get all available quizzes (for documentation purposes)"""
    return {
        "science": len(SCIENCE_QUIZZES),
        "history": len(HISTORY_QUIZZES),
        "celebrity": len(CELEBRITY_QUIZZES),
        "total": len(SCIENCE_QUIZZES) + len(HISTORY_QUIZZES) + len(CELEBRITY_QUIZZES),
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
