from django.forms import ModelForm
from .models import Subscriber


class Subscriber(ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email', 'first_name', 'last_name']
        excludes = ['date_posted']


# class HomeScriberForm(ModelForm):
#     class Meta:
#         model = Subscriber
#         fields = ['email', 'first_name', 'last_name']
#         excludes = ['date_posted']
