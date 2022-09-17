from flask import Flask, render_template, request, redirect, url_for

from base import Arena
from classes import unit_classes
from equipment import Equipment
from unit import PlayerUnit, EnemyUnit

app = Flask(__name__)

heroes = {}

arena = Arena()
equipment = Equipment()


@app.route("/")
def menu_page():
    """
    Главное меню
    """
    return render_template("index.html")


@app.route("/fight/")
def start_fight():
    """
    Экран боя
    """
    arena.start_game(player=heroes["player"], enemy=heroes["enemy"])
    return render_template("fight.html", heroes=heroes)


@app.route("/fight/hit")
def hit():
    """
    Кнопка удара, обновление экрана и
    при продолжении игры возвращает результат удара,
    иначе возвращает итоги игры
    """
    if arena.game_is_running:
        result = arena.player_hit()
    else:
        result = arena.battle_result()

    return render_template("fight.html", heroes=heroes, result=result)


@app.route("/fight/use-skill")
def use_skill():
    """
    Кнопка использования скилла, обновление экрана и
    при продолжении игры пропуск хода
    иначе возвращает итоги игры
    """
    if arena.game_is_running:
        result = arena.player_use_skill()
    else:
        result = arena.battle_result()

    return render_template("fight.html", heroes=heroes, result=result)


@app.route("/fight/pass-turn")
def pass_turn():
    """
    Кнопка пропуск хода, обновление экрана и
    при продолжении игры пропуск хода и переход хода
    сопернику иначе возвращает итоги игры
    """
    if arena.game_is_running:
        result = arena.next_turn()
    else:
        result = arena.battle_result()

    return render_template("fight.html", heroes=heroes, result=result)


@app.route("/fight/end-fight")
def end_fight():
    """
    Завершение игры и выход в главное меню
    """
    return render_template("index.html", heroes=heroes)


@app.route("/choose-hero/", methods=['post', 'get'])
def choose_hero():
    """
    Выбор героя
    """
    if request.method == "GET":
        result = {
            'classes': unit_classes,
            'weapons': equipment.get_weapons_names(),
            'armors': equipment.get_armors_names(),
            'header': "Выберите героя"
            }
        return render_template("hero_choosing.html", result=result)
    elif request.method == "POST":
        name = request.form['name']
        weapon_name = request.form['weapon']
        armor_name = request.form['armor']
        unit_class = request.form['unit_class']
        player = PlayerUnit(
            name=name,
            unit_class=unit_classes.get(unit_class)
            )
        player.equip_weapon(equipment.get_weapon(weapon_name))
        player.equip_armor(equipment.get_armor(armor_name))
        heroes['player'] = player

        return redirect(url_for('choose_enemy'))


@app.route("/choose-enemy/", methods=['post', 'get'])
def choose_enemy():
    """
    Выбор врага
    """
    if request.method == "GET":
        result = {
            'classes': unit_classes,
            'weapons': equipment.get_weapons_names(),
            'armors': equipment.get_armors_names(),
            'header': "Выберите противника"
        }
        return render_template("hero_choosing.html", result=result)
    elif request.method == "POST":
        name = request.form['name']
        weapon_name = request.form['weapon']
        armor_name = request.form['armor']
        unit_class = request.form['unit_class']
        enemy = EnemyUnit(
            name=name,
            unit_class=unit_classes.get(unit_class)
        )
        enemy.equip_weapon(equipment.get_weapon(weapon_name))
        enemy.equip_armor(equipment.get_armor(armor_name))
        heroes['enemy'] = enemy

        return redirect(url_for('start_fight'))


if __name__ == "__main__":
    app.run()
