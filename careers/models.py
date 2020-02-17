from django.db import models
from core import models as core_models


class Career(core_models.TimeStampedModel):
    user = models.ForeignKey(
        "users.User", related_name="careers", on_delete=models.CASCADE
    )
    employer = models.ForeignKey(
        "users.User", related_name="employer_career", on_delete=models.CASCADE
    )
    number = models.IntegerField()

    def __str__(self):
        return f"{self.user} with {self.employer}"
