from typing import List

from fastapi import APIRouter
from stix2.v20 import AttackPattern

from domain.mitre.attack.technique_dto import TechniqueDTO
from mitre.attack.converter.mitre_attack_converter import MitreAttackConverter
from mitre.attack.ics.mitre_attack_ics import MitreAttackICS

router = APIRouter()
mitre_attack_ics = MitreAttackICS()


@router.get("/techniques", tags=["Techniques"], response_model=List[TechniqueDTO])
def get_techniques() -> List[TechniqueDTO]:
    attack_patterns: list[AttackPattern] = mitre_attack_ics.get_techniques()

    techniques: List[TechniqueDTO] = []

    for attack_pattern in attack_patterns:
        attack_pattern_dto: TechniqueDTO = MitreAttackConverter.convert_attack_pattern(attack_pattern)
        techniques.append(attack_pattern_dto)

    return techniques
