from django import forms
from datetime import date
from .models import Subcategory, Type, Record, Category


class RecordAddForm(forms.ModelForm):
    date = forms.DateField(
        label='Дата',
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=date.today
    )
    type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        label='Тип',
        required=True,
        widget=forms.Select(attrs={'id': 'id_type'})
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Категория',
        required=True,
        widget=forms.Select(attrs={'id': 'id_category'})
    )

    class Meta:
        model = Record
        fields = ('name', 'amount', 'comment', 'status', 'date', 'type', 'category', 'subcategory')