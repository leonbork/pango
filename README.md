# Pango Automation Interview Answer
## Weather Discrepancy Analyzer

This project collects and compares current temperature and “feels like” data from two sources — the OpenWeatherMap API and the timeanddate.com website — for 20 global cities. The data is stored in a local SQLite database, analyzed for discrepancies, and output as a CSV report with summary statistics.

## Setup Instructions
###	1.	Clone the repository
 ```
  git clone https://github.com/leonbork/pango
  cd pango
```
### 2. Install dependencies
```
pip install -r requirements.txt
```
### 3. Edit OpenWeatherMap API key 
Edit the file config/config.ini:
```
[API]
API_KEY = your_openweathermap_api_key

[DB]
DB_NAME = data.db
```

## How to Run the Project
```
python main.py
```
This will: <br>
	•	Fetch current temperature and feels-like values for 20 cities <br>
	•	Collect data from both the API and website <br>
	•	Store the results in a SQLite database (data.db) <br>
	•	Generate a CSV report at reports/discrepancy_report.csv

## How to Run the Tests
Run the end-to-end test:
```
pytest tests/test_pipeline.py
```
This test uses real API and scraping, and checks: <br>
	•	That the report was generated <br>
	•	That database values are valid

## How to View and Interpret the Report
After running the project, open:
```
reports/discrepancy_report.csv
```
Each row contains: <br>
	•	City name <br>
	•	API temperature and feels-like <br>
	•	Website temperature and feels-like <br>
	•	Difference in temperature (degrees and percent) <br>

At the end of the report: <br>
	•	Mean discrepancy <br>
	•	Max and min discrepancies <br>
	•	Number of cities exceeding the threshold

## Project Structure
```
.
├── config/                 # API key and DB config
│   └── config.ini
├── modules/                # Supporting logic
│   ├── constants.py
│   └── report_generator.py
├── utilities/              # Data handlers
│   ├── api_helpers.py
│   ├── db_helpers.py
│   └── scraper.py
├── reports/                # Output reports
│   └── discrepancy_report.csv
├── tests/                  # Automated tests
│   └── test_pipeline.py
├── main.py                 # Entry point
├── requirements.txt
└── README.md
```

## Author

Leonid Borkin
