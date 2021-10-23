from django.shortcuts import redirect
from django.test import TestCase, Client

from .models import *


class HomePageTest(TestCase):
    @classmethod
    def setUpTestData(cls):  # создание тестовых данных один раз для всего тест кейса
        # создадим 5 новостей и 7 публикаций
        cls.new1 = News.objects.create(title='new1', content='new1', author='new1')
        cls.new2 = News.objects.create(title='new2', content='new2', author='new2')
        cls.new3 = News.objects.create(title='new3', content='new3', author='new3')
        cls.new4 = News.objects.create(title='new4', content='new4', author='new4')
        cls.new5 = News.objects.create(title='new5', content='new5', author='new5')

        cls.pub1 = Publications.objects.create(title='title1', content='text1', author='1')
        cls.pub2 = Publications.objects.create(title='title2', content='text2', author='2')
        cls.pub3 = Publications.objects.create(title='title3', content='text3', author='3')
        cls.pub4 = Publications.objects.create(title='title4', content='text4', author='4')
        cls.pub5 = Publications.objects.create(title='title5', content='text5', author='5')
        cls.pub6 = Publications.objects.create(title='title6', content='text6', author='6')
        cls.pub7 = Publications.objects.create(title='title7', content='text7', author='7')

    def setUp(self) -> None:
        self.c = Client()  # фиктивный браузер

    def test_empty_url_notfound(self):
        response = self.c.get('')
        self.assertEqual(response.status_code, 404)

    def test_home_page_ok(self):
        response = self.c.get('/home/')
        self.assertEqual(response.status_code, 200)

    def test_num_of_posts_on_page(self):
        response = self.c.get('/home/')
        # одновременно на странице отображается максимум 5 публикаций и 4 новости
        self.assertEqual(len(response.context['page_obj']), 5)
        self.assertEqual(len(response.context['news']), 4)


class DetailNewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.new1 = News.objects.create(title='new1', content='new1', author='new1')
        cls.new2 = News.objects.create(title='new2', content='new2', author='new2')
        cls.new3 = News.objects.create(title='new3', content='new3', author='new3')

        cls.user1 = User.objects.create(username='user1', password='secret1')
        cls.user2 = User.objects.create(username='user2', password='secret2')

        # 3 комментария у первой новости и 1 у второй
        cls.comm1 = CommentNews.objects.create(id_user=cls.user1, id_post=cls.new1, text='text')
        cls.comm2 = CommentNews.objects.create(id_user=cls.user1, id_post=cls.new1, text='text')
        cls.comm3 = CommentNews.objects.create(id_user=cls.user2, id_post=cls.new1, text='text')
        cls.comm4 = CommentNews.objects.create(id_user=cls.user1, id_post=cls.new2, text='text')

    def setUp(self) -> None:
        self.c = Client()

    def test_detail_page_status(self):
        response = self.c.get('/home/new/1/')
        self.assertEqual(response.status_code, 200)

        response = self.c.get('/home/new/10/')
        self.assertEqual(response.status_code, 404)

    def test_num_of_comments(self):
        response1 = self.c.get('/home/new/1/')
        self.assertEqual(len(response1.context['comments']), 3)

        response2 = self.c.get('/home/new/3/')
        self.assertEqual(len(response2.context['comments']), 0)

        # кол-во комментариев на 3 новость увеличилось, а на остальные не изменилось
        response2 = self.c.post('/home/new/3/', {'new_comm': 'text'})
        self.assertEqual(len(response2.context['comments']), 1)
        self.assertEqual(len(response1.context['comments']), 3)








