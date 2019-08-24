from rest_framework.viewsets import ReadOnlyModelViewSet
from resume.models import (
    Resume,
    Skill,
    Certificate,
    Project,
    Language,
    SocialMedia,
)
from resume.serializers import (
    ResumeSerializer,
    SkillSerializer,
    CertificateSerializer,
    ProjectSerializer,
    LanguageSerializer,
    SocialMediaSerializer,
)


class ResumeViewSet(ReadOnlyModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


class SkillViewSet(ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class CertificateViewSet(ReadOnlyModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class ProjectViewSet(ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class LanguageViewSet(ReadOnlyModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class SocialMediaViewSet(ReadOnlyModelViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
