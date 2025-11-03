from django import forms
from .models import Contact

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div
 
class ASKfrom(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'demande','message']
 
    def __init__(self, *args, **kwargs):
        super(ASKfrom, self).__init__(*args, **kwargs)
 
        self.helper = FormHelper()
        self.helper.form_id = 'id_ask_form'
        self.helper.form_method = 'POST'
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Div(
                #Div('first_name', 'last_name', css_class='col-md-6'),
                #Div('email', 'phone', css_class='col-md-6'),
                #Div('demande', css_class='col-md-6'),
                Div('first_name', 'last_name', 'email', 'phone', css_class='col-md-6'),
                Div('demande','message', css_class='col-md-6'), css_class='row'
            ),
            Div(
                Div(Submit('save', 'SEND'), css_class='col-md-12'), css_class='topicsidebarbtn'
            )
        )
        self.helper.form_show_errors = True 

