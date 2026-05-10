# Automation Framework – Selenium & Playwright Pipeline

## 📌 Overview

This project provides a custom automation infrastructure built on top of Selenium and Playwright, designed for control, scalability, deterministic execution, and transparent test orchestration.

The framework introduces:

- Custom Adapter layer over Selenium & Playwright
- Sequential Pipeline execution model (Selenium → Playwright)
- Structured JSON-driven test generation
- Gherkin-style scenario execution
- Feature-based execution flow
- Optional LLM integration for dynamic data generation

Unlike plugin-heavy automation frameworks, this system avoids hidden abstractions and keeps full ownership of:

- Browser lifecycle
- Selector validation
- Scenario orchestration
- Data classification
- Execution strategies
- Test generation logic

---

# 🧠 Core Architecture

## Selenium → Playwright Pipeline

The framework is intentionally split into two independent stages.

---

## 1️⃣ Selenium Layer – Structural Validation

Selenium acts as a lightweight validation and verification layer before actual execution begins.

### Responsibilities

- Validate DOM availability
- Ensure required fields exist
- Detect broken selectors early
- Prevent invalid pages from reaching execution stage
- Catch synchronization issues before Playwright execution

### Goal

Fail fast before expensive execution starts.

---

## 2️⃣ Playwright Layer – Behavioral Execution

After Selenium validates the page structure, Playwright performs the actual user flow execution.

### Responsibilities

- Fill forms
- Trigger actions
- Navigate pages
- Validate success/failure flows
- Capture runtime behavior
- Execute deterministic scenario pipelines

---

# 🧩 Gherkin Feature Execution

The framework uses Gherkin-style FEATURES as the orchestration layer.

Example:

```gherkin
Scenario: PASS cases
  Given valid input data
  When I submit the form
  Then I should be redirected successfully