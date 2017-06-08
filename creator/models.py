from django.contrib.auth.models import User
from django.db import models


class Form(models.Model):
    user = models.ForeignKey(User, default=1)
    form_name = models.CharField(max_length=100, default="New Form")
    header_text = models.CharField(max_length=100)
    body_text = models.CharField(max_length=1000)
    deployed = models.BooleanField(default=False)

    def __str__(self):
        return self.form_name


class TextField(models.Model):
    sr_no = models.PositiveSmallIntegerField(default=0)
    caption = models.CharField(max_length=100)
    question = models.CharField(max_length=1000)
    required = models.BooleanField(default=False)
    parent_form = models.ForeignKey(Form, on_delete=models.CASCADE, default=1)

    def __str__(self):
        self.caption


class NumericField(models.Model):
    sr_no = models.PositiveSmallIntegerField(default=0)
    caption = models.CharField(max_length=100)
    question = models.CharField(max_length=1000)
    required = models.BooleanField(default=False)
    parent_form = models.ForeignKey(Form, on_delete=models.CASCADE, default=1)
    range_high = models.SmallIntegerField(default=0)
    range_low = models.SmallIntegerField(default=-100)
    decimal_places = models.SmallIntegerField(default=5)

    def __str__(self):
        return self.caption