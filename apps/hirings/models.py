from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Hiring(models.Model):
    candidate = models.ForeignKey(
        UserModel, related_name="hirings", on_delete=models.CASCADE
    )
    about_candidate = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
