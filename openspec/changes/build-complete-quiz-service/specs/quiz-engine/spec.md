## ADDED Requirements

### Requirement: Retrieve quiz data for a given category

The system SHALL return a quiz object containing five progressive hints and the correct answer when requested by category. The hints SHALL be sequenced from general to specific to guide the user toward the correct answer.

#### Scenario: Retrieve science quiz

- **WHEN** a user requests a science (nature) quiz
- **THEN** the system returns a Quiz object with id, category="science", 5 hints in progressive order, and the correct answer

#### Scenario: Retrieve history quiz

- **WHEN** a user requests a history (old) quiz
- **THEN** the system returns a Quiz object with id, category="history", 5 hints in progressive order, and the correct answer

#### Scenario: Retrieve celebrity quiz

- **WHEN** a user requests a celebrity (fame) quiz
- **THEN** the system returns a Quiz object with id, category="celebrity", 5 hints in progressive order, and the correct answer

### Requirement: Validate user answer against correct answer

The system SHALL evaluate whether a user's answer matches the correct answer for a given quiz. The validation MUST be case-insensitive and trim whitespace from both sides.

#### Scenario: Correct answer submission

- **WHEN** user submits an answer that matches the correct answer (ignoring case and whitespace)
- **THEN** the system returns validation result indicating correct answer with success status

#### Scenario: Incorrect answer submission

- **WHEN** user submits an answer that does not match the correct answer
- **THEN** the system returns validation result indicating incorrect answer with failure status and the correct answer (optional)

#### Scenario: Answer with whitespace

- **WHEN** user submits an answer with leading or trailing whitespace
- **THEN** the system trims the whitespace and evaluates against the correct answer

#### Scenario: Answer with different casing

- **WHEN** user submits an answer in different case (e.g., "WATER" vs "water")
- **THEN** the system performs case-insensitive comparison and returns correct result

### Requirement: Quiz engine is stateless

The Quiz Service SHALL not maintain state between requests. Each request for a quiz SHALL return consistent data independent of previous requests or sessions.

#### Scenario: Repeated requests return same data

- **WHEN** the same quiz is requested multiple times
- **THEN** the system returns identical quiz data each time (same hints, same answer)

#### Scenario: Multiple concurrent users

- **WHEN** multiple users request quizzes simultaneously
- **THEN** each receives correct data independently without interference
