## ADDED Requirements

### Requirement: Quiz card displays all quiz information

The frontend SHALL display a quiz card component that shows the quiz question category, all five hints in progressive order, and an input field for the user's answer. The component MUST display hints in a visually distinct manner (e.g., numbered list or stacked cards).

#### Scenario: Display science quiz

- **WHEN** a science quiz is loaded
- **THEN** the quiz card displays "Science" category and all 5 science hints in order

#### Scenario: Hint visibility

- **WHEN** user views the quiz card
- **THEN** all 5 hints are visible with clear ordering (1st hint at top, 5th at bottom)

#### Scenario: Answer input field

- **WHEN** user views the quiz card
- **THEN** an input field is present to enter the answer

### Requirement: Answer submission form

The frontend SHALL provide a form that accepts user input and submits the answer to the backend for validation. The form MUST include input validation, submit button, and error display.

#### Scenario: Submit answer

- **WHEN** user enters answer and clicks submit
- **THEN** the system sends answer to backend and waits for validation response

#### Scenario: Empty input validation

- **WHEN** user clicks submit without entering an answer
- **THEN** the form displays error message and prevents submission

#### Scenario: Input length validation

- **WHEN** user enters extremely long input (>500 characters)
- **THEN** the form limits input or displays warning

### Requirement: Result display after submission

The frontend SHALL display the answer validation result (correct or incorrect) with clear visual feedback. If incorrect, the system SHOULD display the correct answer.

#### Scenario: Correct answer result

- **WHEN** backend validates answer as correct
- **THEN** frontend displays success message in clear, positive visual style (e.g., green background)

#### Scenario: Incorrect answer result

- **WHEN** backend validates answer as incorrect
- **THEN** frontend displays failure message in clear, negative visual style (e.g., red background) with the correct answer

#### Scenario: Next quiz navigation

- **WHEN** user completes a quiz
- **THEN** frontend displays button to load the next quiz category

### Requirement: Quiz category selection

The frontend SHALL provide interface for users to select from available quiz categories (Science, History, Celebrity) before or after each quiz.

#### Scenario: Category selection menu

- **WHEN** frontend loads
- **THEN** user can select from Science, History, or Celebrity categories

#### Scenario: Category buttons

- **WHEN** user views category options
- **THEN** buttons or links are clearly labeled with category names

### Requirement: Responsive design

The frontend UI MUST work on desktop, tablet, and mobile devices with appropriate layout adjustments.

#### Scenario: Desktop layout

- **WHEN** frontend is viewed on desktop (>1024px width)
- **THEN** quiz card displays with full width and optimal readability

#### Scenario: Mobile layout

- **WHEN** frontend is viewed on mobile (<768px width)
- **THEN** quiz card adjusts to mobile width with stacked layout and readable text
