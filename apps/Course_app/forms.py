from django import forms
from apps.Course_app.models import CertificatesOfCourses
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.core.exceptions import ValidationError


class DocumentInquiryForm(forms.Form):
    doucoment_number = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "id": "body",
            "placeholder": "شماره مدرک را وارد کنید..."
        }
    ))

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    def clean(self):

        cd = self.cleaned_data

        doucoment_number = cd.get("doucoment_number")

        print(doucoment_number)

        if not CertificatesOfCourses.objects.filter(document_number=doucoment_number).exists():

            raise ValidationError("مدرکی با این شماره وجود ندارد!!!")


