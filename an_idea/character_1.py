from Inventory import *

class Character:
    def __init__(self, name):
        self.name = name
        self.stats = {
            "strength": 10,
            "dexterity": 10,
            "intelligence": 10,
            "health": 100,
        }
        self.inventory = Inventory(parent=self)
        self.status_effects = []  # Each is a dict containing effect info

    def add_status_effect(self, name, duration, tag, on_tick=None, on_expire=None, on_apply=None):
        effect = {
            "name": name,
            "duration": duration,
            "tag": tag,
            "on_tick": on_tick,
            "on_expire": on_expire,
            "on_apply": on_apply
        }

        if on_apply:
            on_apply(self)

        self.status_effects.append(effect)
        print(f"{self.name} gains status: {name} ({duration} {tag})")

    def update_status_effects(self, tag_to_reduce):
        remaining_effects = []
        for effect in self.status_effects:
            if effect["tag"] == tag_to_reduce:
                if effect["on_tick"]:
                    effect["on_tick"](self)

                effect["duration"] -= 1

                if effect["duration"] <= 0:
                    if effect["on_expire"]:
                        effect["on_expire"](self)
                    print(f"{self.name}'s {effect['name']} expired.")
                    continue  # Effect ends

            remaining_effects.append(effect)
        self.status_effects = remaining_effects

    def print_status_effects(self):
        if not self.status_effects:
            print(f"{self.name} has no active status effects.")
            return
        print(f"{self.name}'s Status Effects:")
        for effect in self.status_effects:
            print(f" - {effect['name']} ({effect['duration']} {effect['tag']})")

    def print_stats(self):
        print(f"Stats for {self.name}:")
        for stat, value in self.stats.items():
            print(f" - {stat}: {value}")



#this would be a full file of effects
def poison_tick(character):
    dmg = 5
    character.stats["health"] -= dmg
    print(f"{character.name} takes {dmg} poison damage! Health now {character.stats['health']}.")

def poison_expire(character):
    print(f"{character.name} is no longer poisoned.")

def strength_buff_apply(character):
    character.stats["strength"] += 3
    print(f"{character.name}'s strength increases to {character.stats['strength']}!")

def strength_buff_expire(character):
    character.stats["strength"] -= 3
    print(f"{character.name}'s strength buff fades. Strength is now {character.stats['strength']}.")



if __name__ == "__main__":
    hero = Character("Eryn")

    hero.add_status_effect(
        name="Poison",
        duration=3,
        tag="combat round",
        on_tick=poison_tick,
        on_expire=poison_expire
    )
    
    hero.add_status_effect(
        name="Might",
        duration=2,
        tag="day",
        on_apply=strength_buff_apply,
        on_expire=strength_buff_expire
    )
    
    hero.print_status_effects()
    hero.print_stats()
    
    # Simulate a combat round and a day passing:
    print("\n-- Combat Round --")
    hero.update_status_effects("combat round")
    
    print("\n-- Day Passes --")
    hero.update_status_effects("day")
    