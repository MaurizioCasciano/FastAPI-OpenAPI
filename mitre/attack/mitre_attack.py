from taxii2client.v20 import Server
from taxii2client.v20 import ApiRoot

from mitre.attack.config import MITRE_ATTACK_TAXII_SERVER


class MitreAttack:
    def __init__(self):
        self.server: Server = Server(MITRE_ATTACK_TAXII_SERVER)
        self.apiRoot: ApiRoot = self.server.api_roots[0]
