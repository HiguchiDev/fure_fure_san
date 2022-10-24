import itertools
from django.views.generic import ListView
from top.utils.get_all_choice_pattern import get_all_choice_pattern_permutations
from .models import Answer, Choice
from rest_framework import viewsets
from .serializer import AnswerSerializer


class TopPageView(ListView):
    template_name: str = "top.html"
    model = Choice

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        return queryset

    def get_context_data(self):
        ctx = super().get_context_data()
        return ctx


class AnswerViewSet(viewsets.ReadOnlyModelViewSet):  # GetのみとするためReadOnlyを継承
    """
    /api/answer/?format=json&select1=X&select2=X にアクセスするとjson形式で選択肢にあった回答を返却する。
    Xの部分はChoiceのIDを指定し、selectは&でつなげればいくつでも指定可能。
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_queryset(self, **kwargs):
        """
        Getパラメータ：selectXに該当する選択肢を持つ回答を返す。
        パラメータの指定は順不動。どこに入れてもその組み合わせの回答があれば返却する。
        例）
        select1=1
        select2=2
        select3=3

        choice_id: [1, 2, 3] or [1, 3, 2] or [2, 1, 3] or [2, 3, 1] or [3, 1, 2] or [3, 2, 1]の6パターンで検索
        """
        queryset = super().get_queryset(**kwargs)

        selected_choice_id_list = []
        for k, v in self.request.GET.items():
            if k.startswith("select"):
                selected_choice_id_list.append(v)

        if not selected_choice_id_list:
            return queryset 

        pair_list = get_all_choice_pattern_permutations(selected_choice_id_list, Answer)

        filter_Q = None
        for pair in pair_list:
            if filter_Q is None:
                filter_Q = Answer.get_choice_query(pair)
            else:
                filter_Q |= Answer.get_choice_query(pair)

        return queryset.filter(filter_Q)
