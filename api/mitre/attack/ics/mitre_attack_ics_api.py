from fastapi import APIRouter
from stix2.v20 import AttackPattern

from mitre.attack.ics.mitre_attack_ics import MitreAttackICS

router = APIRouter()
mitre_attack_ics = MitreAttackICS()


@router.get("/techniques", tags=["Techniques"], response_model=list[AttackPattern])
def get_techniques() -> list[AttackPattern]:
    techniques: list[AttackPattern] = mitre_attack_ics.get_techniques()

    return techniques