/**
 * API client service for Quiz Service backend.
 * Handles all HTTP requests to the backend API.
 */

const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

/**
 * Fetch a quiz from a specific category.
 * @param {string} category - Category name: 'nature', 'old', or 'fame'
 * @returns {Promise<Object>} Quiz object with id, category, hints, answer
 * @throws {Error} If the request fails
 */
export async function getQuiz(category) {
    const categoryEndpoints = {
        nature: "/nature",
        old: "/old",
        fame: "/fame",
    };

    const endpoint = categoryEndpoints[category];
    if (!endpoint) {
        throw new Error(`Invalid category: ${category}`);
    }

    const response = await fetch(`${API_BASE_URL}${endpoint}`);
    if (!response.ok) {
        const error = await response.json();
        throw new Error(error.message || "Failed to fetch quiz");
    }

    return response.json();
}

/**
 * Submit an answer for validation.
 * @param {string} quizId - Quiz ID
 * @param {string} userAnswer - User's answer
 * @returns {Promise<Object>} Validation result with is_correct, message, correct_answer
 * @throws {Error} If the request fails
 */
export async function submitAnswer(quizId, userAnswer) {
    const response = await fetch(`${API_BASE_URL}/validate`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            quiz_id: quizId,
            user_answer: userAnswer,
        }),
    });

    if (!response.ok) {
        const error = await response.json();
        throw new Error(error.message || "Failed to validate answer");
    }

    return response.json();
}

/**
 * Check API health.
 * @returns {Promise<Object>} Health status
 */
export async function checkHealth() {
    const response = await fetch(`${API_BASE_URL}/health`);
    if (!response.ok) {
        throw new Error("API is not available");
    }
    return response.json();
}
