
from django.http import HttpResponse
from .models import Person, work
import threading
from django.db import transaction
import uuid

# Create your views here.
@transaction.non_atomic_requests
def hello(request):
    return HttpResponse("a simple crud app using django to access the app got to /task")
@transaction.non_atomic_requests
def todo(request):
    return HttpResponse("todo app")


@transaction.atomic
def createUser(request):
    request.method = "POST"
    print(f"thread id for user creation: {threading.get_ident()}")
    person = Person.objects.create(first_name="ashish", last_name="kumar")
    
    return HttpResponse(f"create user{person.first_name} {person.last_name}")

#Django’s default behavior is to run in autocommit mode. Each query is immediately committed to the database, unless a transaction is active. 
#Django uses transactions or savepoints automatically to guarantee the integrity of ORM operations that require multiple queries, especially delete() and update() queries.
#Django’s TestCase class also wraps each test in a transaction for performance reasons.
""" link to docs : https://docs.djangoproject.com/en/5.2/topics/db/transactions/"""

"""
A common way to handle transactions on the web is to wrap each request in a transaction. Set ATOMIC_REQUESTS to True in the configuration of each database for which you want to enable this behavior.

It works like this. Before calling a view function, Django starts a transaction. If the response is produced without problems, Django commits the transaction. If the view produces an exception, Django rolls back the transaction.

You may perform subtransactions using savepoints in your view code, typically with the atomic() context manager. However, at the end of the view, either all or none of the changes will be committed.



n practice, this feature wraps every view function in the atomic() decorator described below.

Note that only the execution of your view is enclosed in the transactions. Middleware runs outside of the transaction, and so does the rendering of template responses.
"""
@transaction.atomic
def createWork(request):
    request.method = "POST"
    #by default django donot provide a way to access the transaction id but we can create our own transaction id using uuid and attach to the transaction
    #and then we can use this transaction id to track the transaction in the database
    transaction_id = uuid.uuid4()
    def print_id():
        print(f"transaction id: {transaction_id}")
    work_obj = work.objects.create(title="Qt6", description="framework for building crossplateform apps", is_completed=False)
    transaction.on_commit(print_id)
    return HttpResponse(f"create work {work_obj.title} {work_obj.description} {work_obj.is_completed}")