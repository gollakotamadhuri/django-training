from django import forms
from django.core import validators
from django.forms import HiddenInput, Textarea


def check_for_M(name):
    if name[0].lower() != 'm':
        raise forms.ValidationError("Name Should start with M")


class BasicForm(forms.Form):
    name = forms.CharField(validators=[check_for_M])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again")
    text = forms.CharField(widget=Textarea)
    botcatcher = forms.CharField(required=False, widget=HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

#    def clean_botcatcher(self):
#        botcatcher = self.cleaned_data['botcatcher']
#        if len(botcatcher):
#            raise forms.ValidationError("GOTCHA BOT!")
#        return botcatcher
    def clean(self):
        all_clean_data = super().clean()

        uemail = all_clean_data.get('email')
        vemail = all_clean_data.get('verify_email')

        if vemail!=uemail:
            raise forms.ValidationError("Emails don't match!")

