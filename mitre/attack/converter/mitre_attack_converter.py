from stix2.v20 import AttackPattern

from domain.mitre.attack.attack_pattern_dto import AttackPatternDTO, SpecVersion, Timestamp


class MitreAttackConverter:
    @staticmethod
    def convert_attack_pattern(attack_pattern: AttackPattern) -> AttackPatternDTO:
        attack_pattern_dto: AttackPatternDTO = AttackPatternDTO(
            type=attack_pattern.get("type"),
            spec_version=SpecVersion.field_2_0,
            created=str(attack_pattern.get("created").replace(tzinfo=None)
                        .isoformat("T")) + "Z",
            modified=str(attack_pattern.get("modified").replace(tzinfo=None)
                         .isoformat("T")) + "Z",
        )

        attack_pattern_dto.spec_version = SpecVersion.field_2_0
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
        # data sources

        return attack_pattern_dto
