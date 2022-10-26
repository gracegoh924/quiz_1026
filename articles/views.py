from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.models import Article
from articles.serializers import ArticleSerializer # 추가

# Create your views here.
@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST': # 디시리얼라이즈
        serializer = ArticleSerializer(data = request.data) 
        if serializer.is_valid():
            serializer.save() 
            # print(serializer.data)
            # print(request.data['title'])
            return Response(serializer.data) # 완성된 데이터를 보내준다.
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
            # 개발 단계에선 편리하지만 front에 표시하는 건 보안상 좋지 않다.