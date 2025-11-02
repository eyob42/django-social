# dwitter/forms.py
from django import forms
from .models import Dweet

class DweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Dweet something...",
                "class": "textarea is-success is-medium",
            }
        ),
        label="",
        ) # The only field is the message text, and it must be filled.

    class Meta:
        model = Dweet       # This form is for creating new Dweet objects.
        exclude = ("user",) # We DON'T ask the user to specify who is posting. We'll handle that ourselves.