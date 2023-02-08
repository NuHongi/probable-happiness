
app = Flask(__name__)

@app.route('/accountcreate')
def account_form():
    return render_template('index.html')

@app.route('/create_account', methods=['POST'])
def create_account():
    company_user_id = request.form['company_user_id']
    user_id = request.form['user_id']
    company_id = request.form['company_id']
    user_pin = request.form['user_pin']
    user_last_name = request.form['user_last_name']
    user_first_name = request.form['user_first_name']
    user_email = request.form['user_email']
    user_phone = request.form['user_phone']
    
    # Add logic here to process the form data and store it in the database

    return render_template('account_created.html', 
                           company_user_id=company_user_id,