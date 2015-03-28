# django-feedback-bootstrapped
Django package providing a feedback widget styled with Bootstrap


**Usage**

* Add 'feedback' to your INSTALLED_APPS
* Add 'feedback.context_processors.feedback' to TEMPLATE_CONTEXT_PROCESSORS
* Add url(r'^feedback/', include('feedback.urls', namespace="feedback")), to your urls
* Include the feedback template in the page using {% include 'feedback/feedback.html' %} *Must come after the bootstrap js file*
