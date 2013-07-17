from django.db import models

class StudentUID(models.Model):
	user_id=models.CharField(max_length=20, primary_key=True)
	last_name=models.CharField(max_length=100)
	middle_name=models.CharField(max_length=100)
	first_name=models.CharField(max_length=100)
	#date_of_birth=
	gender=models.CharField(max_length=20)
	#profile_picture=models.
	email_id=models.EmailField(max_length=100)

class Login(models.Model):
	u_id=models.ForeignKey(StudentUID)
	#hashed_pass=models.

class CourseID(models.Model):
	course_id=models.CharField(max_length=20, primary_key=True)
	course_name=models.CharField(max_length=100)

class SubjectID(models.Model):
	subject_id=models.CharField(max_length=20, primary_key=True)
	c_id=models.ForeignKey(CourseID)
	subject_name=models.CharField(max_length=100)

class TopicID(models.Model):
	topic_id=models.CharField(max_length=20, primary_key=True)
	c_id=models.ForeignKey(CourseID)
	s_id=models.ForeignKey(SubjectID)
	topic_name=models.CharField(max_length=100)
	topic_description=models.CharField(max_length=1000)

class SubtopicID(models.Model):
	subtopic_id=models.CharField(max_length=20, primary_key=True)
	c_id=models.ForeignKey(CourseID)
	s_id=models.ForeignKey(SubjectID)
	t_id=models.ForeignKey(TopicID)
	subtopic_name=models.CharField(max_length=200)

class Content(models.Model):
	sb_id=models.ForeignKey(SubjectID)
	difficulty_level=models.CharField(max_length=20, primary_key=True)
	introduction=models.TextField()
	concept=models.TextField() 
	reinforcement=models.TextField()
	summary=models.TextField()

class Examples(models.Model):
	sb_id=models.ForeignKey(SubjectID)
	diff_level=models.ForeignKey(Content)
	example=models.TextField()

class QuestionID(models.Model):
	question_id=models.CharField(max_length=20, primary_key=True)
	sb_id=models.ForeignKey(SubjectID)
	level=models.CharField(max_length=100)
	clone_number=models.CharField(max_length=20)
	actual_question=models.TextField()
	option1=models.TextField()
	option2=models.TextField()
	option3=models.TextField()
	option4=models.TextField()
	correct_answer=models.CharField(max_length=20)






