from django import forms
from .models import Formation


class FormationsForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ["title", "description", "video"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['description'].widget.attrs.update(
            {'class': 'w3-input w3-border w3-round w3-border-black'})
        self.fields['video'].widget.attrs.update(
            {'class': 'w3-input w3-round'})
        self.fields['title'].label = "Titre de la formation"
        self.fields['description'].label = "Description"
        self.fields['video'].label = "Fichier vidéo"
