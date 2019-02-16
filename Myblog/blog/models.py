from django.db import models
from django.urls import reverse
from tagging.fields import TagField


class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple descriptions text')
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
    tag = TagField()

    class Meta:
        verbose_name = 'post'  # 테이블의 별칭을 단수복수로 나누고 단수 별칭지정
        verbose_name_plural = 'posts'  # 복수 별칭 지정
        
        db_table = 'blog_posts'  # 데이터베이스에 저장되는 테이블의 이름지정 생략가능 생략하면 디폴트는 blog_post가 되었을 것.
        ordering = ('-modify_date',)  # 내림차순 정리

    def __str__(self):
        return self.title  # 객체의 문자열 표현 메소드 객체.title 속성으로 표시되도록함.

    def get_absolute_url(self):  # 이 메소드가 정의된 객체를 지칭하는 URL반환
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous_post(self):  # modify_date를 컬럼을 기준으로 이전포스트 반환 장고 내장함수인 get_next_by_modify_date()호출
        return self.get_previous_by_modify_date()

    def get_next_post(self):  # 다음포스트 반환
        return self.get_next_by_modify_date()

