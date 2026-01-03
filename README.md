# Codebase Onboarding SaaS

AI-powered platform that helps engineers understand large codebases quickly through intelligent analysis, semantic search, and visual architecture diagrams.

## 🚀 Features

- **GitHub Integration**: Connect any public/private repository via GitHub OAuth
- **AI-Powered Q&A**: Ask questions about your codebase and get intelligent answers
- **Architecture Visualization**: Auto-generated interactive diagrams showing data flow and structure
- **Semantic Code Search**: RAG-powered search across your entire codebase
- **Smart Analysis**: Automatically identifies entry points, dependencies, and code patterns

## 🛠️ Tech Stack

### Frontend
- **Next.js 14** (App Router)
- **Tailwind CSS** + **shadcn/ui**
- **React Flow** (Architecture diagrams)
- **TypeScript**

### Backend
- **FastAPI** (Python)
- **LangChain** (RAG orchestration)
- **OpenAI API** / **Ollama** (Embeddings & LLM)

### Infrastructure
- **Supabase** (PostgreSQL + pgvector)
- **Upstash Redis** (Caching)
- **Vercel** (Frontend hosting)
- **Railway/Render** (Backend hosting)

## 📁 Project Structure

```
codebase_project/
├── frontend/              # Next.js 14 application
│   ├── app/              # App Router pages
│   ├── components/       # React components
│   ├── lib/             # Utilities and configs
│   └── public/          # Static assets
├── backend/              # FastAPI application
│   ├── app/
│   │   ├── api/         # API routes
│   │   ├── services/    # Business logic
│   │   ├── models/      # Database models
│   │   └── core/        # Config and utilities
│   └── requirements.txt
├── shared/               # Shared types and configs
└── docs/                # Documentation
```

## 🚦 Getting Started

### Prerequisites
- Node.js 18+
- Python 3.11+
- PostgreSQL (via Supabase)
- GitHub OAuth App credentials

### Installation

1. **Clone and install dependencies**
```bash
# Install frontend dependencies
cd frontend
npm install

# Install backend dependencies
cd ../backend
pip install -r requirements.txt
```

2. **Configure environment variables**

Create `.env.local` files in both frontend and backend directories (see `.env.example` files)

3. **Run development servers**

```bash
# Terminal 1 - Frontend
cd frontend
npm run dev

# Terminal 2 - Backend
cd backend
uvicorn app.main:app --reload
```

## 🔑 Free Tier Services Setup

- **Supabase**: Sign up at supabase.com (500MB database, 50MB file storage)
- **Upstash Redis**: Free 10K commands/day at upstash.com
- **OpenAI**: $5 free trial credits
- **Vercel**: Unlimited hobby projects
- **Railway**: $5 free credits monthly

## 📝 License

MIT
