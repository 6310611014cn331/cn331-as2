from django.test import TestCase, Client
from django.urls import reverse
from django.db.models import Max
from .models import user_quotas
from subject.models import quotas, detail
from django.contrib.auth.models import User

# Create your tests here.
class UserViewTestCase(TestCase):
    def setUp(self):
        subDetail1 = detail.objects.create(code = "CN111", name = "test CN1", 
        section = "1", semester = "65", year = "2565")

        quotas.objects.create(subject = subDetail1, days = "Monday", time = "9.30 - 12.30", sit = 2)

        user1 = User.objects.create_user(username="monro", password="rororo")
        uq1 = user_quotas.objects.create(user = user1)

        quota = quotas.objects.first()
        quota.user_quota.add(uq1)
    
    def test_login_status_code(self):
        c = Client()
        response = c.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_login_success(self):
        c = Client()
        c.login(username = "monro", password = "rororo")
        response = c.get(reverse("u_index"))
        self.assertEqual(response.status_code, 200)

    def test_login_wrong_user(self):
        c = Client()
        c.login(username = "monto", password = "rororo")
        response = c.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_logout_wrong_pass(self):
        c = Client()
        c.login(username = "monro", password = "tototo")
        response = c.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        c = Client()
        c.logout()
        response = c.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
    
    def test_subject_status_code(self):
        c = Client()
        response = c.get(reverse("subject"))
        self.assertEqual(response.status_code, 200)
    