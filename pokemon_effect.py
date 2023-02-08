"""
Type(18)	Strong Against	                    Weakness
Bug	        Grass, Dark, Psychic	            Fire, Flying, Rock
Dark	    Ghost, Psychic	                    Bug, Fairy, Fighting
Dragon	    Dragon	                            Dragon, Fairy, Ice
Electric	Flying, Water	                    Ground
Fairy	    Fighting, Dark, Dragon	            Poison, Steel
Fighting	Dark, Ice, Normal, Rock, Steel	    Fairy, Flying, Psychic
Fire	    Bug, Grass, Ice, Steel	            Ground, Rock, Water
Flying	    Bug, Fighting, Grass	            Electric, Ice, Rock
Ghost	    Ghost, Psychic	                    Dark, Ghost
Grass	    Ground, Rock, Water	                Bug, Fire, Flying, Ice, Poison
Ground	    Electric, Fire, Poison, Rock, Steel	Grass, Ice, Water
Ice	        Dragon, Flying, Grass, Ground	    Fighting, Fire, Rock, Steel
Normal	    --	                                Fighting
Poison	    Fairy, Grass	                    Ground, Psychic
Psychic	    Fighting, Poison	                Bug, Dark, Ghost
Rock	    Bug, Fire, Flying, Ice	            Fighting, Grass, Ground, Steel, Water
Steel	    Fairy, Ice, Rock	                Fighting, Fire, Ground
Water	    Fire, Ground, Rock	                Electric, Grass
"""

import random
import streamlit as st
import pandas as pd

# Pokemon Battle Simulator with Data Analytics


class Pokemon_Battle:
    def __init__(self, num_battles):
        self.my_pick = []
        self.oppPick = []
        self.outcome = []
        self.flipped_on = []
        self.num_battles = num_battles
        self.battle_data = {"Player Pick": self.my_pick,
                            "Opponent Pick": self.oppPick, "Battle Results": self.outcome, "Coin Flip": self.flipped_on}
        self.all_poke_type = ("BUG", "DARK", "DRAGON", "ELECTRIC", "FAIRY", "FIGHTING", "FIRE", "FLYING",
                              "GHOST", "GRASS", "GROUND", "ICE", "NORMAL", "POISON", "PSYCHIC", "ROCK", "STEEL", "WATER")

# Simulate and log battles
    def simulate_battles(self):
        for i in range(0, self.num_battles):
            mypoke = random.choice(self.all_poke_type)
            opppoke = random.choice(self.all_poke_type)
            battle = self.poke_battle(mypoke, opppoke)
            self.battle_data_add(battle)
        battle_data_frame = pd.DataFrame(self.battle_data)

        return self.display_data_table(battle_data_frame)


# Displays the Options

    def display_options(self):
        st.header("Pokemon Types:")
        st.write("""
        |Type(18)   | Strong Against	|   Weakness|
        | :-------- | :--------- | :---------|
        |Bug	    | Grass, Dark, Psychic	   |Fire, Flying, Rock|
        |Dark |Ghost, Psychic|Bug, Fairy, Fighting|
        |Dragon	|Dragon	 |Dragon, Fairy, |
        |Electric	|Flying, Water	|Ground|
        |Fairy	    |Fighting, Dark, Dragon	 | Poison, Steel |
        |Fighting | Dark, Ice, Normal, Rock, Steel	  |  Fairy, Flying, Psychic |
        |Fire	    | Bug, Grass, Ice, Steel	|Ground, Rock, Water |
        |Flying	    |Bug, Fighting, Grass	|Electric, Ice, Rock|
        |Ghost	    |Ghost, Psychic	  |Dark, Ghost |
        |Grass	    |Ground, Rock, Water |Bug, Fire, Flying, Ice, Poison |
        |Ground	    |Electric, Fire, Poison, Rock, Steel	|Grass, Ice, Water|
        |Ice	    |Dragon, Flying, Grass, Ground	   | Fighting, Fire, Rock, Steel|
        |Normal	    | -- | Fighting |
        |Poison	    |Fairy, Grass	 |Ground, Psychic |
        |Psychic	 |Fighting, Poison	|Bug, Dark, Ghost |
        |Rock	    |Bug, Fire, Flying, Ice	   |Fighting, Grass, Ground, Steel, Water|
        |Steel	    |Fairy, Ice, Rock	 |Fighting, Fire, Ground |
        |Water	   | Fire, Ground, Rock	 |Electric, Grass|
        """)
        st.write("#")

# Display Data Table for results
    def display_data_table(self, dataframe):
        st.table(dataframe)

# Add to Battle Dictionary
    def battle_data_add(self, battle):
        self.battle = battle
        self.my_pick.append(self.battle[0])
        self.oppPick.append(self.battle[1])
        self.outcome.append(self.battle[2])
        self.flipped_on.append(self.battle[3])

# Determines Out come and logs data
    def poke_battle(self, mypoke, opppoke):

        if mypoke == "BUG":
            result, coin_flip = self.poke_bug(opppoke)
        elif mypoke == "DARK":
            result, coin_flip = self.poke_dark(opppoke)
        elif mypoke == "DRAGON":
            result, coin_flip = self.poke_dragon(opppoke)
        elif mypoke == "ELECTRIC":
            result, coin_flip = self.poke_electric(opppoke)
        elif mypoke == "FAIRY":
            result, coin_flip = self.poke_fairy(opppoke)
        elif mypoke == "FIGHTING":
            result, coin_flip = self.poke_fighting(opppoke)
        elif mypoke == "FIRE":
            result, coin_flip = self.poke_fire(opppoke)
        elif mypoke == "FLYING":
            result, coin_flip = self.poke_flying(opppoke)
        elif mypoke == "GHOST":
            result, coin_flip = self.poke_ghost(opppoke)
        elif mypoke == "GRASS":
            result, coin_flip = self.poke_grass(opppoke)
        elif mypoke == "GROUND":
            result, coin_flip = self.poke_ground(opppoke)
        elif mypoke == "ICE":
            result, coin_flip = self.poke_ice(opppoke)
        elif mypoke == "NORMAL":
            result, coin_flip = self.poke_normal(opppoke)
        elif mypoke == "POISON":
            result, coin_flip = self.poke_poison(opppoke)
        elif mypoke == "PSYCHIC":
            result, coin_flip = self.poke_psychic(opppoke)
        elif mypoke == "ROCK":
            result, coin_flip = self.poke_rock(opppoke)
        elif mypoke == "STEEL":
            result, coin_flip = self.poke_steel(opppoke)
        elif mypoke == "WATER":
            result, coin_flip = self.poke_water(opppoke)
        else:
            st.text("An Error has occured with ", opppoke)

        battle = [mypoke, opppoke, result, coin_flip]
        return battle
# Win

    def poke_win(self):
        result = " WIN"
        coin_flip = False
        return result, coin_flip

# Lose
    def poke_lose(self):
        result = "LOSE"
        coin_flip = False
        return result, coin_flip

# Neutral Coin Flip
    def poke_neutral(self):
        coin = random.randint(1, 2)
        if coin == 1:
            result = " WIN"
        else:
            result = "LOSE"
        coin_flip = True
        return result, coin_flip


# Now going over 18 types and Outcome Functions considering Dragon, Ghost, and Normal

# Bug


    def poke_bug(self, opppoke):
        strength = ["GRASS", "DARK", "PSYCHIC"]
        weakness = ["FIRE", "FLYING", "ROCK"]
        if opppoke in strength:
            result, coin_flip = self.poke_win()
        elif opppoke in weakness:
            result, coin_flip = self.poke_lose()
        else:
            result, coin_flip = self.poke_neutral()
        return result, coin_flip

    # Dark

    def poke_dark(self, opppoke):
        strength = ["GHOST", "PSYCHIC"]
        weakness = ["BUG", "FAIRY", "FIGHTING"]
        if opppoke in strength:
            result, coin_flip = self.poke_win()
        elif opppoke in weakness:
            result, coin_flip = self.poke_lose()
        else:
            result, coin_flip = self.poke_neutral()
        return result, coin_flip

    # Dragon - Special case Dragon would be neutral

    def poke_dragon(self, opppoke):
        strength = ["DRAGON"]
        weakness = ["DRAGON", "FAIRY", "ICE"]
        if opppoke in strength:
            result, coin_flip = self.poke_neutral()
        elif opppoke in weakness:
            result, coin_flip = self.poke_lose()
        else:
            result, coin_flip = self.poke_neutral()
        return result, coin_flip

    # Electric

    def poke_electric(self, opppoke):
        strength = ["FLYING", "WATER"]
        weakness = ["GROUND"]
        if opppoke in strength:
            result, coin_flip = self.poke_win()
        elif opppoke in weakness:
            result, coin_flip = self.poke_lose()
        else:
            result, coin_flip = self.poke_neutral()
        return result, coin_flip

    # Fairy

    def poke_fairy(self, opppoke):
        strength = ["FIGHTING", "DARK", "DRAGON"]
        weakness = ["POISON", "STEEL"]
        if opppoke in strength:
            result, coin_flip = self.poke_win()
        elif opppoke in weakness:
            result, coin_flip = self.poke_lose()
        else:
            result, coin_flip = self.poke_neutral()
        return result, coin_flip

    # Fighting

    def poke_fighting(self, opppoke):
        strength = ["DARK", "ICE", "NORMAL", "ROCK", "STEEL"]
        weakness = ["FAIRY", "FLYING", "PSYCHIC"]
        if opppoke in strength:
            result, coin_flip = self.poke_win()
        elif opppoke in weakness:
            result, coin_flip = self.poke_lose()
        else:
            result, coin_flip = self.poke_neutral()
        return result, coin_flip

    # Fire

    def poke_fire(self, opppoke):
        strength = ["BUG", "GRASS", "ICE", "STEEL"]
        weakness = ["GROUND", "ROCK", "WATER"]
        if opppoke in strength:
            result, coin_flip = self.poke_win()
        elif opppoke in weakness:
            result, coin_flip = self.poke_lose()
        else:
            result, coin_flip = self.poke_neutral()
        return result, coin_flip

    # Flying

    def poke_flying(self, opppoke):
        strength = ["BUG", "FIGHTING", "GRASS"]
        weakness = ["ELECTRIC", "ICE", "ROCK"]
        if opppoke in strength:
            result, coin_flip = self.poke_win()
        elif opppoke in weakness:
            result, coin_flip = self.poke_lose()
        else:
            result, coin_flip = self.poke_neutral()
        return result, coin_flip

    # Ghost

    def poke_ghost(self, opppoke):
        strength = ["GHOST", "PSYCHIC"]
        weakness = ["DARK", "GHOST"]
        if opppoke in strength:
            if opppoke == "GHOST":
                result, coin_flip = self.poke_neutral()
            else:
                result, coin_flip = self.poke_win()
        elif opppoke in weakness:
            result, coin_flip = self.poke_lose()
        else:
            result, coin_flip = self.poke_neutral()
        return result, coin_flip

    # Grass

    def poke_grass(self, opppoke):
        strength = ["GROUND", "ROCK", "WATER"]
        weakness = ["BUG", "FIRE", "FLYING", "ICE", "POISON"]
        if opppoke in strength:
            result, coin_flip = self.poke_win()
        elif opppoke in weakness:
            result, coin_flip = self.poke_lose()
        else:
            result, coin_flip = self.poke_neutral()
        return result, coin_flip

    # Ground

    def poke_ground(self, opppoke):
        strength = ["ELECTRIC", "FIRE", "POISON", "ROCK", "STEEL"]
        weakness = ["GRASS", "ICE", "WATER"]
        if opppoke in strength:
            result, coin_flip = self.poke_win()
        elif opppoke in weakness:
            result, coin_flip = self.poke_lose()
        else:
            result, coin_flip = self.poke_neutral()
        return result, coin_flip

    # Ice

    def poke_ice(self, opppoke):
        strength = ["DRAGON", "FLYING", "GRASS", "GROUND"]
        weakness = ["FIGHTING", "FIRE", "ROCK", "STEEL"]
        if opppoke in strength:
            result, coin_flip = self.poke_win()
        elif opppoke in weakness:
            result, coin_flip = self.poke_lose()
        else:
            result, coin_flip = self.poke_neutral()
        return result, coin_flip

    # Normal - Does not have a strength

    def poke_normal(self, opppoke):
        weakness = ["FIGHTING"]
        if opppoke in weakness:
            result, coin_flip = self.poke_lose()
        else:
            result, coin_flip = self.poke_neutral()
        return result, coin_flip

    # Poison

    def poke_poison(self, opppoke):
        strength = ["FAIRY", "GRASS"]
        weakness = ["GROUND", "PSYCHIC"]
        if opppoke in strength:
            result, coin_flip = self.poke_win()
        elif opppoke in weakness:
            result, coin_flip = self.poke_lose()
        else:
            result, coin_flip = self.poke_neutral()
        return result, coin_flip

    # Psychic

    def poke_psychic(self, opppoke):
        strength = ["FIGHTING", "POISON"]
        weakness = ["BUG", "DARK", "GHOST"]
        if opppoke in strength:
            result, coin_flip = self.poke_win()
        elif opppoke in weakness:
            result, coin_flip = self.poke_lose()
        else:
            result, coin_flip = self.poke_neutral()
        return result, coin_flip

    # Rock

    def poke_rock(self, opppoke):
        strength = ["BUG", "FIRE", "FLYING", "ICE"]
        weakness = ["FIGHTING", "GRASS", "GROUND", "STEEL", "WATER"]
        if opppoke in strength:
            result, coin_flip = self.poke_win()
        elif opppoke in weakness:
            result, coin_flip = self.poke_lose()
        else:
            result, coin_flip = self.poke_neutral()
        return result, coin_flip

    # Steel

    def poke_steel(self, opppoke):
        strength = ["FAIRY", "ICE", "ROCK"]
        weakness = ["FIGHTING", "FIRE", "GROUND"]
        if opppoke in strength:
            result, coin_flip = self.poke_win()
        elif opppoke in weakness:
            result, coin_flip = self.poke_lose()
        else:
            result, coin_flip = self.poke_neutral()
        return result, coin_flip

    # Water

    def poke_water(self, opppoke):
        strength = ["FIRE", "GROUND", "ROCK"]
        weakness = ["ELECTRIC", "GRASS"]
        if opppoke in strength:
            result, coin_flip = self.poke_win()
        elif opppoke in weakness:
            result, coin_flip = self.poke_lose()
        else:
            result, coin_flip = self.poke_neutral()
        return result, coin_flip
