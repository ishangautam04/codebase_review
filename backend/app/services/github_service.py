"""
GitHub service for repository operations
"""
from github import Github
from app.core.config import settings
import os
import tempfile
from git import Repo

class GitHubService:
    """Service for interacting with GitHub API and repositories"""
    
    def __init__(self, access_token: str):
        self.github = Github(access_token)
        self.access_token = access_token
    
    async def get_user_repos(self, limit: int = 50):
        """Fetch user's repositories"""
        user = self.github.get_user()
        repos = user.get_repos()[:limit]
        
        return [
            {
                "id": str(repo.id),
                "name": repo.name,
                "full_name": repo.full_name,
                "description": repo.description,
                "url": repo.html_url,
                "language": repo.language,
                "stars": repo.stargazers_count,
            }
            for repo in repos
        ]
    
    async def clone_repository(self, repo_url: str, branch: str = "main") -> str:
        """
        Clone a repository to temporary directory
        
        Returns: Path to cloned repository
        """
        temp_dir = tempfile.mkdtemp(prefix="codebase_")
        
        # Add authentication to URL if needed
        if "github.com" in repo_url and self.access_token:
            repo_url = repo_url.replace(
                "https://github.com",
                f"https://{self.access_token}@github.com"
            )
        
        try:
            Repo.clone_from(repo_url, temp_dir, branch=branch, depth=1)
            return temp_dir
        except Exception as e:
            # Cleanup on failure
            if os.path.exists(temp_dir):
                import shutil
                shutil.rmtree(temp_dir)
            raise Exception(f"Failed to clone repository: {str(e)}")
    
    def get_repo_metadata(self, full_name: str):
        """Get repository metadata from GitHub"""
        repo = self.github.get_repo(full_name)
        
        return {
            "name": repo.name,
            "description": repo.description,
            "language": repo.language,
            "stars": repo.stargazers_count,
            "forks": repo.forks_count,
            "open_issues": repo.open_issues_count,
            "default_branch": repo.default_branch,
            "topics": repo.get_topics(),
        }
