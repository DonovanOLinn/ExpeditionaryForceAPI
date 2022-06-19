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


def scrape_planets():
    my_data = r.get('https://expeditionary-force-by-craig-alanson.fandom.com/wiki/Planets_/_Space')
    soup = BeautifulSoup(my_data.content, "html.parser")
    planet_list = []
    g_info = soup.find_all('li', class_="wds-tabs__tab")
    for x in g_info:
        planet_list.append(x.get_text())
    print(planet_list)


    for x in planet_list:
        print(x)
        planet_data = r.get(f'https://expeditionary-force-by-craig-alanson.fandom.com/wiki/Planets_/_Space#{x}')
        super_soup = BeautifulSoup(planet_data.content, "html.parser")
        g_planet_info = super_soup.find("div", class_="tabber wds-tabber")
        g_table_info = g_planet_info.find("table")
        g_paragraph_info = g_table_info.find("p")
        g_paragraph_info.sup.decompose()
        print(g_paragraph_info.get_text())
        

def scrape_planets2():
    my_data = r.get('https://expeditionary-force-by-craig-alanson.fandom.com/wiki/Category:Planets')
    soup = BeautifulSoup(my_data.content, "html.parser")
    g_planet_info = soup.find("div", class_="category-page__members")
    g_grab_name = g_planet_info.find_all('a', class_="category-page__member-link")
    planet_list = []
    for x in g_grab_name:
        if x.get_text() != 'Planets / Space' and x.get_text() != 'Rahkarsh Diweln':
            planet_list.append(x.get_text())
    #print(planet_list)

    for x in planet_list:
        #print(x)
        planet_data = r.get(f'https://expeditionary-force-by-craig-alanson.fandom.com/wiki/{x}')
        soup = BeautifulSoup(planet_data.content, "html.parser")
        g_grab_box = soup.find("aside", class_="portable-infobox pi-background pi-border-color pi-theme-wikia pi-layout-default")
        try:
            g_grab_nickname = g_grab_box.find(attrs={"data-source": "nickname"})
            nickname = g_grab_nickname.get_text()
        except:
            nickname = "None"

        try:
            g_grab_O_Species = g_grab_box.find(attrs={"data-source": "species2"})
            OccupyingSpecies = g_grab_O_Species.get_text()
        except:
            OccupyingSpecies = "None"

        try:
            g_grab_N_Species = g_grab_box.find(attrs={"data-source": "species1"})
            NativeSpecies = g_grab_N_Species.get_text()
        except:
            NativeSpecies = "None"
        #print(nickname, OccupyingSpecies, NativeSpecies)

        try:
            g_grab_body = soup.find("tbody")
            g_grab_body.aside.decompose()
            g_grab_p = g_grab_body.find_all("p")
            g_grab_p.sup.decompose()
            for x in g_grab_p:
                planetdata = x.get_text()
                print(planetdata)
        except:
            planetdata = "None"

def scrape_ships():
    my_data = r.get('https://expeditionary-force-by-craig-alanson.fandom.com/wiki/Category:Ships')
    soup = BeautifulSoup(my_data.content, "html.parser")
    g_grabships = soup.find_all("a", class_="category-page__member-link")
    ship_list = []
    for x in g_grabships:
        if x.get_text() != "Spacecraft" or x.get_text() != "United Nations Navy":
            ship_list.append(x.get_text())
    
    for x in ship_list:
        ship_data = r.get(f'https://expeditionary-force-by-craig-alanson.fandom.com/wiki/{x}')
        super_soup = BeautifulSoup(ship_data.content, "html.parser")
        g_grab_box = super_soup.find("aside", class_="portable-infobox pi-background pi-border-color pi-theme-wikia pi-layout-default")
        try:
            g_grab_shipname = g_grab_box.find(attrs={"data-source": "title1"})
            shipname = g_grab_shipname.get_text()
            
        except:
            shipname = "None"

        try:
            g_grab_shiptype = g_grab_box.find(attrs={"data-source": "type"})
            g_grab_shiptype_text = g_grab_shiptype.find("div")
            shiptype = g_grab_shiptype_text.get_text()
        except:
            shiptype = "None"

        try:
            g_grab_species = g_grab_box.find(attrs={"data-source": "species"})
            g_grab_species_text = g_grab_species.find("a")
            species_text = g_grab_species_text.get_text()
        except:
            species_text = "None"

        try:
            g_grab_controlAI = g_grab_box.find(attrs={"data-source": "Control AI"})
            g_grab_controlAI_text = g_grab_controlAI.find("div")
            control_AI = g_grab_controlAI_text.get_text()
        except:
            control_AI = "None"

        try:
            g_grab_armament = g_grab_box.find(attrs={"data-source": "armament"})
            g_grab_armament_text = g_grab_armament.find("div")
            armament = g_grab_armament_text.get_text()
        except:
            armament = "None"

        try:
            g_grab_status = g_grab_box.find(attrs={"data-source": "status"})
            g_grab_status_text = g_grab_status.find("div")
            status = g_grab_status_text.get_text()
        except:
            status = "None"

        try:
            g_grab_description = super_soup.find("table")
            #print(g_grab_description)
            g_grab_description.aside.decompose()
            g_grab_description_p = g_grab_description.find_all("p")
            description = ''
            for x in g_grab_description_p:
                x.sup.decompose()
                description += x.get_text()
            #description = g_grab_description_p.get_text()
        except:
            description = "None"

        #print(shipname, shiptype, species_text, control_AI, armament, status, description)
        

def scrapeFactions():
    my_data = r.get('https://expeditionary-force-by-craig-alanson.fandom.com/wiki/Factions_/_Groups')
    soup = BeautifulSoup(my_data.content, "html.parser")
    g_table = soup.find("div", class_="mw-parser-output")
    g_sub_table = g_table.find("ul", class_="wds-tabs")
    g_grab_names = g_sub_table.find_all("a")
    species_list = []
    for x in g_grab_names:
        species_list.append(x.get_text())
    
    # for x in species_list:
    #     my_sub_data = r.get(f'https://expeditionary-force-by-craig-alanson.fandom.com/wiki/Factions_/_Groups#{x}')

    #     super_soup = BeautifulSoup(my_sub_data.content, "html.parser")
    #     g_faction_table = super_soup.find("div", class_="wds-tab__content wds-is-current")
    #     g_sub_faction_table = g_faction_table.find("tbody")
    #     g_sub_sub_faction_table = g_sub_faction_table.find("tbody")
    #     g_faction_name = g_sub_sub_faction_table.find_all("td")
    #     for x in g_faction_name:
    #         print(x.get_text())
        

scrapeFactions()



#scrape_ships()


#scrape_planets2()

#scrape_planets()

#scrapinTime_SpeciesPage(getSpecies())
