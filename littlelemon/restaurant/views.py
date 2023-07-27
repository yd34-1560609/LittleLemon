from django.shortcuts import render
from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer


# Create your views here.
def index(request):
    return render(request, 'index_ll.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer