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
        COMBI_QTY_MAX = 2  # 選択肢によって回答が変化する最大個数
        SELECT_QTY_MAX = 8  # ユーザが選択できる最大個数

        choice_list = Choice.objects.exclude(text='Any')

        # 規定個数以上は登録不可
        if len(choice_list) >= SELECT_QTY_MAX:
            raise Exception(f"エラー：選択肢を登録できるのは{SELECT_QTY_MAX}個までです。")

        super().save(*args, **kwargs)
        choice_list = Choice.objects.exclude(text='Any')

        pair_list = []
        
        # 1～COMBI_QTY_MAX個選択時の全パターンを取得
        for i in range(1, COMBI_QTY_MAX + 1):
            for pair in itertools.combinations(choice_list, i):
                pair = list(pair)  # 後でappendする可能性があるのでリストにする

                if len(pair) < SELECT_QTY_MAX:
                    for j in range(SELECT_QTY_MAX - len(pair)):
                        pair.append(None)
                print(pair)

                pair_list.append(pair)


        # COMBI_QTY_MAX + 1個選んだ場合は選択肢にかかわらず回答が一定のため、ダミーのAny選択肢を入れる
        any_chioce = Choice.objects.filter(text="Any")[0]  #1個しか取れないはずなので0番目を取得
        any_choice_list = []

        for i in range(SELECT_QTY_MAX):
            if (i + 1) <= (COMBI_QTY_MAX + 1):
                any_choice_list.append(any_chioce)
            else:
                any_choice_list.append(None)
        
        pair_list.append(any_choice_list)

        any_choice_list = []
        # ユーザが選択できる最大個数を選んだ場合は特殊なパターンとして回答を用意する
        for i in range(SELECT_QTY_MAX):
            any_choice_list.append(any_chioce)
        
        pair_list.append(any_choice_list)

        # 回答作成（この時点では回答テキストは未挿入。Admin画面で管理ユーザに入れてもらう。）
        for pair in pair_list:
            ans = Answer.objects.filter(
                choice1=pair[0],
                choice2=pair[1],
                choice3=pair[2],
                choice4=pair[3],
                choice5=pair[4],
                choice6=pair[5],
                choice7=pair[6],
                choice8=pair[7],
            )

            # 既に同じ組み合わせの回答が存在していればスキップ
            if ans:
                continue

            Answer.objects.create(
                choice1=pair[0],
                choice2=pair[1],
                choice3=pair[2],
                choice4=pair[3],
                choice5=pair[4],
                choice6=pair[5],
                choice7=pair[6],
                choice8=pair[7],
            )


class Answer(models.Model):
    """
    選択肢に対応する回答
    """
    choice1 = models.ForeignKey(Choice, verbose_name="選択肢1", on_delete=models.CASCADE ,related_name='choice1', null=True)
    choice2 = models.ForeignKey(Choice, verbose_name="選択肢2", on_delete=models.CASCADE ,related_name='choice2', null=True)
    choice3 = models.ForeignKey(Choice, verbose_name="選択肢3", on_delete=models.CASCADE ,related_name='choice3', null=True)
    choice4 = models.ForeignKey(Choice, verbose_name="選択肢4", on_delete=models.CASCADE ,related_name='choice4', null=True)
    choice5 = models.ForeignKey(Choice, verbose_name="選択肢5", on_delete=models.CASCADE ,related_name='choice5', null=True)
    choice6 = models.ForeignKey(Choice, verbose_name="選択肢6", on_delete=models.CASCADE ,related_name='choice6', null=True)
    choice7 = models.ForeignKey(Choice, verbose_name="選択肢7", on_delete=models.CASCADE ,related_name='choice7', null=True)
    choice8 = models.ForeignKey(Choice, verbose_name="選択肢8", on_delete=models.CASCADE ,related_name='choice8', null=True)

    text = models.CharField(verbose_name="回答", max_length=100, null=True)

    def __str__(self):
        return str(self.text)
