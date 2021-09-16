from rest_framework import serializers

from api.models import Report


class ReportSerializer(serializers.ModelSerializer):
    activity = serializers.CharField(max_length=200)
    distance = serializers.FloatField()
    calories = serializers.FloatField()

    class Meta:
        model = Report
        fields = ('user', 'start_activity', 'end_activity', 'activity', 'distance', 'calories')


