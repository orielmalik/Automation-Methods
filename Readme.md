# Automation 

## Overview  
This project provides an abstraction layer over **Playwright** and **Selenium** to enhance maintainability and streamline automation processes. It also includes **tests written using Gherkin syntax**   

## Features  
- **Custom Libraries**: A wrapper layer built on top of Playwright and Selenium to simplify automation.  
- **Gherkin-Based Testing**: Tests are defined using Gherkin syntax for better readability and structure.  
- **Data Analysis with Pandas**: Extracting and analyzing existing data efficiently.  


## Technologies Used  
- ** Selenium 🚀& Playwright 🎭** – For web automation  
- **Pandas🐼** – For data processing and analysis  
- **Gherkin📜** – For behavior-driven testing  






| Name               | Description                                              |
|--------------------|----------------------------------------------------------|
| __init__          | Initializes the PandasHelper class with a file path, data, or DataFrame. |
| detect_encoding   | Detects and returns the encoding of a file.              |
| read_file         | Reads a file (CSV, XLSX, JSON) into a DataFrame.         |
| create_dataframe  | Creates a DataFrame from provided data and columns.      |
| create_series     | Creates a Pandas Series from provided data.              |
| sqlSelect         | Executes an SQL query on a DataFrame using PandaSQL.     |
| create_chart      | Creates and saves a chart (histogram, pie, or plot) based on data. |


## Getting Started  
To install dependencies and set up the project, run:  
```bash
pip install -r requirements.txt
