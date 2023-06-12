import re
import sqlite3
import time

from cs50 import SQL
from flask import Flask, url_for, render_template, flash, redirect, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, generate_code, register_required, send_email, hush

app = Flask(__name__)


# setting up a secret key
app.config['SECRET_KEY'] = hush()

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
db = SQL('sqlite:///website.db')

@app.template_filter('add_hash')
def add_hash(url, hash):
    return url + '#' + hash

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/', endpoint='home')
@app.route('/home/', endpoint='home')
def hello_world():
    return render_template('index.html')
    # return 'Hello from Flask!'

@app.route('/login', methods=['GET', 'POST'])
def login():

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # set up the variables
        email = request.form.get('email', None)
        password = request.form.get('password', None)

        # set up regexp for checks(?=.*[\W_])
        password_regexp = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,32}$"
        email_regex = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$"

        # check vairables
        check_email_regexp = re.search(email_regex, str(email))
        check_password_regexp = re.search(password_regexp, str(password))
        # confirm checks are good

        # confirm checks are good
        if not check_password_regexp:
            return apology('Invalid Password', 'Valid Password')
        elif not check_email_regexp:
            return apology("Invalid Email",'Valid Email')

        # Query database for email
        rows = db.execute("SELECT * FROM users WHERE email = ?", request.form.get("email"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            msg = "Email or Password don't match"
            return render_template("login.html", msg=msg)

        # Remember which user has logged in
        if not 'user_id' in session:
            session["user_id"] = rows[0]["user_id"]


        # Redirect user to home page
        flash('Successfuly Signed In!')
        return redirect("/")

    else:
        if 'user_id' in session:
            flash('You are already signed in! 😆')
            return redirect('/')
        else:
            return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register user"""
    if request.method == 'POST':
        # set up the variables
        email = request.form.get('email')
        password = request.form.get('password')
        confirm = request.form.get('confirmation')
        msg = 'Email is already in use'

        # check if email exist in our data base
        row = db.execute("SELECT email FROM users WHERE email = ?", email )

        if len(row) > 0:
            return render_template('register.html', msg=msg)

        # set up regexp for checks (?=.*[\W_])
        password_regexp = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,32}$"
        email_regex = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$"

        # check vairables
        check_email_regexp = re.search(email_regex, str(email))
        check_password_regexp = re.search(password_regexp, str(password))

        # check for code confirmation and
        if not check_password_regexp:
            return apology('Invalid Password', 'Valid Password')
        elif not check_email_regexp:
            return apology("Invalid Email",'Valid Email')
        elif str(confirm) != str(password):
            return apology('invalid Confirmation','Valid Confirmation')
        else:
            hash_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
            session['password'] = hash_password
            session['email'] = email
            session['code'] = generate_code(6)
            send_email(email, session.get('code'), 1)

            return redirect('/confirm')
    else:
        if 'user_id' in session:
            flash('You are already signed in! 😆')
            return redirect('/')
        else:
            return render_template('register.html')
@app.route('/confirm', methods=['GET', 'POST'])
@register_required
def confirm():
    if request.method == 'POST':
        # set up the variabes
        confirm_code = request.form.get('confirmationCode')
        email = session.get('email', None)
        code = session.get('code', None)
        password = session.get('password', None)
        msg = "Please enter a valid confirmation code."


        # incase the button of confimr was pressed
        if request.form.get('confirm'):
            # incase we could not send the code
            if code == None or email == None or password == None:
                return apology('We encountered an error oops!?', 'Easy regestration? ')
                session.clear()
                flash('Oopsie! we have to register you again 😞')

            # compare confirm code againts random code
            if (str(code.lower()) != str(confirm_code.lower())):
                return render_template('confirm.html', msg=msg)
            else:
                # add to database
                try:
                    db.execute('INSERT INTO users (email, hash) VALUES (?, ?)', email, password)

                    # Query database for the email
                    rows = db.execute('SELECT * FROM users WHERE email = ?', email)

                    # Remember which user has logged in
                    session["user_id"] = rows[0]["user_id"]

                except sqlite3.IntegrityError as err:
                    return apology(f'{err}', 'Your data going into our database')
                    session.clear()
                    flash('Oopsie! we have to register you again 😞')

                flash('Your registration was successful 👍')
                return redirect('/')

        # Handels resending the email button
        elif request.form.get("resend"):
            # do some stuff related to the time module
            current_time = time.time()
            timer = session.get('timer', 0)
            time_delta = current_time - timer

            if time_delta < 120:
                flash(f"You can only resend the code every 2 minutes. Please wait for {120 - int(time_delta)} seconds more.")
                return redirect('/confirm')
            else:
                # first time set the value to the current time
                session['timer'] = current_time
                session['code'] = generate_code(6)
                send_email(email, session.get('code'), 1)
                flash("New code has been sent to your Email.")
                return redirect('confirm')
        # if the process is abandond for some reason
        session.clear()
        flash('Oopsie! we have to register you again 😞')
        return redirect('register')
    else:
        if 'user_id' in session:
            flash('You are already signed in! 😆')
            return redirect('/')
        else:
            return render_template("confirm.html")
@app.route('/reset', methods=['GET', 'POST'])

@app.route('/logout')
def logout():
    """ Log user out """

    # forget any user_id
    session.clear()

    # redirect user to front page
    flash('Signed Out!')
    return redirect('/home')

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)