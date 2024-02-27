# Telecom-Customer-Churn-Analysis-&-Prediction

## Project Overview

This application is designed to help businesses predict customer churn, which refers to the likelihood of customers discontinuing their services or subscriptions. By identifying customers at risk of churn, businesses can implement targeted retention strategies to improve customer satisfaction and reduce revenue loss. Utilizing the Gradient Boosting model for prediction and an analytic customer dashboard on Power BI enables proactive customer retention and profitability enhancement in the telecom sector. Additionally, interactive visualizations are deployed through Streamlit to offer stakeholders actionable insights via a user-friendly web app interface.

## Data Source
Using the Customer Churn dataset as the source of our data. "Predict behavior to retain customers. You can analyze all relevant customer data and develop focused customer retention programs." [IBM Sample Data Sets]. You can find the dataset here [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

## Technologies Used

* Power BI
* Python
* Streamlit
* Pandas
* Plotly
* Scikit-learn
* Joblib 

## Key Features

-   Customer 360* analysis visualization integrated seamlessly within Power BI for comprehensive insights into customer behavior and preferences.
-   Transparent presentation highlighting the comparison between actual and predicted churn rates.
- **Easy Prediction:** Users can easily predict customer churn either one at a time or in bulk by uploading a CSV file.
- **Understandable Insights:** The app provides clear explanations of the prediction results, including the likelihood of churn and important factors influencing the predictions.
- **Actionable Recommendations:** Based on the prediction results, the app offers actionable recommendations for businesses to retain customers and improve their overall experience.
- **Secure and Confidential:** The app ensures the security and confidentiality of customer data, with measures in place to protect sensitive information.


# Data Visualizations
## Overall Dashboard

## Customer Profiles

## Churn Reasons


# Prediction
[photo0]



## How It Works

1. **Choose Prediction Mode:** Select whether you want to predict churn for individual customers online or in bulk by uploading a CSV file.
2. **Input Customer Data:** For online prediction, enter the relevant customer information such as tenure, services used, and contract details. For batch prediction, upload a CSV file containing multiple customer records.
3. **View Prediction Results:** Once the prediction is complete, the app displays the likelihood of churn for each customer along with detailed insights and recommendations.
4. **Take Action:** Based on the insights provided, businesses can take proactive steps to retain at-risk customers and improve overall customer satisfaction.
5. **Download Results:** If needed, users can download the prediction results for further analysis or reporting purposes.

# Benefits

- **Improved Customer Retention:** By identifying customers at risk of churn, businesses can implement targeted retention strategies to reduce churn rates and increase customer loyalty.
- **Enhanced Decision Making:** The app provides valuable insights into the factors influencing churn, helping businesses make informed decisions about resource allocation and customer engagement.
- **Cost Savings:** Retaining existing customers is often more cost-effective than acquiring new ones. By reducing churn, businesses can save on acquisition costs and increase revenue.
- **Competitive Advantage:** By proactively addressing churn, businesses can differentiate themselves from competitors and build a reputation for excellent customer service.

# Challenge & Limitations

The Customer Churn Prediction App may exhibit limitations such as potential bias in model predictions, challenges in interpreting complex model decisions, and the need for continuous updates to address evolving customer behavior and market dynamics.

## Demo 1

## Demo 2

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

**Project Structure**

*   `data/`: Contains raw telecom datasets (.csv, .h5, or other format)
*   `models/`: Gradient Boosting model  (e.g., a .pkl or .joblib file)
*   `Code/`:  Script for data cleaning, feature engineering, and train/test splits.
*   `app.py`: Core Streamlit application code. 


**Contact & Connect**

For further inquiries or to discuss potential collaborations, please feel free to connect with me on LinkedIn: (https://www.linkedin.com/in/poch-vibolvatanak-507007157/)
