# Automation Framework – Selenium & Playwright Pipeline

## 📌 Overview
This project provides a **custom automation infrastructure** built on top of **Selenium** and **Playwright**, designed for **control, scalability, and clarity**.

The framework introduces:
- A **custom Adapter layer** over Selenium & Playwright  
- A **Pipeline execution model** (Selenium → Playwright)  
- **Data-driven testing** based on structured JSON files  
- **Gherkin-style tests** for readability and BDD alignment  

Unlike plugin-based approaches, this framework avoids hidden behavior and gives full ownership over browser lifecycle, execution order, and test logic.

---

## 🧠 Core Concept – Pipeline Architecture

1. **Selenium (Gatekeeper)**
   - Validates page structure
   - Ensures all fields from JSON exist in the DOM
   - Detects missing / renamed / broken locators
   - Stops the pipeline early if the page is invalid

2. **Playwright (Runner)**
   - Executes real UI interactions
   - Runs positive, negative, boundary, and security tests
   - Supports combinatorial testing via CLI flags

This guarantees:
- No wasted Playwright runs on broken pages
- Faster feedback
- Clear separation of responsibilities

---

## ✨ Features

- **Custom Browser Adapters**
  - `SeleniumAdapter`
  - `PlaywrightAdapter`
- **No pytest-playwright dependency**
- **Single-run pipeline (no duplicated tests)**
- **CLI-controlled data expansion**
- **JSON-driven automation**
- **Gherkin-ready test structure**
- **Deterministic browser lifecycle**

---

## 🛠 Technologies Used

- **Selenium 🚀** – DOM validation, structure verification  
- **Playwright 🎭** – Fast and reliable UI execution  
- **Pytest 🧪** – Test orchestration  
- **Gherkin 📜** – Behavior-driven test definitions  
- **JSON 📂** – Test data & field definitions  

---

## 📁 QA Testing Websites – Test Data Collection

A curated set of JSON files with real-world test data for popular QA practice websites.

