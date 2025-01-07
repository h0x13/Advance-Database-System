from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver

# Create your models here.
class Admin_Account(models.Model): # This is the model for the admin login

    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Admin Account"
        verbose_name_plural = "Admin Accounts"

@receiver(post_save, sender=Admin_Account)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        User.objects.create_user(
            username=instance.username,
            password=instance.password,
        )


@receiver(pre_delete, sender=Admin_Account)
def delete_user_account(sender, instance, **kwargs):
    try:
        user = User.objects.get(username=instance.username)
        user.delete()
    except User.DoesNotExist:
        pass


# class Audit_Trail(models.Model):
#     account = models.ForeignKey(Admin_Account, on_delete=models.CASCADE)
#     login_timw = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.username

#     class Meta:
#         verbose_name = "Audit Trail"
#         verbose_name_plural = "Audit Trails"


class Coffee(models.Model): # This is the model for the coffee
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Coffee"
        verbose_name_plural = "Coffees"