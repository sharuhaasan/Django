## Question 3: By default do django signals run in the same database transaction as the caller?

'Yes, by default Django signals run in the same database transaction as the caller.'
'This means that if the signal handler raises an exception, the original database transaction will be rolled back.'
'''
'transaction.get_autocommit()' checks if the code is running within a transaction (False means its inside a transaction).
'User.objects.create(username='user', password='password')' within an 'atomic' block, ensuring a database transaction.
When the signal executes, it will print whether its running within the transaction or outside the transaction. 
Since Django signals run in the same transaction by default, we will see "Signal running within the same transaction" in the output.
If the signal ran in a separate transaction, the user creation would not roll back.
'''

#code snippet:
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import transaction

@receiver(post_save, sender=User)
def signal_receiver(sender, instance, **kwargs):
    if transaction.get_autocommit():
        print("Signal running outside of a transaction")
    else:
        print("Signal running within the same transaction")

with transaction.atomic():
    User.objects.create(username='user', password='password')
