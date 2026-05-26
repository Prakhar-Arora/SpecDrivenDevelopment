/**
 * ResultDisplay component shows correct/incorrect feedback.
 */

export function ResultDisplay({ result, onNextQuiz, showAnswer, onRevealAnswer }) {
    if (!result) return null;

    const isCorrect = result.is_correct;
    const shouldShowAnswer = isCorrect || showAnswer;

    return (
        <div className={`result-display result-${isCorrect ? "correct" : "incorrect"}`}>
            <div className="result-banner">
                <div className="result-icon">{isCorrect ? "✓" : "✗"}</div>
                <div>
                    <p className="result-title">{isCorrect ? "Correct" : "Not quite"}</p>
                    <p className="result-message">{result.message}</p>
                </div>
            </div>
            {result.correct_answer && shouldShowAnswer && (
                <p className="correct-answer">
                    The answer was: <strong>{result.correct_answer}</strong>
                </p>
            )}
            {!isCorrect && result.correct_answer && !showAnswer && (
                <button
                    type="button"
                    onClick={onRevealAnswer}
                    className="reveal-button"
                >
                    Reveal answer
                </button>
            )}
            <button onClick={onNextQuiz} className="next-button">
                Next Quiz
            </button>
        </div>
    );
}
