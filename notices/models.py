from django.db import models
from core import models as core_models


class Genre(core_models.TimeStampedModel):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Notice(core_models.TimeStampedModel):
    genre = models.ManyToManyField(Genre, related_name="notices")
    employer = models.ForeignKey(
        "users.User", related_name="notices", on_delete=models.CASCADE
    )
    deadline = models.IntegerField(default=10)
    edited_length = models.IntegerField(default=10, null=True, blank=True)

    def __str__(self):
        return f"{self.employer} on {self.created}"

    def notice_video(self):
        try:
            (video,) = self.videos.all()[:1]
            return video.video.url
        except ValueError:
            return None

    def get_applications(self):
        applications = self.applications.all()
        return applications

    class Meta:
        ordering = [
            "-created",
        ]


class NoticeVideo(core_models.TimeStampedModel):
    video = models.FileField(upload_to="notice_video",)
    notice = models.OneToOneField(
        "Notice", related_name="video", on_delete=models.CASCADE,
    )

