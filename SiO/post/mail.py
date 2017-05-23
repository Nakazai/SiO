from anymail.message import attach_inline_image_file
from django import forms

from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Div, HTML, \
    Field, Submit
from crispy_forms.bootstrap import FormActions


class mailHandler(forms.Form):
    subject = forms.CharField(required=False)
    receiver = forms.EmailField(label='Send to')
    # cc = forms.EmailField(label='Send via Cc', required=False)
    # bcc = forms.EmailField(label='Send via Bcc', required=False)
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 50}),
                              required=False)

    def __init__(self, *args, **kwargs):
        super(mailHandler, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form'
        self.helper.layout = Layout(
            Field(
                None,
                Div(
                    HTML('''
                           {% if messages %}
                           {% for message in messages %}
                           <center><p {% if message.tags %}
                           class="alert alert-{{ message.tags }}"
                           {% endif %}>{{ message }}
                           <button type="button" name="message" class="close" data-dismiss="alert" aria-hidden="true">&times;</button></p>
                           </center>{% endfor %}{% endif %}
                            '''),
                    Div('subject',
                        Field('receiver', placeholder='Email address',
                              required=True),
                        # Field('cc', placeholder='Email address',
                        #       ),
                        # Field('bcc', placeholder='Email address',
                        #       ),
                        'message',
                        FormActions(
                            Submit('submit', 'Send', css_class='btn btn-lg btn-block'),

                        ),
                        ),
                ),
            ),
        )
