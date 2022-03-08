from django.db import models

# Create your models here.

class Weight:

    user = models.ForeignKey("users.User", verbose_name="user", on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5)
    created_at = models.DateField(auto_now_add=True)


class Height:

    user = models.ForeignKey("users.User", verbose_name="user", on_delete=models.CASCADE)
    height = models.DecimalField(max_digits=5)
    created_at = models.DateField(auto_now_add=True)
