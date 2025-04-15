"""
Django includes a “signal dispatcher” which helps decoupled applications get notified when actions occur elsewhere in the framework. In a nutshell, signals allow certain senders to notify a set of receivers that some action has taken place. They’re especially useful when many pieces of code may be interested in the same events.
"""
"""
django signals are used when you want to perform some action after a certain event has occurred. For example, you might want to send an email after a user registers, or log an action after a model instance is saved.
You can use signals to decouple your code and make it more modular. Instead of having to write code that directly
interacts with the event, you can create a signal and connect it to a receiver function that will handle the event.
"""

"""
like for example you want to see if an user  is created than normally what will you do is fire a request to see if user is created or not and then you will do the action but with signals you can just connect the signal to the receiver function and it will automatically fire when the event occurs.
also it saves you from writing the same code again and again for different events. or here in particular different type of user creation. maybe you want to send a mail or something everytime a user is created.
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Person, work
import time
import threading
from django.db import connection
from django.db import transaction

#by default django signals are synchronous and blocking means untill one signal is not completed exectuing it 
#won't move to the next signal 
#too observe the blocking and synchronous nature of signals in django i used time.sleep() so we can observe it happening 
#to head over to the 127.0.0.1:8000/user as by at this endpoint we are creating the user and firing the signals


@receiver(post_save, sender=Person)
def message_1(sender,instance,created,**kwargs):
    time.sleep(10)
    #by comparing the thread id of both the view and signal we can confirm that the running on same thread that is 
    #same thread as the caller 
    
    print(f"thread id for signal: {threading.get_ident()}")
    if created:
        print("msg1")
    else:
        print("msg1 else part")

@receiver(post_save, sender=Person)
def message_2(sender,instance,created,**kwargs):
    time.sleep(10)
    if created:
        print("msg2")
    else:
        print("msg2 else part")

@receiver(post_save, sender=Person)
def message_3(sender,instance,created,**kwargs):
    time.sleep(10)
    if created:
        print("msg3")
    else:
        print("msg3 else part")

@receiver(post_save, sender=Person)
def message_4(sender,instance,created,**kwargs):
    time.sleep(10)
    if created:
        print("msg4")
    else:
        print("msg4 else part")

@receiver(post_save, sender=Person)
def message_5(sender,instance,created,**kwargs):
    time.sleep(10)
    if created:
        print("msg5")
    else:
        print("msg5 else part")


#signal reciver for creatework
@receiver(post_save, sender=work)
def check_work(sender,instance,created,**kwargs):
    print("we are inside a transaction:", connection.in_atomic_block)
    
"""
django does not provide any way to access the transaction id 
but as we know that our signal above is for the view creatework 
the transaction is same as the view transaction

"""