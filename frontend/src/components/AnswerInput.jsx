/**
 * AnswerInput component with form and submit button.
 */

import { useState } from "react";

export function AnswerInput({ onSubmit, disabled = false }) {
    const [answer, setAnswer] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        if (answer.trim()) {
            onSubmit(answer.trim());
            setAnswer("");
        }
    };

    return (
        <form onSubmit={handleSubmit} className="answer-form">
            <label className="answer-label" htmlFor="answer-input">
                Your best guess
            </label>
            <div className="answer-row">
                <input
                    id="answer-input"
                    type="text"
                    value={answer}
                    onChange={(e) => setAnswer(e.target.value)}
                    placeholder="Type a name, place, or thing"
                    disabled={disabled}
                    className="answer-input"
                />
                <button type="submit" disabled={disabled} className="submit-button">
                    Check answer
                </button>
            </div>
        </form>
    );
}
