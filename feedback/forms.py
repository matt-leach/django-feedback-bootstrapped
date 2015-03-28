from django.forms import ModelForm
from django.forms.widgets import HiddenInput
from feedback.models import Feedback


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ["text", "url"] # user, time added separately 

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['url'].widget = HiddenInput()
        self.fields['text'].widget.attrs.update({"placeholder": "Enter feedback here"})
        self.fields['text'].label = False

    class Media:
         css = {
             'all': ('/static/feedback/feedback.css',),
         }
         js = ('/static/feedback/feedback.js', )
