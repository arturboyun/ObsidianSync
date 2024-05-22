# Obsidian Sync

[![Issues](https://img.shields.io/badge/issues-black?style=flat&logo=github)](https://github.com/arturboyun/ObsidianSync/issues)
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

2. Create a new Git repository on a hosting service such as GitHub, GitLab, or Bitbucket.
3. Clone the repository to your local machine:

```bash
git clone https://your-repo-url.git $HOME/Obsidian/Vault
```
4. Checkout and set upstream branch

```bash
cd $HOME/Obsidian/Vault
git branch --set-upstream-to=origin/main main
```
**!CHANGE `main` to your branch name!**

5. Run the installation script:

```bash
cd ObsidianSync
chmod +x install.sh
./install.sh
```

6. Enter the path to your Obsidian vault and the URL of the Git repository.
7. Well done! You are now ready to synchronize your Obsidian notes with the Git repository.

## Usage

1. Make changes to your Obsidian notes as usual.
2. Service in background will automatically synchronize your notes with the Git repository.

## Update Settings

Just run the installation script again:

```bash
cd ObsidianSync
./install.sh
```

## Systemd Service (Start / Restart / Stop / Logs)

### Start 
```bash
sudo systemctl restart obsidian_sync.service
```

### Restart
```bash
sudo systemctl restart obsidian_sync.service
```

### Stop
```bash
sudo systemctl stop obsidian_sync.service
```

### Logs
```bash
sudo journalctl -u obsidian_sync
```

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

For any questions or inquiries, please contact [arturboyun.t.me](https://arturboyun.t.me) or [arturboyun@gmail.com](mailto:arturboyun@gmail.com)
