## Question 2: Do django signals run in the same thread as the caller?

'Yes, Django signals run in the same thread as the caller by default.'
'This means they do not spawn new threads unless explicitly configured to do so.'
'''
'signal_receiver' prints the current thread's name when the signal executes.
By comparing the thread name in the main execution to the thread name in the signal receiver, we can confirm if they are the same.
If signals were executed in a 'different' thread, the thread names would differ.
Since Django signals are synchronous and run in the same thread as the caller, the thread names will match.
'''

#code snippet:
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading

@receiver(post_save, sender=User)
def signal_receiver(sender, instance, **kwargs):
    print(f"Signal running in thread: {threading.current_thread().name}")

print(f"Main function running in thread: {threading.current_thread().name}")
User.objects.create(username='user', password='password')
