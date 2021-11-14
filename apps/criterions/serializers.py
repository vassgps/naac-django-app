# CMS / Serializer
from rest_framework import serializers
from .models import CriterionMaster
from .fields.field_names import fc1_1_1


# Tags for Page
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CriterionMaster
        field_tup = ('id', 'user') + fc1_1_1
        fields = field_tup
