# Open_banking_hackathon_2018

Open banking hackathon (Using AI/ML to reduce risk and aid decision making in lending out loan to companies. )

The latest_loan_approval_train.py file will use the predict_loan_approval_cleaned_new.csv file to train the ML algorithm and generate the model. The intelligence of the predictive model is exported into a binary file loan_predict_model_file . Now this binary file can be used to predict the loan risk. 

Now the UI part is impletmented using Python Flask web frame work. Below are the supporting files. The template structure houses the supporting HTML like Jinja templates and static folder houses the images, logos and css files.

loan_predict_UI.py
templates --
            | -404-error.html
            | -500-error.html
            | -form-new.html
            | -prediction_output.html
            | -welcome.html
static  ----
            | - Light-blue.jpg
            | - style.css
            | - Team_logo.png

