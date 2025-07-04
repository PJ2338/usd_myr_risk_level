# USD/MYR Risk Level Classifier

This Streamlit web application classifies the **risk level** of the USD/MYR exchange rate movement — **Low**, **Medium**, or **High** — based on recent macroeconomic indicators and their changes.

The model is trained using a **Naive Bayes classifier** with resampled data using **SMOTE** to handle class imbalance.

---

## Model Overview

- **Target Variable:** `cat_USD_MYR` (Categorical: 1 = Low Risk, 2 = Medium Risk, 3 = High Risk)
- **Algorithm Used:** Naive Bayes Classifier
- **Resampling:** SMOTE (Synthetic Minority Over-sampling Technique)

---

## Input Features

Malaysia: Changes in Unemployment Rate, CPI, Net Trade Volume
USA: Changes in Interest Rate, M1 in circulation
Global: Gold Volatility Index, CBOE Volatility Index

