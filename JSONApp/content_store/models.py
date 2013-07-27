from django.db import models
#from django.conf import settings
#from django.contrib.auth.models import AbstractUser

class Student(models.Model):
    GENDER_CHOICES = (
        ('F', 'FEMALE'),
        ('M', 'MALE'),
    )

    UID = models.IntegerField(
        primary_key=True)  # should be a combination of Publisher ID + Course ID + student rollno as padding with generic size.
    FirstName = models.CharField(max_length=30)
    MiddleName = models.CharField(max_length=30, blank=True)
    LastName = models.CharField(max_length=30)
    Date_Of_Birth = models.DateField(auto_now_add=True)
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Profile_Pic = models.FileField(upload_to='Student_profile_pictures', blank=True)
    EmailID = models.EmailField(max_length=255, unique=True)

    def __unicode__(self):
        return u"%s %s  %s" % (self.FirstName, self.MiddleName, self.LastName)


class Login(models.Model):
    student_id = models.ForeignKey(Student)
    Hashed_Pass = models.TextField(unique=True)


class CourseList(models.Model):
    CourseID = models.IntegerField(primary_key=True) # must be assigned using mapping Refrence table of course
    CourseName = models.CharField(max_length=100)

    def __unicode__(self):
        return u"%s" % (self.CourseName)


class SubjectList(models.Model):
    Course = models.ForeignKey(CourseList)
    SubjectID = models.IntegerField(primary_key=True) # Will be assigned using mapping refrence table
    SubjectName = models.CharField(max_length=100)

    def __unicode__(self):
        return u"%s" % (self.SubjectName)


class TopicList(models.Model):
    Course = models.ForeignKey(CourseList)
    Subject = models.ForeignKey(SubjectList)
    TopicID = models.IntegerField(primary_key=True)
    TopicName = models.CharField(max_length=100)
    Description = models.TextField()

    def __unicode__(self):
        return u"%s" % (self.TopicName)


class SubtopicList(models.Model):
    Course = models.ForeignKey(CourseList)
    Subject = models.ForeignKey(SubjectList)
    Topic = models.ForeignKey(TopicList)
    SubtopicID = models.IntegerField(primary_key=True)
    SubtopicName = models.CharField(max_length=100)

    def __unicode__(self):
        return u"%s" % (self.SubtopicName)


class Content(models.Model):
    DIFFICULTY_CHOICES = (
        ('E', 'EASY'),
        ('M', 'MEDIUM'),
        ('H', 'HARD'),
        ('A', 'ADVANCED'),

    )

    Subtopic = models.ForeignKey(SubtopicList)
    DifficultyLevel = models.CharField(max_length=1, choices=DIFFICULTY_CHOICES)
    Introduction = models.TextField()
    Concept = models.TextField()
    Reinforcement = models.TextField()
    Summary = models.TextField()

    def __unicode__(self):
        return u"%s" % (self.DifficultyLevel)


class Example(models.Model):
    Content = models.ForeignKey(Content)  # Here Content table is referenced using Primary Key id of content table.
    Example = models.TextField()


class Question(models.Model):
    LEVEL_CHOICES = (
        ('E', 'EASY'),
        ('M', 'MEDIUM'),
        ('H', 'HARD'),
        ('A', 'ADVANCED'),

    )

    OPTION_CHOICES = (
        ('A', 'Option1'),
        ('B', 'Option2'),
        ('C', 'Option3'),
        ('D', 'Option4'),
    )

    QuestionID = models.AutoField(primary_key=True)
    Subtopic = models.ForeignKey(SubtopicList)
    Level = models.CharField(max_length=1, choices=LEVEL_CHOICES)
    CloneNumber = models.IntegerField()
    ActualQuestion = models.TextField()
    Option1 = models.TextField()
    Option2 = models.TextField()
    Option3 = models.TextField()
    Option4 = models.TextField()
    CorrectAnswer = models.CharField(max_length=1, choices=OPTION_CHOICES)

    def __unicode__(self):
        return self.QuestionID


class StudentAnalytics(models.Model):
    LEVEL_CHOICES = (
        ('E', 'EASY'),
        ('M', 'MEDIUM'),
        ('H', 'HARD'),
        ('A', 'ADVANCED'),

    )

    ProgressID = models.AutoField(primary_key=True)
    UID = models.ForeignKey(Student)
    SubtopicID = models.ForeignKey(SubtopicList)
    Level = models.CharField(max_length=1, choices=LEVEL_CHOICES)
    CloneNumber = models.IntegerField()
    TimeStamp = models.DateTimeField()
    CurrentCorrect = models.IntegerField()
    ContentBacktrack = models.IntegerField()

    def __unicode__(self):
        return self.ProgressID


class StudentAnswer(models.Model):
    ProgressID = models.ForeignKey(StudentAnalytics)
    #	Question = models.ForeignKey(Question)
    SelectedOption = models.CharField(max_length=1)
    CorrectAnswer = models.ForeignKey(Question)

    def __unicode__(self):
        return self.ProgressID


class CloneTime(models.Model):
    ProgressID = models.ForeignKey(StudentAnalytics)
    CloneTime = models.TimeField()

    def __unicode__(self):
        return self.ProgressID


class Hit_table(models.Model):
    UID = models.ForeignKey(Student)
    subtopic = models.ForeignKey(SubtopicList)
    level = models.CharField(max_length=1)
    hits = models.IntegerField()


class FallbackPushup(models.Model):
    UID = models.ForeignKey(Student)
    SubtopicID = models.ForeignKey(SubtopicList)
    Fallbacks = models.IntegerField()
    Pushups = models.IntegerField()
    TimeOnContent = models.TimeField()
    TotalTime = models.TimeField()

    def __unicode__(self):
        return u"Fallbacks %s and Pushups %s" % (self.Fallbacks, self.Pushups)
