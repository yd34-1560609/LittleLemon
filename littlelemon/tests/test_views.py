from django.test import TestCase
from restaurant.models import Menu
class MenuViewTest(TestCase):
    
    def setup(self):
        Menu.objects.create(title="AAAA",price=99,inventory=12)
    
    def test_getall(self):
        items = Menu.objects.all()
        for item in items: 
            self.assertEqual(str(item), "AAAA : 99")