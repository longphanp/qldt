from rest_framework import serializers
from accounts.serializers import AccountSerializer
from persons.serializers import PersonSerializer, AchievementSerializer, HealthSerializer
from school.serializers import ClassroomSerializer
from .models import Student
from school.models import Classroom
from persons.utils import create_person, update_person, create_health, update_health, assign_health
from accounts.utils import create_account, update_account
from school.utils import assign_classroom_by_id, get_classroom

import logging
logger = logging.getLogger(__name__)


class StudentSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    person = PersonSerializer()
    health = HealthSerializer(required=False, allow_null=True)
    classroom_id = serializers.IntegerField()

    class Meta:
        model = Student
        fields = ['id', 'account', 'person', 'classroom_id', 'admission_year', 'health', 'status']

    def create(self, validated_data):
        person_model = create_person(validated_data.pop('person'))
        account_model = create_account(validated_data.pop('account'))
        try:
            student = Student.objects.create(account=account_model,
                                             person=person_model,
                                             **validated_data)
        except Exception:
            raise serializers.ValidationError('Something wrong with your student information')

        try:
            create_health(validated_data.pop('health'))
        except KeyError:
            pass

        student.save()
        return student

    def update(self, instance, validated_data):
        try:
            update_account(instance.account, validated_data.pop('account'))
        except KeyError:
            pass

        try:
            update_person(instance.person, validated_data.pop('person'))
        except KeyError:
            pass

        try:
            if instance.health is None:
                health = create_health(validated_data.pop('health'))
                assign_health(instance, health)
            else:
                update_health(student, validated_data.pop('health'))
        except:
            pass

        instance.classroom_id = validated_data.get('classroom_id', instance.classroom_id)
        instance.status = validated_data.get('status', instance.status)
        instance.admission_year = validated_data.get('admission_year', instance.admission_year)
        instance.save()
        return instance
