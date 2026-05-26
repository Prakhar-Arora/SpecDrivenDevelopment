## ADDED Requirements

### Requirement: Support for predefined quiz categories

The system SHALL support three quiz categories: Science (nature), History (old), and Celebrity (fame). Each category MUST have its own set of quiz questions with associated hints.

#### Scenario: Science category exists

- **WHEN** user requests science quiz via /nature endpoint
- **THEN** system returns quiz with science-specific hints and answer

#### Scenario: History category exists

- **WHEN** user requests history quiz via /old endpoint
- **THEN** system returns quiz with history-specific hints and answer

#### Scenario: Celebrity category exists

- **WHEN** user requests celebrity quiz via /fame endpoint
- **THEN** system returns quiz with celebrity-specific hints and answer

### Requirement: Category data structure

The system SHALL organize category data in a way that allows easy addition of new categories. Category data MUST include question pool, hints, answers, and category metadata.

#### Scenario: Category data storage

- **WHEN** QuizService initializes
- **THEN** category data is loaded with all questions organized by category identifier

#### Scenario: Category metadata

- **WHEN** quiz is requested
- **THEN** response includes category identifier matching endpoint or parameter

### Requirement: Extensible category system

Adding new categories MUST follow a consistent pattern and require minimal code changes. New categories SHOULD be added by registering new data without modifying endpoint logic.

#### Scenario: Add new category (Phase 2)

- **WHEN** developer wants to add a new category
- **THEN** they add category data following existing pattern and optionally create new endpoint following /<category> pattern

#### Scenario: Consistent category pattern

- **WHEN** new category is added
- **THEN** response format matches existing categories (id, category, hints[], answer)

### Requirement: Each category has minimum 5 hints per quiz

Each category MUST provide a minimum of five hints per quiz question. Hints MUST be ordered progressively from general to specific.

#### Scenario: Complete hint set

- **WHEN** quiz is requested
- **THEN** response includes exactly 5 hints (or configurable minimum)

#### Scenario: Hint progression

- **WHEN** examining hints in order
- **THEN** hints progress from broad/general information (hint 1) to specific answer indicators (hint 5)

### Requirement: Multiple quizzes per category

Each category SHOULD support multiple different quiz questions that users can encounter. System SHOULD return variety to encourage repeat usage.

#### Scenario: Different quiz each session

- **WHEN** user requests same category multiple times
- **THEN** user may receive different quiz (if multiple available) or same quiz (if only one available)

#### Scenario: Question pool

- **WHEN** QuizService is initialized
- **THEN** each category has pool of available questions
