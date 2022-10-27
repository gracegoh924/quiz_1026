from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from articles.models import Article
from articles.serializers import ArticleSerializer # 추가

# Create your views here.
@api_view(['GET', 'POST'])
def articleAPI(request):
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
            return Response(serializer.data, status=status.HTTP_201_CREATED) # 완성된 데이터를 보내준다.
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
            # 개발 단계에선 편리하지만 front에 표시하는 건 보안상 좋지 않다.

@api_view(['GET', 'PUT', 'DELETE'])
def articleDetailAPI(request, article_id):
    if request.method == 'GET':
        # return Response(article) 이렇게는 할 수 없고
        # article = Article.objects.get(id=article_id) # 1004를 저장
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # 위 상세페이지처럼, 복사해서 가져와서 수정을 해줘야 한다.
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article, data=request.data) 
        # (원래data:읽기, 나중에들어온data) 앞의data를 뒤data로 바꾸어주는 것.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


