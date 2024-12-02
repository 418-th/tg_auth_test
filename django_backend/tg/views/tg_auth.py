from django.shortcuts import redirect
from django.contrib.auth import login, get_user_model

from rest_framework.views import APIView


from ..serializers import TgUserSerializer

User = get_user_model()


class TgAuthAPIView(APIView):

    @staticmethod
    def serialize(request, serializer=TgUserSerializer):
        serializer = serializer(data=request)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data

    def get(self, request, *args, **kwargs):
        data = self.serialize(request.GET)
        user = User.objects.get_or_create_user(data)
        login(request, user)
        request.session.save()
        return redirect('/auth')
