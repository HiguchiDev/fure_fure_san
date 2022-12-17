from django.views.generic import TemplateView
from .models import Answer, Category, Feeling
from rest_framework import viewsets
from .serializer import AnswerSerializer
from django.db.models import Q


class TopPageView(TemplateView):
    template_name: str = "top.html"

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        return queryset

    def get_context_data(self):
        ctx = super().get_context_data()

        ctx["categories"] = Category.objects.all()
        ctx["feelings"] = Feeling.objects.all()
        return ctx


class AnswerViewSet(viewsets.ReadOnlyModelViewSet):  # GetのみとするためReadOnlyを継承
    """
    /api/answer/?format=json&category_id=X&feeling_id=X にアクセスするとjson形式で選択肢にあった回答を返却する。
    Xの部分はそれぞれのIDを指定する。
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)

        category_id = self.request.GET["category_id"]
        feeling_id = self.request.GET["feeling_id"]
        filter_Q = Q(
            category_id=category_id,
            feeling_id=feeling_id
        )

        return queryset.filter(filter_Q)
