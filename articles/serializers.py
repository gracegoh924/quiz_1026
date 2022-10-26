from rest_framework import serializers
from articles.models import Article

 # 시리얼라이저란? 모델에 입력한 걸 계속 쓰지 않기 위한 drf 도구
class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = '__all__' # 모든 필드를 다루겠다.
