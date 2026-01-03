# Codebase Onboarding SaaS

AI-powered platform that helps engineers understand large codebases quickly through intelligent analysis, semantic search, and visual architecture diagrams.

## 🎯 Project Vision & Goals

This project aims to solve the onboarding challenge that engineers face when joining new teams or exploring unfamiliar codebases. The platform enables developers to understand complex codebases in hours instead of weeks.

### Core Objectives

1. **Rapid Codebase Understanding**: Reduce onboarding time from weeks to hours by providing AI-powered insights and automated documentation
2. **Intelligent Code Navigation**: Enable natural language queries about code functionality, dependencies, and architecture
3. **Visual Architecture Discovery**: Automatically generate interactive diagrams showing data flow, component relationships, and system structure
4. **Context-Aware Search**: Implement semantic search that understands code intent beyond keyword matching
5. **Knowledge Preservation**: Create searchable knowledge bases from codebases that persist team insights

### Planned Features (Roadmap)

#### Phase 1 (MVP - Current)
- ✅ GitHub OAuth integration
- ✅ Repository cloning and indexing
- ✅ Basic AI Q&A with RAG
- 🚧 Architecture diagram generation
- 🚧 Code search with semantic understanding

#### Phase 2 (Enhancement)
- 📋 Multi-repository support
- 📋 Custom documentation generation
- 📋 Code change explanations (PR analysis)
- 📋 Team collaboration features (shared annotations)
- 📋 Video walkthrough generation

#### Phase 3 (Advanced)
- 📋 IDE extensions (VS Code, IntelliJ)
- 📋 Real-time code suggestions
- 📋 Onboarding path recommendations
- 📋 Integration with Slack/Discord
- 📋 Custom model training on private codebases

### Use Cases

- **New Team Members**: Quickly understand where to start, key components, and coding patterns
- **Open Source Contributors**: Navigate unfamiliar projects and find contribution opportunities
- **Code Reviews**: Get context on changes and understand impact across the codebase
- **Technical Due Diligence**: Evaluate code quality and architecture for acquisitions
- **Legacy Code Maintenance**: Understand undocumented systems and dependencies

### Technical Challenges to Solve

- Efficient embedding generation and storage for large codebases (100K+ files)
- Accurate architecture diagram generation from code structure
- Context-aware code chunking that preserves semantic meaning
- Reducing LLM costs while maintaining quality
- Real-time updates when repositories change

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
