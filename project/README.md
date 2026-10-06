# PROJECT INSTALLATION AND RUN GUIDE

## 1. Requirements

The project uses:

- Python 3.11
- pygame 2.5.2
- matplotlib 3.11.2

The library versions are fixed in `requirements.txt` to ensure compatibility with the required environment.

---

## 2. Install Python 3.11

### Windows

Check installed Python versions:

```powershell
py -0p
```

If Python 3.11 is not installed, install it with:

```powershell
winget install Python.Python.3.11
```

After installation, close and reopen the terminal.

Check Python 3.11:

```powershell
py -3.11 --version
```

Expected output:

```text
Python 3.11.x
```

### macOS 13.7.8 Ventura - Intel Core i5

Check Python 3.11:

```bash
python3.11 --version
```

If Python 3.11 is not installed and Homebrew is available:

```bash
brew install python@3.11
```

Check again:

```bash
python3.11 --version
```

Expected output:

```text
Python 3.11.x
```

---

## 3. Install Libraries

Open a terminal in the `project` directory.

### Windows

```powershell
py -3.11 -m pip install -r requirements.txt
```

### macOS

```bash
python3.11 -m pip install -r requirements.txt
```

Contents of `requirements.txt`:

```txt
pygame==2.5.2
matplotlib==3.11.2
```

---

## 4. Run the Project

Run all commands from the root `project` directory.

### Windows

```powershell
py -3.11 main.py
```

### macOS

```bash
python3.11 main.py
```

---

## 5. Compare UCS and A*

### Windows

```powershell
py -3.11 -m source.mode.single.experiments.compare_algorithms
```

### macOS

```bash
python3.11 -m source.mode.single.experiments.compare_algorithms
```

The results are saved to:

```text
source/mode/single/experiments/results/compare_algorithms.csv
```

---

## 6. Plot the Results

After running the comparison:

### Windows

```powershell
py -3.11 -m source.mode.single.experiments.plot_results
```

### macOS

```bash
python3.11 -m source.mode.single.experiments.plot_results
```

The generated chart is saved in:

```text
source/mode/single/experiments/results/
```

---

## 7. Verify the Heuristic

### Windows

```powershell
py -3.11 -m source.mode.single.experiments.verify_heuristic
```

### macOS

```bash
python3.11 -m source.mode.single.experiments.verify_heuristic
```

---

## Note

Run all commands from the `project` directory:

```text
project/
├── main.py
├── requirements.txt
└── source/
```

Do not run the experiment commands while inside the `source` directory.

If this error appears:

```text
ModuleNotFoundError: No module named 'source'
```

go back to the `project` directory and run the command again.

For Windows, always use:

```text
py -3.11
```

For macOS, always use:

```text
python3.11
```

This ensures that the project runs with Python 3.11 instead of another installed Python version.