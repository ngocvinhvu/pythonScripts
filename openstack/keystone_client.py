import os

from keystoneauth1.identity import v3
from keystoneauth1.session import Session
from keystoneclient.v3 import client as keystone_client



def create_admin_session():
    keystone_authtoken = {
        'auth_url': '',
        'username': '',
        'password': '',
        'user_domain_name': 'Default',
        'project_name': 'admin',
        'project_domain_name': 'Default'
    }
    auth = v3.Password(**keystone_authtoken)
    return Session(auth=auth).get_token()

print(create_admin_session())
