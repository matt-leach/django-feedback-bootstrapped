from django import http

from feedback.forms import FeedbackForm


def add_feedback(request):
    """
    Ajax view for validating and saving a feedback form
    """
    if request.method != "POST":
        return http.HttpResponseNotAllowed("POST")

    form = FeedbackForm(request.POST)
    if form.is_valid():
        feedback = form.save(commit=False)
        feedback.user = request.user  # Add the user   
        feedback.save()
        return http.HttpResponse()
    else:
        # Form isn't valid, return generic 400
        return http.HttpResponseBadRequest()
    