/**
 * CategorySelector component with category buttons.
 */

const CATEGORIES = [
    { id: "nature", label: "Nature", displayName: "Science" },
    { id: "old", label: "History", displayName: "History" },
    { id: "fame", label: "Celebrity", displayName: "Celebrity" },
];

export function CategorySelector({ onSelectCategory, disabled = false }) {
    return (
        <div className="category-selector">
            <h2>Pick your lane</h2>
            <p className="category-subtitle">Each round stacks five hints. Choose your vibe.</p>
            <div className="category-buttons">
                {CATEGORIES.map((cat) => (
                    <button
                        key={cat.id}
                        onClick={() => onSelectCategory(cat.id)}
                        disabled={disabled}
                        className="category-button"
                        title={cat.displayName}
                    >
                        <span className="category-title">{cat.label}</span>
                        <span className="category-caption">{cat.displayName}</span>
                    </button>
                ))}
            </div>
        </div>
    );
}
