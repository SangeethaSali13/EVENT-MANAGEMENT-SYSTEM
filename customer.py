from flask import *
from database import *

customer=Blueprint('customer',__name__)

@customer.route('/customerhome')
def customerhome():
	return render_template('customerhome.html')

@customer.route('/customervieweventcategories')	
def customervieweventcategories():
	data={}
	q="select * from eventcategories"
	res=select(q)
	data['eventcategories']=res
	return render_template('customervieweventcategories.html',data=data)

@customer.route('/customervieweventpackages')
def customervieweventpackages():	
	data={}
	q="select * from eventpackages where status='available'"
	res=select(q)
	data['eventpackages']=res

	return render_template('customervieweventpackages.html',data=data)

@customer.route('/customerviewaddfeatures')
def customerviewaddfeatures():	
	data={}
	q="select * from features"
	res=select(q)
	data['features']=res
	return render_template('customerviewaddfeatures.html',data=data)	

@customer.route('/customermanagecustomevent',methods=['get','post'])	
def customermanagecustomevent():
	cid=session['cid']
	data={}
	q="select * from customevent where customer_id='%s'"%(cid)
	res=select(q)
	data['customevent']=res

	if 'manage' in request.form:
		customeventtitle=request.form['cet']
		budgetamount=request.form['ba']
		q="insert into customevent values(null,'%s','%s','%s',CURDATE(),'pending')" %(cid,customeventtitle,budgetamount)
		insert(q)

		return redirect(url_for('customer.customermanagecustomevent'))
	
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
			
	if action=="delete":
		q="delete from customevent where custom_event_id='%s'" %(id)
		delete(q)
		return redirect(url_for('customer.customermanagecustomevent'))

	if action=="update":
		q="select * from customevent where custom_event_id='%s'" %(id)
		res=select(q)
		data['cust']=res
	if 'update' in request.form:
		customeventtitle=request.form['cet']
		budgetamount=request.form['ba']
		q="update customevent set custom_event_title='%s',budget_amount='%s' where custom_event_id='%s'" %(customeventtitle,budgetamount,id)
		update(q)
		return redirect(url_for('customer.customermanagecustomevent'))			
	return render_template('customermanagecustomevent.html',data=data)

@customer.route('/customer_book_eventpackages',methods=['get','post'])
def customer_book_eventpackages():
 
	pid=request.args['pid']
	cid=session['cid']
	if 'submit' in request.form:
		bookingdate=request.form['bd']
		bookingtime=request.form['bt']
		bookingvenue=request.form['bv']
		q="insert into booking values(null,'%s','%s','%s','%s','%s','pending','event package')" %(pid,cid,bookingdate,bookingtime,bookingvenue)
		insert(q)
		return redirect(url_for('customer.customer_book_eventpackages',pid=pid))
	return render_template('customer_book_eventpackages.html')

@customer.route('/customer_manage_custom_event_details',methods=['get','post'])	
def customer_manage_custom_event_details():
	ceid=request.args['ceid']
	data={}
	q="select * from features"
	res=select(q)
	data['feature']=res
	if 'customevent' in request.form:
		feature=request.form['feature']
		q="insert into customeventdetails values(null,'%s','%s')"%(ceid,feature)
		insert(q)
	return render_template('customer_manage_custom_event_details.html',data=data)

@customer.route('/customersendcomplaint',methods=['get','post'])
def customersendcomplaint():
	cid=session['cid']
	data={}
	q="select * from complaints where customer_id='%s'" %(cid)
	res=select(q)
	data['complaints']=res

	if 'submit' in request.form:
		complaint=request.form['ct']
		q="insert into complaints values(null,'%s','%s',CURDATE(),'pending')" %(complaint,cid)
		insert(q)
	return render_template('customersendcomplaint.html',data=data)

@customer.route('/customersendfeedback',methods=['get','post'])
def customersendfeedback():
	cid=session['cid']
	data={}
	q="select * from feedback"
	res=select(q)
	data['feedback']=res

	if 'submit' in request.form:
		feedback=request.form['fb']
		q="insert into feedback values(null,'%s','%s',CURDATE())" %(feedback,cid)
		insert(q)
	return render_template('customersendfeedback.html',data=data)

@customer.route('/customervieweventbooking')
def customervieweventbooking():
	data={}
	cid=session['cid']
	q="select * from booking inner join eventpackages on(eventpackages.package_id=booking.event_id) where customer_id='%s'" %(cid)
	res=select(q)
	data['booking']=res
	return render_template('customervieweventbooking.html',data=data)

@customer.route('/customermakepayment',methods=['get','post'])	
def customermakepayment():

	bid=request.args['bid']

	amt=request.args['amt']
	data={}
	data['amt']=amt
	q="select * from booking inner join eventpackages on(booking.event_id=eventpackages.`package_id`) inner join packagedetails using(package_id) inner join features using(feature_id) where booking_id='%s'"%(bid)
	print(q)
	res=select(q)
	print(res)
	data['pdetails']=res
	q="select * from payment"
	res=select(q)
	data['payment']=res

	if 'submit' in request.form:
		amount=request.form['at']
		q="insert into payment values(null,'%s','%s',CURDATE())" %(bid,amount)
		insert(q)
		q="update booking set booking_status='Paid' where booking_id='%s'"%(bid)
		update(q)
		return redirect(url_for('customer.customervieweventbooking'))
	return render_template('customermakepayment.html',data=data)

@customer.route('/customer_view_send_proposal')
def customer_view_send_proposal():

	ceid=request.args['ceid']
	data={}
	q="select * from proposal where custom_event_id='%s'"%(ceid)
	res=select(q)
	data['proposal']=res
	return render_template('customer_view_send_proposal.html',data=data)	

@customer.route('/customer_custom_event_payments',methods=['get','post'])	
def customer_custom_event_payments():
	ceventid=request.args['ceventid']
	bamount=request.args['bamount']
	if 'submit' in request.form:
		q="update proposal set proposal_status='Paid' where custom_event_id='%s'"%(ceventid)
		update(q)
		q="update customevent set custom_event_status='Paid' where custom_event_id='%s'"%(ceventid)
		update(q)
		return redirect(url_for('customer.customer_view_send_proposal'))

	return render_template('customer_custom_event_payments.html',bamount=bamount)


@customer.route('/customer_view_bill',methods=['get','post'])	
def customer_view_bill():

	bid=request.args['bid']

	
	data={}

	q="select * from booking inner join eventpackages on(booking.event_id=eventpackages.`package_id`) inner join packagedetails using(package_id) inner join features using(feature_id) where booking_id='%s'"%(bid)
	print(q)
	res=select(q)
	print(res)
	data['pdetails']=res
	
	return render_template('customer_view_bill.html',data=data)
