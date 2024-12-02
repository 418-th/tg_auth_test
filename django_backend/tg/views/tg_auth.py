from django.http import JsonResponse
from django.contrib.auth import login, get_user_model
from django.shortcuts import render
from django.conf import settings

from rest_framework.views import APIView

from cryptography.fernet import Fernet

from ..serializers import TgUserSerializer

User = get_user_model()
BOT_NAME = settings.BOT_NAME
AUTH_URL = settings.AUTH_URL
SALT = Fernet.generate_key()


class TgAuthAPIView(APIView):
    fernet = Fernet(SALT)

    def encrypt_token(self, token: str) -> str:
        encrypted_token = self.fernet.encrypt(token.encode())
        return encrypted_token.decode()

    def decrypt_token(self, token: str) -> str:
        decrypted_token = self.fernet.decrypt(token.encode())
        return decrypted_token.decode()

    @staticmethod
    def serialize(request, serializer=TgUserSerializer):
        serializer = serializer(data=request)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data

    def get(self, request, *args, **kwargs):

        if (
                request.GET.get('token')
                and not request.user.is_authenticated
        ):
            token = self.decrypt_token(request.GET.get('token'))
            try:
                user = User.objects.get(tg_auth_token=token)
            except User.DoesNotExist:
                print('HUI')
                return render(
                    request,
                    'auth.html',
                    context={
                        'error': f'token already used'
                    }
                )
            login(request, user)
            request.session.save()
            User.objects.update_token(user.tg_id)

        return render(
            request,
            'auth.html',
            context={
                'bot_name': BOT_NAME,
                'auth_url': AUTH_URL,
            }
        )

    def post(self, request, *args, **kwargs):
        data = self.serialize(request.data)
        user, token = User.objects.get_or_create_user(data)

        return JsonResponse(
            {
                'status': 'success',
                'token': self.encrypt_token(token),
            }
        )
