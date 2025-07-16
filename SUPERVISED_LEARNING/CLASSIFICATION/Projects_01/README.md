# 🛡️ Fraud Detection System - A Machine Learning Approach

This repository contains a complete pipeline for detecting fraudulent financial transactions using a logistic regression model. The solution includes data preprocessing, model training, evaluation, and deployment as a real-time web application using Streamlit.

---

## 📌 Project Overview

This system is designed to assist financial institutions in identifying fraudulent transactions in real-time. The logistic regression model is trained on real-world transaction data and provides high recall for fraud detection.

- ⚙️ Model: Logistic Regression
- 🎯 Accuracy: 95%
- 🔍 Recall (Fraudulent cases): 94%
- 🌐 Web Interface: Built with Streamlit

---

## 📊 Dataset

The dataset includes anonymized records of financial transactions with the following features:

- `type`: Transaction type (e.g. CASH IN, CASH OUT, PAYMENT)
- `amount`: Monetary amount of the transaction
- `oldbalanceOrg`: Initial balance of the sender
- `newbalanceOrig`: New balance of the sender
- `oldbalanceDest`: Initial balance of the receiver
- `newbalanceDest`: New balance of the receiver
- `isFraud`: Target variable (0 = legitimate, 1 = fraud)

> **Note:** The dataset is extremely imbalanced, with fraudulent cases representing ~0.13% of all transactions.

---

## ⚙️ Features

- 🔄 Preprocessing pipeline (standardization + one-hot encoding)
- 📈 Model training and evaluation
- 📊 Confusion matrix, ROC and precision-recall curves
- 🖥️ Real-time prediction interface (Streamlit)
- 🧠 Feature importance analysis

---

## 🚀 Getting Started
### 📦 Dependencies

This project depends on the following main Python libraries:

| Package             | Description                                                                                    |
| ------------------- | ---------------------------------------------------------------------------------------------- |
| `numpy`             | Bibliothèque de calcul scientifique pour les tableaux multidimensionnels.                      |
| `pandas`            | Manipulation et analyse de données sous forme de DataFrame.                                    |
| `seaborn`           | Visualisation de données statistiques avec des graphiques élégants.                            |
| `matplotlib.pyplot` | Création de graphiques personnalisés (histogrammes, courbes, etc.).                            |
| `scikit-learn`      | Librairie de Machine Learning pour le prétraitement, modélisation, évaluation, pipelines, etc. |
| `joblib`            | Sauvegarde et chargement rapide de modèles et d’objets Python.                                 |
| `base64`            | Encodage et décodage des données en base64, souvent utilisé pour l’export.                     |


### 🚀 Installation and Setup
pip install -r requirements.txt 
download the data from kaggle 
run the app  :   streamlit run deploy.py

--- 
###  🧪 Model Performance
| Metric    | Legitimate | Fraudulent |
| --------- | ---------- | ---------- |
| Precision | 1.00       | 0.02       |
| Recall    | 0.95       | 0.94       |
| F1-Score  | 0.97       | 0.04       |

### 👨‍💻 Author
MO EHAB
📧 muhammed35ehab@gmail.com
📞 +216-55520742


