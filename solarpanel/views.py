from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .models import Customer, Agents

from .forms import AddCustomerForm


@csrf_exempt
def loginPage(request):
    return render(request, "examples/pages/login.html")


@csrf_exempt
def loggedin(request):
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            template_name = 'user_registration/login.html'
            current_username = request.POST.get('username')
            current_password = request.POST.get('password')
            user = authenticate(username=current_username,
                                password=current_password)
            request.session['username'] = user.username
            Specific_User = User.objects.get(username=current_username)
            totaldriver = len(Driver.objects.all())
            context = {
                'foo': totaldriver
            }
            if user is not None:
                login(request, user)
                return render(request, 'examples/dashboard.html', context)
            else:
                print('User not found')
        else:
            context = {'LoginError': 'Please enter valid username or password'}
            return render(request, 'examples/pages/login.html', context)
    else:
        return render(request, 'examples/dashboard.html')"""
    return render(request, 'examples/dashboard.html')


def addcustomers(request):
    if request.method == 'POST':
        customer = Customer.objects.create(
            customer_name = request.POST['customer_name'],
            customer_address = request.POST['customer_address'],
            customer_phonenumber = request.POST['customer_phonenumber'],
            customer_Zipcode = request.POST['customer_zipcode'],
            agent = Agents.objects.get(id=request.user.id)
        )
        return redirect('loggedin')
    else:

        return render(request, 'examples/addCustomers.html')


@csrf_exempt
def customerdetails(request):
    if request.method == 'POST':
        total_kwh = int(request.POST['usage'])
        previous_total_price = int(request.POST['previous_total_cost'])
        current_price = int(request.POST['price'])
        years_since_proposal = int(request.POST['years_since_proposal'])
        price_per_kwh = previous_total_price / total_kwh
        current_total = current_price * total_kwh
        previous_savings = years_since_proposal * (previous_total_price - current_total)
        future_savings = 25 * (previous_total_price - current_total)
        context = {
            'previous_savings': previous_savings,
            'future_savings': future_savings
        }
        print(context)
        return render(request, 'examples/showadvantages.html', context)
    else:
        return render(request, 'examples/customerdetails.html')


@csrf_exempt
def customerList(request):
    customers = Customer.objects.filter(agent=Agents.objects.get(id=request.user.id))
    context ={
        'users':customers
    }
    return render(request, 'examples/customers.html', context)