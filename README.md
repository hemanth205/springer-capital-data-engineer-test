# Springer Capital Data Engineer Test

## Project Overview
This project processes referral data using Python and Pandas.  
It reads a CSV file, performs basic data profiling, and generates an Excel report.

## Project Structure

springer-capital-data-engineer-test/
│
├── data/                     # Input data files
├── your_script.py            # Python script for processing
├── referral_report.csv       # Output processed dataset
├── profiling_report.xlsx     # Performance profiling report
├── data_dictionary.xlsx      # Data description
├── Dockerfile                # Docker configuration
└── README.md                 # Project documentation

## Requirements

Python 3.x

Required Python libraries:
- pandas
- openpyxl

Install dependencies:

pip install pandas openpyxl

## How to Run

Run the script using:

python your_script.py

## Output

The script generates:

- referral_report.csv
- profiling_report.xlsx

## Author

Hemanth Naidu  
Data Engineer Intern Assessment



## Running with Docker

Build the Docker image:

docker build -t referral-project .

Run the container:

docker run referral-project

The script will process the CSV file and generate the output reports.

## Running without Docker

Install dependencies:

pip install pandas openpyxl

Run the script:

python your_script.py



## How to Run the Project

### Option 1 — Run using Docker

docker build -t referral-project .
docker run referral-project

### Option 2 — Run using Virtual Environment (venv)

python -m venv venv
venv\Scripts\activate
pip install pandas openpyxl
python your_script.py

### Option 3 — Run using Global Python

pip install pandas openpyxl
python your_script.py



## Code Workflow

1. The script loads the referral dataset from the CSV file.

2. Using the pandas library, the data is read into a DataFrame for processing.

3. Basic data profiling is performed such as:
   - Counting rows
   - Checking data structure
   - Measuring processing time
   - Monitoring memory usage

4. The processed data is saved into a new file:
   referral_report.csv

5. A profiling report is generated and exported as:
   profiling_report.xlsx

6. A data dictionary file is included to describe the dataset columns:
   data_dictionary.xlsx

