import os

from keystoneauth1.identity import v3
from keystoneauth1.session import Session
from keystoneclient.v3 import client as keystone_client



def create_admin_session():
    keystone_authtoken = {
        'auth_url': 'http://172.19.242.10:5000/v3',
        'username': 'admin',
        'password': 'V2VsY29tZTEyMw',
        'user_domain_name': 'Default',
        'project_name': 'admin',
        'project_domain_name': 'Default'
    }
    auth = v3.Password(**keystone_authtoken)
    return Session(auth=auth).get_token()

print(create_admin_session())
