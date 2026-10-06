# PROJECT INSTALLATION AND RUN GUIDE

## 1. Requirements

The project uses:

- Python 3.11
- pygame 2.5.2
- matplotlib 3.11.2

The library versions are fixed in `requirements.txt` to ensure that the project can be installed and executed on the required macOS environment.

## 2. Install Libraries

Open a terminal in the `project` directory.

### Windows

Check Python:

```powershell
python --version
```

Install the required libraries:

```powershell
python -m pip install -r requirements.txt
```

### macOS 13.7.8 Ventura - Intel Core i5

Check Python:

```bash
python3 --version
```

Install the required libraries:

```bash
python3 -m pip install -r requirements.txt
```

Contents of `requirements.txt`:

```txt
pygame==2.5.2
matplotlib==3.11.2
```

## 3. Run the Project

Run all commands from the root `project` directory.

### Windows

```powershell
python main.py
```

### macOS

```bash
python3 main.py
```

## 4. Compare UCS and A*

### Windows

```powershell
python -m source.mode.single.experiments.compare_algorithms
```

### macOS

```bash
python3 -m source.mode.single.experiments.compare_algorithms
```

The results are saved to:

```text
source/mode/single/experiments/results/compare_algorithms.csv
```

## 5. Plot the Results

After running the comparison:

### Windows

```powershell
python -m source.mode.single.experiments.plot_results
```

### macOS

```bash
python3 -m source.mode.single.experiments.plot_results
```

The generated chart is saved in:

```text
source/mode/single/experiments/results/
```

## 6. Verify the Heuristic

### Windows

```powershell
python -m source.mode.single.experiments.verify_heuristic
```

### macOS

```bash
python3 -m source.mode.single.experiments.verify_heuristic
```

## Note

Run the commands from the `project` directory:

```text
project/
├── main.py
├── requirements.txt
└── source/
```

Do not run `python -m source...` commands while inside the `source` directory.

If this error appears:

```text
ModuleNotFoundError: No module named 'source'
```

go back to the `project` directory and run the command again.
