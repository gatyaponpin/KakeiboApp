from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from records.models import Kakeibo
from records.serializers.kakeibo_list_serializer import KakeiboListSerializer

class KakeiboListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        queryset = Kakeibo.objects.select_related('category').filter(
            user=user,
            deleted_at__isnull=True
        ).order_by('-day', '-created_at')

        serializer = KakeiboListSerializer(queryset, many=True)
        return Response(serializer.data)