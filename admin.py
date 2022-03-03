from flask import *
from database import *
 
admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
	return render_template('adminhome.html')

@admin.route('/adminmanageeventcategories',methods=['get','post'])
def adminmanageeventcategories():
	data={}
	q="select * from eventcategories"
	res=select(q)
	data['eventcategories']=res




	if 'submit' in request.form:
		cname=request.form['cn']
		q="insert into eventcategories values(null,'%s')" %(cname)
		insert(q)
		return redirect(url_for('admin.adminmanageeventcategories'))
	
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None
			
	if action=="delete":
		q="delete from eventcategories where category_id='%s'" %(id)
		delete(q)
		return redirect(url_for('admin.adminmanageeventcategories'))

	if action=="update":
		q="select * from eventcategories where category_id='%s'" %(id)
		res=select(q)
		data['cat']=res
		if 'update' in request.form:
			categoryname=request.form['cn']
			print(categoryname)
			q="update eventcategories set category_name='%s' where category_id='%s'" %(categoryname,id)
			update(q)			
			return redirect(url_for('admin.adminmanageeventcategories'))
	return render_template('adminmanageeventcategories.html',data=data) 

@admin.route('/adminmanageeventspackages',methods=['get','post'])
def adminmanageeventspackages():
	data={}
	q="select * from eventpackages"
	res=select(q)
	data['eventpackages']=res

	if "submit" in request.form:
		packagetitle=request.form['pt']
		packagedescription=request.form['pd']
		q="insert into eventpackages values(null,'%s',0,'%s','pending')" %(packagetitle,packagedescription)
		insert(q)
		return redirect(url_for('admin.adminmanageeventspackages'))	

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None

	if action=="delete":
		q="delete from eventpackages where package_id='%s'" %(id)
		delete(q)
		return redirect(url_for('admin.adminmanageeventspackages'))

	if action=="update":
		q="select * from eventpackages where package_id='%s'" %(id)
		res=select(q)
		data['pak']=res

	if action=="available":
		q="update eventpackages set status='available' where package_id='%s'" %(id)
		print(q)
		update(q)
		return redirect(url_for('admin.adminmanageeventspackages'))		

	if 'update' in request.form:
		packagetitle=request.form['pt']
	
		packagedescription=request.form['pd']
		q="update eventpackages set package_title='%s',package_description='%s' where package_id='%s'" %(packagetitle,packagedescription,id)
		print(q)
		update(q)	

		return redirect(url_for('admin.adminmanageeventspackages'))	
	return render_template('adminmanageeventspackages.html',data=data) 

@admin.route('/adminaddfeatures',methods=['get','post'])
def adminaddfeatures():
	data={}
	q="select * from features"
	res=select(q)
	data['features']=res

	if "submit" in request.form:
		featuretitle=request.form['ft']
		featuredescription=request.form['fd']
		q="insert into features values(null,'%s','%s')" %(featuretitle,featuredescription)
		insert(q)
		return redirect(url_for('admin.adminaddfeatures'))

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None

	if action=="delete":
		q="delete from features where feature_id='%s'" %(id)
		delete(q)
		return redirect(url_for('admin.adminaddfeatures'))

	if action=="update":
		q="select * from features where feature_id='%s'" %(id)	
		res=select(q)
		data['feat']=res
	if 'update' in request.form:
		featuretitle=request.form['ft']	
		featuredescription=request.form['fd'] 
		q="update features set feature_title='%s',feature_description='%s' where   feature_id='%s'" %(featuretitle,featuredescription,id)   	
		update(q)
		return redirect(url_for('admin.adminaddfeatures'))
	return render_template("adminaddfeatures.html",data=data) 		

@admin.route('/adminviewcustomevents')	
def adminviewcustomevents():
	data={}
	q="select * from customevent"
	res=select(q)
	data['customevent']=res
	print(res)
	return render_template('adminviewcustomevents.html',data=data)

@admin.route('/adminviewpayments')	
def adminviewpayments():
	data={}
	q="select * from payment"
	res=select(q)
	data['payment']=res
	return render_template('adminviewpayments.html',data=data)

@admin.route('/adminviewfeedback')
def adminviewfeedback():
	data={}
	q="select * from feedback"
	res=select(q)
	data['feedback']=res
	return render_template('adminviewfeedback.html',data=data)

@admin.route('/adminviewcomplaints',methods=['get','post'])
def adminviewcomplaints():
	data={}

	q="select * from complaints"
	res=select(q)
	data['complaints']=res

	j=0
	for i in range(1,len(res)+1):
		if 'replys'+str(i) in request.form:
			reply=request.form['reply'+str(i)]
			print(res[j]['complaint_id'])
			q="update complaints set reply='%s' where complaint_id='%s'"%(reply,res[j]['complaint_id'])
			print(q)
			update(q)
			return redirect(url_for('admin.adminviewcomplaints'))
		j=j+1


	
	return render_template('adminviewcomplaints.html',data=data)	

@admin.route('/admin_view_event_package_booking')	
def admin_view_event_package_booking():
		data={}
		q="select * from booking"
		res=select(q)
		data['booking']=res
		if 'action' in request.args:
			action=request.args['action']
			bid=request.args['bid']
		else:
			action=None
		if action=='accept':
			q="update booking set booking_status='accept' where booking_id='%s'"%(bid)
			update(q)
			return redirect(url_for('admin.admin_view_event_package_booking'))
		if action=='reject':
			q="update booking set booking_status='reject' where booking_id='%s'"%(bid)
			update(q)
			return redirect(url_for('admin.admin_view_event_package_booking'))
		return render_template('admin_view_event_package_booking.html',data=data)	

@admin.route('/admin_manage_package_details',methods=['get','post'])	
def admin_manage_package_details():
	pid=request.args['pid']

	data={}
	data['pid']=pid
	q="select * from features"
	res=select(q)
	data['feature']=res
	q="select * from  eventpackages inner join packagedetails using(package_id) inner join features using(feature_id) where package_id='%s'"%(pid)
	res=select(q)
	if res:
		data['pdetails']=res
		print(res)
	if 'package' in request.form:
		feature=request.form['feature']
		amt=request.form['amt']
		q="select * from packagedetails where package_id='%s'"%(pid)
		res=select(q)
		if res:
			q="select * from packagedetails where package_id='%s' and feature_id='%s'"%(pid,feature)
			res=select(q)
			if res:
				package_details_id=res[0]['package_details_id']
				preamt=res[0]['amt']
				q="update packagedetails set amt='%s' where  package_details_id='%s'"%(amt,package_details_id)
				update(q)
				q="update eventpackages set package_amount=package_amount+'%s'-'%s' where package_id='%s'"%(amt,preamt,pid)
				update(q)
				return redirect(url_for('admin.admin_manage_package_details',pid=pid))
			else:
				q="insert into packagedetails values(null,'%s','%s','%s')"%(pid,feature,amt)
				insert(q)
				q="update eventpackages set package_amount=package_amount+'%s' where package_id='%s'"%(amt,pid)
				update(q)
				return redirect(url_for('admin.admin_manage_package_details',pid=pid))

		else:
			q="insert into packagedetails values(null,'%s','%s','%s')"%(pid,feature,amt)
			insert(q)
			q="update eventpackages set package_amount=package_amount+'%s' where package_id='%s'"%(amt,pid)
			update(q)
			return redirect(url_for('admin.admin_manage_package_details',pid=pid))
	if 'action' in request.args:
		package_details_id=request.args['package_details_id']
		q="select * from packagedetails where package_details_id='%s'"%(package_details_id)
		res=select(q)	
		preamt=res[0]['amt']
		q="update eventpackages set package_amount=package_amount-'%s' where package_id='%s'"%(preamt,pid)
		update(q)
		q="delete from packagedetails where package_details_id='%s'"%(package_details_id)
		delete(q)
		return redirect(url_for('admin.admin_manage_package_details',pid=pid))

	return render_template('admin_manage_package_details.html',data=data)



@admin.route('/admin_view_packdetails',methods=['get','post'])	
def admin_view_packdetails():
	pid=request.args['pid']

	data={}
	data['pid']=pid
	q="select * from features"
	res=select(q)
	data['feature']=res
	q="select * from  eventpackages inner join packagedetails using(package_id) inner join features using(feature_id) where package_id='%s'"%(pid)
	res=select(q)
	data['pdetails']=res
	print(res)
	
	return render_template('admin_view_packdetails.html',data=data)

@admin.route('/admin_send_proposal',methods=['get','post'])
def admin_send_proposal():
	ceventid=request.args['ceventid']
	data={}

	if 'submit' in request.form:
		proposalamount=request.form['pa']
		q="insert into proposal values(null,'%s',CURDATE(),'%s','pending')" %(ceventid,proposalamount)
		insert(q)
	return render_template('admin_send_proposal.html',data=data)