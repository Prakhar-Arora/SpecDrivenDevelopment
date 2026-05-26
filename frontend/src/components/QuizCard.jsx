/**
 * QuizCard component combining category display, hints, and input.
 */

import { HintList } from "./HintList";
import { AnswerInput } from "./AnswerInput";
import { ResultDisplay } from "./ResultDisplay";

export function QuizCard({
    quiz,
    result,
    loading,
    onSubmitAnswer,
    onNextQuiz,
    revealedHints,
    attempts,
    onRevealHint,
    showAnswer,
    onRevealAnswer,
}) {
    if (!quiz) return null;

    const categoryNames = {
        science: "Science",
        history: "History",
        celebrity: "Celebrity",
    };

    return (
        <div className="quiz-card">
            <div className="quiz-meta">
                <span className="quiz-chip">
                    {categoryNames[quiz.category] || quiz.category}
                </span>
            </div>

            <div className="quiz-title-row">
                <h2>Progressive hints</h2>
                <div className="quiz-meta-row">
                    <span className="quiz-count">
                        {revealedHints}/{quiz.hints?.length || 0} revealed
                    </span>
                    <span className="attempt-pill">Tries: {attempts}</span>
                </div>
            </div>

            <div className="quiz-content">
                <section className="hints-section">
                    <div className="hint-controls">
                        <button
                            type="button"
                            className="hint-button"
                            onClick={onRevealHint}
                            disabled={
                                loading ||
                                result ||
                                revealedHints >= (quiz.hints?.length || 0)
                            }
                        >
                            Reveal next hint
                        </button>
                        <span className="hint-status">
                            {revealedHints >= (quiz.hints?.length || 0)
                                ? "All hints revealed"
                                : "Tap to reveal when you need it"}
                        </span>
                    </div>
                    <HintList hints={quiz.hints} visibleCount={revealedHints} />
                </section>

                {!result && (
                    <section className="input-section">
                        <AnswerInput onSubmit={onSubmitAnswer} disabled={loading} />
                    </section>
                )}

                {result && (
                    <ResultDisplay
                        result={result}
                        onNextQuiz={onNextQuiz}
                        showAnswer={showAnswer}
                        onRevealAnswer={onRevealAnswer}
                    />
                )}
            </div>
        </div>
    );
}
