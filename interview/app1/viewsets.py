from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from app1.serializers import SolutionSerializer


class SolutionViewset(APIView):

    def post(self, request):
        ss = SolutionSerializer(data=request.data)
        if ss.is_valid():
            data = {
                "X": ss.data["X"],
                "time_req": ss.data["time_req"],
                "msg": "Can't jump!" if ss.data["time_req"] == -1 else "Jump successfully"
            }
            return Response(
                data=data,
                status=status.HTTP_200_OK if ss.data["time_req"] != -1 else status.HTTP_400_BAD_REQUEST
            )
        else:
            data = {
                "X": ss.data["X"],
                "time_req": -1,
                "msg": ss.errors
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)




