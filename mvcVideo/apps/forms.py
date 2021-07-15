from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'


class FechasForm(forms.Form):
    fechaInicio = forms.DateField(
        required=True, label='Fecha Inicial', widget=DateInput)
    fechaFin = forms.DateField(
        required=True, label='Fecha Final', widget=DateInput)
