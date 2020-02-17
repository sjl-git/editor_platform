from django.db import models
from core import models as core_models


class Project(core_models.TimeStampedModel):
    name = models.CharField(max_length=80)
    contract = models.ForeignKey(
        "contracts.Contract", related_name="projects", on_delete=models.CASCADE
    )
    confirmed = models.BooleanField(default=False)


class ProjectFile(core_models.TimeStampedModel):
    project = models.ForeignKey(
        "projects.Project", related_name="files", on_delete=models.CASCADE
    )
    source = models.FileField(upload_to="project_source", null=True, blank=True)

    def get_source_name(self):
        full_name = str(self.source)
        split_name = full_name.split("/")
        return split_name[1]


class EditedVideo(core_models.TimeStampedModel):
    name = models.CharField(max_length=120)
    video = models.FileField(upload_to="edited_video")
    thumbnail = models.ImageField(
        upload_to="edited_video_thumbnail", null=True, blank=True
    )
    project = models.ForeignKey(
        "projects.Project", related_name="edited_videos", on_delete=models.CASCADE
    )
    confirmed = models.BooleanField(default=False)


class Comment(core_models.TimeStampedModel):
    comment = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="comments", null=True, on_delete=models.CASCADE
    )
    project = models.ForeignKey(
        "projects.Project", related_name="comments", on_delete=models.CASCADE
    )
