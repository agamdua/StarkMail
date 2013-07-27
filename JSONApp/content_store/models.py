from django.db import models


class StudentUID(models.Model):
    GENDER_CHOICES = (('F', 'FEMALE'),
                      ('M', 'MALE'))
    user_id = models.TextField(primary_key=True)  # unix time-stamp
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    date_of_birth = models.DateTimeField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    profile_picture = models.FileField(upload_to="Student Profile Pictures")
    email_id = models.EmailField(unique=True)

    def __unicode__(self):
        return u"%s %s  %s" % (self.first_name, self.middle_name, self.last_name)


class Login(models.Model):
    u_id = models.ForeignKey(StudentUID)
    hashed_pass = models.TextField()


class CourseID(models.Model):
    course_id = models.TextField(primary_key=True)
    course_name = models.CharField(max_length=100)

    def __unicode__(self):
        return u"%s" % self.course_name


class SubjectID(models.Model):
    subject_id = models.TextField(primary_key=True)
    c_id = models.ForeignKey(CourseID)
    subject_name = models.CharField(max_length=100)

    def __unicode__(self):
        return u"%s" % self.subject_name


class TopicID(models.Model):
    topic_id = models.TextField(primary_key=True)
    c_id = models.ForeignKey(CourseID)
    s_id = models.ForeignKey(SubjectID)
    topic_name = models.CharField(max_length=100)
    topic_description = models.CharField(max_length=1000)

    def __unicode__(self):
        return u"%s" % self.topic_name


class SubtopicID(models.Model):
    subtopic_id = models.TextField(primary_key=True)
    c_id = models.ForeignKey(CourseID)
    s_id = models.ForeignKey(SubjectID)
    t_id = models.ForeignKey(TopicID)
    subtopic_name = models.CharField(max_length=200)

    def __unicode__(self):
        return u"%s" % self.subtopic_name


class Content(models.Model):
    sb_id = models.ForeignKey(SubjectID)
    difficulty_level = models.CharField(primary_key=True)
    introduction = models.TextField()
    concept = models.TextField()
    reinforcement = models.TextField()
    summary = models.TextField()


class Examples(models.Model):
    sb_id = models.ForeignKey(SubjectID)
    diff_level = models.ForeignKey(Content)
    example = models.TextField()

    def __unicode__(self):
        return u"%s" % self.example


class QuestionID(models.Model):
    LEVEL_CHOICES = (('E', 'EASY'),
                     ('M', 'MEDIUM'),
                     ('H', 'HARD'),
                     ('A', 'ADVANCE'))

    question_id = models.TextField(primary_key=True)
    sb_id = models.ForeignKey(SubjectID)
    level = models.CharField(choices=LEVEL_CHOICES)
    clone_number = models.CharField(max_length=20)
    actual_question = models.TextField()
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()
    correct_answer = models.CharField(max_length=20)


class StudentAnalyticsID(models.Model):
    student_analytics_p_id = models.TextField(primary_key=True)
    student_u_id = models.ForeignKey(StudentUID)
    student_subtopic_id = models.ForeignKey(Content)
    s_diff_level = models.CharField(max_length=10)
    s_clone_no = models.IntegerField()
    s_time_stamp = models.DateTimeField(auto_now_add=True)
    s_current_correct = models.IntegerField()
    s_content_backtrack = models.IntegerField()


class StudentAnswer(models.Model):
    student_answer_p_id = models.ForeignKey(StudentAnalyticsID)
    question_number = models.IntegerField()
    s_selected_option = models.TextField()
    s_correct_answer = models.ForeignKey(QuestionID)


class CloneTime(models.Model):
    clone_p_id = models.ForeignKey(StudentAnalyticsID)
    clone_time = models.DateTimeField()


class HitTable(models.Model):
    h_u_id = models.ForeignKey(StudentUID)
    h_subtopic_id = models.ForeignKey(SubtopicID)
    h_level = models.CharField(max_length=10)
    hits = models.IntegerField()


class FallbackPushup(models.Model):
    fp_uid = models.ForeignKey(StudentUID)
    fp_subtopic_id = models.ForeignKey(SubtopicID)
    fallbacks = models.IntegerField()
    pushups = models.IntegerField()
    time_on_content = models.DateTimeField()
    total_time = models.DateTimeField()


class TeacherUID(models.Model):
    teacher_uid = models.TextField()
    teacher_name = models.TextField()

