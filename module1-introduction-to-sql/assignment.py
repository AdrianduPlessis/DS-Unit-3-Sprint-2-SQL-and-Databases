import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
cur = conn.cursor()


def question1():
    """How many total Characters are there?"""
    query = "SELECT COUNT(*) FROM charactercreator_character"
    result = cur.execute(query).fetchone()[0]
    print(f' There are {result} characters\n')


def question2():
    """How many of each specific subclass?"""
    subclasses = ['cleric', 'fighter', 'mage', 'necromancer', 'thief']
    for subclass in subclasses:
        query = f"SELECT COUNT(*) FROM charactercreator_{subclass}"
        count = cur.execute(query).fetchone()[0]
        print(f'There are {count} {subclass} type characters.')

    result = cur.execute(query).fetchone()


def question3():
    """How many total Items?"""
    query = "SELECT COUNT(*) FROM armory_item"
    result = cur.execute(query).fetchone()[0]
    print(f'\nTotal items:\t\t{result}\n')


def question4():
    """How many of the Items are weapons? How many are not?"""
    items = cur.execute("SELECT COUNT(*) FROM armory_item").fetchone()[0]
    weapons = cur.execute("SELECT COUNT(*) FROM armory_weapon").fetchone()[0]
    non_weapon_items = items - weapons
    print(f'Weapon items:\t\t{weapons}')
    print(f'Non-weapon items:\t{non_weapon_items}')


def question5():
    """How many Items does each character have? (Return first 20 rows)"""
    query = "SELECT character_id FROM charactercreator_character"
    characters = cur.execute(query).fetchall()

    for character in characters:
        query_weapons = """SELECT * FROM character_inventory"""



def question6():
    """How many Weapons does each character have? (Return first 20 rows)"""
    query = "SELECT COUNT(*) FROM charactercreator_character"
    result = cur.execute(query).fetchone()
    print(result[0])


def question7():
    """On average, how many Items does each Character have?"""
    query = "SELECT COUNT(*) FROM charactercreator_character"
    result = cur.execute(query).fetchone()
    print(result[0])


def question8():
    """On average, how many Weapons does each character have?"""
    query = "SELECT COUNT(*) FROM charactercreator_character"
    result = cur.execute(query).fetchone()
    print(result[0])


question1()
question2()
question3()
question4()
question5()