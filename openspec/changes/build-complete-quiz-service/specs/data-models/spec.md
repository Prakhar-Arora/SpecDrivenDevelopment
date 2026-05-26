## ADDED Requirements

### Requirement: Quiz data model

The system SHALL define a Quiz model that represents a complete quiz question with hints and answer. The Quiz model MUST include: id (unique identifier), category (science/history/celebrity), hints (ordered array), and answer (correct response).

#### Scenario: Quiz model structure

- **WHEN** a Quiz object is created
- **THEN** it contains id: string, category: string, hints: array of Hint objects, answer: string

#### Scenario: Quiz serialization

- **WHEN** a Quiz object is serialized to JSON
- **THEN** all fields are present and properly typed in the JSON output

### Requirement: Hint data model

The system SHALL define a Hint model representing a single hint within a quiz. Each Hint MUST include: order (sequence number 1-5), text (the actual hint content), and optional difficulty indicator.

#### Scenario: Hint model structure

- **WHEN** a Hint object is created
- **THEN** it contains order: integer (1-5), text: string

#### Scenario: Hint ordering

- **WHEN** hints are stored in the Quiz model
- **THEN** they are ordered by sequence number from 1 to 5

### Requirement: AnswerSubmission data model

The system SHALL define a model for receiving user answer submissions. The model MUST include: quiz_id (identifies the quiz being answered) and user_answer (the submitted answer text).

#### Scenario: Answer submission structure

- **WHEN** a user submits an answer
- **THEN** the system receives quiz_id (string) and user_answer (string)

### Requirement: AnswerValidation response model

The system SHALL define a response model for answer validation results. The model MUST include: is_correct (boolean), message (human-readable result), and optionally correct_answer (for display after failure).

#### Scenario: Correct answer response

- **WHEN** answer validation is successful
- **THEN** response contains is_correct: true, message describing success

#### Scenario: Incorrect answer response

- **WHEN** answer validation fails
- **THEN** response contains is_correct: false, message describing failure, and correct_answer: string

### Requirement: Type safety with validation

All models SHALL use type hints and validation to ensure data integrity. Models MUST reject invalid data and provide clear error messages.

#### Scenario: Invalid hint order

- **WHEN** hint order is outside range 1-5
- **THEN** model validation fails with clear error message

#### Scenario: Empty required field

- **WHEN** required field (e.g., hint text) is empty or null
- **THEN** model validation fails with clear error message
