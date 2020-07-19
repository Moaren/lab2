from debug import *
from zoodb import *
import rpclib

def login(username, password):
    ## Fill in code here.
    with rpclib.client_connect('/authsvc/sock') as c:
        kwargs = {'username':username,'password':password}
        go = c.call('login',**kwargs)
        return go

def register(username, password):
    ## Fill in code here.
    with rpclib.client_connect('/authsvc/sock') as c:
        kwargs = {'username':username,'password':password}
        print "register kwargs=%s" % kwargs
        go = c.call('register',**kwargs)
        return go

def check_token(username, token):
    ## Fill in code here.
    with rpclib.client_connect('/authsvc/sock') as c:
        kwargs = {'username':username,'token':token}
        go = c.call('check_token',**kwargs)
        return go
