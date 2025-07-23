def poison_tick(character):
    dmg = 5
    character.health -= dmg
    print(f"{character.name} takes {dmg} poison damage! Health now {character.health}.")

def poison_expire(character):
    print(f"{character.name} is no longer poisoned.")

def strength_buff_apply(character):
    character.stats["strength"] += 3
    print(f"{character.name}'s strength increases to {character.stats['strength']}!")

def strength_buff_expire(character):
    character.stats["strength"] -= 3
    print(f"{character.name}'s strength buff fades. Strength is now {character.stats['strength']}.")

def get_defualt_skills(character):
    character.add_skill("mining")
    character.add_skill("blacksmithing")  # uses default scaling