from django.db import models

# Create your models here.

class Member(models.Model):
    GENDER=(

        
        ('Male','Male'),
        ('Female','Female'),
    )
    name=models.CharField(max_length=200)
    gender=models.CharField(max_length=300,choices=GENDER)
    phone=models.CharField(max_length=300)
    date_joined=models.DateField()
    next_of_kin=models.CharField(max_length=200,null=True)
    next_of_kin_Phone=models.CharField(max_length=300,null=True)

   

    def __str__(self):
        return self.name

class Loan(models.Model):
    STATUS=(
        ('New','New'),
        ('Approved','Approved'),
        ('Pending','Pending'),

    )
    member=models.ForeignKey(Member,on_delete=models.CASCADE)
    date_applied=models.DateField()
    amount=models.PositiveIntegerField()
    status=models.CharField(max_length=300,choices=STATUS)

    def __str__(self):
        return self.status



