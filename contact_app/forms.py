from django import forms

class ContaktForm(forms.Form):
    user_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':('Ihr Email')}), required=True, label='')
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':('Ihr Name')}), required=True, label='')
    betreff = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':('Betreff')}), required=True, label='')
    nachricht = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':('Schreiben Sie mir eine Nachricht')}), required=True, label= '', max_length=3000)
