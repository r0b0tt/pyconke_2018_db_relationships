from django.db import models

# One to One Relationship Models
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('N', 'Non-Binary'),
)


class Citizen(models.Model):
    """
    Model to store user details
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    id_number = models.CharField(max_length=50)
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Passport(models.Model):
    """
    Model to store passport details
    """
    passport_holder = models.OneToOneField(
        Citizen,
        on_delete=models.CASCADE,
        related_name='passport_citizen'
    )
    passport_number = models.CharField(max_length=100)
    date_issued = models.DateField(auto_now=True)
    expiry_date = models.DateField()

    def __str__(self):
        return '{}'.format(self.passport_number)


#  One to Many Relationship Models
class Customer(models.Model):
    """
    Model to store customer details
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Order(models.Model):
    """
    Model to store
    """
    order_number = models.CharField(max_length=100, unique=True)
    amount = models.IntegerField()
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='order_customer'
    )
