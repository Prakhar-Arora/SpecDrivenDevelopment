import '../styles/Home.css'

export default function Home({ categories, onSelectCategory }) {
    return (
        <div className="home-container">
            <div className="home-content">
                <div className="header-section">
                    <h1 className="main-title">Quiz Challenge</h1>
                    <p className="subtitle">Test your knowledge with progressive hints. Can you guess it all?</p>
                </div>

                <div className="categories-grid">
                    {categories.map((category) => (
                        <div
                            key={category.id}
                            className="category-card"
                            style={{ borderColor: category.color }}
                            onClick={() => onSelectCategory(category.id)}
                        >
                            <div className="category-header" style={{ backgroundColor: category.color }}>
                                <h2>{category.title}</h2>
                            </div>
                            <p className="category-description">{category.description}</p>
                            <button className="start-button" style={{ backgroundColor: category.color }}>
                                Start Quiz
                            </button>
                        </div>
                    ))}
                </div>

                <div className="info-section">
                    <div className="info-card">
                        <span className="info-icon">💡</span>
                        <h3>How it works</h3>
                        <p>Receive 5 progressive hints and guess the answer before the final clue</p>
                    </div>
                    <div className="info-card">
                        <span className="info-icon">🎯</span>
                        <h3>Challenge yourself</h3>
                        <p>Each category offers unique questions to expand your knowledge</p>
                    </div>
                    <div className="info-card">
                        <span className="info-icon">⭐</span>
                        <h3>Learn & Enjoy</h3>
                        <p>Discover fascinating facts from science, history, and celebrity world</p>
                    </div>
                </div>
            </div>
        </div>
    )
}
