import os
from pathlib import Path
import time
from typing import Callable
from rich import print


class Watcher:
    def __init__(self, path: Path, interval: int | None = 5):
        if path is None:
            raise ValueError("Path cannot be None")
        if not path.exists():
            raise FileNotFoundError(f"Path {path} does not exist")
        if not path.is_dir():
            raise NotADirectoryError(f"Path {path} is not a directory")
        if not isinstance(path, Path):
            raise TypeError("Path must be a Path object")

        if interval is not None and not isinstance(interval, int):
            raise TypeError("Interval must be an integer")
        if interval is not None and interval < 0:
            raise ValueError("Interval must be a positive integer")

        self.interval = interval
        self.path = path
        self.current_data: dict = dict()
        self.running = True
        self.on_change_events: list[Callable] = [
            lambda: print("[green]Changes detected!")
        ]
        self.on_startup_events: list[Callable] = [
            lambda: print("[green]Changes detected!")
        ]
        self.on_shutdown_events: list[Callable] = [
            lambda: print("[green]Changes detected!")
        ]

    def on_change(self, func: Callable):
        self.on_change_events.append(func)

    def on_startup(self, func: Callable):
        self.on_startup_events.append(func)

    def on_shutdown(self, func: Callable):
        self.on_shutdown_events.append(func)

    def start(self):
        print(f"[green bold]Starting to watch {self.path}")
        print("[yellow]Press Ctrl+C to exit", end="\n\n")

        for hook in self.on_startup_events:
            hook()

        self.current_data = self.get_last_modified_time(self.path)

        while self.running:
            print("[blue]Checking for changes...")
            try:
                new_data = self.get_last_modified_time(self.path)
                if new_data != self.current_data:
                    self.current_data = new_data

                    for hook in self.on_change_events:
                        hook()

                time.sleep(self.interval)
            except KeyboardInterrupt:
                print("\nExiting...")
                self.running = False

        for hook in self.on_shutdown_events:
            hook()

    def get_last_modified_time(self, path: Path):
        data = path.walk()
        result = dict()
        for root, dirs, files in data:
            for file in files:
                file_path = path / file
                try:
                    result[file] = file_path.stat().st_mtime
                except FileNotFoundError:
                    continue
            for dir in dirs:
                inner_result = self.get_last_modified_time(path / dir)
                result.update(inner_result)
        return result


if __name__ == "__main__":
    watcher = Watcher(Path(__file__).parent.parent.resolve())
    watcher.start()
