from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    price = serializers.IntegerField()
    decription = serializers.CharField()
    
    def validate_name(self, value):
        if value.isdigit():
            raise serializers.ValidationError("Name raqam bolish mumjin emas")
        return value
    
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError(detail={"messages": "Price 0 dan katta bolsin"})
        return value



class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    age = serializers.IntegerField()
    grade = serializers.CharField()
    
    def validate_name(self, value):
        if value.isdigit():
            raise serializers.ValidationError("Name raqam bolish mumjin emas")
        return value
    
    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError(detail={"messages": "Age 0 dan katta bolsin"})
        return value



class CourseSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    credit = serializers.IntegerField()
    description = serializers.CharField()
    
    def validate_title(self, value):
        if value.isdigit():
            raise serializers.ValidationError("Title raqam bolish mumjin emas")
        return value
    
    def validate_credit(self, value):
        if value < 0:
            raise serializers.ValidationError(detail={"messages": "Credit 0 dan katta bolsin"})
        return value



class TeacherSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    subject = serializers.CharField()
    experience_years = serializers.IntegerField()
    
    def validate_name(self, value):
        if value.isdigit():
            raise serializers.ValidationError("Name raqam bolish mumjin emas")
        return value
    
    def validate_experience_years(self, value):
        if value < 0:
            raise serializers.ValidationError(detail={"messages": "Experience 0 dan katta bolsin"})
        return value
