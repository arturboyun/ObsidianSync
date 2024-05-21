import datetime
from pathlib import Path
from rich import print
from git import Repo


class Syncher:
    def __init__(self, repository_path: Path, repo_url: str):
        if not isinstance(repository_path, Path):
            raise TypeError("Parameter 'repository_path' must be a Path object!")
        if not Path(repository_path).exists():
            raise FileNotFoundError(f"The path {repository_path} does not exist!")
        if not repo_url or not isinstance(repo_url, str):
            raise TypeError("Parameter 'repo_url' must be a string!")

        self.repository_path = repository_path
        self.repo_url = repo_url

    def sync(self):
        print("[green bold]Syncing your Obsidian vault with Git Repository...")
        repo = Repo.init(self.repository_path)
        
        if "origin" not in repo.remotes:
            print(f"[yellow]Adding remote origin {self.repo_url}...")
            remote = repo.create_remote("origin", self.repo_url)

        remote = repo.remote("origin")

        print("[green bold]Pulling changes from remote repository...")
        remote.pull()

        print("[green bold]Adding changes to local repository...")
        repo.git.add(all=True)

        print("[green bold]Committing changes...")
        now = datetime.datetime.now()
        repo.index.commit(f"Obsidian Sync - {now.strftime('%Y-%m-%d %H:%M:%S')}")

        print("[green bold]Pushing changes to remote repository...")
        remote.push()
        print("[green bold]Sync complete!")
