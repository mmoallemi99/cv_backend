from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Resume, Skill, Certificate, Project, Language, SocialMedia

from jalali_date.admin import ModelAdminJalaliMixin
from jalali_date.widgets import AdminDateWidget

admin.site.unregister(Group)


@admin.decorators.register(Resume)
class ResumeAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    formfield_overrides = {
        'birth_date': {'widget': AdminDateWidget},
    }
    # list_display =


@admin.decorators.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'resume', 'proficiency', )
    list_filter = ('title', 'proficiency', )


@admin.decorators.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'resume', 'organization', )
    list_filter = ('organization', )


@admin.decorators.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'resume', 'organization', 'date_completed', )
    list_filter = ('organization', )


@admin.decorators.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass
    # list_display =


@admin.decorators.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    pass
    # list_display =
