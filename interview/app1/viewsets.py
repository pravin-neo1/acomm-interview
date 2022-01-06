from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from app1.models import solution
from app1.serializers import SolutionSerializer


class SolutionViewset(APIView):

    def post(self, request):
        solution_serializer = SolutionSerializer(data=request.data)
        if solution_serializer.is_valid():
            time_req, msg = solution(**request.data)
            data = {
                "time_req": time_req,
                "X": solution_serializer.validated_data["X"],
                "msg": msg
            }
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            return Response({"msg": solution_serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)




