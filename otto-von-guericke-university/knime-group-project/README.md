# HCC Survivals: Hepatocellular Carcinoma Survival Prediction

A machine learning project predicting patient survival outcomes for hepatocellular carcinoma (liver cancer) using clinical and laboratory data.

## 👥 Team Members

- Ashish Soni
- Darshit Paresh Shah
- Momtaj Anar Monni
- Roland Schnee

**Repository layout**

- `KNIME_GROUP10.knwf`: The KNIME workflow file. Open this in KNIME to reproduce the analysis and rerun all nodes.
- `dataset/hcc-data.txt`: The dataset used in the project. It contains the input features and target labels used for modeling and analysis.
- `LICENSE`: Project license information.
- `HCC Group-10.pdf`: Project report

## 🎯 Project Objective

Predict whether a patient will survive diagnosed liver cancer based on clinical and laboratory parameters.

- **Positive (1)**: Patient Survives
- **Negative (0)**: Death

## 📊 Dataset Overview

- **Total Instances**: 165 patients
- **Total Attributes**: 49 features + 1 class attribute
- **Feature Types**: 24 nominal features with binary values
- **Data Quality Challenge**: Only 8 patients have complete data

## 🔍 Data Understanding

### Key Findings

- Significant missing data: Only 8 patients with complete records
- Non-ignorable missing values
- No semantic or syntactic errors detected
- Correlation analysis performed with threshold of 0.7

### Data Characteristics

The dataset exhibits patterns in:

- Age at diagnosis vs. Gender
- Grams of alcohol per day vs. Oxygen saturation
- Major dimension of nodules (cm) vs. Haemoglobin

## 🛠️ Data Preparation Pipeline

### 1. Data Cleaning

- **Outlier Treatment**: Closely permitted value approach
- **Missing Value Substitution**:
  - Median for numerical features
  - Most frequent value for categorical features
- **Feature Reduction**: Removed columns with >60% missing values

### 2. Feature Selection

Applied forward feature selection technique to identify the most predictive attributes.

#### Selected Features (7 attributes achieving ~79% accuracy)

1. **Hepatitis B Core Antibody**
2. **Hepatitis C Virus Antibody**
3. **Endemic Countries**
4. **International Normalized Ratio (INR)**
5. **Ascites Degree**
6. **Alpha-Fetoprotein (ng/mL)**
7. **Mean Corpuscular Volume (fl)**
8. **Alkaline Phosphatase (U/L)**

## 🤖 Modeling Approach

### Algorithm

- **Model**: Naive Bayes Classifier
- **Validation**: 10-Fold Cross-Validation

### Rationale

Naive Bayes was selected due to:

- Effectiveness with small datasets
- Robustness to missing data after preprocessing
- Good performance with binary classification problems
- Computational efficiency

## 📈 Results

### Model Performance

- **Accuracy**: ~77%
- **Key Finding**: 7 attributes are sufficient to classify patient survival outcomes

### Limitations

- Small dataset size (165 instances)
- High percentage of missing values
- Achieving higher accuracy is challenging given data constraints
