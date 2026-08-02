from django.contrib.auth.password_validation import validate_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from review_engine.api.account_serializer import ChangePasswordSerializer, DeleteAccountSerializer

class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            {
                "username": request.user.username,
                "email": request.user.email,
            }
        )
        
    
class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        if not user.check_password(serializer.validated_data["old_password"]):
            return Response(
                {
                "message": "Old password is incorrect."
                },
            status=status.HTTP_400_BAD_REQUEST
            )
        validate_password(serializer.validated_data["new_password"],user)
        user.set_password(serializer.validated_data["new_password"])
        user.save()
        return Response(
            {
                "message": "Password changed successfully. Please login again."
            }
        )

class DeleteAccountAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request):
        serializer = DeleteAccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        if not user.check_password(serializer.validated_data["password"]):
            return Response(
                {
                    "message": "Password is incorrect."
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        user.delete()
        return Response(
            {
                "message": "Account deleted successfully."
            }
        )
        