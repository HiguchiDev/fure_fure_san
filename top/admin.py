from django.contrib import admin

from top.models import Answer, Choice

# Register your models here.
class ChoiceAdmin(admin.ModelAdmin):
    readonly_fields = (
        'id',
    )

    list_display = (
        'id',
        'text',
    )

class AnswerAdmin(admin.ModelAdmin):
    readonly_fields = (
        'id',
        'choice1',
        'choice2',
        'choice3',
        'choice4',
        'choice5',
        'choice6',
        'choice7',
        'choice8',
    )

    list_display = (
        'id',
        'text',
        'choice1',
        'choice2',
        'choice3',
        'choice4',
        'choice5',
        'choice6',
        'choice7',
        'choice8',
    )


admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)
