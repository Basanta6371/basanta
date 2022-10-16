from django.db import models

class Students(models.Model):
   sname = models.CharField(max_length=20)
   email = models.EmailField(max_length=20)
   loc = models.CharField(max_length=20)
   def __str__(self):
      return self.sname

   
class Course(models.Model):
   abcd = models.OneToOneField(Students,on_delete = models.CASCADE)
   cname = models.CharField(max_length=20)
   fee = models.IntegerField()
   iname = models.CharField(max_length=20)
