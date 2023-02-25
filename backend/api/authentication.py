# setting up authentication as a class in it's own file so it's easier to import and use

from rest_framework.authentication import TokenAuthentication as BaseTokenAuth

class TokenAuthentication(BaseTokenAuth):
    keyword = 'Token'