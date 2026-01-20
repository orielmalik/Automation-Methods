# Automation 

## Overview  
This project provides an abstraction layer over **Playwright** and **Selenium** to enhance maintainability and streamline automation processes. It also includes **tests written using Gherkin syntax**   

## Features  
- **Custom Libraries**: A wrapper layer built on top of Playwright and Selenium to simplify automation.  
- **Gherkin-Based Testing**: Tests are defined using Gherkin syntax for better readability and structure.
## Technologies Used  
- ** Selenium 🚀& Playwright 🎭** – For web automation  
- **Gherkin📜** – For behavior-driven testing  


# QA Testing Websites - Test Data Collection

A comprehensive collection of JSON files containing test data for popular QA testing practice websites.

## 📁 Project Structure

```
qa-testing-websites/
├── index.json                    # Index of all websites
├── the-internet-herokuapp.json   # The Internet Herokuapp test data
├── saucedemo.json                # SauceDemo test data
├── demoblaze.json                # DemoBlaze test data
├── demoqa.json                   # DemoQA test data
├── automationexercise.json       # Automation Exercise test data
└── automation-playground.json    # Automation Playground test data
```

## 🌐 Websites Included

| Website | URL | Description |
|---------|-----|-------------|
| **The Internet Herokuapp** | https://the-internet.herokuapp.com | Most popular practice site - login forms, checkboxes, dropdowns, file uploads, dynamic content, alerts |
| **SauceDemo** | https://www.saucedemo.com | E-commerce demo - login, products, cart, checkout (Sauce Labs) |
| **DemoBlaze** | https://www.demoblaze.com | Electronics store - products, cart, orders, signup/login |
| **DemoQA** | https://demoqa.com | Interactive elements - forms, tables, widgets, date pickers, automation practice |
| **Automation Exercise** | https://automationexercise.com | Full online store - registration, login, products, cart, payment |
| **Automation Playground** | https://play1.automationcamp.ir | Specific exercises - checkboxes, alerts, iframes, forms, keyboard/mouse events |

## 📋 JSON Structure

Each JSON file contains:

```json
{
  "website": "https://example.com",
  "pages": {
    "pageName": {
      "url": "https://example.com/page",
      "fields": {
        "fieldName": {
          "id": "element-id",
          "name": "element-name",
          "type": "text|email|password|checkbox|radio|select|file|textarea",
          "placeholder": "Placeholder text",
          "testValues": ["", "valid", "invalid", "edge-case", "!@#$%"]
        }
      }
    }
  }
}
```

## 🧪 Test Value Types

Each field contains an array of test values covering:

| Type | Description | Example |
|------|-------------|---------|
| **Empty** | Empty string for required field validation | `""` |
| **Valid** | Correct/expected input values | `"test@example.com"` |
| **Invalid** | Incorrect format or type values | `"invalid-email"` |
| **Boundary** | Edge cases (min/max lengths) | `"a"`, `"verylongstring..."` |
| **Special Characters** | Symbol testing | `"!@#$%^&*()"` |
| **Security** | SQL injection, XSS attempts | `"<script>alert('xss')</script>"` |
| **Unicode** | Non-English characters | `"ישראל"`, `"中文"`, `"أحمد"` |
| **Whitespace** | Spaces and trimming tests | `" "`, `"  value  "` |

## 🚀 Usage

### For Manual Testing
Review the JSON files to get ideas for test cases and edge cases to try on each website.

### For Automated Testing
Load the JSON files in your test framework to data-drive your tests:

```javascript
// JavaScript example
const testData = require('./saucedemo.json');
const loginTests = testData.pages.login.fields.username.testValues;

loginTests.forEach(username => {
  test(`Login with username: ${username}`, async () => {
    await page.fill('#user-name', username);
    // ... rest of test
  });
});
```

```python
# Python example
import json

with open('saucedemo.json') as f:
    test_data = json.load(f)

usernames = test_data['pages']['login']['fields']['username']['testValues']

for username in usernames:
    # Test each username value
    driver.find_element(By.ID, 'user-name').send_keys(username)
```

## 📝 Notes

- All element IDs and selectors were gathered by inspecting the actual websites
- Test values include both positive and negative test cases
- Some fields may have changed if the websites are updated
- Always verify selectors before using in automated tests

## 🔗 Additional Resources

- [UI Testing Checklist](https://www.browserstack.com/guide/ui-testing-checklist)
- [Website QA Checklist](https://marker.io/blog/website-qa-checklist)
- [OWASP Web Checklist](https://github.com/0xRadi/OWASP-Web-Checklist)







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
