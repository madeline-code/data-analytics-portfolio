# Healthcare Data Wrangling and Analysis

## Project Overview

This project demonstrates an end-to-end data wrangling workflow using Python and Jupyter Notebook. Two public healthcare datasets were collected using different acquisition methods, cleaned, assessed for quality and tidiness issues, merged into a single analytical dataset, and analyzed to answer a research question.

The goal of the project was to determine whether county-level median household income is associated with emergency room utilization among Medicare beneficiaries.

---

## Research Question

**Is there a relationship between median household income and emergency room visits per 1,000 Medicare beneficiaries at the county level in the United States?**

---

## Datasets

### Centers for Medicare & Medicaid Services (CMS)
- Source: CMS Geographic Variation Public Use File
- Acquisition Method: Manual CSV download
- Variables Used:
  - County FIPS Code
  - Medicare Beneficiary Count
  - Emergency Room Visits per 1,000 Beneficiaries

### U.S. Census Bureau American Community Survey
- Source: Census Bureau ACS 5-Year API
- Acquisition Method: REST API using Python Requests
- Variables Used:
  - Population
  - Median Household Income
  - People Living in Poverty

---

## Project Workflow

- Collected data from both a CSV file and a REST API
- Assessed data quality and tidiness
- Removed missing values from key variables
- Converted variables to appropriate numeric data types
- Created standardized county FIPS codes for joining datasets
- Removed unnecessary variables
- Merged datasets into a single analytical dataset
- Saved raw and cleaned datasets separately
- Produced visualizations to answer the research question

---

## Technologies Used

- Python
- Pandas
- Requests
- Matplotlib
- Jupyter Notebook

---

## Repository Contents
