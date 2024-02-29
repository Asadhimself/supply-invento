from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20,
        choices=[
            ("Admin", "Administrator"),
            ("Supplier", "Supply Manager"),
            ("Storekeeper", "Storekeeper"),
            ("Teacher", "Teacher"),
        ],
        default="Teacher",
    )
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
        default=None,
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email} - {self.role}"
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class OrderTable(models.Model):
    name = models.CharField(max_length=50, null=False)
    image_url = models.URLField()
    quantity = models.PositiveIntegerField(default=1)
    measurement = models.CharField(max_length=25)
    delivered_quantity = models.PositiveIntegerField(default=None, blank=True, null=True)
    teachers_comments = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField(default=None, blank=True, null=True)
    teacher_recieved = models.PositiveIntegerField(default=None, blank=True, null=True)
    st_comments = models.TextField(null=True, blank=True)
    sm_comments = models.TextField(null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    date_of_reciept = models.DateTimeField(blank=True, null=True)
    STATUS = [
        ("Pending", "Pending order"),
        ("Partially In Stock", "Order is partially in Stock"),
        ("Fully recieved", "Order is fully recieved to teacher"),
    ]
    status = models.CharField(max_length=25, choices=STATUS, default=STATUS[0][0])
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
