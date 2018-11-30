
#function for loading the saved model in memory and using it to predict the output

def loan_predict (input_list):

    #loading the ML model we created earlier into memory. We need not train the model again to use it for prediction
    import pickle

    with open('loan_predict_model_file', 'rb') as f:
        model_loan = pickle.load(f)

    X_new = input_list
    Y_new = model_loan.predict(X_new)
    Y_new = Y_new[0]
    Y_new = str(round(Y_new,0))
    Y_new = int(Y_new[0])

    #Returing the prediction score based on the input passed to this model
    return Y_new
