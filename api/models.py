from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()
    
    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)
    credit = models.IntegerField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    experience_years = models.IntegerField()

    def __str__(self):
        return self.name