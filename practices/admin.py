from django import forms
from django.contrib import admin
from practices.models import Subject, Practice, Axis, Comment

class AxisInline(admin.StackedInline):
    model = Axis
    max_num = 2

class SubjectAdmin(admin.ModelAdmin):
    exclude = ["id"]
    inlines = [AxisInline,]

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Practice)
admin.site.register(Comment)
