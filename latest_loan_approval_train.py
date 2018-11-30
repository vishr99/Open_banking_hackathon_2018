import pandas as pd


# Importing the training data into pandas framework
url ="C:\\Users\\VISHAL\\PycharmProjects\\untitled\\HACKATHON\\predict_loan_approval_cleaned_new.csv"

dataset = pd.read_csv(url)
dataset.columns



#Selecting The Prediction Target
y = dataset.Loan_risk

#Choosing "Features"
dataset_features = ['itr(mn INR)', 'kyc_docs', 'bank_statements', 'existing_loan_value(mn INR)', 'existing_loan_duration(yrs)',
                      'cibil_score', 'assets(mn INR)', 'loan_requirement']
X = dataset[dataset_features]
X.describe()

#Building the Machine learning Model using decision Tree regression
from sklearn.tree import DecisionTreeRegressor
loan_model = DecisionTreeRegressor(random_state=1)
loan_model.fit(X , y)


# Saving model to a file to be used for prediction.
import pickle
with open('loan_predict_model_file','wb') as f:
    pickle.dump(loan_model , f)

print("Training completed.... ready to predict :)")