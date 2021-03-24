from django import forms

class ContaktForm(forms.Form):
    user_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':('E-Mail')}), required=True, label='')
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':('Name')}), required=True, label='')
    betreff = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':('Betreff')}), required=True, label='')
    telefon = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':('Telefon')}), required=True, label='')
    nachricht = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':('Schreiben Sie uns eine Nachricht')}), required=True, label= '', max_length=3000)
