from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20,
        choices=[
            ("admin", "Administrator"),
            ("supplier", "Supply Manager"),
            ("storekeeper", "Storekeeper"),
            ("customer", "Usually teacher"),
        ],
        default="customer",
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    user_class = models.CharField(
        max_length=20,
        choices=[
            ("EYPYP", "EYPYP"),
            ("PYP", "PYP"),
            ("MYP", "MYP"),
            ("DP", "DP"),
        ],
        null=True,
        blank=True,
        default=None
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f"{self.email} - {self.role}"


class OrderTable(models.Model):
    name = models.CharField(max_length=50, null=False)
    image_url = models.URLField()
    quantity = models.PositiveIntegerField(default=1)
    measurement = models.CharField(max_length=25)
    delivered_quantity = models.PositiveIntegerField(default=None)
    teachers_comments = models.TextField(null=True)
    price = models.PositiveIntegerField(default=None)
    teacher_recieved = models.PositiveIntegerField(default=None)
    st_comments = models.TextField(null=True)
    sm_comments = models.TextField(null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    date_of_reciept = models.DateTimeField(blank=True, null=True)
    STATUS = [
        ("Pending", "Pending order"),
        ("Partially In Stock", "Order is done and partially in Stock"),
        ("Fully recieved", "Order is fully recieved to teacher"),
    ]
    status = models.CharField(max_length=25, choices=STATUS, default=STATUS[0][0])
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
