from django import forms
from bandasApp.models import CadastroBandas


class CadastroBandasForm(forms.ModelForm):
    nomeBanda = forms.CharField(max_length=128, help_text="digite o nome da banda para cadastrar")
    tempoCarreira = forms.IntegerField(help_text="digite o tempo de carreira ex:1,2,3...")
    dataFundacao = forms.DateField(help_text="exemplo de data 1990-07-20")
    categoria = forms.CharField(max_length=128,help_text = 'exemplo rock,sertaneja')
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = CadastroBandas
        fields = ('nomeBanda',)


