from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True)
    email = forms.EmailField(label="Email", required=True)
    mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea(), required=True)