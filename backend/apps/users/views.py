from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from django.contrib.sessions.models import Session

from .models import User
class Login(ObtainAuthToken):
    
    def post(self, request, *args, **Kwargs):

        login_serializer = self.serializer_class(data=request.data, context={'request': request})
        
        if login_serializer.is_valid():
            
            user = User.objects.filter(
                username=login_serializer.validated_data['username']
            ).first()
            
            token, created = Token.objects.get_or_create(user=user)

            if created:
                return Response({"message": "excellent", "token": str(token)}, status=status.HTTP_201_CREATED)
            else:
                """
                all_sessions = Session.objects.filter(expire_date__gte=timezone.now())
                if all_sessions:
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()

                token.delete()
                token = Token.objects.create(user=user)
                """
                token.delete()
                return Response({"message": "Already session exists"}, status=status.HTTP_409_CONFLICT)
        else:
            return Response({"message": "bad"}, status=status.HTTP_400_BAD_REQUEST)
