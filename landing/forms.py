from django import forms


class IndexForm(forms.Form):
    my_text = forms.CharField()
    my_email = forms.EmailField()
    my_another_text = forms.CharField()
    my_text_area = forms.CharField(widget=forms.Textarea)
