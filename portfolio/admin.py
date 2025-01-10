from django.contrib import admin
from .models import Technology, Category, Project, Blog, Tag, Skill

class TechnologyInline(admin.TabularInline):
    model = Project.technologies.through
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    search_fields = ('title', 'description')
    list_filter = ('category', 'technologies')
    inlines = [TechnologyInline]
    exclude = ('technologies',)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'content')
    list_filter = ('published_date', 'author')
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)

admin.site.register(Technology)
admin.site.register(Category)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)
admin.site.register(Skill, SkillAdmin)

