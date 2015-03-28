from django.forms import ModelForm
from feedback.models import Feedback


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ["text", "url"] # user, time added separately 

    class Media:
         css = {
             'all': ('/static/feedback/feedback.css',),
         }