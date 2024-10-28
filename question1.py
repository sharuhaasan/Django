## Question 1: By default are django signals executed synchronously or asynchronously? 

'By default, Django signals are executed synchronously.'
"In Django, when a signal is sent; it executes all registered receiver functions immediately and in the same flow of execution as the main process."

'''
The 'time.sleep(5)' call demonstrates that the signal handler blocks the execution of the main thread.
'post_save' signal triggers after a new User is created.
The signal handler 'signal_receiver' simulates a long-running task with time.sleep(5).
If Django signals were asynchronous, we would see "User creation completed" printed immediately.
Since Django signals are 'synchronous' by default, the "User creation completed" message will only print after the signal receiver completes its execution.
proving Django signals are synchronous nature.
If the signal were asynchronous, the time taken would be very short, as the caller would not wait for the signal handler.
'''
#code snippet:
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def signal_receiver(sender, instance, **kwargs):
    print("Signal received: Starting a long task")
    time.sleep(5)  
    print("Signal received: Task completed")

User.objects.create(username='user', password='password')
print("User creation completed")

