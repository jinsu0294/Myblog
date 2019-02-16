from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'


    #TemplateView를 사용하는 경우에는 필수적으로 template_name 클래스 변수를 오버라이딩으로 지정해줘야함.
    #템플릿 상속은 3단계로 구성 최상위 탬플릿은 사이트 전체의 룩앤필을 정의하는 것으로 보통은 파일명을 base.html로 하지만 원하는 이름 가능.

