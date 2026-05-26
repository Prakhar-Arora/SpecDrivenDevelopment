/**
 * Quiz Service App - Main React component with state management
 */

import { useState, useEffect } from "react";
import "./App.css";
import {
    CategorySelector,
    QuizCard,
} from "./components/index";
import { getQuiz, submitAnswer, checkHealth } from "./services/api";

function App() {
    const [currentQuiz, setCurrentQuiz] = useState(null);
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [apiReady, setApiReady] = useState(false);
    const [revealedHints, setRevealedHints] = useState(1);
    const [attempts, setAttempts] = useState(0);
    const [showAnswer, setShowAnswer] = useState(false);
    const statusText = apiReady ? "API Online" : error ? "API Offline" : "Connecting";

    // Check API health on mount
    useEffect(() => {
        checkHealth()
            .then(() => setApiReady(true))
            .catch((err) => {
                setError("Backend API is not available. Please ensure the backend server is running on http://localhost:8000");
                console.error("API health check failed:", err);
            });
    }, []);

    const handleRetryConnection = async () => {
        setError(null);
        setApiReady(false);

        try {
            await checkHealth();
            setApiReady(true);
        } catch (err) {
            setError("Backend API is not available. Please ensure the backend server is running on http://localhost:8000");
            console.error("API health check failed:", err);
        }
    };

    // Load quiz for selected category
    const handleSelectCategory = async (category) => {
        setLoading(true);
        setError(null);
        setResult(null);
        setRevealedHints(1);
        setAttempts(0);
        setShowAnswer(false);

        try {
            const quiz = await getQuiz(category);
            setCurrentQuiz(quiz);
        } catch (err) {
            setError(`Failed to load quiz: ${err.message}`);
            console.error("Error loading quiz:", err);
        } finally {
            setLoading(false);
        }
    };

    // Submit answer for validation
    const handleSubmitAnswer = async (answer) => {
        if (!currentQuiz) return;

        setLoading(true);
        setError(null);
        setAttempts((prev) => prev + 1);
        setShowAnswer(false);

        try {
            const validationResult = await submitAnswer(currentQuiz.id, answer);
            setResult(validationResult);
        } catch (err) {
            setError(`Failed to validate answer: ${err.message}`);
            console.error("Error validating answer:", err);
        } finally {
            setLoading(false);
        }
    };

    // Load next quiz from same category
    const handleNextQuiz = async () => {
        if (!currentQuiz) return;

        const categoryMap = {
            science: "nature",
            history: "old",
            celebrity: "fame",
        };

        const categoryId = categoryMap[currentQuiz.category];
        await handleSelectCategory(categoryId);
    };

    const handleRevealHint = () => {
        if (!currentQuiz) return;
        setRevealedHints((prev) => Math.min(prev + 1, currentQuiz.hints.length));
    };

    const handleRevealAnswer = () => {
        setShowAnswer(true);
    };

    return (
        <div className="app">
            <div className="ambient-grid" aria-hidden="true" />
            <header className="site-header">
                <div className="brand">
                    <div className="brand-mark">QZ</div>
                    <div>
                        <p className="brand-title">Quiz Service</p>
                        <p className="brand-tag">Curated clues, quick wins.</p>
                    </div>
                </div>
                <div className={`status-pill ${apiReady ? "online" : "offline"}`}>
                    <span className="status-dot" />
                    <span>{statusText}</span>
                </div>
            </header>

            <main className="layout">
                <section className="hero-panel">
                    <div className="hero-copy">
                        <h1>Guess with momentum.</h1>
                        <p>
                            Five progressive hints. Three categories. Fast feedback. Pick a
                            lane and sharpen your instincts.
                        </p>
                        <div className="hero-stats">
                            <div className="stat-card">
                                <p className="stat-label">Categories</p>
                                <p className="stat-value">3</p>
                            </div>
                            <div className="stat-card">
                                <p className="stat-label">Hints per quiz</p>
                                <p className="stat-value">5</p>
                            </div>
                            <div className="stat-card">
                                <p className="stat-label">Status</p>
                                <p className="stat-value">Live</p>
                            </div>
                        </div>
                        <div className="hero-note">
                            Tip: short answers work best. Try a single word or name.
                        </div>
                    </div>

                    <div className="hero-card">
                        {error && (
                            <div className="error-message">
                                <p>{error}</p>
                                <button
                                    className="ghost-button"
                                    type="button"
                                    onClick={handleRetryConnection}
                                >
                                    Retry connection
                                </button>
                            </div>
                        )}

                        {!apiReady && !error && (
                            <div className="loading-message">
                                <div className="spinner" aria-hidden="true" />
                                <p>Connecting to API...</p>
                            </div>
                        )}

                        {apiReady && !currentQuiz && (
                            <CategorySelector
                                onSelectCategory={handleSelectCategory}
                                disabled={loading}
                            />
                        )}
                    </div>
                </section>

                <section className="play-panel">
                    {currentQuiz ? (
                        <QuizCard
                            quiz={currentQuiz}
                            result={result}
                            loading={loading}
                            onSubmitAnswer={handleSubmitAnswer}
                            onNextQuiz={handleNextQuiz}
                            revealedHints={revealedHints}
                            attempts={attempts}
                            onRevealHint={handleRevealHint}
                            showAnswer={showAnswer}
                            onRevealAnswer={handleRevealAnswer}
                        />
                    ) : (
                        <div className="empty-state">
                            <div className="empty-visual">
                                <div className="orb" />
                                <div className="orb" />
                                <div className="orb" />
                            </div>
                            <h3>Ready when you are.</h3>
                            <p>Select a category to load your first quiz.</p>
                        </div>
                    )}
                </section>
            </main>

            <footer className="app-footer">
                <div>
                    <p>
                        Backend API: <code>http://localhost:8000</code>
                    </p>
                    <p>
                        API Docs:{" "}
                        <a href="http://localhost:8000/docs" target="_blank" rel="noreferrer">
                            Swagger UI
                        </a>{" "}
                        |{" "}
                        <a href="http://localhost:8000/redoc" target="_blank" rel="noreferrer">
                            ReDoc
                        </a>
                    </p>
                </div>
                <p className="footer-meta">Built for quick, delightful quizzes.</p>
            </footer>
        </div>
    );
}

export default App;
