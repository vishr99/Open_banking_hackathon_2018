
#function for loading the saved model in memory and using it to predict the output
def loan_predict (input_list):
    #print("Values in list are "+ str(input_list))

    import pickle

    with open('loan_predict_model_file', 'rb') as f:
        model_loan = pickle.load(f)

    #print("Making predictions for loan application")

    X_new = input_list

    Y_new = model_loan.predict(X_new)
    Y_new = Y_new[0]
    Y_new = str(round(Y_new,0))
    Y_new = int(Y_new[0])
    #print(Y_new)

    # if Y_new == 0 :
    #     print('Loan risk is low :) ' )
    # elif Y_new == 1 :
    #     print('Loan risk is medium :| ')
    # elif Y_new == 2:
    #     print('Loan risk is high :( ')
    # else:
    #     print('Loan risk is very high  :O !!!!')

    return Y_new

#passing inputs to the model for testing
# input_list = [[10.3,0,0,10,15,8,20,500]]
# print(loan_predict(input_list))
