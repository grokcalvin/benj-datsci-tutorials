from dataclasses import dataclass
from typing import Dict, List
import random

# random.seed(1234)



@dataclass
class Player:
    name: str
    health: int
    damage: int


# class PlayerMove:
@dataclass
class Party:
    players: List[Player]


def pick_player(party: Party):
    key =  random.randrange(len(party.players))
    return party.players[key]

def player_party(player: Player, party: Party):
    return player in party.players


def player_died(player: Player, party: Party, all_players: list):
    if player.health <= 0:
        party.players = [p for p in party.players if p != player]

        all_players = [p for p in all_players if p != player]
    return party, all_players


@dataclass
class PlayerMove:
    me: Player

    def attack(self, them: Player):
        them.health = them.health - self.me.damage
  



def main():
    player1 = Player("calvin", 100, 10)
    player2 = Player("Banjo", 100, 10)
    player3 = Player("Owen", 100, 10)
    player4 = Player("Tess", 100, 10)
    party1 = Party(players=[player1, player2])
    party2 = Party(players=[player3, player4])

    all_players = party1.players + party2.players
    
    moves = 100
    for move_num in range(1, moves):
        if len(party1.players) == 0:
            print(f'Party 1 won!')
            break
        if len(party2.players) == 0:
            print(f'Party 2 won!')
            break
        for player in all_players:
    
            if player_party(player, party1):
                player_to_attack = pick_player(party2)
                move = PlayerMove(me=player)
                move.attack(them=player_to_attack)
                party1, all_players = player_died(player, party1, all_players)
            else:
                player_to_attack = pick_player(party1)
                move = PlayerMove(me=player)
                move.attack(them=player_to_attack)
                party2, all_players = player_died(player, party2, all_players)
            
        
            print(player_to_attack)


if __name__ == '__main__':
    main()

