from rest_framework import serializers

from .models import Account, Activity, ActivityStatus, Contact, ContactSource, ContactStatus

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"

class ActivityStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityStatus
        fields = "__all__"

class ContactSerializer(serializer.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

class ContactSourceSerializer(serializer.ModelSerializer):
    class Meta:
        model = ContactSource
        fields = "__all__"

class ContactStatusSerializer(serializer.ModelSerializer):
    class Meta:
        model = ContactStatus
        fields = "__all__"