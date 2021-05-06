
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
import speech_recognition as sr
from rest_framework import status

class UploadFile(APIView):
    parser_class = (FileUploadParser,)

    def put(self, request, format=None):
        if 'file' not in request.data:
            raise ParseError("Empty content")

        f = request.data['file']
        r = sr.Recognizer()
        harvard = sr.AudioFile(f)
        with harvard as source:
            audio = r.record(source)
        msg = r.recognize_google(audio)

        return Response({"msg" : msg },status=status.HTTP_201_CREATED)