from django.test import TestCase
from .models import detail, quotas
from django.contrib.auth.models import User
from users.models import user_quotas

# Create your tests here.
class SubjectTestCase(TestCase):
    def setUp(self):
        subDetail1 = detail.objects.create(code = "CN111", name = "test CN1", 
        section = "1", semester = "65", year = "2565")

        quotas.objects.create(subject = subDetail1, days = "Monday", time = "9.30 - 12.30", sit = 2)
    
    def test_sit_available(self):
        quota = quotas.objects.first()
        self.assertTrue(quota.sit_is_available())

    def test_sit_not_available(self):
        user1 = User.objects.create_user(username="monro", password="rororo")
        user2 = User.objects.create_user(username="monto", password="tototo")

        uq1 = user_quotas.objects.create(user = user1)
        uq2 = user_quotas.objects.create(user = user2)

        quota = quotas.objects.first()
        quota.user_quota.add(uq1)
        quota.user_quota.add(uq2)

        self.assertFalse(quota.sit_is_available())
