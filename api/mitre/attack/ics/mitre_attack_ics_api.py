from typing import List

from fastapi import APIRouter
from stix2.v20 import AttackPattern

from domain.mitre.attack.attack_pattern_dto import AttackPatternDTO, Type
from mitre.attack.converter.mitre_attack_converter import MitreAttackConverter
from mitre.attack.ics.mitre_attack_ics import MitreAttackICS

router = APIRouter()
mitre_attack_ics = MitreAttackICS()


@router.get("/techniques", tags=["Techniques"], response_model=List[AttackPatternDTO])
def get_techniques() -> List[AttackPatternDTO]:
    attack_patterns: list[AttackPattern] = mitre_attack_ics.get_techniques()

    techniques: List[AttackPatternDTO] = []

    for attack_pattern in attack_patterns:
        attack_pattern_dto: AttackPatternDTO = MitreAttackConverter.convert_attack_pattern(attack_pattern)
        techniques.append(attack_pattern_dto)

    return techniques
