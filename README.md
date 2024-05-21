# Obsidian Sync

<!-- [![Build Status](https://img.shields.io/travis/your-username/your-repo.svg)](https://travis-ci.org/your-username/your-repo)
[![Coverage](https://img.shields.io/codecov/c/github/your-username/your-repo.svg)](https://codecov.io/gh/your-username/your-repo)
[![Dependencies](https://img.shields.io/david/your-username/your-repo.svg)](https://david-dm.org/your-username/your-repo)
[![DevDependencies](https://img.shields.io/david/dev/your-username/your-repo.svg)](https://david-dm.org/your-username/your-repo?type=dev)
[![GitHub Issues](https://img.shields.io/github/issues/your-username/your-repo.svg)](https://test.com) -->

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Description

This project provides a solution for syncing Obsidian notes through a Git repository. It allows you to seamlessly manage your Obsidian notes using version control and collaborate with others.

## Features

- Automatic synchronization of Obsidian notes with a Git repository
- Support for version control operations such as commit, push, and pull
- Customizable synchronization settings
- ~~Conflict resolution for simultaneous edits~~

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/arturboyun/ObsidianSync.git
```

2. Create virtual environment and install dependencies:

```bash
cd ObsidianSync
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Create a new Git repository on a hosting service such as GitHub, GitLab, or Bitbucket.
4. Clone the repository to your local machine:

```bash
git clone https://your-repo-url.git
```

5. Run the following command to set your settings and install the systemd service:

```bash
chmod +x install.sh
./install.sh
```

6. Enter the path to your Obsidian vault and the URL of the Git repository.
7. Well done! You are now ready to synchronize your Obsidian notes with the Git repository.

## Usage

1. Make changes to your Obsidian notes as usual.
2. Use the provided CLI commands or the GUI interface to perform synchronization operations.
3. Collaborate with others by pushing and pulling changes from the Git repository.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

For any questions or inquiries, please contact [arturboyun.t.me](https://arturboyun.t.me) or [arturboyun@gmail.com](mailto:arturboyun@gmail.com)
