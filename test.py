from stix2.v20.sdo import AttackPattern

from mitre.attack.ics.mitre_attack_ics import MitreAttackICS

if __name__ == '__main__':
    mitre_attack_ics = MitreAttackICS()

    techniques: list[AttackPattern] = mitre_attack_ics.get_techniques()
    technique = techniques[0]

    print(technique.serialize(sort_keys=True, indent=4))
    # print(technique.object_properties())
    # print(technique.properties)
