from rest_framework import viewsets
from rest_framework.routers import Response
from rest_framework.views import APIView

from .serializers import (
    SubmissionSerializer,
    KnapsackOutputSerializer,
    KnapsackSerializer,
)

from .models import Submission


class SubmissionViewSet(viewsets.ModelViewSet):
    """
    Entrypoint for submissions
    """

    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer


def knapSack(W, items):
    val, wt, n = [], [], len(items)
    for item in items:
        val.append(item["value"])
        wt.append(item["weight"])

    dp = [0 for _ in range(W + 1)]  # Making the dp array

    for i in range(1, n + 1):  # taking first i elements
        for w in range(W, 0, -1):  # starting from back,so that we also have data of
            # previous computation when taking i-1 items
            if wt[i - 1] <= w:
                # finding the maximum value
                dp[w] = max(dp[w], dp[w - wt[i - 1]] + val[i - 1])

    return dp[W]  # returning the maximum value of knapsack


class KnapsackView(APIView):
    def post(self, request, format=None):
        input_serializer = KnapsackSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        in_data = input_serializer.data

        sub = Submission.objects.create(input=in_data)

        max_value = knapSack(in_data["max_weight"], in_data["items"])

        # output_serializer = KnapsackOutputSerializer(initial={"max_value": max_value})
        # out_data = output_serializer.data
        out_data = {"max_value": max_value}

        sub.output = out_data
        sub.save()

        return Response(out_data)
