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


WarriorClass = UnitClass('Армен', 100.0, 70.0, 5.0, 3.0, 2.0, '') # TODO Инициализируем экземпляр класса UnitClass и присваиваем ему необходимые значения аттрибуотов

ThiefClass = UnitClass('Давид', 100.0, 70.0, 5.0, 3.0, 2.0, '') # TODO действуем так же как и с войном

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}