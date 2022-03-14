from django import forms
from .models import *
from django.utils.datastructures import MultiValueDict
from django.contrib.auth.forms import UserCreationForm


class ArrayFieldSelectMultiple(forms.CheckboxSelectMultiple):
    """This is a Form Widget for use with a Postgres ArrayField. It implements
    a multi-select interface that can be given a set of `choices`.

    You can provide a `delimiter` keyword argument to specify the delimeter used.

    """

    def __init__(self, *args, **kwargs):
        # Accept a `delimiter` argument, and grab it (defaulting to a comma)
        self.delimiter = kwargs.pop("delimiter", ",")
        super(ArrayFieldSelectMultiple, self).__init__(*args, **kwargs)

    def render_options(self, choices, value):
        # value *should* be a list, but it might be a delimited string.
        if isinstance(value, str):  # python 2 users may need to use basestring instead of str
            value = value.split(self.delimiter)
        return super(ArrayFieldSelectMultiple, self).render_options(choices, value)

    def value_from_datadict(self, data, files, name):
        if isinstance(data, MultiValueDict):
            # Normally, we'd want a list here, which is what we get from the
            # SelectMultiple superclass, but the SimpleArrayField expects to
            # get a delimited string, so we're doing a little extra work.
            return self.delimiter.join(data.getlist(name))
        return data.get(name, None)


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    type = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email", "type", "first_name", "last_name")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.type = self.cleaned_data['type']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user


class ClientMoreForm(forms.ModelForm):
    class Meta:
        model = ClientMore
        widgets = {
            'subscription': ArrayFieldSelectMultiple(choices=ClientMore.Subscriptions.choices),

            # 'boiler_data_shown': ArrayFieldSelectMultiple(choices=ClientMore.BOILER_DATA_CHOICES)
        }
        fields = '__all__'  # required for Django 3.x



class EmailForm(forms.Form):
    email = forms.EmailField(required=True)









