from rest_framework import serializers
from resume.models import Resume, Skill, Certificate, Project, Language, SocialMedia


class ResumeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Resume
        fields = '__all__'


class SkillSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Skill
        fields = '__all__'


class CertificateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Certificate
        fields = '__all__'


class ProjectSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class LanguageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Language
        fields = '__all__'


class SocialMediaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SocialMedia
        fields = '__all__'
