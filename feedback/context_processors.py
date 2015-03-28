from feedback.forms import FeedbackForm


def feedback(request):    
    return {"feedback_form": FeedbackForm(initial={'url': request.build_absolute_uri()})}

    
    