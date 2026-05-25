import { useState } from 'react'
import '../styles/Quiz.css'

export default function Quiz({
    quizData,
    hints,
    currentHintIndex,
    setCurrentHintIndex,
    userAnswer,
    setUserAnswer,
    onSubmitAnswer,
    showAnswer,
    isCorrect,
    onNextQuestion,
    onBackToHome,
    selectedCategory,
}) {
    const categoryEmojis = {
        nature: '🧪',
        old: '📚',
        fame: '⭐',
    }

    const handleRevealHint = () => {
        if (currentHintIndex < hints.length - 1) {
            setCurrentHintIndex(currentHintIndex + 1)
        }
    }

    const handleKeyPress = (e) => {
        if (e.key === 'Enter' && !showAnswer) {
            onSubmitAnswer()
        }
    }

    return (
        <div className="quiz-container">
            <div className="quiz-header">
                <button className="back-button" onClick={onBackToHome}>
                    ← Back
                </button>
                <h1 className="quiz-title">{categoryEmojis[selectedCategory]} Quiz Challenge</h1>
                <div className="hint-counter">
                    Hint {currentHintIndex + 1}/{hints.length}
                </div>
            </div>

            <div className="quiz-content">
                <div className="hints-section">
                    <h2 className="hints-title">Hints</h2>
                    <div className="hints-container">
                        {hints.map((hint, index) => (
                            <div
                                key={index}
                                className={`hint-item ${index <= currentHintIndex ? 'revealed' : 'hidden'} ${index === currentHintIndex ? 'current' : ''
                                    }`}
                            >
                                <span className="hint-number">Hint {index + 1}</span>
                                <p className="hint-text">{index <= currentHintIndex ? hint : '?'}</p>
                            </div>
                        ))}
                    </div>

                    {currentHintIndex < hints.length - 1 && !showAnswer && (
                        <button className="reveal-hint-button" onClick={handleRevealHint}>
                            Reveal Next Hint →
                        </button>
                    )}
                </div>

                <div className="answer-section">
                    <h2 className="answer-title">Your Answer</h2>

                    {!showAnswer ? (
                        <>
                            <input
                                type="text"
                                className="answer-input"
                                placeholder="Type your answer here..."
                                value={userAnswer}
                                onChange={(e) => setUserAnswer(e.target.value)}
                                onKeyPress={handleKeyPress}
                                disabled={showAnswer}
                            />
                            <button className="submit-button" onClick={onSubmitAnswer} disabled={!userAnswer.trim()}>
                                Submit Answer
                            </button>
                        </>
                    ) : (
                        <div className={`result-section ${isCorrect ? 'correct' : 'incorrect'}`}>
                            <div className="result-icon">
                                {isCorrect ? '✓' : '✗'}
                            </div>
                            <h3 className="result-title">
                                {isCorrect ? 'Correct Answer!' : 'Incorrect'}
                            </h3>
                            <p className="result-message">
                                {isCorrect
                                    ? `Great job! You guessed it correctly!`
                                    : `The correct answer is: `}
                            </p>
                            {!isCorrect && (
                                <p className="correct-answer">{quizData?.answer}</p>
                            )}
                            {isCorrect && (
                                <p className="explanation">{quizData?.answer}</p>
                            )}
                            <button className="next-button" onClick={onNextQuestion}>
                                Next Question →
                            </button>
                        </div>
                    )}
                </div>
            </div>
        </div>
    )
}
