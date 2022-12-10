from django.shortcuts import render
from .forms import PizzaForm


# Create your views here.
def home(request):
    return render(request, 'pizza/home.html', {"key":"value"})


def order(request):
    if request.method == "POST":
        filled_form = PizzaForm(request.POST, request.FILES)
        if filled_form.is_valid():
            note = 'Thanks for Ordering Pizza with toppings %s, %s, %s of size %s. The order is on its way.' % \
                   (filled_form.cleaned_data['topping1'], filled_form.cleaned_data['topping2'],
                    filled_form.cleaned_data['topping3'], filled_form.cleaned_data['size'])
            new_pizza_form = PizzaForm()
            return render(request, 'pizza/order.html', {"pizza_form": new_pizza_form, "note":note})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {"pizza_form": form})

