from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    DEGREES = {
        "Basic Sciences": "Basic Sciences",
        "Physiopathology": "Physiopathology",
        "Medical Extern": "Medical Extern",
        "Medical Intern": "Medical Intern",
        "General Practicioner": "General Practicioner",
        "Medical Resident": "Medical Resident",
        "Medical Specialist": "Medical Specialist",
        "Fellowship": "Fellowship",
        "Superspecialist":"Superspecialist",
        " ": "-None-",
    }
    UNIS = {
        "MUMS": "علوم پزشکی مشهد",
        "TUMS": "علوم پزشکی تهران",
         "----": "-None-",
    }
    # , help_text="بهتر است به فارسی بنویسید."
    first_name= models.CharField(max_length=50,)
    last_name= models.CharField(max_length=50)
    degree = models.CharField(max_length=20, choices=DEGREES, null=True, blank=True,
            help_text=(
            "Your current degree."
        ),)

    university= models.CharField(max_length=4, choices=UNIS, null=True, blank=True,
            help_text=(
            "Your current university."
        ),)
# Create your models here.
