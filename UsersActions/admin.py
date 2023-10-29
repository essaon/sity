from tkinter.messagebox import QUESTION
from django.contrib import admin
from . import models

admin.site.site_header = "Mental Damage"
admin.site.site_title = "Illness"
admin.site.index_title = "Welcome Versality"


class ChoiseInLine(admin.TabularInline):
    model = models.Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Info', {'fields': [
                  'publish_date'], 'classes': ['collapse']}),
                 ]
    inlines = [ChoiseInLine]


admin.site.register(models.Questions, QuestionAdmin)
