from django.forms import ModelForm
from .models import Practice


# hidden_field_defaults = ("date_of_first_submit", "date_of_latest_submit", "id")


class PracticeForm(ModelForm):
    class Meta:
        model = Practice
        fields = '__all__'
