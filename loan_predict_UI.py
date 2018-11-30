from flask import Flask, render_template,request,redirect,url_for,flash
from flask_wtf import FlaskForm ,Form
from wtforms import StringField, PasswordField ,SubmitField, RadioField,SelectField,validators ,IntegerField,FloatField
from wtforms.validators import InputRequired,data_required

from HACKATHON_UPDATED.latest_loan_approval_predict import loan_predict

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'

class LoginForm(FlaskForm):
    firmname = StringField('Firm Name',validators=[InputRequired('* Username is a mandatory field')])
    itr = FloatField('ITR (In million INR)', validators=[InputRequired('* Username is a mandatory field')])
    kycdocs = IntegerField('KYC Flag', [validators.number_range(min=0, max=1)])
    bankstmts = IntegerField('Bank Statements Flag', [validators.number_range(min=0, max=1)])
    existing_loan_value = FloatField ('Existing loan value</br>(In million INR)',validators=[InputRequired('* Username is a mandatory field')])
    loan_pending_term = IntegerField('Loan tenure (Yrs)')
    cibil_score = IntegerField('Cibil Score', [validators.number_range(min=0, max=10)])
    assets = FloatField ('Assets (mn INR)' , validators=[InputRequired('* Username is a mandatory field')])
    loan_requirement = FloatField ('Loan requirement (mn INR)' , validators=[InputRequired('* Username is a mandatory field')])


@app.route("/")
@app.route("/welcome")
def home():
    return render_template('welcome.html')


@app.route('/form-new',methods=['GET', 'POST'])

def form_new():
    form = LoginForm()

    if form.validate_on_submit():
        firmname = str(format(form.firmname.data))
        itr = str(format(form.itr.data))
        kycdocs = str(format(form.kycdocs.data))
        bankstmts = str(format(form.bankstmts.data))
        existing_loan_value = str(format(form.existing_loan_value.data))
        loan_pending_term = str(format(form.loan_pending_term.data))
        cibil_score = str(format(form.cibil_score.data))
        assets = str(format(form.assets.data))
        loan_requirement =  str(format(form.loan_requirement.data))

        if request.method == 'POST':

                input_list = [[itr, kycdocs, bankstmts, existing_loan_value, loan_pending_term, cibil_score, assets,
                               loan_requirement]]
                #print(input_list)
                loan_risk_score = loan_predict(input_list)
                if loan_risk_score == 0 :
                    loan_risk = 'LOW'
                elif loan_risk_score == 1 :
                    loan_risk = 'MEDIUM'
                elif loan_risk_score == 2:
                    loan_risk = 'HIGH'
                else:
                    loan_risk = 'VERY HIGH'

                #print(loan_risk)
                return render_template('prediction_output.html', loan_risk = loan_risk ,firmname = firmname )
        else:
                return 'Failure'
    return render_template('form-new.html', form=form)



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404-error.html'),404

@app.errorhandler(500)
def server_error(e):
    return render_template('500-error.html'),500


if __name__ == '__main__':
    app.run(debug=True)