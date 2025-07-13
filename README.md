# PythonSelenium_Demo: BDD Framework with Behave
This is a Python-based Selenium test automation framework using BDD with Behave.  
It covers UI test cases for websites like Wikipedia, IMDb, ReactJS, and SauceDemo, with CSV-based data-driven testing, logging, screenshots on failure, and HTML reporting.
## Folder Structure

PythonSelenium_Demo/
├── features/
│ ├── combined.feature # Contains all feature scenarios
│ ├── steps/
│ │ └── step_definitions.py # All step definitions
│ ├── testdata/
│ │ └── data.csv # Test credentials for SauceDemo
│ └── utils/
│ └── logger.py # Logging utility
├── logs/ # Logs generated during test execution
├── screenshots/ # Screenshots saved on test failure
├── reports/ # HTML test report
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .gitignore # Ignored files for Git

---

### ✅ 4. **Tech Stack / Tools Used**
```markdown
## Tech Stack

- 🐍 Python 3.x
- 🧪 Selenium WebDriver
- 🧾 Behave (BDD Framework)
- 📦 WebDriver Manager
- 🧰 CSV for data-driven testing
- 🖼️ Screenshots on failure
- 📄 Logging
- 📊 HTML Report (`behave-html-formatter`)

## Installation

1. Clone the repo:
```bash
git clone https://github.com/priyankkamarsetty/PythonSelenium_Demo.git
cd PythonSelenium_Demo

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # Mac

3. Install dependencies:
pip install -r requirements.txt

## Run Tests
Run all scenarios:
```bash
behave

To run and generate an HTML report (if you install behave-html-formatter):
behave -f behave_html_formatter:HTMLFormatter -o reports/report.html

## Screenshots & Logs

- 📷 Screenshots for failed steps are saved in the `screenshots/` folder.
- 📘 Logs are stored in the `logs/` folder as `test_log.txt`.

## Test Scenarios Included

- Wikipedia search (Selenium and JavaScript)
- IMDb movie search (Inception)
- ReactJS docs navigation
- SauceDemo login tests:
  - Valid login
  - Invalid login
  - Locked-out user
  - CSV-based login testing

## Author

👤 Priyankka Marsetty  
[GitHub Profile](https://github.com/priyankkamarsetty)



