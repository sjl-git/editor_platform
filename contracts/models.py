from django.db import models
from core import models as core_models


class Contract(core_models.TimeStampedModel):
    employer = models.ForeignKey(
        "users.User", related_name="contracts", on_delete=models.CASCADE
    )
    editor = models.ForeignKey(
        "users.User", related_name="editor_contracts", on_delete=models.CASCADE
    )
    cost = models.IntegerField()

    def __str__(self):
        return f"{self.editor} by {self.employer}"


class Message(core_models.TimeStampedModel):
    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    contract = models.ForeignKey(
        "contracts.Contract", related_name="messages", on_delete=models.CASCADE
    )
