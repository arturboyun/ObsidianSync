from ast import main
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
        self.repo = Repo.init(self.repository_path)

    def sync(self):
        print("[green bold]Syncing your Obsidian vault with Git Repository...")

        if "origin" not in self.repo.remotes:
            print(f"[yellow]Adding remote origin {self.self.repo_url}...")
            remote = self.repo.create_remote("origin", self.self.repo_url)

        remote = self.repo.remote("origin")

        try:
            print("[green bold]Adding changes to local repository...")
            self.repo.git.add(all=True)

            print("[green bold]Committing changes...")
            now = datetime.datetime.now()
            self.repo.index.commit(
                f"Obsidian Sync - {now.strftime('%Y-%m-%d %H:%M:%S')}"
            )

            print("[green bold]Pulling changes from remote repository...")
            try:
                remote.pull()
            except:
                self.merge_ours()

            print("[green bold]Adding changes to local repository...")
            self.repo.git.add(all=True)

            print("[green bold]Committing changes...")
            now = datetime.datetime.now()
            self.repo.index.commit(
                f"Obsidian Sync - {now.strftime('%Y-%m-%d %H:%M:%S')}"
            )

            print("[green bold]Pushing changes to remote repository...")
            remote.push()
            print("[green bold]Sync complete!")
        except Exception as e:
            print(f"[red bold]Error: {e}")
            print("[red bold]Sync failed!")
            return

    def merge_ours(self):
        print("[green bold]Merging changes from remote repository...")
        self.repo.git.merge(no_ff=True)
        self.repo.git.add(all=True)
        self.repo.index.commit("Merged changes from remote repository")
        print("[green bold]Merge complete!")
