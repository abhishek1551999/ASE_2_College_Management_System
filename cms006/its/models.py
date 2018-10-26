from __future__ import unicode_literals
from django.db import models


class role(models.Model):
	role_id = models.AutoField(primary_key=True,default='1')
	role_name = models.CharField(max_length=50)

class student(models.Model):
	s_id = models.AutoField(primary_key=True,default='1')
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	sroll_no = models.CharField(max_length=30)
	dob = models.DateField()
	gender = models.CharField(max_length=20)
	mobile = models.CharField(max_length=50)
	spswd = models.CharField(max_length=50)
	email = models.EmailField(max_length=70)
	role_id = models.ForeignKey(role,on_delete=models.CASCADE)
	sem_id = models.IntegerField()
	cur_yos = models.IntegerField()
	reg_year = models.IntegerField()
	
class logged(models.Model):
	sid = models.IntegerField()
	
class faculty(models.Model):
	f_id = models.AutoField(primary_key=True,default='1')
	fac_name = models.CharField(max_length=100)
	froll_no = models.CharField(max_length=30,null=True)
	ph_no = models.CharField(max_length=100)
	course_off = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	role_id = models.ForeignKey(role,on_delete=models.CASCADE)
	fpswd = models.CharField(max_length=50)

class logged2(models.Model):
	fid = models.IntegerField()

class adm(models.Model):
	a_id = models.AutoField(primary_key=True,default='1')
	ad_name = models.CharField(max_length=100)
	aroll_no = models.CharField(max_length=30)
	role_id = models.ForeignKey(role,on_delete=models.CASCADE)
	apswd = models.CharField(max_length=50)


class logged3(models.Model):
	aid = models.IntegerField()

class course(models.Model):
	c_id = models.AutoField(primary_key=True,default='1')
	course_name = models.CharField(max_length=100)
	f_id = models.ForeignKey(faculty,on_delete=models.CASCADE,null=True)
class timetable(models.Model):
	day_id = models.IntegerField()
	timeslots = models.CharField(max_length=30)
	c_id = models.ForeignKey(course,on_delete=models.CASCADE)
	
class Grade(models.Model):
	s_id = models.ForeignKey(student,on_delete=models.CASCADE)
	c_id = models.ForeignKey(course,on_delete=models.CASCADE)
	grades = models.CharField(max_length=30)

class Attendance(models.Model):
	date = models.DateField()
	s_id = models.ForeignKey(student,on_delete=models.CASCADE)
	c_id = models.ForeignKey(course,on_delete=models.CASCADE)
	mark = models.BooleanField(default=False)
	
class Leave(models.Model):
	s_id = models.ForeignKey(student,on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	leave_roll_no = models.CharField(max_length=100)
	reason = models.CharField(max_length=100)
	leave_from = models.DateField()
	leave_to = models.DateField()
	no_ofdays = models.IntegerField()
	email = models.EmailField(max_length=70,null=True,blank=True)
class Query(models.Model):
	query = models.CharField(max_length=100)
	s_id = models.ForeignKey(student,on_delete=models.CASCADE)
	a_id = models.ForeignKey(adm,on_delete=models.CASCADE,null=True)
	def __str__(self):
		return self.query
class Answerqueryadmin(models.Model):
	query = models.CharField(max_length=100)
	s_id = models.ForeignKey(student,on_delete=models.CASCADE)
	a_id = models.ForeignKey(adm,on_delete=models.CASCADE,null=True)
class Events(models.Model):
	event_id = models.AutoField(primary_key=True,default='1')
	event_name = models.CharField(max_length=30)
	description = models.CharField(max_length=30)
	schedule = models.CharField(max_length=30)


