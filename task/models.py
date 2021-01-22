from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

#user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class Activity(models.Model):
    
    activity_name = models.CharField(max_length=30, help_text='Posição Operacional')

    def __str__(self):
        return self.activity_name


class AppUser(models.Model):
    
    name = models.CharField(max_length=100, help_text='Nome do Usuário')
    activity = models.ForeignKey(Activity, on_delete=models.PROTECT, null=True, blank=True)
    photo = models.FileField(upload_to='uploads/photos/', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    created_au = models.DateTimeField(auto_now_add=True)
    update_au = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Status(models.Model):

    status_name = models.CharField(max_length=30)

    def __str__(self):
        return self.status_name


class Task(models.Model):

    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    doc = models.CharField(max_length=255)
    rev = models.CharField(max_length=3)
    comment = models.TextField()
    elab = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='elab')
    verif = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='verif') #models.CharField(max_length=255)
    #status_date = models.DateTimeField(upload_to='uploads/%Y/%m/%d/')
    #user = models.OneToOneField(User, on_delete=models.PROTECT)
    created_tk = models.DateTimeField(auto_now_add=True)
    update_tk = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.doc

