from rest_framework.generics import ListCreateAPIView, ListAPIView

from core.models import Token, YF
from core.serializers import TokenSerializer, YFSerializer


class ListCreateTokensView(ListCreateAPIView):
    serializer_class = TokenSerializer
    queryset = Token.objects.all()


class RetrieveTokensForUserView(ListAPIView):
    def get_queryset(self):
        return Token.objects.filter(user=self.kwargs['user'])

    serializer_class = TokenSerializer


class ListCreateYFsView(ListCreateAPIView):
    serializer_class = YFSerializer
    queryset = YF.objects.all()


class RetrieveYFsForUserView(ListAPIView):
    def get_queryset(self):
        return YF.objects.filter(user=self.kwargs['user'])

    serializer_class = YFSerializer
