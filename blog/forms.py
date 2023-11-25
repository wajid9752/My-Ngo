from django import forms 
from .models import Contact,Volunteer




class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "phone_number", "email", "subject", "message"]

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        # Set the 'required' attribute for mandatory fields
        self.fields['name'].required = True
        self.fields['phone_number'].required = True
        self.fields['message'].required = True

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ["name", "phone_number","age", "email", "address","skills", "message"]

  



