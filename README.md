---

# Industrial Copper Modeling

### Domain: Manufacturing

🔗 **Live App**: [Streamlit App](https://industrialcoppermodelling-ragha22.streamlit.app/)

---

## 📌 Problem Statement

The copper industry often grapples with noisy, skewed sales and pricing data, making manual prediction and analysis inefficient and inaccurate. Additionally, the challenge of identifying quality leads based on sales status adds complexity to decision-making. This project aims to:

* Build a **Regression Model** to predict the continuous variable `Selling_Price`.
* Develop a **Classification Model** to predict lead conversion status (`WON` or `LOST`).
* Create an **interactive Streamlit web application** to allow users to input features and get real-time predictions for either task.

---

## 🗂️ Dataset Description

The dataset contains information on copper product sales including transactional, customer, and product specifications.

| Feature         | Description                                          |
| --------------- | ---------------------------------------------------- |
| `id`            | Unique identifier for each record                    |
| `item_date`     | Transaction date                                     |
| `quantity tons` | Quantity sold (in tons)                              |
| `customer`      | Customer identifier                                  |
| `country`       | Customer country                                     |
| `status`        | Status of deal (e.g., WON, LOST)                     |
| `item type`     | Type of item sold                                    |
| `application`   | Application code for item                            |
| `thickness`     | Thickness of the item                                |
| `width`         | Width of the item                                    |
| `material_ref`  | Material reference code                              |
| `product_ref`   | Product reference code                               |
| `delivery date` | Delivery date                                        |
| `selling_price` | Selling price of the product (Target for Regression) |

---

## 🔍 Approach

### 1. Data Understanding

* Identified variable types (categorical/continuous)
* Treated anomalies in `material_ref` (e.g., values starting with `00000`)
* Handled reference columns as categorical features

### 2. Data Preprocessing

* Imputed missing values using statistical techniques (mean/median)
* Handled outliers via **IQR method** and **Isolation Forest**
* Treated skewness with **log transformation** and **Box-Cox**
* Encoded categorical variables using **One-Hot** and **Label Encoding**

### 3. Exploratory Data Analysis (EDA)

* Visualized skewness and outliers using `Seaborn` (boxplot, violinplot)
* Correlation heatmaps to drop highly correlated features

### 4. Feature Engineering

* Created new informative features when needed
* Dropped redundant or highly correlated features

### 5. Model Building

#### Regression:

* Tree-based models (Random Forest, XGBoost) used due to data non-linearity and noise
* Target: `selling_price`
* Evaluation Metrics: MAE, RMSE, R² Score

#### Classification:

* Models: Logistic Regression, ExtraTreesClassifier, XGBClassifier
* Target: `status` (filtered for `WON`, `LOST`)
* Evaluation Metrics: Accuracy, Precision, Recall, F1-score, AUC-ROC

### 6. Streamlit Application

* Choose task: Regression or Classification
* Input fields for all feature columns (excluding target)
* Model predictions displayed instantly
* Behind the scenes:

  * Applied same preprocessing (scaling, encoding, transformation)
  * Loaded trained models using `pickle`

---

## ✅ Conclusion

This end-to-end machine learning solution offers real-time insights into copper product pricing and lead conversion. By automating predictions and deploying them via a simple web app, the project supports better decision-making in the manufacturing domain.



## Getting Started

To run the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/raghavendranhp/Industrial_copper_modelling.git
   cd industrial-copper-modeling
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute the main script:
   ```bash
   python main_script.py
   ```

4. Access the Streamlit web application by opening the provided URL in your browser.

## Project Structure

```
industrial-copper-modeling/
│
├── data/                  # Directory for storing datasets
├── models/                # Directory for saving trained models
├── Copper_Modelling.ipynb # Jupyter notebooks for exploration and analysis
├── .gitignore
├── main_script.py         # Main script for running the project
├── requirements.txt       # List of project dependencies
└── README.md              # Project documentation
```

## Contributions

Contributions to the project are welcome. If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
