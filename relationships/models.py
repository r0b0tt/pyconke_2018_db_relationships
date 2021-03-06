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
    id_number = models.CharField(max_length=50, unique=True)
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
    Model to store order details
    """
    order_number = models.CharField(max_length=100, unique=True)
    amount = models.IntegerField()
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='order_customer'
    )

    def __str__(self):
        return '{}-{}'.format(self.customer.first_name, self.amount)


# Many to Many Relationships
class Subject(models.Model):
    """
    Model to store subject details
    """
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name


class Student(models.Model):
    """
    Model to store student details
    """
    student_number = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    subjects = models.ManyToManyField(
        Subject,
        related_name='subject_students'
    )

    def __str__(self):
        return '{}: {}'.format(self.first_name, self.student_number)



