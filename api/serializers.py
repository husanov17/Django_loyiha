from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(required = True)
    price = serializers.IntegerField()
    decription = serializers.CharField()



class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    age = serializers.IntegerField()
    grade = serializers.CharField()
    

class CourseSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    credit = serializers.IntegerField()
    description = serializers.CharField()


class TeacherSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    subject = serializers.CharField()
    experience_years = serializers.IntegerField()
