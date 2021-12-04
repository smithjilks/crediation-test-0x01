from django.test import TestCase
from . models import User
from uuid import uuid4


class UserTest(TestCase):
        """Tests the user model"""

        def setUp(self):
                id = str(uuid4())
                User.objects.create(firstname="first_name", lastname="last_name", email="test@test.com", id=id)

                id2 = str(uuid4())
                User.objects.create(firstname="first_name", lastname="last_name", email="test2@test.com", id=id2)

        def test_instance(self):
                """Test instance of class"""
               
                user =  User.objects.get(email="test@test.com")
                self.assertIsInstance(user, User)
        
        def test_uuid(self):
                """Tests that UUID is unique everytime it is created"""

                field_name = 'id'

                user =  User.objects.get(email="test@test.com")
                user2 = User.objects.get(email="test2@test.com")

                field_object = User._meta.get_field(field_name)
                user_id = field_object.value_from_object(user)
                user2_id = field_object.value_from_object(user2)


                self.assertNotEquals(user_id, user2_id)
