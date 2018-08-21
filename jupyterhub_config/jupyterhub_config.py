# Configuration file for jupyterhub.
import os
import socket
# configuration for Auth0 authentication
from oauthenticator.auth0 import Auth0OAuthenticator
c.JupyterHub.authenticator_class = 'oauthenticator.auth0.Auth0OAuthenticator'
c.Auth0OAuthenticator.scope = ['openid','email']
c.Authenticator.whitelist = whitelist = set()
c.Authenticator.admin_users = admin = set()
c.JupyterHub.spawner_class = 'kubespawner.KubeSpawner'
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.hub_ip = '0.0.0.0'
c.JupyterHub.cleanup_servers = False
c.KubeSpawner.start_timeout = 60 * 5
c.KubeSpawner.image_spec = 'saurssaurav/fusesingleuser:latest'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
host_ip = s.getsockname()[0]
s.close()
c.KubeSpawner.hub_connect_ip = host_ip
c.JupyterHub.hub_connect_ip = c.KubeSpawner.hub_connect_ip
c.KubeSpawner.service_account = 'default'
#c.KubeSpawner.storage_pvc_ensure = False
c.JupyterHub.allow_named_servers = True

