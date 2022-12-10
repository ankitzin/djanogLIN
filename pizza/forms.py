from django import forms
from .models import Pizza

# class PizzaForm(forms.Form):
#     """ Dummy Pizza form using direct filed"""
#     topping1 = forms.CharField(label='topping 1', max_length=100)
#     topping2 = forms.CharField(label='topping 2', max_length=100)
#     topping3 = forms.CharField(label='topping 3', max_length=100)
#     size = forms.ChoiceField(label='Size', choices=[('Small','Small'), ('Medium', 'Medium'), ('Large', 'Large')])


class PizzaForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'topping3', 'size']
        labels = {'topping1': 'Topping 1', 'topping2': 'Topping 3', 'topping3': 'Topping 3'}
