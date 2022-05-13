from django.shortcuts import render
from account.models import Account
from user.models import User
from transaction.models import Transaction

import csv
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'adminView/index.html')

def detail(request):
    pk = request.POST['userId']
    user = User.objects.get(id=pk)
    accounts = Account.objects.filter(user=user.id)
    transactions = Transaction.objects.filter(user=user)

    context = {
        'user' : user,
        'accounts': accounts,
        'transactions' : transactions
    }
    return render(request, 'adminView/detail.html', context)

def csvReport(request, pk):
    headerAccount = ['ID', 'USER ID', 'TYPE', 'AMOUNT']
    headerTransaction = ['ID', 'USER ID', 'ACTION', 'AMOUNT']
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=report.csv'
    print(pk)
    user = User.objects.get(id=pk)
    accounts = Account.objects.filter(user=user.id)
    
    writer = csv.writer(response)
    writer.writerow(headerAccount)

    for account in accounts:
        writer.writerow([account.id, account.user,  account.type, account.amount])
    
    transactions = Transaction.objects.filter(user=user)
    writer.writerow([])
    writer.writerow([])

    writer.writerow(headerTransaction)

    for transaction in transactions:
        writer.writerow([transaction.id, transaction.user, transaction.action, transaction.amount])

    return response