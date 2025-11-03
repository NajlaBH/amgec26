from django import forms
from .models import AbstractSubmission

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div, Field
 
class AbstractSubmissionForm(forms.ModelForm):
    #document = forms.FileField(label="Abstract file", help_text="Please check your format before submission.")

    class Meta:
        model = AbstractSubmission
        fields = ['title', 'first_name', 'last_name', 'email', 'phone', 
        'institution','laboratory','presentation','subject','topic','document']

    def __init__(self, *args, **kwargs):
        super(AbstractSubmissionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id_abstrac_sub_form'
        self.helper.form_method = 'POST'
        self.helper.form_tag = True
        self.helper.enctype = 'multipart/form-data'
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('title', css_class='form-group col-md-3 mb-0', wrapper_class='custom-label-wrapper'),
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('phone', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('institution', css_class='form-group col-md-6 mb-0'),
                Column('laboratory', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('topic', css_class='form-group col-md-6 mb-0'),
                Column('subject', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('presentation', css_class='form-group col-md-4 mb-0'),
                Column('document', css_class='form-group col-md-6 mb-0',label="Abstract file", help_text="Please check your format before submission.",upload_to='documents/submissions/abstracts/'),
                css_class='form-row'
            ),
            Submit('submit', 'Submit', css_class='btn btn-primary mt-3')
        )
        self.helper.form_show_errors = True 