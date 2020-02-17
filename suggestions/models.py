from django.db import models
from core import models as core_models


class Suggestion(core_models.TimeStampedModel):
    proposer = models.ForeignKey(
        "users.User", related_name="sended_suggestions", on_delete=models.CASCADE
    )
    other_side = models.ForeignKey(
        "users.User", related_name="received_suggestions", on_delete=models.CASCADE
    )
    cost = models.IntegerField()
    application = models.OneToOneField(
        "applications.Application", related_name="suggestion", on_delete=models.CASCADE
    )
    has_answer = models.BooleanField(default=False)


class Answer(core_models.TimeStampedModel):
    answerer = models.ForeignKey(
        "users.User", related_name="answers", on_delete=models.CASCADE
    )
    recepient = models.ForeignKey(
        "users.User", related_name="received_answers", on_delete=models.CASCADE
    )
    answer = models.BooleanField()
    suggestion = models.OneToOneField(
        "suggestions.Suggestion", related_name="answer", on_delete=models.CASCADE
    )
