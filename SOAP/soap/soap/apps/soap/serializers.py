from spyne.util.django import DjangoComplexModel
from .models import Submission as SubmissionModel


class Submission(DjangoComplexModel):
    class Attributes(DjangoComplexModel.Attributes):
        django_model = SubmissionModel
