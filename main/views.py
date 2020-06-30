from rest_framework.views import APIView
from rest_framework.response import Response
from happyjob.settings import logger


class HomePage(APIView):

    def get(self, request):
        logger.info("New req")
        return Response(data={"msg": "hi"}, status=200)
