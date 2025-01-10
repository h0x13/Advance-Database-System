from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
from datetime import datetime

# Create your models here.
# ADMIN ACCOUNT MODEL
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


def img_path(instance, filename):
    ext = filename.split(".")[-1]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{timestamp}.{ext}"


# COFFEE MODEL
class Coffee(models.Model): # This is the model for the coffee
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to=img_path, default="default.jpg", blank=True,)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Coffee"
        verbose_name_plural = "Coffees"




# ORDER MODEL
class Order(models.Model): # This is the model for the orders
    # STATUS_CHOICES = [
    #     ('Pending', 'Pending'),
    #     ('Delivered', 'Delivered'),
    # ]
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE, related_name="coffees")
    user = models.ForeignKey('z_user.User_Account', on_delete=models.CASCADE)  # Connect to user account
    quantity = models.IntegerField(default=0)
    order_at = models.DateTimeField(auto_now_add=True)
    # status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ['-order_at']


# Admin Logs
class AdminLogs(models.Model):
    admin = models.ForeignKey(Admin_Account, on_delete=models.CASCADE)
    action = models.CharField(max_length=50, default='default')
    log_time = models.DateTimeField(auto_now_add=True)


# UNFINISH
