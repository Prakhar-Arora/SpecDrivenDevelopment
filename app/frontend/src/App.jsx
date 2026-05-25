import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'
import Home from './components/Home'
import Quiz from './components/Quiz'
import Loading from './components/Loading'
import Error from './components/Error'

const API_BASE_URL = 'http://localhost:8000'

function App() {
  const [currentPage, setCurrentPage] = useState('home')
  const [selectedCategory, setSelectedCategory] = useState(null)
  const [quizData, setQuizData] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [hints, setHints] = useState([])
  const [currentHintIndex, setCurrentHintIndex] = useState(0)
  const [userAnswer, setUserAnswer] = useState('')
  const [showAnswer, setShowAnswer] = useState(false)
  const [isCorrect, setIsCorrect] = useState(null)

  const categories = [
    { id: 'nature', title: '🧪 Science Quiz', description: 'Test your scientific knowledge', color: '#6366f1' },
    { id: 'old', title: '📚 History Quiz', description: 'Challenge your historical expertise', color: '#ec4899' },
    { id: 'fame', title: '⭐ Celebrity Quiz', description: 'Identify famous personalities', color: '#f59e0b' },
  ]

  const fetchQuiz = async (categoryId) => {
    setLoading(true)
    setError(null)
    try {
      const response = await axios.get(`${API_BASE_URL}/${categoryId}`)
      setQuizData(response.data)
      setHints(response.data.hints || [])
      setCurrentHintIndex(0)
      setUserAnswer('')
      setShowAnswer(false)
      setIsCorrect(null)
      setSelectedCategory(categoryId)
      setCurrentPage('quiz')
    } catch (err) {
      setError(`Failed to fetch quiz. Make sure the backend is running on ${API_BASE_URL}`)
      console.error('Error fetching quiz:', err)
    } finally {
      setLoading(false)
    }
  }

  const handleCategorySelect = (categoryId) => {
    fetchQuiz(categoryId)
  }

  const handleSubmitAnswer = () => {
    const correct = userAnswer.toLowerCase().trim() === (quizData?.answer || '').toLowerCase().trim()
    setIsCorrect(correct)
    setShowAnswer(true)
  }

  const handleNextQuestion = () => {
    fetchQuiz(selectedCategory)
  }

  const handleBackToHome = () => {
    setCurrentPage('home')
    setSelectedCategory(null)
    setQuizData(null)
    setHints([])
    setCurrentHintIndex(0)
    setUserAnswer('')
    setShowAnswer(false)
    setIsCorrect(null)
  }

  return (
    <div className="app-container">
      {loading && <Loading />}
      {error && <Error message={error} onDismiss={() => setError(null)} />}

      {!loading && !error && currentPage === 'home' && (
        <Home categories={categories} onSelectCategory={handleCategorySelect} />
      )}

      {!loading && !error && currentPage === 'quiz' && quizData && (
        <Quiz
          quizData={quizData}
          hints={hints}
          currentHintIndex={currentHintIndex}
          setCurrentHintIndex={setCurrentHintIndex}
          userAnswer={userAnswer}
          setUserAnswer={setUserAnswer}
          onSubmitAnswer={handleSubmitAnswer}
          showAnswer={showAnswer}
          isCorrect={isCorrect}
          onNextQuestion={handleNextQuestion}
          onBackToHome={handleBackToHome}
          selectedCategory={selectedCategory}
        />
      )}
    </div>
  )
}

export default App
