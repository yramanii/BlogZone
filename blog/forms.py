from blog.email import send_email
from django import forms
from .models import contact, createBlog # login
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout, Submit, ButtonHolder
from .tasks import send_mail_task

class contactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'fill this out',
                'First_Name',
                'Last_Name',
                'Email',
                'Description'
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button green')
            )
        )
    
    class Meta:

        model = contact
        fields = '__all__'

    def send_email(self):
        send_mail_task.delay(
            self.cleaned_data['First_Name'], self.cleaned_data['Email'], self.cleaned_data['Description'])


class blogForm(forms.ModelForm):

    class Meta:

        model = createBlog
        fields = ['input', 'author', 'title', 'image', 'file']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                
                'input',
                'author',
                'title',
                'image',
                'file',
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button green')
            )
        )
        
# class loginForm(forms.ModelForm):

#     class Meta:

#         model = login
#         fields = ['username', 'password']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             Fieldset(
#                 'fill this out',
#                 'username',
#                 'password',
#             ),
#         )
        
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class signupForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(signupForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class loginForm(UserCreationForm):

    class Meta:

        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'fill this out',
                'username',
                'password',
            ),
        )
        