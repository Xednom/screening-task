from django.urls import reverse
from django.test import TestCase
from api.models import AgileValue, AgilePrinciple


class ApiTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        AgileValue.objects.create(title="testtitle_value", body="testbody_value")
        AgilePrinciple.objects.create(
            title="testtitle_principle", body="testbody_principle"
        )

    def test_value_max_length(self):
        value = AgileValue.objects.get(id=1)

        value_max_length = value._meta.get_field("title").max_length
        self.assertEquals(value_max_length, 300)

    def test_principle_max_length(self):
        principle = AgilePrinciple.objects.get(id=1)

        principle_max_length = principle._meta.get_field("title").max_length
        self.assertEquals(principle_max_length, 300)

    def test_api_status_code(self):
        response_values = self.client.get(
            "http://127.0.0.1:8000/api/v1/agile-values/", follow=True
        )
        response_principles = self.client.get(
            "http://127.0.0.1:8000/api/v1/agile-principles/", follow=True
        )
        self.assertEquals(response_values.status_code, 200)
        self.assertEquals(response_principles.status_code, 200)
