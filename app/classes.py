from dataclasses import dataclass

from app.skills import Skill


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass = UnitClass('Воин', 60.0, 30.0, 0.8, 0.9, 1.2, {'Свирепый пинок': {'stamina': 6, 'damage': 12}})

ThiefClass = UnitClass('Вор', 50.0, 25.0, 1.5, 1.2, 1.0, {'Мощный укол': {'stamina': 5, 'damage': 15}})

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}
