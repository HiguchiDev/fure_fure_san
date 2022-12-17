from cgitb import text
from django.db import models

# Create your models here.
from django.db import models
from django.db.models import Q


class Category(models.Model):
    """
    カテゴリ
    """
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        super().save(args, kwargs)
        feeling = Feeling.objects.all()

        for f in feeling:
            Answer.objects.create(
                category=self,
                feeling=f,
                image_no=1,
            )

# Create your models here.
class Feeling(models.Model):
    """
    選択肢
    """
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        super().save(args, kwargs)
        category = Category.objects.all()

        for c in category:
            Answer.objects.create(
                category=c,
                feeling=self,
                image_no=1,
            )

class Answer(models.Model):
    """
    選択肢に対応する回答
    """
    category = models.ForeignKey(Category, verbose_name="カテゴリ", on_delete=models.CASCADE ,related_name='category', default="", null=False)
    feeling = models.ForeignKey(Feeling, verbose_name="気持ち", on_delete=models.CASCADE ,related_name='feeling', default="", null=False)
    text = models.CharField(verbose_name="回答", max_length=100, null=True)
    image_no = models.IntegerField(verbose_name="回答時に表示する画像番号", choices=[(1, 1), (2, 2), (3, 3)], default=1, null=False)

    def __str__(self):
        return str(self.text)
