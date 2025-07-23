from Inventory import *
from effect_and_skill_functions import *
class Character:
    def __init__(self, name):
        self.name = name
        self.stats = {
            "strength": 10,
            "dexterity": 10,
            "fortitude": 10,
            "health": 100,
        }
        self.inventory = Inventory(parent=self)
        self.status_effects = []  # Each is a dict containing effect info
        self.skills = {}
        get_defualt_skills(self)

    def add_skill(self, skill_name, initial_threshold=50, scaling_factor=1.5):
        """Adds a new skill with a name, XP threshold, and a scaling function."""
        if skill_name not in self.skills:
            self.skills[skill_name] = {
                "xp": 0,
                "level": 1,
                "threshold": initial_threshold,
                "scaling_factor": scaling_factor
            }

    def add_skill_xp(self, skill_name, xp_amount):
        """Adds XP to a skill and handles level-ups using its scaling function."""
        if skill_name not in self.skills:
            print(f"Skill '{skill_name}' not found. Add it first with add_skill().")
            return

        skill = self.skills[skill_name]
        skill["xp"] += xp_amount

        # Handle level-up loop
        while skill["xp"] >= skill["threshold"]:
            skill["xp"] -= skill["threshold"]
            skill["level"] += 1
            skill["threshold"] = skill["scaling_factor"] *skill["threshold"]
            print(f"🔼 {self.name} leveled up {skill_name}! Now level {skill['level']}.")

    def get_skill_info(self, skill_name):
        """Returns a summary of a skill."""
        if skill_name in self.skills:
            skill = self.skills[skill_name]
            return {
                "level": skill["level"],
                "xp": skill["xp"],
                "threshold": skill["threshold"]
            }
        else:
            return None

    def print_skills(self):
        print(f"\n🛠️  {self.name}'s Skills:")
        for name, info in self.skills.items():
            print(f"  • {name}: Level {info['level']} ({info['xp']} / {info['threshold']} XP)")

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
    

    char = Character("Elric")

    # Add some skills with optional scaling functions
    char.add_skill("mining", initial_threshold=50, scaling_factor=1.5)
    char.add_skill("blacksmithing")  # uses default scaling

    # Add XP
    char.add_skill_xp("mining", 80)
    char.add_skill_xp("blacksmithing", 120)

    # Check skill state
    char.print_skills()