from django.db import models

FA12 = 'FA12'
FA2 = 'FA2'

TOKEN_TYPE_CHOICES = (
    (FA12, 'FA12'),
    (FA2, 'FA2'),
)


class Token(models.Model):
    user = models.CharField(
        max_length=36,
    )
    token = models.CharField(
        max_length=36,
    )
    type = models.CharField(
        max_length=4,
        choices=TOKEN_TYPE_CHOICES,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )


class YF(models.Model):
    user = models.CharField(
        max_length=36,
    )
    yf = models.CharField(
        max_length=36,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
