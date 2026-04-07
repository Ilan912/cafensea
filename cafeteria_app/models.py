from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit = models.FloatField(default=0)
    credit_depense = models.FloatField(default=0)
    boursier = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    available = models.BooleanField(default=True)
    stock = models.IntegerField()
    offre = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_student_profile(sender, instance, **kwargs):
    if hasattr(instance, 'student'):
        instance.student.save()

    def __str__(self):
        return f"{self.student} - {self.product}"