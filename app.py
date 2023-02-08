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

import streamlit as st
import pandas as pd
from PIL import Image
from pathlib import Path
from pokemon_effect import *

# started as a list but changed to a tuple since the content never changes for better memory allocation.
# changed to a set as the order does not matter for the way I'm using to check for values which didn't work so went back to tuple


# pokegame()

# --- Path Settings ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- General Settings ---
PAGE_TITLE = "Pokemon Battle Simulator with Data Analytics | Gerald Fleming"
PAGE_ICON = "💊"
Name = "Gerald Fleming"
DESCRIPTION = """
Pokemon Battle Simulator with Data Analytics
"""
EMAIL = "geraldfleming04@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/gerald-fleming-07909890/",
    "GitHub": "https://github.com/Gdog12g4",
}
PROJECTS = {
    "✂️Pokemon Type Game": "https://github.com/Gdog12g4/Pokemon_Type_Game",
    "✂️Placeholder2": "link2",
    "✂️Placeholder3": "link3",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- Load CSS, PDF & Profile Pic ---
with open(css_file) as f:
    st.markdown("<style>{}</style".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- Options ---
st.title(DESCRIPTION)
st.write('#')


num_battles = st.number_input(
    'Enter number of simulated battles: \n(MAX - 10000)', min_value=0, max_value=10000, value=0)

# sets game
lets_battle = Pokemon_Battle(num_battles)

# Simulates Battles and logs them
lets_battle.simulate_battles()

# displays rules
lets_battle.display_options()


st.write('#')
st.write('#')
st.write("---")

col3, col4 = st.columns(2, gap="small")
with col3:
    st.image(profile_pic, width=260)

with col4:
    st.header(Name)

    st.download_button(
        label=":clipboard: Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("✉️", EMAIL)

# --- SOCIAL LINKS ---
st.write("#")  # empty paragraph
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- Projects & Acomplishments ---
st.write("#")
st.subheader("📂**Projects & Accomplishments**")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
