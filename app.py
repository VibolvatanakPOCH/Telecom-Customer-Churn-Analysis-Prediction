import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from imblearn.combine import SMOTEENN
import joblib
import base64


# Load the model using joblib
model = joblib.load('gradient_boosting_model.joblib')

def predict(model, input_df):
    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)[:, 1]  # Probability of positive class (churn)
    return prediction[0], probability[0]

def preprocess_data(batch_df):
    # Drop any non-numeric columns or columns not used by the model
    relevant_columns = ['tenure', 'OnlineSecurity', 'OnlineBackup', 'TechSupport', 'Contract', 'MonthlyCharges', 'TotalCharges']
    batch_df = batch_df[relevant_columns]
    
    # Convert categorical variables to numerical (if necessary)
    # For example, if columns like 'OnlineSecurity', 'OnlineBackup', 'TechSupport' have string values like 'Yes', 'No', 'No internet service'
    # you may need to convert them to numeric values (e.g., 0, 1, 2)
    batch_df['OnlineSecurity'] = batch_df['OnlineSecurity'].map({'No': 0, 'Yes': 2, 'No internet service': 1})
    batch_df['OnlineBackup'] = batch_df['OnlineBackup'].map({'No': 0, 'Yes': 2, 'No internet service': 1})
    batch_df['TechSupport'] = batch_df['TechSupport'].map({'No': 0, 'Yes': 2, 'No internet service': 1})
    
    # Ensure all columns are numeric
    batch_df = batch_df.apply(pd.to_numeric, errors='coerce')
    
    # Handle missing values (if any)
    batch_df.fillna(0, inplace=True)  # Replace NaN values with 0
    
    return batch_df

def main():
    
    st.set_page_config(page_title="Customer Churn Prediction", page_icon=":bar_chart:", layout="wide")

    from PIL import Image
    image = Image.open('images/data-analysis.png')
    image2 = Image.open('images/workflow.png')
    image3 = Image.open('images/important.png')
    image4 = Image.open('images/action.png')
    image5 = Image.open('images/image.png')
    image6 = Image.open('images/work.png')
    
    
    add_selectbox = st.sidebar.selectbox(
        "How would you like to predict?",
        ('Online', 'Batch'))
    st.sidebar.info('This app is created to predict Customer Churn')
    
    if add_selectbox == 'Online':
        st.sidebar.image(image2, use_column_width=True)
        st.image(image, use_column_width=False)
        
        st.title("Predicting Customer Churn")
    
        # Add subtitle to describe input values
        st.subheader("Input Values:")
        st.write("[0 = No , 1 = No Internet Service , 2 = Yes]")
        
        # Add GitHub link
        st.sidebar.markdown("### Download Full Resources")
       
        if st.sidebar.button("Download", key="github_download"):
            st.sidebar.markdown(f"[on Github Repository](https://github.com/Vatanak8/Telecom-Customer-Churn-Analysis-Prediction)")

        # Add social media buttons with icons
        st.sidebar.markdown("### Get in Touch:")

        linkedin_link = "https://www.linkedin.com/in/poch-vibolvatanak-507007157/"
        medium_link = "https://medium.com/@pochvibolvatanak"
        telegram_link = "https://t.me/VibolVatanak"
        github_link = "https://github.com/Vatanak8"

        st.sidebar.markdown(
            f"""
            [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)]({linkedin_link})
            [![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)]({medium_link})
            [![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)]({telegram_link})
            [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)]({github_link})
            """
        )

        tenure = st.number_input('Tenure (Months):', min_value=1, max_value=72, value=1, key='tenure')
        OnlineSecurity = st.selectbox('Does the customer have Online Security?', ['', 2, 1, 0], key='OnlineSecurity')
        OnlineBackup = st.selectbox('Does the customer have Online Backup?', ['', 2, 1, 0], key='OnlineBackup')
        TechSupport = st.selectbox('Does the customer have Tech Support?', ['', 2, 1, 0], key='TechSupport')
        Contract = st.selectbox('Contract Type: [0 = Month to Month, 1 = 1 Year , 2 = 2 Year]', ['', 2, 1, 0], key='Contract')
        MonthlyCharges = st.number_input('Monthly Charges ($)', min_value=18, max_value=120, value=18, key='MonthlyCharges')
        TotalCharges = st.number_input('Total Charges ($):', min_value=18, max_value=9000, value=18, key='TotalCharges')

        output = ""
        input_dict = {
            'tenure': [tenure],
            'OnlineSecurity': [OnlineSecurity],
            'OnlineBackup': [OnlineBackup],
            'TechSupport': [TechSupport],
            'Contract': [Contract],
            'MonthlyCharges': [MonthlyCharges],
            'TotalCharges': [TotalCharges],
        }

        input_df = pd.DataFrame(input_dict)

        if st.button("Predict"):
            # Check if all required fields are filled
            if input_df.isnull().values.any() or '' in [tenure, OnlineSecurity, OnlineBackup, TechSupport, Contract, MonthlyCharges, TotalCharges]:
                st.error("Please input the required informations!")
            else:
                prediction, probability = predict(model=model, input_df=input_df)
                output = "Customer is Churn" if prediction == 1 else "Customer is not Churn"
                st.success(output)
                st.write(f"Probability of Churn: {probability:.2f}")
                
                # Fetch feature importance
                st.image(image3)
                feature_importance = model.feature_importances_
                df_importance = pd.DataFrame({
                    'Feature': input_df.columns,
                    'Importance': feature_importance
                })
                df_importance = df_importance.sort_values(by='Importance', ascending=False)
                st.subheader("Feature Importance:")
                st.write(df_importance)
                
                # Interactive bar chart for feature importance
                st.subheader("Interactive Feature Importance:")
                st.bar_chart(df_importance.set_index('Feature')['Importance'])
                
                # Summary of Input Values
                st.subheader("Summary of Input Values:")
                st.write(input_df)
                
                # Interpretation of Feature Importance
                st.subheader("Interpretation of Feature Importance:")
                st.write(
                    """
                    - **Tenure (Months):** The length of time a customer has been with the company. Longer tenures may indicate higher loyalty.
                    - **Online Security:** Whether the customer has online security services. Having online security can reduce the risk of cyber threats.
                    - **Online Backup:** Indicates whether the customer has online backup services. Having backup can protect data from loss.
                    - **Tech Support:** Indicates whether the customer has access to technical support. Tech support can provide assistance in resolving issues.
                    - **Contract Type:** Specifies the type of contract. Longer contract durations may indicate stronger commitment from customers.
                    - **Monthly Charges:** The amount the customer pays per month. Higher charges may indicate more premium services.
                    - **Total Charges:** The total charges incurred by the customer. Higher total charges may indicate more usage of services.
                    """
                )
                
                # Recommendations based on Insights
                st.image(image4)
                st.subheader("Recommendations:")
                st.write(
                    """
                    - Offer incentives or discounts to customers with longer tenures to encourage loyalty. [Learn More](https://www.linkedin.com/pulse/9-proven-customer-retention-strategies-your-business-/?trk=public_post)
                    - Promote the importance of online security and backup services to customers without them. [Learn More](https://utilitiesone.com/telecommunication-towers-and-ensuring-network-security)
                    - Enhance technical support services to improve customer satisfaction and retention. [Learn More](https://www.process.st/how-to/improve-customer-retention-in-internet-and-technical-services/)
                    - Provide special offers or benefits for customers opting for longer contract durations. [Learn More](https://agencyanalytics.com/blog/agency-client-contracts)
                    - Consider adjusting pricing strategies based on the analysis of monthly and total charges. [Learn More](https://blog.hubspot.com/sales/pricing-strategy)
                    """
                )
    
    elif add_selectbox == 'Batch':
        st.empty()  # Hide previous content
        st.sidebar.image(image5, use_column_width=True)
        st.image(image6, use_column_width=False) 
        
        # Add GitHub link
        st.sidebar.markdown("### Download Full Resources")
       
        if st.sidebar.button("Download", key="github_download"):
            st.sidebar.markdown(f"[on Github Repository](https://github.com/Vatanak8/Telecom-Customer-Churn-Analysis-Prediction)")

        # Add social media buttons with icons
        st.sidebar.markdown("### Get in Touch:")

        linkedin_link = "https://www.linkedin.com/in/poch-vibolvatanak-507007157/"
        medium_link = "https://medium.com/@pochvibolvatanak"
        telegram_link = "https://t.me/VibolVatanak"
        github_link = "https://github.com/Vatanak8"

        st.sidebar.markdown(
            f"""
            [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)]({linkedin_link})
            [![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)]({medium_link})
            [![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)]({telegram_link})
            [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)]({github_link})
            """
        )
        
        st.header("Batch Prediction")
        
        # Allow user to upload a CSV file
        uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])
        
        if uploaded_file is not None:
            # Read the uploaded file
            batch_df = pd.read_csv(uploaded_file)
            
            # Preprocess the data
            processed_batch_df = preprocess_data(batch_df)
            
            # Perform batch prediction
            batch_predictions = model.predict(processed_batch_df)
            batch_probabilities = model.predict_proba(processed_batch_df)[:, 1]
            

            # Add predictions and probabilities to the original DataFrame
            batch_df['Predictions'] = batch_predictions
            batch_df['Probability'] = batch_probabilities
            
            
            # Calculate probability score for '1' and '0'
            probability_score_1 = batch_df[batch_df['Predictions'] == 1]['Probability'].mean()
            probability_score_0 = batch_df[batch_df['Predictions'] == 0]['Probability'].mean()

            # Display the original DataFrame with calculated probability scores for '1' and '0'
            st.subheader("Original DataFrame with Probability Scores:")
            batch_df_with_scores = batch_df.copy()
            batch_df_with_scores['Probability Score (Churn=1)'] = probability_score_1
            batch_df_with_scores['Probability Score (Churn=0)'] = probability_score_0
            st.write(batch_df_with_scores)

            
            # Display the original DataFrame
            #st.subheader("Original DataFrame:")
            #st.write(batch_df)
            
            
            # Explanation of Batch Prediction Results
            st.subheader("Explanation of Batch Prediction Results:")
            st.write(
                """
                The batch prediction results display the predictions and probabilities of churn for each customer record.
                - **Predictions:** Indicates whether each customer is predicted to churn (1) or not churn (0).
                - **Probability:** Represents the likelihood of churn for each customer, with higher probabilities indicating 
                  a higher likelihood of churn.
                """
            )
            
            
            # Download the updated DataFrame as a CSV file
            csv_file = batch_df_with_scores.to_csv(index=False)
            download_button_html = f'<a href="data:file/csv;base64,{base64.b64encode(csv_file.encode()).decode()}" download="batch_predictions.csv"><button style="background-color:#4CAF50; color:white; padding: 10px 15px; text-align: center; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 8px;"><i class="fa fa-download"></i> Download Batch Predictions</button></a>'
            st.markdown(download_button_html, unsafe_allow_html=True)
            
            
            # Visualization: Count plot of predicted churn
            st.subheader("Count of Predicted Churn vs Non-Churn Customers:")
            churn_count = batch_df['Predictions'].value_counts().reset_index()
            churn_count.columns = ['Prediction', 'Count']
            fig1 = px.bar(churn_count, x='Prediction', y='Count', color='Prediction', labels={'Prediction': 'Churn Prediction', 'Count': 'Count'})
            st.plotly_chart(fig1, use_container_width=True)
            
            # Visualization: Bar plot of probabilities
            st.subheader("Probabilities of Churn for Each Customer:")
            fig2 = go.Figure()
            fig2.add_trace(go.Scatter(
                x=batch_df.index,
                y=batch_df['Probability'],
                mode='markers',
                marker=dict(color='blue', size=10),
                hovertemplate='Customer Index: %{x}<br>Probability of Churn: %{y:.2f}<extra></extra>'
            ))
            fig2.update_layout(xaxis_title='Customer Index', yaxis_title='Probability of Churn', title='Probabilities of Churn for Each Customer')
            st.plotly_chart(fig2, use_container_width=True)
            
            
            # Add enhanced explanation about the prediction process
            st.subheader("Prediction Process:")
            st.write(
                """
                The prediction process involves analyzing various factors to determine whether a customer is likely to churn. 
                This includes:
                - **Tenure:** The length of time a customer has been with the company. Longer tenures may indicate higher loyalty.
                - **Online Security:** Whether the customer has online security services. Having online security can reduce the risk of cyber threats.
                - **Online Backup:** Indicates whether the customer has online backup services. Having backup can protect data from loss.
                - **Tech Support:** Indicates whether the customer has access to technical support. Tech support can provide assistance in resolving issues.
                - **Contract Type:** Specifies the type of contract. Longer contract durations may indicate stronger commitment from customers.
                - **Monthly Charges:** The amount the customer pays per month. Higher charges may indicate more premium services.
                - **Total Charges:** The total charges incurred by the customer. Higher total charges may indicate more usage of services.

                By analyzing these factors, the machine learning model assigns a probability to each customer, indicating the likelihood of churn. 
                Higher probabilities suggest a higher likelihood of churn, while lower probabilities indicate lower risk. 
                This information enables businesses to identify at-risk customers and implement targeted retention strategies.
                """
            )
            
            
            # Feature Importance
            st.image(image3)
            st.subheader("Feature Importance:")
            feature_importance = model.feature_importances_
            df_importance = pd.DataFrame({
                'Feature': processed_batch_df.columns,
                'Importance': feature_importance
            })
            df_importance = df_importance.sort_values(by='Importance', ascending=False)
            st.write(df_importance)
            
            # Summary Statistics
            st.subheader("Summary Statistics:")
            st.write(processed_batch_df.describe())
            
            
            
            # Recommendations based on Batch Prediction Results
            st.image(image4)
            st.subheader("Recommendations based on Batch Prediction Results:")
            st.write(
                """
                Based on the batch prediction results, businesses can take the following actions to mitigate churn and improve 
                customer retention:
                - Identify customers with high probabilities of churn and offer targeted incentives or discounts to encourage 
                  continued engagement.
                - Implement proactive customer outreach programs to address potential issues and enhance satisfaction.
                - Analyze patterns and trends among churned customers to identify common factors and adjust business strategies 
                  accordingly.
                - Focus on delivering exceptional customer experiences to build loyalty and long-term relationships.
                """
            )
            


        

if __name__ == '__main__':
    main()
