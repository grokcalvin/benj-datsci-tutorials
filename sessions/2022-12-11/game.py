from inventory_entities import Inventory, HealthIncrease
from player_entities import make_elf, make_goblin, make_human


def main():
    elf = make_elf(level=3)
    apple = HealthIncrease(
        name="apple",
        health_amount=10,
        quantity=1
    )
    print(elf.health)
    elf.health -= 50
    print(elf.health)
    elf = apple.action(elf)
    print(elf.health)



if __name__ == '__main__':
    main()
