from django.contrib import admin

from top.models import Answer, Choice

# Register your models here.
class ChoiceAdmin(admin.ModelAdmin):
    pass

class AnswerAdmin(admin.ModelAdmin):
    readonly_fields = ('choice1', 'choice2', 'choice3')
    list_display = ('text', 'choice1', 'choice2', 'choice3')


admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)
