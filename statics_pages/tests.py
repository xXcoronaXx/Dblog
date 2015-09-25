from django.test import TestCase
from config.models import *
from .models import *
from django.contrib.auth.models import User

class TestViews(TestCase):

	def setUp(self):
		self.admin = User.objects.create_superuser('1234', 'test@test.com', '1234')
		self.config = Config.objects.create(pk=1, title='Dblog title', subtitle='Dblog subtitle')
		self.config.save()
		self.p1 = Page.objects.create(pk=1,title='p1',text='bla bla',visible=True, author=self.admin)
		self.p1.save()
		self.p2 = Page.objects.create(pk=2,title='p2',text='bla bla',visible=False, author=self.admin)
		self.p2.save()

	def test_call_view_page(self):
		p1 = Page.objects.get(pk=1)
		response = self.client.get('/page/'+p1.slug+'/')
		self.assertEqual(response.status_code, 200)

	def test_call_preview_page_denied(self):
		p2 = Page.objects.get(pk=2)
		response = self.client.get('/page/admin/'+p2.slug+'/')
		self.assertEqual(response.status_code, 302)

	def test_call_preview_page(self):
		self.client.login(username='1234', password='1234')
		p2 = Page.objects.get(pk=2)
		response = self.client.get('/page/admin/'+p2.slug+'/')
		self.assertEqual(response.status_code, 200)