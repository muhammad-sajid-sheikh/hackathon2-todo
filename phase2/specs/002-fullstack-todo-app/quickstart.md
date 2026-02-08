# Quickstart Guide: Todo Full-Stack Web Application

## Prerequisites

- Python 3.11+
- Node.js 18+
- Docker and Docker Compose (for local development)
- Neon PostgreSQL account and connection string

## Setup Instructions

### 1. Environment Configuration

Create a `.env` file in the project root with the following variables:

```env
# Database Configuration
DATABASE_URL="postgresql://username:password@ep-xxx.us-east-1.aws.neon.tech/dbname?sslmode=require"

# Authentication Configuration
AUTH_SECRET="your-super-secret-jwt-secret-here"
AUTH_TRUST_HOST=true

# Application Configuration
BACKEND_CORS_ORIGINS=["http://localhost:3000"]

# Better Auth Configuration
BETTER_AUTH_URL="http://localhost:8000"
BETTER_AUTH_SECRET="your-better-auth-secret"
```

### 2. Backend Setup (FastAPI)

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up the database:
```bash
python -m src.database.setup
```

4. Run the backend server:
```bash
uvicorn src.main:app --reload --port 8000
```

### 3. Frontend Setup (Next.js)

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

4. Visit `http://localhost:3000` to access the application.

## Running Tests

### Backend Tests
```bash
cd backend
pytest tests/
```

### Frontend Tests
```bash
cd frontend
npm run test
```

## API Endpoints

### Task Management
- `GET /api/{user_id}/tasks` - Get all tasks for a user
- `POST /api/{user_id}/tasks` - Create a new task
- `GET /api/{user_id}/tasks/{id}` - Get a specific task
- `PUT /api/{user_id}/tasks/{id}` - Update a task
- `DELETE /api/{user_id}/tasks/{id}` - Delete a task
- `PATCH /api/{user_id}/tasks/{id}/complete` - Toggle task completion

### Authentication
- Better Auth provides standard endpoints for login, signup, and logout

## Development Workflow

1. Create a feature branch from `main`
2. Implement changes following the specification
3. Write/update tests for new functionality
4. Run all tests to ensure nothing is broken
5. Submit a pull request with clear description of changes
6. Wait for code review and approval

## Deployment

### Using Docker
```bash
docker-compose up --build
```

### Environment Variables for Production
Make sure to set appropriate environment variables for production deployment, especially:
- Secure JWT secrets
- Production database URL
- CORS settings
- Authentication provider configuration