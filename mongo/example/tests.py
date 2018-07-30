from django.test import TestCase
from .models import Example
import test_addons
# Create your tests here.
class ModelTestCase(test_addons.MongoTestCase):
    # A MongoTestCase needs this argument to use the test database
    allow_database_queries = True
    # creating a song in setup to run multiple tests with one object
    def setUp(self):
        self.old_count = Example.objects.count()
        self.object = Example.objects.create(nombre="An Object", servicio="9", ciudad="", fecha=None, total_factura=0.0)

    # deletion after tests are complete
    def tearDown(self):
        self.object.delete()
    # basic count test
    def test_model_can_create(self):
        new_count = Example.objects.count()
        self.assertNotEqual(self.old_count, new_count)
    """ The following two tests are included to ensure django ids and pks are not interfered in the djongo compiling. 
    See full doc for more on my experience with this """

    def test_model_has_id(self):
        self.assertIsNotNone(self.object.id)

    def test_model_has_pk(self):
        self.assertIsNotNone(self.object.pk)