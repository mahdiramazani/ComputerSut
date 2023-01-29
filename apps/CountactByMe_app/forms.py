from django import forms
from .models import ContactUs
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class CountactUsForm(forms.Form):

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)




