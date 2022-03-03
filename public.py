from flask import *
from database import *


public=Blueprint('public',__name__)


@public.route('/')
def home():
	return render_template("home.html")

@public.route('/login',methods=['get','post'])
def login():
	if "login" in request.form:
		uname=request.form['un']
		passwd=request.form['pwd']
		q="select * from login where username='%s' and password='%s'"%(uname,passwd)
		res=select(q)
		if res:
			session['lid']=res[0]['login_id']
			if res[0]['login_type']=="admin":
				return redirect(url_for('admin.adminhome'))
			if res[0]['login_type']=="customer":
				q="select * from customer where login_id='%s'"%(session['lid'])
				res=select(q)
				session['cid']=res[0]['customer_id']
				return redirect(url_for('customer.customerhome'))	
		else:
			flash("COMPLETE YOUR REGISTRATION BEFORE TRY TO LOGIN")

	return render_template("login.html")

@public.route('/customer_registration',methods=['get','post'])
def customer_registration():
	if "register" in request.form:
		fn=request.form['fname']
		ln=request.form['lname']
		gen=request.form['gender']
		hou=request.form['housename']
		pl=request.form['place']
		pin=request.form['pincode']
		em=request.form['email']
		phone=request.form['phno']
		uname=request.form['un']
		passwd=request.form['pwd']
		q="insert into login values(null,'%s','%s','customer')" %(uname,passwd)
		id=insert(q)
		q="insert into customer values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(id,fn,ln,gen,hou,pl,pin,em,phone)
		insert(q)
		
		flash("Register Successfully")
		return redirect(url_for('public.customer_registration'))
	return render_template("customer_registration.html")

