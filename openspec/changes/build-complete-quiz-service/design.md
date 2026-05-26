## Context

Building the Quiz Service API from scratch requires establishing the complete architecture for a three-tier application:

- **Backend**: FastAPI serving quiz endpoints with in-memory question pools
- **Frontend**: Interactive UI for quiz interaction
- **Data Layer**: Type-safe models for Quiz, Category, and Answer objects

Current state: Project directory structure exists but no implementation code. DevOps baseline and deployment infrastructure out of scope.

## Goals / Non-Goals

**Goals:**

- Establish a clean, maintainable API that serves quiz questions with progressive hints
- Build responsive frontend that guides users through quiz interaction
- Define extensible data models for easy category addition
- Implement validation, error handling, and API documentation
- Create production-ready code following project conventions
- Enable phased development with clear layer separation

**Non-Goals:**

- Persistent storage (in-memory only for MVP)
- User authentication or authorization
- Advanced analytics or scoring systems
- Multi-player or competitive features
- Performance optimization beyond basic conventions
- Deployment infrastructure (Azure, Kubernetes, etc.)

## Decisions

### 1. API Architecture: RESTful Endpoints per Category

**Decision**: Implement three separate GET endpoints (`/nature`, `/old`, `/fame`) that each return a complete quiz object with all hints.

**Rationale**:

- Simple, predictable REST pattern
- Easy for frontend to consume
- Matches README specifications
- Clear separation by category

**Alternatives Considered**:

- Single `/quiz` endpoint with category parameter → Less discoverable in API docs
- Streaming hints progressively → Adds complexity, not needed for MVP

**Example API Contract**:

```
GET /nature
{
  "id": "nature_001",
  "category": "science",
  "hints": [
    "I am found throughout nature in various forms",
    "I am essential to all living organisms",
    "I can exist in three states: solid, liquid, and gas",
    "I make up about 70% of the Earth's surface",
    "I am H2O"
  ],
  "answer": "water"
}
```

### 2. Data Models: Strongly Typed with Pydantic

**Decision**: Use Pydantic for type-safe data models in Python backend.

**Rationale**:

- FastAPI integration is seamless
- Automatic validation and documentation
- TypeScript/frontend mirrors possible
- Follows project conventions (type hints)

**Models**:

```python
class Hint(BaseModel):
    order: int
    text: str

class Quiz(BaseModel):
    id: str
    category: str
    hints: List[Hint]
    answer: str

class AnswerSubmission(BaseModel):
    quiz_id: str
    user_answer: str
```

### 3. Quiz Engine: Stateless Service Layer

**Decision**: Implement `QuizService` class that manages quiz logic without persistent state.

**Rationale**:

- Pure functions for hint management and answer validation
- Testable in isolation
- Easy to extend with new categories
- Supports stateless deployment model

**Interface**:

```python
class QuizService:
    def get_quiz(self, category: str) -> Quiz
    def validate_answer(self, quiz_id: str, user_answer: str) -> AnswerValidation
    def get_hint_by_order(self, quiz_id: str, hint_order: int) -> str
```

### 4. Frontend Framework: React with Vite

**Decision**: Use React with Vite as the build tool and dev server for optimal development experience.

**Rationale**:

- Matches Node.js frontend stack in config
- Vite provides significantly faster dev server startup and HMR than traditional webpack
- Component-based architecture mirrors quiz UI naturally
- Rich ecosystem for forms and state management
- Vite's dev server runs on port 5173 by default

**Components**:

- `QuizContainer` (main wrapper, state management)
- `QuizCard` (displays current hints and input)
- `HintList` (renders progressive hints)
- `AnswerInput` (form with validation)
- `ResultDisplay` (correct/incorrect feedback)

### 5. API Documentation: Swagger + ReDoc

**Decision**: Leverage FastAPI's built-in OpenAPI integration at `/docs` and `/redoc`.

**Rationale**:

- Zero configuration needed
- Auto-generates from type hints
- Interactive testing built-in
- Matches README specification

### 6. Error Handling: Standardized HTTP Responses

**Decision**: Return consistent error objects with status codes, messages, and optional details.

**Rationale**:

- Frontend can standardize error handling
- Easier debugging and logging
- Follows REST conventions

**Error Contract**:

```json
{
  "status": 400,
  "error": "invalid_input",
  "message": "Answer cannot be empty",
  "timestamp": "2026-05-26T10:30:00Z"
}
```

### 7. Development Workflow: Dual Servers with Vite

**Decision**: Run backend (`uvicorn`) on port 8000 and frontend (Vite dev server) on port 5173 in separate terminals during development.

**Rationale**:

- Clear separation of concerns
- Easier to debug each layer independently
- Vite's HMR enables instant feedback during frontend development
- Frontend can mock API while backend develops
- Production: frontend built as static files via `npm run build`, served by backend or CDN

## Risks / Trade-offs

| Risk | Impact | Mitigation |
|------|--------|-----------|
| In-memory data loss on restart | Development only, acceptable for MVP | Document limitation; add persistent store in Phase 2 |
| Category data hardcoded in code | Not extensible without code changes | Implement data loader pattern; move to JSON files in Phase 2 |
| No input validation initially | Could accept invalid answers | Add validation layer in tasks phase |
| Frontend-backend coupling | Changes require coordination | Define API contracts clearly in design phase |
| No error handling on edge cases | Production robustness concern | Implement try-catch blocks and error middleware |
| No rate limiting | Potential abuse | Document as Phase 2 feature; add middleware later |

## Implementation Phases

**Phase 1 (Foundation)**: Core API + Basic UI

- Backend: FastAPI entry point, Quiz model, basic endpoints
- Frontend: Quiz card component, hint display, answer submission
- Integration: API contract testing

**Phase 2 (Refinement)**: Error handling, validation, documentation

- Comprehensive error responses
- Input validation (length, special chars)
- API documentation improvements

**Phase 3 (Polish)**: Testing, optimization, user experience

- Unit tests for quiz logic
- End-to-end tests
- UI/UX improvements

## Migration Plan

### Local Development Setup

1. Backend: Install Python 3.7+, FastAPI, Uvicorn → `pip install -r requirements.txt`
2. Frontend: Initialize with Vite via `npm create vite@latest frontend -- --template react` and `npm install`
3. Run backend: `cd backend && uvicorn app.main:app --reload`
4. Run frontend: `cd frontend && npm run dev` (runs on <http://localhost:5173>)
5. Access API docs: `http://localhost:8000/docs`
6. Access frontend: `http://localhost:5173`

### Deployment (Future)

1. Build frontend: `npm run build` → static files
2. Serve with FastAPI: `static_files` mount or separate CDN
3. Deploy to cloud: Container-based (Docker) to Azure Container Instances or AKS

## Open Questions

1. **Category Data Storage**: Where to store quiz questions initially? JSON files or Python dicts?
   - Recommendation: Start with Python dicts in `quiz_data.py`, migrate to JSON files if needed

2. **Frontend Framework Decision**: React vs Vue?
   - Recommendation: React for broader ecosystem; Vue acceptable if team prefers

3. **Answer Validation**: Exact match only or fuzzy matching?
   - Recommendation: Start with exact match (case-insensitive), add fuzzy in Phase 2

4. **Hint Reveal Strategy**: All hints upfront or progressive reveal?
   - Recommendation: All upfront with visual ordering; implement progressive reveal as optional Phase 2 feature

5. **CORS Configuration**: How to handle cross-origin requests?
   - Recommendation: Enable CORS for `localhost:3000` in development; make configurable for production
