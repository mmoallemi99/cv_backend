from rest_framework.routers import DefaultRouter

from .views import (
    ResumeViewSet,
    SkillViewSet,
    CertificateViewSet,
    ProjectViewSet,
    LanguageViewSet,
    SocialMediaViewSet,
)


router = DefaultRouter()
router.register(r'resumes', ResumeViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'certificates', CertificateViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'languages', LanguageViewSet)
router.register(r'social_medias', SocialMediaViewSet)

urlpatterns = router.urls

