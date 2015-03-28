from django.test import TestCase
from django.contrib.auth.models import User

from feedback.models import Feedback


class TestAddFeedbackView(TestCase):
    
    def setUp(self):
        # Create User and login
        self.u = User.objects.create(username="user")
        self.u.set_password("foobar")
        self.u.save()
        self.client.login(username="user", password="foobar")
    
    def test_method_must_be_post(self):
        resp = self.client.get("/feedback/add/")
        self.assertEqual(resp.status_code, 405) # HttpResponseNotAllowed
        
    def test_no_data_returns_400(self):
        # form is not valid
        resp = self.client.post("/feedback/add/")
        self.assertEqual(resp.status_code, 400) # HttpResponseBadRequest
        
    def test_bad_data_returns_400(self):
        # form is not valid - invalid URL
        resp = self.client.post("/feedback/add/", {"text": "Sample Feedback", "url": "NOT AN URL"})
        self.assertEqual(resp.status_code, 400) # HttpResponseBadRequest
        
    def test_create_feedback_works(self):
        # Check we have no feedback initially
        self.assertEqual(Feedback.objects.count(), 0)
        
        resp = self.client.post("/feedback/add/", {"text": "Sample Feedback", "url": "http://localhost:8000/"})
        self.assertEqual(resp.status_code, 200) # HttpResponseBadRequest
        
        # Check we now have 1 feedback object
        self.assertEqual(Feedback.objects.count(), 1)
        
        # Check this Feedback object is as we expect
        feedback = Feedback.objects.all()[0]
        self.assertEqual(feedback.text, "Sample Feedback")
        self.assertEqual(feedback.url, "http://localhost:8000/")
        self.assertEqual(feedback.user, self.u)