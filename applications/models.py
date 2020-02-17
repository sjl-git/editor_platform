from django.db import models
from core import models as core_models


class Application(core_models.TimeStampedModel):
    applicant = models.ForeignKey(
        "users.User", related_name="applications", on_delete=models.CASCADE
    )
    cost = models.IntegerField()
    video = models.FileField(upload_to="application_video", null=True, blank=True)
    notice = models.ForeignKey(
        "notices.Notice", related_name="applications", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.created} by {self.applicant}"

    class Meta:
        ordering = [
            "-created",
        ]
