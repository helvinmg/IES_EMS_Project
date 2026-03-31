from django.db import models

#This will create a table in db with name employee
class Employee(models.Model):
    name=models.CharField(max_length=30)
    desg=models.CharField(max_length=50)
    salary=models.FloatField(default=25000)

    def __str__(self):#string representation of the object
        return self.name+" - "+self.desg
#Create a Model named Manager with following fields
#-Name,TeamName,Salary,ReporteeCount
class Manager(models.Model):
    name=models.CharField(max_length=30)
    teamname=models.CharField(max_length=50)
    salary=models.FloatField()
    reporteecount=models.IntegerField(default=0)

    def __str__(self):
        return self.name+" - "+self.teamname