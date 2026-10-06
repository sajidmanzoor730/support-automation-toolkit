Python & Bash Automation

A practical automation toolkit for operational data processing, log analysis, validation, and repeatable troubleshooting workflows using Python, Bash, SQL, and API-based workflows.

Project Overview

This project demonstrates how repetitive operational tasks can be converted into structured, repeatable workflows.

The focus is on:

- Log parsing and structured data extraction
- Data validation and quality checks
- SQL-based operational analysis
- API health checks
- Repeatable command-line workflows
- Troubleshooting documentation
- Automation-ready operational processes

1. Log Analysis

Python scripts can be used to parse structured and semi-structured operational logs and extract useful information for analysis.

Typical outputs include:

- Error counts
- Event frequency
- Failure categories
- Timestamp-based patterns
- Repeated issues
- Operational exceptions

Example workflow:

Raw Logs
   ↓
Python Parser
   ↓
Structured Records
   ↓
Validation
   ↓
SQL Analysis
   ↓
Operational Report

2. Python Automation

Python is used for repeatable data-processing and operational tasks.

Example capabilities:

- Parse log files
- Extract structured fields
- Detect recurring errors
- Validate records
- Transform data for analysis
- Generate summary outputs
- Support repeatable quality checks

Example:

import re
from collections import Counter

errors = []

with open("application.log", "r", encoding="utf-8") as file:
    for line in file:
        match = re.search(r"ERROR_CODE=(\d+)", line)

        if match:
            errors.append(match.group(1))

error_counts = Counter(errors)

for code, count in error_counts.items():
    print(code, count)

3. SQL Analysis

Structured operational records can be loaded into SQL for further analysis.

Example analysis areas:

- Error frequency
- Issue categories
- Resolution trends
- SLA performance
- Repeat issues
- Operational volume
- Time-based patterns

Example query:

SELECT
    error_code,
    COUNT(*) AS error_count
FROM operational_logs
GROUP BY error_code
ORDER BY error_count DESC;

4. API Health Checks

API workflows can be tested using repeatable health-check processes.

Checks can include:

- HTTP status codes
- Response time
- Authentication status
- Required response fields
- Error responses
- Endpoint availability

Example workflow:

API Request
   ↓
Status Check
   ↓
Response Validation
   ↓
Performance Check
   ↓
Result Logged

5. Bash Automation

Bash commands can be used to simplify recurring operational tasks.

Examples:

grep "ERROR" application.log

grep "ERROR" application.log | wc -l

grep "WARNING" application.log > warnings.log

These workflows can be combined with Python scripts to create repeatable data-processing pipelines.

6. Data Validation

Automation can also support basic data-quality checks before analysis.

Example checks:

- Missing values
- Duplicate records
- Invalid formats
- Unexpected categories
- Invalid timestamps
- Empty records
- Unexpected error codes

A simple validation workflow:

Input Data
   ↓
Schema Check
   ↓
Missing-Value Check
   ↓
Duplicate Check
   ↓
Format Validation
   ↓
Clean Output

7. Operational Workflow

The overall approach is designed around reducing repetitive manual work and making operational analysis easier to reproduce.

Collect
  ↓
Parse
  ↓
Validate
  ↓
Transform
  ↓
Analyze
  ↓
Document

This structure can be adapted to support operations reporting, data-quality workflows, technical investigations, and KPI analysis.

Project Structure

python-bash-automation/
│
├── scripts/
│   └── log_parser.py
│
├── bash/
│   └── operational_checks.sh
│
├── sql/
│   └── operational_analysis.sql
│
├── docs/
│   └── workflow.md
│
└── README.md

Tools & Technologies

- Python
- Bash
- SQL
- Regular Expressions
- REST APIs
- JSON
- Linux
- Git

What This Project Demonstrates

- Python-based automation
- Operational data processing
- Log parsing
- SQL analysis
- Data validation
- API testing
- Repeatable workflows
- Technical documentation
- Root-cause investigation

Analyst Relevance

Although the project includes technical operations workflows, the underlying approach is directly applicable to data analytics:

collect → clean → validate → transform → analyze → report

This project demonstrates the ability to turn operational information into structured data that can be analyzed and used for decision-making.

---

Built by Sajid Manzoor

Data Analyst | SQL | Python | Power BI | Excel
