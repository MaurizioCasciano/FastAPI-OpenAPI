from stix2.v20 import AttackPattern, CourseOfAction

from domain.mitre.attack.technique_dto import TechniqueDTO, SpecVersion as TechniqueSpecVersion
from domain.mitre.attack.mitigation_dto import MitigationDTO, SpecVersion as MitigationSpecVersion


class MitreAttackConverter:
    @staticmethod
    def convert_attack_pattern(attack_pattern: AttackPattern) -> TechniqueDTO:
        attack_pattern_dto: TechniqueDTO = TechniqueDTO(
            type=attack_pattern.get("type"),
            spec_version=TechniqueSpecVersion.field_2_0,
            created=str(attack_pattern.get("created").replace(tzinfo=None)
                        .isoformat("T")) + "Z",
            modified=str(attack_pattern.get("modified").replace(tzinfo=None)
                         .isoformat("T")) + "Z",
        )

        # attack_pattern_dto.spec_version = SpecVersion.field_2_0
        # attack_pattern_dto.type = attack_pattern.get("type")
        attack_pattern_dto.name = attack_pattern.get("name")
        attack_pattern_dto.description = attack_pattern.get("description")
        attack_pattern_dto.kill_chain_phases = attack_pattern.get("kill_chain_phases")
        attack_pattern_dto.external_references = attack_pattern.get("external_references")
        attack_pattern_dto.object_marking_refs = attack_pattern.get("object_marking_refs")
        # attack_pattern_dto.created = attack_pattern.get("created")
        attack_pattern_dto.created_by_ref = attack_pattern.get("created_by_ref")
        # attack_pattern_dto.modified = attack_pattern.get("modified")
        attack_pattern_dto.id = attack_pattern.get("id")
        # platforms
        attack_pattern_dto.x_mitre_platforms = attack_pattern.get("x_mitre_platforms")
        # data sources
        attack_pattern_dto.x_mitre_platforms = attack_pattern.get("x_mitre_data_sources")

        return attack_pattern_dto

    @staticmethod
    def convert_course_of_action(course_of_action: CourseOfAction) -> MitigationDTO:
        mitigation_dto: MitigationDTO = MitigationDTO(
            type=course_of_action.get("type"),
            spec_version=MitigationSpecVersion.field_2_0,
            created=str(course_of_action.get("created").replace(tzinfo=None)
                        .isoformat("T")) + "Z",
            modified=str(course_of_action.get("modified").replace(tzinfo=None)
                         .isoformat("T")) + "Z",
        )

        mitigation_dto.name = course_of_action.get("name")
        mitigation_dto.description = course_of_action.get("description")

        return mitigation_dto
