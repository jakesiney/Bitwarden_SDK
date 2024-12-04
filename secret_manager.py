from bitwarden_sdk import Bitwarden
from decouple import config

organization_id = config("organization_id")
access_token = config("access_token")


class SecretManager:
    def __init__(self, organization_id, access_token):
        self.organization_id = organization_id
        self.access_token = access_token
        self.bw = Bitwarden()

    def authenticate(self):
        self.bw.auth.login_access_token(self.access_token, self.organization_id)

    def get_secret(self, secret_key: str) -> str:
        secret = self.bw.get_secret(secret_key)
        return secret

    def save_secret(self, secret_key: str, secret_value: str):
        self.bw.save_secret(secret_key, secret_value)

secret_manager = SecretManager(organization_id, access_token)
secret_manager.authenticate()

