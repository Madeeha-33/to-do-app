from django.test import SimpleTestCase
from django.urls import reverse , resolve
from todolist.views import IndexClassView , add , edit , delete , taskstatus, details
#from views import DetailView
from users.views import logout_view
from django.contrib.auth.views import LoginView
from users.views import register
class TestUrls(SimpleTestCase):
    def test_logout(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func , logout_view)
    def test_register(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register )

    def test_login(self):
        url = reverse('login')
        #
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class , LoginView)

    def test_IndexClassView(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class , IndexClassView)

    def test_task_add(self):
        url = reverse('add')
        self.assertEquals(resolve(url).func , add)
    def test_task_edit(self):
        url = reverse('edit' , args= [1])
        self.assertEquals(resolve(url).func, edit)
    def test_task_delete(self):
        url =  reverse('delete' , args=[1])
        self.assertEquals(resolve(url).func , delete)
    def test_task_taskstatus(self):
        url = reverse('taskstatus' , args=[2])
        self.assertEquals(resolve(url).func , taskstatus)

