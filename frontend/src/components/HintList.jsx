/**
 * HintList component displays quiz hints in order.
 */

export function HintList({ hints, visibleCount = 0 }) {
    if (!hints || hints.length === 0) {
        return <div className="hints-empty">No hints available</div>;
    }

    const visibleHints = hints.slice(0, visibleCount);
    if (visibleHints.length === 0) {
        return <div className="hints-empty">No hints revealed yet</div>;
    }

    return (
        <div className="hints-list">
            {visibleHints.map((hint) => (
                <div key={hint.order} className="hint-item">
                    <span className="hint-number">{hint.order}</span>
                    <span className="hint-text">{hint.text}</span>
                </div>
            ))}
        </div>
    );
}
