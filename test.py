from stix2.v20.sdo import AttackPattern, CourseOfAction
from stix2.utils import STIXdatetime

from mitre.attack.ics.mitre_attack_ics import MitreAttackICS
from domain.mitre.attack.attack_pattern_dto import AttackPatternDTO, SpecVersion

if __name__ == '__main__':
    mitre_attack_ics = MitreAttackICS()

    techniques: list[AttackPattern] = mitre_attack_ics.get_techniques()
    technique = techniques[0]

    # AttackPattern --> AttackPatternDTO

    print(technique.serialize(sort_keys=False, indent=4))

    # print("Created")
    # print(str(technique.get("created").replace(tzinfo=None).isoformat("T")) + "Z")
    # print(str(technique.get("created").microsecond).rstrip("0"))
    #
    # print("Modified")
    # print(str(technique.get("modified").isoformat("T")) + "Z")

    # attack_pattern_dto: AttackPatternDTO = AttackPatternDTO().parse_obj(technique.__dict__)
    attack_pattern_dto: AttackPatternDTO = AttackPatternDTO(spec_version=SpecVersion.field_2_0,
                                                            created=str(technique.get("created").replace(tzinfo=None)
                                                                        .isoformat("T")) + "Z",
                                                            modified=str(technique.get("modified").replace(tzinfo=None)
                                                                         .isoformat("T")) + "Z",
                                                            **technique.__dict__)

    print(attack_pattern_dto.json())

    mitigations: list[CourseOfAction] = mitre_attack_ics.get_mitigations()
    mitigation: CourseOfAction = mitigations[0]

    print(mitigation.serialize(sort_keys=False, indent=4))
