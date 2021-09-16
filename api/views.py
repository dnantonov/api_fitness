from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.models import Report
from api.serializers import ReportSerializer


class ActivityViewSet(ModelViewSet):
    queryset = Report.objects.select_related('user').all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response(user_data, status=status.HTTP_201_CREATED)

