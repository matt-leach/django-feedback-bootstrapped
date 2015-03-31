from django import http
from django.views.generic import View

from feedback.forms import FeedbackForm


class AddFeedbackView(View):

    def form_valid(self, form):
        feedback = form.save(commit=False)
        feedback.user = self.request.user  # Add the user
        feedback.save()
        return http.HttpResponse()

    def post(self, request, *args, **kwargs):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            # Form isn't valid, return generic 400
            return http.HttpResponseBadRequest()
