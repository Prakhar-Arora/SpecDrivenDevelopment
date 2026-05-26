## ADDED Requirements

### Requirement: GET /nature endpoint returns science quiz

The system SHALL provide a GET endpoint at `/nature` that returns a quiz object for science/nature category. The response MUST include an id, category identifier, array of five hints, and the correct answer.

#### Scenario: Request science quiz

- **WHEN** client sends GET request to `/nature`
- **THEN** system returns HTTP 200 with Quiz object containing science hints

#### Scenario: Response format validation

- **WHEN** client receives response from `/nature`
- **THEN** response contains fields: id (string), category (string), hints (array of 5 objects), answer (string)

### Requirement: GET /old endpoint returns history quiz

The system SHALL provide a GET endpoint at `/old` that returns a quiz object for history category. The response MUST include an id, category identifier, array of five hints, and the correct answer.

#### Scenario: Request history quiz

- **WHEN** client sends GET request to `/old`
- **THEN** system returns HTTP 200 with Quiz object containing history hints

#### Scenario: Response structure

- **WHEN** client receives response from `/old`
- **THEN** response contains fields: id (string), category (string), hints (array of 5 objects), answer (string)

### Requirement: GET /fame endpoint returns celebrity quiz

The system SHALL provide a GET endpoint at `/fame` that returns a quiz object for celebrity category. The response MUST include an id, category identifier, array of five hints, and the correct answer.

#### Scenario: Request celebrity quiz

- **WHEN** client sends GET request to `/fame`
- **THEN** system returns HTTP 200 with Quiz object containing celebrity hints

#### Scenario: Response format

- **WHEN** client receives response from `/fame`
- **THEN** response contains fields: id (string), category (string), hints (array of 5 objects), answer (string)

### Requirement: Endpoints return consistent response format

All endpoints (/nature, /old, /fame) SHALL return Quiz objects with identical structure regardless of category to enable consistent frontend handling.

#### Scenario: Cross-endpoint consistency

- **WHEN** client receives responses from any endpoint
- **THEN** all responses have identical JSON structure with same field names and types
