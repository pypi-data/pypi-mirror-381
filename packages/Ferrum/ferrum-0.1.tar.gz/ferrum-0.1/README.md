# Ferrum  🜜 
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

---

Ferrum is a **lightweight**, **cross-platform** Python project package manager (PPPM).  
Install or uninstall Python packages from your project with a *single* line of code.


## Features

- Install multiple packages silently
- Version pinning support
- Uninstall with a single command
- Cross-platform: Linux, macOS, Windows
- Simple usage: `ferrum.forge()` and `ferrum.purge()`

---

## Usage

### Install packages

```python
import ferrum

# Install latest versions
ferrum.forge(["numpy", "scipy"])

# Install specific versions
ferrum.forge(["numpy==1.26.0", "scipy==1.10.1"])
ferrum.forge({"numpy": "1.26.0", "scipy": "1.10.1"})
```

### Uninstall packages

```python
import ferrum

ferrum.purge(["numpy", "scipy"])
```

### Verbose mode

Show pip errors if install/uninstall fails:

```python
ferrum.forge(["numpy==1.26.0"], verbose=True)
ferrum.purge(["numpy"], verbose=True)
```
### Summary mode

Show the user a summary of installed packages after install:

```python
ferrum.forge(["numpy"], summary=True)
```
This produces output in this format:
```
Forging numpy...
Forge summary:
  numpy: success
Purging numpy...
Purge summary:
  numpy: success
```

---

## Contact

- GitHub Issues: [Ferrum Issues](https://github.com/literal-gargoyle/ferrum/issues)
- Author: literal-gargoyle