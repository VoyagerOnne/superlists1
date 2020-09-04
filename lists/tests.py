from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from .views import home_page


class HomePageTest(TestCase):
    """Тест домашней страницы"""

    def test_root_url_resolves_to_home_page_view(self):
        """Тест: корневой url преобразуется в представление домашней страницы"""
        found = resolve('/')
        self.assertEqual(found.func, home_page)


class HomePageTest(TestCase):
    """Тест: домашняя страница возвращает правильный html"""
    request = HttpRequest()    # То что Django увидит когда пользователь запросит страницу
    response = home_page(request)
    html = response.content.decode('utf8')
    self.assertIn('<title>To-Do lists</title>', html)
