# Research: Todo Full-Stack Web Application

## Decision: Technology Stack Selection
**Rationale**: Selected the technology stack based on the specification requirements and current industry standards. The combination of Next.js 16+ (App Router), Python FastAPI, SQLModel ORM, and Neon Serverless PostgreSQL provides a modern, scalable, and secure foundation for the multi-user todo application.

**Alternatives considered**:
- Backend: Django vs FastAPI - Chose FastAPI for better performance and modern async support
- Frontend: React with Create React App vs Next.js - Chose Next.js for built-in routing and SSR capabilities
- Auth: Custom JWT implementation vs Better Auth - Chose Better Auth for battle-tested solution and ease of integration
- DB: SQLite vs PostgreSQL - Chose Neon Serverless PostgreSQL for scalability and production-readiness

## Decision: Authentication Strategy
**Rationale**: Implemented stateless JWT-based authentication to maintain consistency with the backend's stateless nature. Better Auth provides a secure, well-maintained solution that handles JWT generation, validation, and refresh mechanisms.

**Alternatives considered**:
- Session-based authentication - Rejected as it violates the stateless backend requirement
- OAuth providers only - Rejected as email/password authentication is required per spec
- Custom JWT implementation - Rejected as Better Auth offers more security features and reduces risk

## Decision: Database Design Approach
**Rationale**: Using SQLModel as the ORM provides a modern approach with Pydantic integration, which is perfect for FastAPI applications. Neon Serverless PostgreSQL offers auto-scaling capabilities and excellent performance characteristics for the application's requirements.

**Alternatives considered**:
- SQLAlchemy alone - Rejected as SQLModel provides better integration with Pydantic models
- MongoDB - Rejected as relational structure needed for user-task relationships
- Traditional PostgreSQL vs Serverless - Chose serverless for easier scaling and cost-effectiveness

## Decision: API Endpoint Structure
**Rationale**: Following RESTful principles with user-specific routes (e.g., `/api/{user_id}/tasks`) ensures proper data isolation while maintaining API clarity. This approach naturally enforces the requirement that users can only access their own data.

**Alternatives considered**:
- JWT-decoded user ID from token - Rejected as explicit user_id in route makes debugging easier and provides an additional validation layer
- Generic task endpoints with filter parameters - Rejected as user-specific routes better express the security model

## Decision: Frontend State Management
**Rationale**: Using Next.js App Router with React Server Components where appropriate, and client components for interactive features. JWT tokens will be stored in httpOnly cookies when possible or in secure local storage with proper protection measures.

**Alternatives considered**:
- Redux/Zustand for state management - Rejected as Next.js App Router provides sufficient data fetching capabilities
- Client-side routing vs App Router - Chose App Router for better SEO and initial load performance

## Decision: Task Status Management
**Rationale**: Using enum values for task status (to-do, in-progress, completed) provides clear semantics while being efficient in the database. Priority levels (low, medium, high) offer practical categorization without complexity.

**Alternatives considered**:
- Boolean 'completed' field vs status enum - Chose enum for better UX with in-progress tasks
- Numeric priority vs text labels - Chose text labels for better clarity and potential i18n support