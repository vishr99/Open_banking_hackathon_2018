import pandas as pd
from sklearn.metrics import accuracy_score


url ="C:\\Users\\VISHAL\\PycharmProjects\\untitled\\HACKATHON\\predict_loan_approval_cleaned_new.csv"

dataset = pd.read_csv(url)
dataset.columns
#print(dataset.columns)


#Selecting The Prediction Target
y = dataset.Loan_risk

#Choosing "Features"
dataset_features = ['itr(mn INR)', 'kyc_docs', 'bank_statements', 'existing_loan_value(mn INR)', 'existing_loan_duration(yrs)',
                      'cibil_score', 'assets(mn INR)', 'loan_requirement']
X = dataset[dataset_features]
X.describe()
#print(X.describe())
#print(type(X))

#Building the Model
from sklearn.tree import DecisionTreeRegressor
loan_model = DecisionTreeRegressor(random_state=1)
loan_model.fit(X , y)

#Making Predictions
#print("Making predictions for loan application")
#X_new = [[10,1,1,2,10,5,150,2]]
# X_new = [[2420,1,1,1198,15,7,90,175]]
#
# Y_new = loan_model.predict(X_new)
# Y_new = Y_new[0]
# Y_new = str(round(Y_new,0))
# Y_new = int(Y_new[0])
# print(Y_new)
#
# if Y_new == 0 :
#     print('Loan risk is low :) ' )
# elif Y_new == 1 :
#     print('Loan risk is medium :| ')
# elif Y_new == 2:
#     print('Loan risk is high :( ')
# else:
#     print('Loan risk is very high  :O !!!!')

#-----------------------------------
# Saving model to a file
import pickle
with open('loan_predict_model_file','wb') as f:
    pickle.dump(loan_model , f)

print("Training completed.... I am ready to predict :)")