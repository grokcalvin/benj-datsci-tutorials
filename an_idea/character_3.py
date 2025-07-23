from effect_and_skill_functions import *
from Inventory import *
class Character:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.xp_threshold = 100
        self.xp_scaling_factor = 1.5

        self.stats = {
            "strength": 10,
            "dexterity": 10,
            "fortitude": 10
        }

        #update this so every level increases health and morewith more fortitude.
        self.max_health = 100 * (1+(0.1*((self.stats["fortitude"])-10)//2))
        self.health = self.max_health

        self.inventory = Inventory(parent=self)
        self.status_effects = []  # Each is a dict containing effect info
        self.skills = {}
        get_defualt_skills(self)

    # ================== Character XP & Leveling ==================

    def add_xp(self, amount):
        self.xp += amount
        while self.xp >= self.xp_threshold:
            self.xp -= self.xp_threshold
            self.level += 1
            self.xp_threshold = int(self.xp_threshold * self.xp_scaling_factor)
            print(f"🎉 {self.name} leveled up! Now level {self.level}")
            self.level_up_menu()

    def level_up_menu(self):
        Input = False
        while not Input:

            print("\n🔧 Choose a stat to increase:")
            stat_options = list(self.stats.keys())
            for i, stat in enumerate(stat_options, 1):
                print(f"{i}. {stat.capitalize()} ({self.stats[stat]})")
        
            choice = input("Enter number of stat to increase: ")
            try:
                index = int(choice) - 1
                if 0 <= index < len(stat_options):
                    chosen_stat = stat_options[index]
                    self.stats[chosen_stat] += 1
                    print(f"✅ {chosen_stat.capitalize()} increased to {self.stats[chosen_stat]}")
                    Input = True
                else:
                    print("⚠️ Invalid choice. No stat increased.")
            except ValueError:
                print("⚠️ Invalid input. No stat increased.")

    # ================== Skill System ==================

    def add_skill(self, skill_name, initial_threshold=50, scaling_factor=1.5):
        if skill_name not in self.skills:
            self.skills[skill_name] = {
                "xp": 0,
                "level": 1,
                "threshold": initial_threshold,
                "scaling_factor": scaling_factor
            }

    def add_skill_xp(self, skill_name, xp_amount):
        if skill_name not in self.skills:
            print(f"Skill '{skill_name}' not found. Add it first with add_skill().")
            return

        skill = self.skills[skill_name]
        skill["xp"] += xp_amount

        while skill["xp"] >= skill["threshold"]:
            skill["xp"] -= skill["threshold"]
            skill["level"] += 1
            skill["threshold"] = int(skill["threshold"] * skill["scaling_factor"])
            print(f"🔼 {self.name} leveled up {skill_name}! Now level {skill['level']}.")

    def get_skill_info(self, skill_name):
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

    # ================== Status Effect System ==================

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
                    continue

            remaining_effects.append(effect)
        self.status_effects = remaining_effects

    def print_status_effects(self):
        if not self.status_effects:
            print(f"{self.name} has no active status effects.")
            return
        print(f"{self.name}'s Status Effects:")
        for effect in self.status_effects:
            print(f" - {effect['name']} ({effect['duration']} {effect['tag']})")

    # ================== Utility ==================

    def print_stats(self):
        print(f"\n📊 Stats for {self.name} (Level {self.level})")
        for stat, value in self.stats.items():
            print(f" - {stat.capitalize()}: {value}")
        print(f"XP: {self.xp} / {self.xp_threshold}")

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
    char.add_xp(100)