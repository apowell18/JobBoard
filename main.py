from flask import Flask, render_template
from forms import RegisterJobSeekerForm,LoginForm, RegisterCompanyForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a8302621bd11d012ab09fe863f4cb347'
#create dictionary
buisnessPosts = [
    {
        'company_name': "Walmart",
        'job_title': "Data Analyst",
        'job_location': "California",
        'content': "Here is the requirements",
        'job_type': "Full-Time",
        'job_description': "Conduct advanced statistical analysis to provide actionable insights, identify trends, and measure performance.",
        'job_qualifications': "Must have Bachelors in Statistics, Computer Science, or anything realted",
        'salary': "$22 per hour",
        'contact': "https://www.youtube.com",
        'date_posted':'May 05, 2021'
    }
]
@app.route("/")
def home():
    return render_template("home.html", bPosts = buisnessPosts)

@app.route("/about")
def about():
    return render_template("about.html", title='About')

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title='Login',form=form)

@app.route("/signupCompany")
def signUpCompany():
    form = RegisterCompanyForm()
    return render_template("Company/signupCompany.html", title='Registeration',form=form)

@app.route("/signupUser")
def signupUser():
    form = RegisterJobSeekerForm()
    return render_template("JobSeeker/signupUser.html", title='Registeration',form=form)





@app.route("/createboard")
def createBoard():
    return render_template("createboard.html", title='Create Job Board')

@app.route("/profile")
def profile():
    return render_template("profile.html", title='Profile')

if __name__ == '__main__':
    app.run(debug=True)
