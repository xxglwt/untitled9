from django.db import models

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=500)
    pub_date=models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    vote=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
def user_directory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id,filename)

class MyModel(models.Model):
    upload=models.FileField(upload_to=user_directory_path)
