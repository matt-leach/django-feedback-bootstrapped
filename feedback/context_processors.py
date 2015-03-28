from feedback.forms import FeedbackForm


def feedback(request):    
    return {"feedback_form": FeedbackForm(auto_id=False, initial={'url': request.build_absolute_uri()})}

    
    