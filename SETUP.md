# 🚀 Setup Guide - Codebase Onboarding SaaS

This guide will help you set up the development environment and get the application running locally.

---

## Prerequisites

Make sure you have the following installed:

- **Node.js** 18+ ([Download](https://nodejs.org/))
- **Python** 3.11+ ([Download](https://www.python.org/downloads/))
- **Git** ([Download](https://git-scm.com/downloads))

---

## Step 1: Install Dependencies

### Frontend (Next.js)

```bash
cd frontend
npm install
```

### Backend (FastAPI)

```bash
cd backend
pip install -r requirements.txt
```

---

## Step 2: Set Up Free-Tier Services

### 2.1 Supabase (PostgreSQL + pgvector)

1. Go to [supabase.com](https://supabase.com) and sign up
2. Create a new project
3. Go to **Project Settings** → **Database**
4. Copy the **Connection String** (Transaction mode)
5. In the SQL Editor, run:
   ```sql
   CREATE EXTENSION IF NOT EXISTS vector;
   ```

### 2.2 GitHub OAuth App

1. Go to GitHub → Settings → Developer settings → OAuth Apps
2. Click **New OAuth App**
3. Fill in:
   - **Application name**: Codebase Onboarding (or your choice)
   - **Homepage URL**: `http://localhost:3000`
   - **Authorization callback URL**: `http://localhost:3000/api/auth/callback/github`
4. Copy **Client ID** and **Client Secret**

### 2.3 Upstash Redis

1. Go to [upstash.com](https://upstash.com) and sign up
2. Create a new Redis database (free tier)
3. Copy the **Redis URL**

### 2.4 OpenAI API

1. Go to [platform.openai.com](https://platform.openai.com)
2. Sign up and get $5 free credits
3. Create an API key in **API Keys** section

**Alternative (Free)**: Use [Groq](https://groq.com) or run [Ollama](https://ollama.ai) locally

---

## Step 3: Configure Environment Variables

### Frontend

Create `frontend/.env.local`:

```env
# API Configuration
NEXT_PUBLIC_API_URL=http://localhost:8000

# NextAuth Configuration
NEXTAUTH_URL=http://localhost:3000
NEXTAUTH_SECRET=your-secret-here-generate-with-openssl-rand-base64-32

# GitHub OAuth
GITHUB_ID=your-github-oauth-app-id
GITHUB_SECRET=your-github-oauth-app-secret

# Supabase
NEXT_PUBLIC_SUPABASE_URL=your-supabase-project-url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-supabase-anon-key
```

**Generate NEXTAUTH_SECRET:**
```bash
openssl rand -base64 32
```

### Backend

Create `backend/.env`:

```env
# FastAPI Configuration
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=True

# Database (Supabase PostgreSQL)
DATABASE_URL=postgresql://user:password@host:5432/dbname

# GitHub OAuth
GITHUB_CLIENT_ID=your-github-oauth-app-id
GITHUB_CLIENT_SECRET=your-github-oauth-app-secret
GITHUB_REDIRECT_URI=http://localhost:3000/api/auth/callback/github

# OpenAI API
OPENAI_API_KEY=your-openai-api-key

# Redis (Upstash)
REDIS_URL=redis://default:password@host:6379

# JWT Secret
SECRET_KEY=your-secret-key-generate-with-openssl-rand-hex-32
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Application Settings
ALLOWED_ORIGINS=http://localhost:3000
MAX_REPO_SIZE_MB=500
EMBEDDING_MODEL=text-embedding-3-small
LLM_MODEL=gpt-4o-mini
```

**Generate SECRET_KEY:**
```bash
openssl rand -hex 32
```

---

## Step 4: Run the Development Servers

Open **two terminal windows**:

### Terminal 1: Frontend

```bash
cd frontend
npm run dev
```

Frontend will run on: **http://localhost:3000**

### Terminal 2: Backend

```bash
cd backend
uvicorn app.main:app --reload
```

Backend will run on: **http://localhost:8000**

API docs available at: **http://localhost:8000/docs**

---

## Step 5: Verify Setup

1. **Frontend**: Open http://localhost:3000 - you should see the landing page
2. **Backend Health Check**: Visit http://localhost:8000/api/v1/health
   ```json
   {"status": "healthy", "service": "Codebase Onboarding API", "version": "0.1.0"}
   ```
3. **API Documentation**: Visit http://localhost:8000/docs for Swagger UI

---

## Next Steps

### Implement Core Features:

1. **GitHub OAuth Flow** - Complete authentication in `backend/app/api/v1/auth.py`
2. **Repository Ingestion** - Implement cloning and parsing in `repositories.py`
3. **RAG Pipeline** - Add embeddings generation and vector storage
4. **Chat Interface** - Build the frontend chat UI and connect to backend
5. **Architecture Visualization** - Implement react-flow diagrams

### Database Schema:

Create tables in Supabase SQL Editor:

```sql
-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    github_id VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    avatar_url TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Repositories table
CREATE TABLE repositories (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id),
    github_id VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    url TEXT NOT NULL,
    analyzed BOOLEAN DEFAULT FALSE,
    analyzed_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Code chunks table with vector embeddings
CREATE TABLE code_chunks (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    repo_id UUID REFERENCES repositories(id),
    file_path TEXT NOT NULL,
    content TEXT NOT NULL,
    start_line INTEGER,
    end_line INTEGER,
    embedding vector(1536),  -- OpenAI embedding dimension
    metadata JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Create index for vector similarity search
CREATE INDEX ON code_chunks USING ivfflat (embedding vector_cosine_ops);
```

---

## Troubleshooting

### Port Already in Use

```bash
# Kill process on port 3000 (frontend)
npx kill-port 3000

# Kill process on port 8000 (backend)
npx kill-port 8000
```

### Python Dependencies Issues

```bash
# Use virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Database Connection Issues

- Verify Supabase connection string format
- Ensure pgvector extension is enabled
- Check firewall/network settings

---

## Deployment (Optional - Production)

### Frontend (Vercel)
```bash
cd frontend
vercel
```

### Backend (Railway)
1. Push to GitHub
2. Connect Railway to your repo
3. Add environment variables in Railway dashboard
4. Deploy automatically on push

---

## Resources

- [Next.js Documentation](https://nextjs.org/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [LangChain Documentation](https://python.langchain.com)
- [Supabase Documentation](https://supabase.com/docs)
- [React Flow Documentation](https://reactflow.dev)

---

## Need Help?

Check out the implementation TODOs in the code:
- `backend/app/api/v1/*.py` - API endpoint implementations
- `backend/app/services/*.py` - Service layer logic
- `frontend/app/` - Frontend pages and components

Happy coding! 🚀
