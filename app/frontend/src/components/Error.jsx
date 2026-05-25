import '../styles/Error.css'

export default function Error({ message, onDismiss }) {
    return (
        <div className="error-container">
            <div className="error-box">
                <div className="error-icon">⚠️</div>
                <h3>Oops! Something went wrong</h3>
                <p>{message}</p>
                <button className="error-button" onClick={onDismiss}>
                    Dismiss
                </button>
            </div>
        </div>
    )
}
