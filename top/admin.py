from django.contrib import admin

from top.models import Answer, Category, Feeling

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = (
        'id',
    )

    list_display = (
        'id',
        'text',
    )

class FeelingAdmin(admin.ModelAdmin):
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
        'category',
        'feeling',
    )

    list_display = (
        'id',
        'text',
        'category',
        'feeling',
        'image_no',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Feeling, FeelingAdmin)
admin.site.register(Answer, AnswerAdmin)
