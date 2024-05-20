from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Sokak Adı', max_length=100, required=False)
    min_fiyat = forms.IntegerField(label='Min Fiyat', required=False)
    max_fiyat = forms.IntegerField(label='Max Fiyat', required=False)