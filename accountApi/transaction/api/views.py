from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from transaction.models import Transaction
from transaction.api.serializers import TransactionSerializer, USerTransactionSerializer

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication


@api_view(['GET'])
def user_transaction(request, user_id):
    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,) 

    user_id = request.user.id
    print("user_id: ", user_id)
    if request.method == 'GET':
      user_account_detial = Transaction.objects.filter(
          user=user_id
      )
      serializer = USerTransactionSerializer(user_account_detial, many=True)
      return Response(serializer.data)


@api_view(['GET', 'POST'])
def transaction_list(request):

    if request.method == 'GET':
        transaction = Transaction.objects.all()
        serializer = TransactionSerializer(transaction, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HHTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def transaction_detail(request, pk):
    try:
        transaction = Transaction.objects.get(pk=pk)
    except Transaction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
       serializer = TransactionSerializer(transaction)
       return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HHTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)