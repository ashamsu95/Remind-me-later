from rest_framework import serializers
from .models import Reminder

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ['id', 'message', 'reminder_time', 'reminder_method']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        reminder = Reminder.objects.create(user=user, **validated_data)
        return reminder