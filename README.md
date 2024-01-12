
# Industrial Copper Modeling Project

## Introduction

The Industrial Copper Modeling project is a data science project aimed at utilizing machine learning techniques to address challenges in the copper industry, specifically focusing on sales and pricing data. The project includes the development of regression and classification models, as well as the creation of an interactive web application using Streamlit.

## Project Structure

The project follows a structured approach, including the following key components:

1. **Data Understanding and Preprocessing:**
   - Identification of variable types and preprocessing steps.
   - Treatment of outliers, missing values, and skewness.

2. **Exploratory Data Analysis (EDA):**
   - Visualization of outliers and skewness using Seaborn's plots.
   - Feature engineering and correlation analysis.

3. **Model Building and Evaluation:**
   - Regression model using Decision Tree Regressor.
   - Classification model using Decision Tree Classifier.
   - Model optimization and evaluation metrics.

4. **Streamlit Web Application:**
   - Creation of an interactive web page for model predictions.
   - Input fields for user-provided data.
   - Display of predicted 'Selling_Price' or 'Status.'

5. **Model Persistence:**
   - Saving of trained models, scaler, and encoders using the Pickle module.

6. **Learning Outcomes:**
   - Development of Python programming skills.
   - Proficiency in data preprocessing, EDA, and machine learning modeling.
   - Experience in creating interactive web applications with Streamlit.

7. **Project Evaluation Metrics:**
   - Code modularity and maintainability.
   - Portability across different environments.
   - Availability of a public GitHub repository with proper documentation.
   - Adherence to PEP 8 coding standards.

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
