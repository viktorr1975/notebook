from django import forms
from . import models


class CustomMMCF(forms.ModelMultipleChoiceField):
    ''' Customises the labels for checkboxes    '''
    pass
    def label_from_instance(self, member):
        return "% s" % member.name

class NoteForm(forms.ModelForm):
    class Meta:
        model = models.Notes
        fields = ["title", "content", "tags"]
        title = forms.CharField()
        content = forms.CharField(widget=forms.Textarea)
    tags = CustomMMCF(
        required=False,
        queryset=models.Tags.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
