from .crud.registraion import RegisterView
from .crud.superuser import SuperUser
from .crud.update import UserUpdate
from GenericResponse import returnresponse

RegisterView()
SuperUser()
UserUpdate()


from rest_framework import generics
from rest_framework.response import Response
from django.core.mail import send_mail,EmailMessage
from CRM_project.settings import EMAIL_HOST_USER

from .serializers import regserialzer
from .models import Account
class reg(generics.GenericAPIView):
    serializer_class = regserialzer

    def post(self, request):
        ser = regserialzer(data=request.data)
        ser.is_valid()
        ser.save()
        message="mail sent success"
        subject="New regitered"
        EMAIL = ['hemadhu7@gmail.com']
        send_mail(subject,message,EMAIL_HOST_USER,recipient_list=EMAIL,fail_silently=True)
        x = returnresponse(200,ser.data,"success")
        return Response(x)
    def get(self, request):
        s = Account.object.all()
        return Response(s)


