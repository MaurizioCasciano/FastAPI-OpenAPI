from typing import List

from fastapi import APIRouter
from stix2.v20 import AttackPattern, CourseOfAction

from domain.mitre.attack.mitigation_dto import MitigationDTO
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
        technique_dto: TechniqueDTO = MitreAttackConverter.convert_attack_pattern(attack_pattern)
        techniques.append(technique_dto)

    return techniques


@router.get("/mitigations", tags=["Mitigations"], response_model=List[MitigationDTO])
def get_mitigations() -> List[MitigationDTO]:
    course_of_actions: list[CourseOfAction] = mitre_attack_ics.get_mitigations()

    mitigations_dto: List[MitigationDTO] = []

    for course_of_action in course_of_actions:
        mitigation_dto: MitigationDTO = MitreAttackConverter.convert_course_of_action(course_of_action)
        mitigations_dto.append(mitigation_dto)

    return mitigations_dto
