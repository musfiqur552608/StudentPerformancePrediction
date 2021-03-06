from django.db import models

# Create your models here.
class StudentPerformance(models.Model):
    student_id = models.IntegerField()
    sex = models.IntegerField()
    age = models.IntegerField()
    address = models.IntegerField()
    famsize = models.IntegerField()
    Pstatus = models.IntegerField()
    Medu = models.IntegerField()
    Fedu = models.IntegerField()
    Mjob = models.IntegerField()
    Fjob = models.IntegerField()
    reason = models.IntegerField()
    guardian = models.IntegerField()
    traveltime = models.IntegerField()
    studytime = models.IntegerField()
    failures = models.IntegerField()
    schoolsup = models.IntegerField()
    famsup = models.IntegerField()
    paid = models.IntegerField()
    activities = models.IntegerField()
    nursery = models.IntegerField()
    higher = models.IntegerField()
    internet = models.IntegerField()
    famrel = models.IntegerField()
    freetime = models.IntegerField()
    health = models.IntegerField()
    absences = models.IntegerField()
    quiz = models.IntegerField()
    assignment = models.IntegerField()
    exam1 = models.IntegerField()
    exam2 = models.IntegerField()
    
    def __str__(self):
        return str(self.student_id)