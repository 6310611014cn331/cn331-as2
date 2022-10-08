from ast import arguments
from django.test import TestCase, Client
from django.urls import reverse
from django.db.models import Max
from .models import user_quotas
from subject.models import quotas, detail
from django.contrib.auth.models import User

# Create your tests here.
class LoginTestCase(TestCase):
    def setUp(self):
        subDetail1 = detail.objects.create(code = "CN111", name = "test CN1", 
        section = "1", semester = "65", year = "2565")

        quotas.objects.create(subject = subDetail1, days = "Monday", time = "9.30 - 12.30", sit = 2)

        user1 = User.objects.create_user(username="monro", password="rororo")
        uq1 = user_quotas.objects.create(user = user1)

        user2 = User.objects.create_user(username="monto", password="tototo")
        uq2 = user_quotas.objects.create(user = user2)

        quota = quotas.objects.first()
        quota.user_quota.add(uq1)

    def test_login_status_code(self):
        c = Client()
        response = c.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_login_success(self):
        c = Client()
        c.post(reverse("login"), {"username":"monro", "password":"rororo"})
        response = c.get(reverse("u_index"))
        self.assertEqual(response.status_code, 200)

    def test_index_notlogin(self):
        c = Client()
        response = c.get(reverse("u_index"))
        self.assertEqual(response.status_code, 302)

    def test_login_wrong_user(self):
        c = Client()
        c.post(reverse("login"), {"username":"monoo", "password":"rororo"})
        response = c.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_logout_wrong_pass(self):
        c = Client()
        c.post(reverse("login"), {"username":"monro", "password":"toroto"})
        response = c.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        c = Client()
        c.get(reverse("logout"))
        response = c.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_subject_not_login(self):
        c = Client()
        response = c.get(reverse("subject"))
        self.assertEqual(response.status_code, 302)

    def test_subject_page_not_login(self):
        c = Client()
        sub = detail.objects.first()
        response = c.get(reverse("subject", args=(sub.id,)))
        self.assertEqual(response.status_code, 302)

    def test_quotas_not_login(self):
        c = Client()
        response = c.get(reverse("quotas", args = ("monro",)))
        self.assertEqual(response.status_code, 302)
    

class UserViewTestCase(TestCase):
    def setUp(self):
        subDetail1 = detail.objects.create(code = "CN111", name = "test CN1", 
        section = "1", semester = "65", year = "2565")

        quotas.objects.create(subject = subDetail1, days = "Monday", time = "9.30 - 12.30", sit = 2)

        user1 = User.objects.create_user(username="monro", password="rororo")
        uq1 = user_quotas.objects.create(user = user1)

        user2 = User.objects.create_user(username="monto", password="tototo")
        uq2 = user_quotas.objects.create(user = user2)

        quota = quotas.objects.first()
        quota.user_quota.add(uq1)

    def test_subject_status_code(self):
        c = Client()
        c.login(username = "monro", password = "rororo")
        response = c.get(reverse("subject"))
        self.assertEqual(response.status_code, 200)

    def test_subject_context(self):
        c = Client()
        c.login(username = "monro", password = "rororo")
        response = c.get(reverse("subject"))
        self.assertEqual(response.context["subject"].count(), 1)

    def test_subject_page(self):
        c = Client()
        c.login(username = "monro", password = "rororo")
        sub = detail.objects.first()
        response = c.get(reverse("subject", args=(sub.id,)))
        self.assertEqual(response.status_code, 200)
    
    def test_quotas_status_code(self):
        c = Client()
        c.login(username = "monro", password = "rororo")
        u = user_quotas.objects.first()
        response = c.get(reverse("quotas", args = (u,)))
        self.assertEqual(response.status_code, 200)

    def test_book(self):
        c = Client()
        c.login(username = "monto", password = "tototo")
        user = User.objects.get(username="monto")
        u = user_quotas.objects.get(user = user)
        q = quotas.objects.first()
        c.post(reverse("book", args = ("monto",)), {"quotas" : q.id})
        self.assertEqual(u.subject.count(), 1)

    def test_delete(self):
        c = Client()
        c.login(username = "monro", password = "rororo")
        user = User.objects.get(username="monro")
        u = user_quotas.objects.get(user = user)
        q = quotas.objects.first()
        c.post(reverse("delete", args = ("monro",q.id)))
        self.assertEqual(u.subject.count(), 0)

    def test_weird_url(self):
        c = Client()
        c.login(username = "monro", password = "rororo")
        response = c.get('/something/weird/')
        self.assertEqual(response.status_code, 404)

    