from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver


# Create your models here.
class User_Account(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "User Account"
        verbose_name_plural = "User Accounts"

@receiver(post_save, sender=User_Account)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        User.objects.create_user(
            username=instance.username,
            email=instance.email,
            password=instance.password,
        )
    
@receiver(pre_delete, sender=User_Account)
def delete_user_account(sender, instance, **kwargs):
    try:
        user = User.objects.get(username=instance.username)
        user.delete()
    except User.DoesNotExist:
        pass