# Sales Analyzer

## CPUF001 Software Foundation – S1 Development Project

### Project Overview

Sales Analyzer is a Python data processing program developed for the CPUF001 Software Foundation Development Project. The program reads sales data from a CSV input file, validates the data, performs sales calculations and generates an output report.

The program is designed to demonstrate Python programming concepts including functions, selection, iteration, file handling, validation, command-line arguments and modular programming.

## Features

* Reads sales data from a CSV file.
* Accepts the input file through the command line.
* Validates the input file and required data fields.
* Calculates total sales revenue.
* Calculates average sale value.
* Identifies the highest sale.
* Identifies the lowest sale.
* Calculates total quantity sold.
* Calculates revenue by category.
* Identifies the best-selling product.
* Generates an output report.
* Provides error checking for invalid input files.

## Project Structure

```text
R0-Sales-Analyzer/
│
├── main.py
├── calculations.py
├── file_handler.py
├── validator.py
├── input.csv
├── run.bat
├── README.md
└── .gitignore
```

### File Descriptions

| File              | Purpose                                                  |
| ----------------- | -------------------------------------------------------- |
| `main.py`         | Main program that controls the data processing workflow  |
| `calculations.py` | Contains the sales calculation functions                 |
| `file_handler.py` | Handles reading input data and writing the output report |
| `validator.py`    | Validates the input file and sales data                  |
| `input.csv`       | Sample sales data used for testing                       |
| `run.bat`         | Command-line script used to execute the program          |
| `README.md`       | Project documentation                                    |
| `.gitignore`      | Specifies files that should not be committed to GitHub   |

## Requirements

The following software is required:

* Python 3
* Windows Command Prompt or PowerShell
* Git, if cloning or managing the repository locally

## How to Run the Program

### Method 1 – Python Command Line

Open Command Prompt or PowerShell in the project directory and run:

```bash
python main.py input.csv
```

The program validates the input file, processes the sales data and generates the analysis output.

### Method 2 – Batch Script

Run:

```bash
run.bat input.csv
```

The batch script executes the Python data processing program using the supplied CSV file.

## Input Data

The program uses a CSV file containing sales information. The input file is supplied to the program as a command-line argument.

The program checks the input file before processing and reports errors when required files or data fields are invalid.

## Output

After successful processing, the program displays the sales analysis and creates an output report containing the calculated results.

The output includes information such as:

* Total transactions
* Total quantity sold
* Total revenue
* Average sale
* Highest sale
* Lowest sale
* Best-selling product
* Revenue by category

## Programming Concepts Demonstrated

The project demonstrates:

* Python functions
* Variables and data types
* Sequence
* Selection using conditional statements
* Iteration using loops
* Command-line arguments
* CSV file handling
* Input validation
* Error handling
* Modular programming
* File output

## Assessment

This repository contains the code and supporting files for:

**Module:** CPUF001 – Software Foundation
**Assignment:** S1 – Development Project

The Development Document is submitted separately through the required assessment submission system.
