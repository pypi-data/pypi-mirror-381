# openvsc

A lightweight CLI tool to quickly open your local repositories in **Visual Studio Code**.

---

## Installation

You can install the tool locally with:

```bash
pip install .
```

Or once published to PyPI:

```bash
pip install openvsc
```

---

## Usage

```bash
openvsc [command] [arguments]
```

### Commands

- `<repo_name>`  
  Opens the given repo in VS Code (must be inside the root).

- `--list`  
  Lists all repos in the current root directory.

- `--show-root`  
  Shows the currently configured repos root.

- `--set-root <path>`  
  Sets a new repos root directory.

- `--reset-root`  
  Resets the repos root to default.

- `--help`  
  Displays the help message.

---

## Examples

```bash
# Open a repo called "my-project"
openvsc my-project

# List all repos in your root directory
openvsc --list

# Change the root to ~/Desktop/Projects
openvsc --set-root ~/Desktop/Projects

# Show current root
openvsc --show-root
```

---

## License

MIT License. See [LICENSE](LICENSE) for details.
