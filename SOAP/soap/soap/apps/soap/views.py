from django.db.utils import IntegrityError

from spyne.error import ResourceNotFoundError, ResourceAlreadyExistsError
from spyne.model.complex import Iterable
from spyne.model.primitive import Integer
from spyne.protocol.soap import Soap11
from spyne.application import Application
from spyne.decorator import rpc
from spyne.util.django import DjangoService
from spyne.model.complex import Array

import json

from .models import Submission as SubmissionModel

from .serializers import Submission


class SortService(DjangoService):
    """
    Service for sorts handling
    """

    @rpc(Array(Integer), _returns=Array(Integer))
    def sort(ctx, array):
        input_data = json.dumps(array)
        sub = SubmissionModel.objects.create(input=input_data)
        output_data = sorted(array)
        sub.output = json.dumps(output_data)
        sub.save()
        return output_data

    @rpc(Integer, Integer, _returns=Iterable(Submission))
    def list_submissions(ctx, limit, offset):
        limit, offset = limit or 20, offset or 0  # default
        return SubmissionModel.objects.all()[offset : offset + limit]

    @rpc(Integer, _returns=Submission)
    def get_submission(ctx, pk):
        try:
            return SubmissionModel.objects.get(pk=pk)
        except SubmissionModel.DoesNotExist:
            raise ResourceNotFoundError("submission")

    @rpc(Submission, _returns=Submission)
    def create_submission(ctx, submission):
        try:
            return SubmissionModel.objects.create(**submission.as_dict())
        except IntegrityError:
            raise ResourceAlreadyExistsError("Submission")

    @rpc(Submission, _returns=Submission)
    def update_submission(ctx, submission):
        return SubmissionModel.objects.filter(pk=submission.pk).update(
            **submission.as_dict()
        )


app = Application(
    [
        SortService,
    ],
    "soap.app.soap",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11(),
)
