from tkinter.messagebox import QUESTION
from django.contrib import admin
from . import models


class ChoiseInLine(admin.TabularInline):
    model = models.Choise
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Info', {'fields': [
                  'publish_date'], 'classes': ['collapse']}),
                 ]
    inlines = [ChoiseInLine]


admin.site.register(models.Questions, QuestionAdmin)
