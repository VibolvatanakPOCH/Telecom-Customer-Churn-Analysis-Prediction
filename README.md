# Telecom-Customer-Churn-Analysis-&-Prediction

## Project Overview

This application is designed to help businesses predict customer churn, which refers to the likelihood of customers discontinuing their services or subscriptions. By identifying customers at risk of churn, businesses can implement targeted retention strategies to improve customer satisfaction and reduce revenue loss. Utilizing the Gradient Boosting model for prediction and an analytic customer dashboard on Power BI enables proactive customer retention and profitability enhancement in the telecom sector. Additionally, interactive visualizations are deployed through Streamlit to offer stakeholders actionable insights via a user-friendly web app interface.

## Data Source
Using the Customer Churn dataset as the source of our data. "Predict behavior to retain customers. You can analyze all relevant customer data and develop focused customer retention programs." [IBM Sample Data Sets]. You can find the dataset here: [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

## Technologies Used

* Power BI
* Python
* Streamlit
* Pandas
* Plotly
* Scikit-learn
* SMOTEENN
* Joblib 

## Key Features

- **Customer 360 analysis** visualization integrated seamlessly within Power BI for comprehensive insights into customer behavior and preferences.
- **Transparent presentation** highlighting the comparison between actual and predicted churn rates.
- **Easy Prediction:** Users can easily predict customer churn either one at a time or in bulk by uploading a CSV file.
- **Understandable Insights:** The app provides clear explanations of the prediction results, including the likelihood of churn and important factors influencing the predictions.
- **Actionable Recommendations:** Based on the prediction results, the app offers actionable recommendations for businesses to retain customers and improve their overall experience.
- **Secure and Confidential:** The app ensures the security and confidentiality of customer data, with measures in place to protect sensitive information.


# 🔍 Data Visualization 
## 📊 Telecom Customer Churn Dashboard Summary

 Analyze customer segmentation based on demographics, usage patterns, and contract types to gain insights into churn behavior over time, while ensuring data security measures align with regulatory compliance standards. For full experience and interaction with the dashboard, Here is the link to the dashboard: [Telecom Customer Churn Analysis Dashboard](https://www.novypro.com/project/telecom-customer-churn-analysis---power-bi)

- 🎯**Customer Segmentation**
"Segmentation of customers based on demographics, usage patterns, and contract types provides insights into churn behavior across different customer segments."

- 📈 **Churn Trend Analysis**
"Trend analysis depicts churn patterns over time, enabling businesses to identify seasonality and trend changes to anticipate future churn."

- 🔒 **Data Security Measures**
"Explanation of measures taken to ensure the security and confidentiality of customer data, aligning with regulatory compliance standards."

<img width="1283" alt="D1" src="https://github.com/Vatanak8/Telecom-Customer-Churn-Analysis-Prediction/assets/95983559/358b66f7-d7b9-439f-ad14-60cdc9c13ae1">


## 📊 Customer Profile Overview

- 👤 **Customer ID:** Identify individual customers within the system.

- 🔄 **Churn Index:** Track the likelihood of customers churning based on historical data and predictive models.

- 💰 **Total Charge:** Monitor the total charges incurred by each customer, aiding in financial analysis and customer valuation.

- 🛡️ **Risk Level:** Assess the risk associated with each customer's churn probability, guiding targeted retention strategies.

- 📝 **Personal Details:** Include demographic information such as age, gender, and location to understand customer characteristics.

- 📄 **Contract Details:** Review contract specifics, including contract type, duration, and terms, to tailor retention offers effectively.

- 💼 **Other Details:** Incorporate additional relevant information such as service usage patterns, customer feedback, and engagement metrics to enrich customer profiles and inform retention efforts.

<img width="1097" alt="D2" src="https://github.com/Vatanak8/Telecom-Customer-Churn-Analysis-Prediction/assets/95983559/ebf72061-41a8-4171-a359-29c5d0b51e85">

## 📊 Customer Churn Reasons Overview

- 💰 **Total Charge Analysis:** Investigate the correlation between total charges and churn, quantifying the impact of expenditure on customer retention.

- 💵 **Total Charge of Risk Customers:** Evaluate the total charges of high-risk and very high-risk customers in dollars to pinpoint financial implications associated with churn-prone segments.

- 🛡️ **Risk Group Distribution:** Categorize customers into risk groups (non-risky, low-risky, risky, high-risk, very high-risky) based on churn probability, providing a numerical breakdown alongside dollar figures to illustrate the financial stakes associated with each risk category.

- 📈 **Number of Risky Customers:** Quantify the count of customers in each risk category and associated expenditure in dollars, facilitating a comprehensive understanding of churn risk distribution and financial impact across different customer segments.

<img width="1100" alt="D3" src="https://github.com/Vatanak8/Telecom-Customer-Churn-Analysis-Prediction/assets/95983559/9bc78c2d-3d32-4bd1-a08f-0d6f43051d05">


# Model Prediction - Streamlit Web App

[fdfdd]  
#### Prediction Options
![WA1 - 2 Prediction Option](https://github.com/Vatanak8/Telecom-Customer-Churn-Analysis-Prediction/assets/95983559/96aecb33-c24c-45e8-b7e6-e23144b5a00c)

# Benefits

- **Improved Customer Retention:** By identifying customers at risk of churn, businesses can implement targeted retention strategies to reduce churn rates and increase customer loyalty.
- **Enhanced Decision Making:** The app provides valuable insights into the factors influencing churn, helping businesses make informed decisions about resource allocation and customer engagement.
- **Cost Savings:** Retaining existing customers is often more cost-effective than acquiring new ones. By reducing churn, businesses can save on acquisition costs and increase revenue.
- **Competitive Advantage:** By proactively addressing churn, businesses can differentiate themselves from competitors and build a reputation for excellent customer service.

# Challenge & Limitations

The Customer Churn Prediction App may exhibit limitations such as potential bias in model predictions, challenges in interpreting complex model decisions, and the need for continuous updates to address evolving customer behavior and market dynamics.

## How It Works

1. **Choose Prediction Mode:** Select whether you want to predict churn for individual customers online or in bulk by uploading a CSV file.
2. **Input Customer Data:** For online prediction, enter the relevant customer information such as tenure, services used, and contract details. For batch prediction, upload a CSV file containing multiple customer records.
3. **View Prediction Results:** Once the prediction is complete, the app displays the likelihood of churn for each customer along with detailed insights and recommendations.
4. **Take Action:** Based on the insights provided, businesses can take proactive steps to retain at-risk customers and improve overall customer satisfaction.
5. **Download Results:** If needed, users can download the prediction results for further analysis or reporting purposes.

#### Online Prediction
![WA2 - Online Prediction](https://github.com/Vatanak8/Telecom-Customer-Churn-Analysis-Prediction/assets/95983559/a6284582-db9c-49a2-8193-fd54fca9c09d)

#### Explanation & Recommendation
![WA3 - Online Result Explanation   Recommendation](https://github.com/Vatanak8/Telecom-Customer-Churn-Analysis-Prediction/assets/95983559/7dfbc100-ab69-45cc-a0e4-29eeb410c900)

#### Batch Prediction & Download Predicted Report (.csv)
![WA4 - Batch Prediction + Download](https://github.com/Vatanak8/Telecom-Customer-Churn-Analysis-Prediction/assets/95983559/319e3e88-a8c1-4f3a-8399-36c7e7175167)

#### Explanation 
![WA5 - Batch Result Explanation](https://github.com/Vatanak8/Telecom-Customer-Churn-Analysis-Prediction/assets/95983559/ec6c6007-51c1-418d-8200-b0128014358e)


## Installation

To install and run the app locally, follow these steps:

1.  **Clone Repository:**
    ```bash
    git clone https://github.com/Vatanak8/Telecom-Customer-Churn-Analysis-Prediction
    ```

2.  **Environment Setup:**
    ```bash
    pip install -r requirements.txt 
    ```

3.  **Launch App:**
    ```bash
    streamlit run app.py 
    ```

## Project Structure

*   `data/`: Contains raw telecom datasets (.csv, .h5, or other format)
*   `codels/`: Gradient Boosting model  (e.g., a .pkl or .joblib file)
*   `code/`:  Script for data cleaning, feature engineering, and train/test splits.
*   `app.py`: Core Streamlit application code. 


## Contact & Connect

For further inquiries or to discuss potential collaborations, please feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/poch-vibolvatanak-507007157/)
