<!-- SYNC IMPACT REPORT
Version change: 1.0.0 → 1.1.0
Modified principles: None (new constitution)
Added sections: All sections (new constitution creation)
Removed sections: None
Templates requiring updates:
  - .specify/templates/plan-template.md ✅ updated
  - .specify/templates/spec-template.md ✅ updated
  - .specify/templates/tasks-template.md ✅ updated
  - .specify/templates/commands/sp.constitution.md ✅ updated
Templates requiring manual review: None
Follow-up TODOs: None
-->

# Todo Full-Stack Web Application Constitution

## Core Principles

### I. Spec-First Development
No implementation occurs without an approved, written specification. Every feature must originate from a documented spec that defines scope, interfaces, and acceptance criteria before any code is written.

### II. Deterministic Reproducibility
All development phases produce deterministic, reproducible outputs. Build, test, and deployment processes must yield identical results across environments given identical inputs.

### III. Security-by-Design
Authentication and authorization are enforced consistently throughout the application. Security measures are integrated from the initial design phase, not added as an afterthought.

### IV. Separation of Concerns
Frontend, backend, authentication, and data layers must remain clearly separated with well-defined interfaces. Components should be independently developable, testable, and deployable.

### V. Agentic Development Enforcement
No manual coding outside of Claude Code prompt-driven generation. All implementation follows the established agentic development workflow: Spec → Plan → Tasks → Implement → Review.

### VI. End-to-End Authentication Consistency
JWT-based authentication works seamlessly from frontend to backend. User identity and authorization are verified at every data access point, with consistent enforcement across all API endpoints.

## Technology Standards

### Backend and Data Layer
- Backend: Python FastAPI for API services
- ORM: SQLModel for database interactions
- Database: Neon Serverless PostgreSQL for cloud-native scalability
- API style: RESTful, resource-oriented endpoints

### Frontend and Authentication
- Frontend: Next.js 16+ (App Router) for modern web application
- Authentication: Better Auth with JWT enabled for secure user management
- All API endpoints require valid JWT tokens after authentication introduction

### Security Standards
- All API endpoints require valid JWT after auth is introduced
- JWT signature verified using shared secret
- User identity must be derived from token, not client input
- Task ownership enforced on every CRUD operation
- Unauthorized access returns HTTP 401
- Forbidden cross-user access returns HTTP 403

## Development Workflow

### Specification Requirements
- Every feature must trace back to a written spec
- All API behaviors must be explicitly defined before planning
- Authentication rules must be enforced at every data access point
- User data isolation is mandatory and non-negotiable

### Implementation Constraints
- No shared database sessions between frontend and backend
- No hardcoded secrets (environment variables only)
- Must support multiple concurrent users
- Backend logic must be stateless and JWT-based
- Frontend must never assume trust without backend verification

### Quality Gates
- Spec-first development: No implementation without approved spec
- Deterministic, reproducible outputs at every phase
- Security-by-design enforcement
- Complete separation of concerns
- Agentic development workflow compliance

## Governance

This constitution establishes the foundational principles governing the Todo Full-Stack Web Application development. All implementation, planning, and development activities must comply with these principles. Any deviation from these principles requires formal amendment documentation with justification. All team members are responsible for ensuring compliance during code reviews, testing, and deployment processes. Version control of specifications, plans, and implementations must align with the constitutional principles defined herein.

**Version**: 1.1.0 | **Ratified**: 2026-02-06 | **Last Amended**: 2026-02-06
