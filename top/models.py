from cgitb import text
from django.db import models

# Create your models here.
from django.db import models
import itertools


# Create your models here.
class Choice(models.Model):
    """
    選択肢
    """
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        choice_list = Choice.objects.exclude(text='Any')

        CHOICE_SELECT_MAX = 3
        pair_list = []
        
        # 1～（CHOICE_SELECT_MAX-1）個選択時の全パターンを取得
        for i in range(1, CHOICE_SELECT_MAX):  # 1～(CHOICE_SELECT_MAX -1)
            for pair in itertools.combinations(choice_list, i):
                pair = list(pair)  # 後でappendする可能性があるのでリストにする
                if len(pair) < CHOICE_SELECT_MAX:
                    for j in range(CHOICE_SELECT_MAX - len(pair)):
                        pair.append(None)

                pair_list.append(pair)


        # CHOICE_SELECT_MAX個選んだ場合は最初に選んだ選択肢によって回答が決まる（他の選択肢は関係なし）ので、ダミーのAny選択肢を入れる
        any_chioce = Choice.objects.filter(text="Any")[0]  #1個しか取れないはずなので0番目を取得
        for c in choice_list:
            pair_list.append([c, any_chioce, any_chioce])
        

        # 回答作成（この時点では回答テキストは未挿入。Admin画面で管理ユーザに入れてもらう。）
        for pair in pair_list:
            ans = Answer.objects.filter(
                choice1=pair[0],
                choice2=pair[1],
                choice3=pair[2],
            )

            # 既に同じ組み合わせの回答が存在していればスキップ
            if ans:
                continue

            Answer.objects.create(
                choice1=pair[0],
                choice2=pair[1],
                choice3=pair[2],
            )


class Answer(models.Model):
    """
    選択肢に対応する回答
    """
    choice1 = models.ForeignKey(Choice, on_delete=models.CASCADE ,related_name='choice1', null=True)
    choice2 = models.ForeignKey(Choice, on_delete=models.CASCADE ,related_name='choice2', null=True)
    choice3 = models.ForeignKey(Choice, on_delete=models.CASCADE ,related_name='choice3', null=True)

    text = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.text)
