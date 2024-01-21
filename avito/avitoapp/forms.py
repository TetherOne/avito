from django import forms

from .models import Ad



class AdForm(forms.ModelForm):
    """

    Форма для создания объявления

    """
    class Meta:
        model = Ad
        fields = 'name', 'description', 'price', 'address', 'preview', 'phone'

    images = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"allow_multiple_selected": True}), required=False)



class AdSearchForm(forms.Form):
    """

    Форма для поиска объявления

    """
    search_term = forms.CharField(
        label='',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'style': 'width: 200px; height: 20px; border-radius: 3px;'})
    )