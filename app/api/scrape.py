import requests as r
import pandas as pd
import datetime
from bs4 import BeautifulSoup
from sqlalchemy import create_engine

def getSpecies():
    my_data = r.get('https://expeditionary-force-by-craig-alanson.fandom.com/wiki/Category:Species')
    soup = BeautifulSoup(my_data.content, "html.parser")
    species_list = []
    g_findmembers = soup.find_all("a", class_="category-page__member-link")
    #print(soup)
    #g_indmembers = g_findmembers.find
    #print(g_findmembers[1].get_text())
    for x in g_findmembers:
        if x.get_text() == 'Military Ranks' or x.get_text() == 'Known Species in ExForce':
            continue
        species_list.append(x.get_text())
    #print(species_list)
    return species_list




def scrapinTime_SpeciesPage(species_list):
    for x in species_list:
        print(x)
        my_data = r.get(f'https://expeditionary-force-by-craig-alanson.fandom.com/wiki/{x}')
        soup = BeautifulSoup(my_data.content, "html.parser")

        #g_specieslist = soup.find("a", title="Category:Rindhalu Coalition")

        g_info = soup.find("aside", class_ = "portable-infobox" )

        g_subinfo_name = g_info.find(attrs={"data-source": "title1"})
        try:
            g_subinfo_appearence = g_info.find(attrs={"data-source":"general_apperance"})
            g_appearence = g_subinfo_appearence.find("div")
            appearence = g_appearence.get_text()
        except:
            appearence = 'Unknown'

        try:
            g_subinfo_patron = g_info.find(attrs={"data-source":"patron_species"})
            g_patron = g_subinfo_patron.find("div")
            patron = g_patron.get_text()
        except:
            patron = 'Unknown'
            
        try:
            g_subinfo_client = g_info.find(attrs={"data-source":"client_species"})
            g_client = g_subinfo_client.find("div")
            client = g_client.get_text()
        except:
            client = 'None'

        try:
            g_subinfo_tech_level = g_info.find(attrs={"data-source":"tech_level"})
            g_tech = g_subinfo_tech_level.find("div")
            tech_level = g_tech.get_text()
        except:
            tech_level = 'unknown'

        try:
            g_subinfo_nickname = g_info.find(attrs={"data-source":"nickname"})
            g_nickname = g_subinfo_nickname.find("div")
            nickname = g_nickname.get_text()
        except:
            nickname = 'None'

        name = g_subinfo_name.get_text()
        
        print(name, appearence, patron, client, tech_level, nickname)    

scrapinTime_SpeciesPage(getSpecies())
