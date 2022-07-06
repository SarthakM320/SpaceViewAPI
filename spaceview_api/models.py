from django.db import models

# Create your models here.

class User(models.Model):
    class Sex(models.TextChoices):
        male = '1','male'
        female = '2','female'
        unknown = '3', 'Prefer not to say'
    class Employment_status(models.TextChoices):
        employer = '1', 'Employer'
        employee = '2', 'Employee'
        self_employed = '3', 'Self Employed'
        unemployed = '4', 'Unemployed'
        student = '5', 'Student'
    class Marital_status(models.TextChoices):
        married = '1', 'Married'
        unmarried = '2', 'Unmarried'

    class Decision_status(models.TextChoices):
        liberal = '1', 'Liberal'
        socialist = '2', 'Socialist'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField(null=False)
    sex = models.CharField(max_length=9,choices=Sex.choices, default=Sex.male)
    employment_status = models.CharField(max_length=9, choices=Employment_status.choices, default=Employment_status.student)
    marital_status = models.CharField(max_length=9, choices=Marital_status.choices, default=Marital_status.unmarried)
    decision_status = models.CharField(max_length=9, choices=Decision_status.choices, default=Decision_status.socialist)
    

class Question(models.Model):
    question = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

class Options(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank = True)
    user = models.ManyToManyField(User,blank=True)
    choice_text = models.CharField(max_length=50)
    selected = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text

    # class Meta:
    #     unique_together = ["id", "user"]







