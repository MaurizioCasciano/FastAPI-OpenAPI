from stix2 import TAXIICollectionSource, Filter
from stix2.v20.sdo import AttackPattern
from taxii2client.v20 import Collection

from mitre.attack.mitre_attack import MitreAttack


class MitreAttackICS(MitreAttack):

    def __init__(self):
        super().__init__()
        self.collection: Collection = next(filter(lambda c: c.title == "ICS ATT&CK", self.apiRoot.collections))
        self.source: TAXIICollectionSource = TAXIICollectionSource(self.collection)

    def get_techniques(self) -> list[AttackPattern]:
        return self.source.query([
            Filter('type', '=', 'attack-pattern'),
            Filter('kill_chain_phases.kill_chain_name', '=', 'mitre-ics-attack')
        ])
