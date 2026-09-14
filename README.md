# FST Branch Analyzer

A Python CLI utility for analyzing applicant-to-seat competitiveness ratios across different FST (Faculté des Sciences et Techniques) cities and academic branches.

## Overview

The FST Branch Analyzer allows users to record applicant counts and available seat numbers for university branches, compute competitiveness ratios, rank options in ascending order, and log analysis results to a text file (`FST.txt`).

## Key Features

- Ratio Computation: Calculates the exact applicant-per-seat ratio for each branch.
- Automated Ranking: Sorts branches in ascending order based on competitiveness.
- Error Validation: Prevents division by zero and invalid input types.
- Data Logging: Appends evaluation reports to `FST.txt`.

## System Requirements

- Python 3.8 or higher.

## Installation and Execution

Run `main.py` directly using Python:
```bash
python main.py
```

## Project File Structure

```
fst-analyzer/
│
├── main.py         # Console interactive entry point
├── fst_analyzer.py # Logic for ratio computation, ranking, and file persistence
├── FST.txt         # Text file output log
├── .gitignore      # Git exclusion rules
└── README.md       # Project documentation
```

## License

This project is licensed under the MIT License.
