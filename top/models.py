from cgitb import text
from django.db import models

# Create your models here.
from django.db import models
import itertools

from top.utils.const_max_qty import MAX_QTY
from top.utils.get_all_choice_pattern import get_all_choice_pattern_combinations
from top.utils.get_model_field_qty import get_model_field_qty
from django.db.models import Q


# Create your models here.
class Choice(models.Model):
    """
    選択肢
    """
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        SELECT_QTY_MAX = get_model_field_qty(Answer, "choice")
        choice_list = Choice.objects.exclude(text='Any')

        # 規定個数以上は登録不可
        if len(choice_list) >= SELECT_QTY_MAX:
            raise Exception(f"エラー：選択肢を登録できるのは{SELECT_QTY_MAX}個までです。")

        super().save(*args, **kwargs)
        choice_list = Choice.objects.exclude(text='Any')

        pair_list = get_all_choice_pattern_combinations(choice_list, Answer)

        # MAX_QTY.COMBI_QTY_MAX + 1個選んだ場合は選択肢にかかわらず回答が一定のため、ダミーのAny選択肢を入れる
        any_chioce = Choice.objects.filter(text="Any")[0]  #1個しか取れないはずなので0番目を取得
        any_choice_list = []

        for i in range(SELECT_QTY_MAX):
            if (i + 1) <= (MAX_QTY.COMBI_QTY_MAX + 1):
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

    @classmethod
    def get_choice_query(self, param_list):
        return Q(
            choice1__id=param_list[0],
            choice2__id=param_list[1],
            choice3__id=param_list[2],
            choice4__id=param_list[3],
            choice5__id=param_list[4],
            choice6__id=param_list[5],
            choice7__id=param_list[6],
            choice8__id=param_list[7],
        )

    def __str__(self):
        return str(self.text)
