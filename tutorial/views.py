# 클래스 기반의 Rest CRUD 처리
from tutorial.models import blog
from tutorial.serializers import blogSerializer
from rest_framework import generics

# generics 에 목록과 생성 API 가 정의되어 있다
class blogList(generics.ListCreateAPIView):
    queryset = blog.objects.all()
    serializer_class = blogSerializer

# generics 에 상세, 수정, 삭제 API가 정의되어 있다
class blogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = blog.objects.all()
    serializer_class = blogSerializer