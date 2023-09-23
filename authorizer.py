from abc import ABC, abstractmethod

class Authorizer(ABC):

    @abstractmethod
    def authorize(self):
        pass

class AuthorizationError(Exception):
    def __init__(self, message):
        super().__init__(message)

class SMSAuthorizer(Authorizer):

    def authorize(self):
        # TODO: figure out why this prevents reviewing but still prints review submitted successfully
        raise AuthorizationError("Not authorized to post review")