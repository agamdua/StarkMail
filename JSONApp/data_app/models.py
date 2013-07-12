from django.db import models


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






