from flask import Flask , request, jsonify,render_template, request, flash
from flask_sqlalchemy import SQLAlchemy



app = Flask('__name__')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.secret_key = b'_5#y2L"F4Q8zksldkjfksd/'
db = SQLAlchemy(app)

#  booking table model 

class Booking(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_num = db.Column(db.Integer(), unique=True, nullable=False)
    case = db.Column(db.String(120), unique=False, nullable=True)
    message = db.Column(db.String(900), unique=False, nullable=False)
    
with app.app_context():
	db.create_all()

def __repr__(self):
    return '<Booking %r>' % self.name, self.email, self.phone_num, self.case, self.message


    		
	

#  contact us table model

class Contact(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_num = db.Column(db.Integer(), unique=True, nullable=False)
    subject = db.Column(db.String(120), unique=False, nullable=True)
    message = db.Column(db.String(900), unique=False, nullable=False)

    with app.app_context():
    	db.create_all()
    	
def __repr__(self):
        	return '<Contact %r>' % self.name, self.email, self.phone_num, self.subject, self.message
    


"""


@app.route('/')
@app.route('/home', methods=['GET' , 'POST'])
def home():
	if request.method == 'POST':
		name = request.form["names"]
		email = request.form["emails"]
		phone_num = request.form["phones"]
		case = request.form["subjects"]
		message = request.form["messages"]
		upload = Booking( name = name, email=email, phone_num=phone_num, case = case ,message = message)
		db.session.add(upload)
		db.session.commit()
		flash('You booked successfully ')
		return render_template('index.html')

	else:
		return render_template('index.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
	if request.method == 'POST':
		username = request.form["names"]
		email = request.form["emails"]
		phoneNO = request.form["phones"]
		subject = request.form["subjects"]
		message = request.form["messages"]
		upload = Contact( name = name, email=email, phone_num=phone_num, subject = subject,message = message)
		db.session.add(upload)
		db.session.commit()
		flash('Your message has been sent!')
		return render_template('contact.html')

	else:

		return render_template("contact.html")

"""





if __name__ == "__main__":
	app.run(debug=True)


