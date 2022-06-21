from unicodedata import name
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import requests as r
import pandas as pd
from bs4 import BeautifulSoup
from sqlalchemy import create_engine

db = SQLAlchemy()


engine = create_engine('postgresql://cnqbetrz:3cO7Dwbxef-k8cA6gaN7FjUUqnwq9La6@raja.db.elephantsql.com/cnqbetrz')
#print('check')
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




def scrapinTime_SpeciesPage(species_list, engine):
    species_dict = {'species_name':[], 'appearence':[], 'patron':[], 'client':[], 'tech_level':[], 'nickname':[], 'coalition':[], 'image':[]}
    for x in species_list:
        #print(x)
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

        try:
            g_coalition = soup.find(attrs={"data-tracking-label":"categories-top-more-1"})
            coalition = g_coalition.get_text()
        except:
            coalition = 'Unknown Coalition'

        try:
            g_s_image = g_info.find(attrs={"data-image-key":"Jeraptha.jpg"})
            s_image = g_s_image.get("src")
        except:
            s_image = 'No Image'

        name = g_subinfo_name.get_text()

        #species_dict = {'Name':[], 'Appearence':[], 'Patron':[], 'Client':[], 'Tech Level':[], 'Nickname':[]}
        species_dict['species_name'].append(name)
        species_dict['appearence'].append(appearence)
        species_dict['patron'].append(patron)
        species_dict['client'].append(client)
        species_dict['tech_level'].append(tech_level)
        species_dict['nickname'].append(nickname)
        species_dict['coalition'].append(coalition)
        species_dict['image'].append(s_image)
        
    df = pd.DataFrame.from_dict(species_dict)
    df.to_sql(con=engine, name='species', if_exists='append', index=False)



# def scrape_planets():
#     my_data = r.get('https://expeditionary-force-by-craig-alanson.fandom.com/wiki/Planets_/_Space')
#     soup = BeautifulSoup(my_data.content, "html.parser")
#     planet_list = []
#     g_info = soup.find_all('li', class_="wds-tabs__tab")
#     for x in g_info:
#         planet_list.append(x.get_text())
#     print(planet_list)


#     for x in planet_list:
#         print(x)
#         planet_data = r.get(f'https://expeditionary-force-by-craig-alanson.fandom.com/wiki/Planets_/_Space#{x}')
#         super_soup = BeautifulSoup(planet_data.content, "html.parser")
#         g_planet_info = super_soup.find("div", class_="tabber wds-tabber")
#         g_table_info = g_planet_info.find("table")
#         g_paragraph_info = g_table_info.find("p")
#         g_paragraph_info.sup.decompose()
#         print(g_paragraph_info.get_text())
        

def scrape_planets2(engine):
    print("Scrape_Planets2 Started")
    my_data = r.get('https://expeditionary-force-by-craig-alanson.fandom.com/wiki/Category:Planets')
    soup = BeautifulSoup(my_data.content, "html.parser")
    g_planet_info = soup.find("div", class_="category-page__members")
    g_grab_name = g_planet_info.find_all('a', class_="category-page__member-link")
    planet_list = []
    for x in g_grab_name:
        if x.get_text() != 'Planets / Space' and x.get_text() != 'Rahkarsh Diweln':
            planet_list.append(x.get_text())
    #print(planet_list)
    planet_dict = {"name":[], "nickname":[], "species_name":[], "nativespecies":[], "planetdata":[]}
    for x in planet_list:
        #print(x)
        name = x
        planet_data = r.get(f'https://expeditionary-force-by-craig-alanson.fandom.com/wiki/{x}')
        super_soup = BeautifulSoup(planet_data.content, "html.parser")
        g_grab_box = super_soup.find("aside", class_="portable-infobox pi-background pi-border-color pi-theme-wikia pi-layout-default")
        try:
            g_grab_nickname = g_grab_box.find(attrs={"data-source": "nickname"})
            nickname = g_grab_nickname.get_text()
        except:
            nickname = "None"

        try:
            g_grab_O_Species = g_grab_box.find(attrs={"data-source": "species2"})
            g_grab_species_name = g_grab_O_Species.find("a")
            OccupyingSpecies = g_grab_species_name.get_text()
            print(OccupyingSpecies)
        except:
            OccupyingSpecies = "None"

        try:
            g_grab_N_Species = g_grab_box.find(attrs={"data-source": "species1"})
            NativeSpecies = g_grab_N_Species.get_text()
        except:
            NativeSpecies = "None"
        #print(nickname, OccupyingSpecies, NativeSpecies)

        try:
            g_grab_body = super_soup.find("tbody")
            g_grab_body.aside.decompose()
            #g_grab_body.sup.decompose()
            g_grab_p = g_grab_body.find_all("p")
            #print(g_grab_p)
            for x in g_grab_p:
                #x.sup.decompose()
                planetdata = x.get_text()
                #print(planetdata)
        except:
            planetdata = "None"

        #planet_dict = {"Name":[], "Nickname":[], "OccupyingSpecies":[], "NativeSpecies":[], "PlanetData":[]}
        planet_dict["name"].append(name)
        planet_dict["nickname"].append(nickname)
        planet_dict["species_name"].append(OccupyingSpecies)
        planet_dict["nativespecies"].append(NativeSpecies)
        planet_dict["planetdata"].append(planetdata)
    df = pd.DataFrame.from_dict(planet_dict)
    df.to_sql(con=engine, name='planets', if_exists='append', index=False)
        #print(name, nickname, OccupyingSpecies, NativeSpecies, planetdata)

def scrape_ships(engine):
    my_data = r.get('https://expeditionary-force-by-craig-alanson.fandom.com/wiki/Category:Ships')
    soup = BeautifulSoup(my_data.content, "html.parser")
    g_grabships = soup.find_all("a", class_="category-page__member-link")
    ship_list = []
    for x in g_grabships:
        if x.get_text() != "Spacecraft" or x.get_text() != "United Nations Navy":
            ship_list.append(x.get_text())
    
    ship_dict = {"shipname":[], "shiptype":[], "species_name":[], "controlai":[], "armament":[], "status":[], "description":[]}

    for x in ship_list:
        #print(x)
        ship_data = r.get(f'https://expeditionary-force-by-craig-alanson.fandom.com/wiki/{x}')
        super_soup = BeautifulSoup(ship_data.content, "html.parser")
        g_grab_box = super_soup.find("aside", class_="portable-infobox pi-background pi-border-color pi-theme-wikia pi-layout-default")
        if x == 'Spacecraft' or x == 'United Nations Navy' or x == 'Types of Conveyance':
            print(f'skipped {x}')
            continue
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
            print(f'{x} {species_text}')

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

        #ship_dict = {"Shipname":[], "Shiptype":[], "Species_text":[], "ControlAI":[], "Armament":[], "Status":[], "Description":[]}
        ship_dict['shipname'].append(shipname)
        ship_dict['shiptype'].append(shiptype)
        ship_dict['species_name'].append(species_text)
        ship_dict['controlai'].append(control_AI)
        ship_dict['armament'].append(armament)
        ship_dict['status'].append(status)
        ship_dict['description'].append(description)
    df = pd.DataFrame.from_dict(ship_dict)
    df.to_sql(con=engine, name='ships', if_exists='append', index=False)
        #print(shipname, shiptype, species_text, control_AI, armament, status, description)
        

# def scrapeFactions():
#     my_data = r.get('https://expeditionary-force-by-craig-alanson.fandom.com/wiki/Factions_/_Groups')
#     soup = BeautifulSoup(my_data.content, "html.parser")
#     g_table = soup.find_all("div", class_="wds-tab__content")
#     word_list = []
#     for x in g_table:
#         x.th.decompose()
#         word_list.append(x.get_text())
#     print(word_list)        
        #print(x.get_text())

    # for x in g_table:
    #     g_sub_table = x.find("td")
    #     #g_sub_table.th.decompose()
    #     #if g_sub_table.get_text()
    #     print(g_sub_table)

    # g_table = soup.find("div", class_="mw-parser-output")
    # g_sub_table = g_table.find("ul", class_="wds-tabs")
    # g_grab_names = g_sub_table.find_all("a")
    # species_list = []
    # for x in g_grab_names:
    #     species_list.append(x.get_text())
    # print(species_list)
    # for x in species_list:
    #     my_sub_data = r.get(f'https://expeditionary-force-by-craig-alanson.fandom.com/wiki/Factions_/_Groups#{x}')

    #     super_soup = BeautifulSoup(my_sub_data.content, "html.parser")
    #     g_faction_table = super_soup.find("div", class_="wds-tab__content wds-is-current")
    #     g_sub_faction_table = g_faction_table.find("tbody")
    #     g_sub_sub_faction_table = g_sub_faction_table.find("tbody")
    #     g_faction_name = g_sub_sub_faction_table.find_all("td")
    #     for x in g_faction_name:
    #         print(x.get_text())
        

def scrapeBooks(engine):
    my_data = r.get('https://expeditionary-force-by-craig-alanson.fandom.com/wiki/Category:Books')
    soup = BeautifulSoup(my_data.content, "html.parser")
    g_grab_names = soup.find_all("li", class_="category-page__member")
    book_list = []
    for x in g_grab_names:
        sub_names = x.find("a", class_="category-page__member-link")
        #print(sub_names.get_text())
        if sub_names.get_text() == 'Freefall':
            pass
        elif sub_names.get_text() == 'Reading Order':
            pass
        else:
            book_list.append(sub_names.get_text())
    #print(book_list)
    books_dict = {"bookname":[], "author":[], "narrator":[], "release":[], "publisher":[], "runtime":[], "previous":[], "next":[], "authorsummary":[], "image":[]}
    for x in book_list:
        #print(x)
        sub_data = r.get(f'https://expeditionary-force-by-craig-alanson.fandom.com/wiki/{x}')
        super_soup = BeautifulSoup(sub_data.content, "html.parser")

        try:
            g_book_name = super_soup.find(attrs={"data-source": "title1"})
            bookname = g_book_name.get_text()
            #print(bookname)
        except:
            bookname = "unknown"

        try:
            g_author = super_soup.find(attrs={"data-source": "author"})
            author = g_author.get_text()
        except:
            author = 'Unknown'

        try:
            g_narrator = super_soup.find(attrs={"data-source": "narrator"})
            narrator = g_narrator.get_text()
        except:
            narrator = "Unknown"

        try:
            g_release = super_soup.find(attrs={"data-source": "release"})
            release = g_release.get_text()
        except:
            release = "Unknown"

        try:
            g_publisher = super_soup.find(attrs={"data-source": "publisher"})
            publisher = g_publisher.get_text()
        except:
            publisher = "Unknown"

        try:
            g_run_time = super_soup.find(attrs={"data-source": "run_time"})
            run_time = g_run_time.get_text()
        except:
            run_time = "Unknown"

        try:
            g_previous = super_soup.find(attrs={"data-source": "previous"})
            previous = g_previous.get_text()
        except:
            previous = "Unknown"

        try:
            g_next = super_soup.find(attrs={"data-source": "next"})
            next = g_next.get_text()
        except:
            next = "Unknown"

        try:
            g_author_summary = super_soup.find_all('blockquote')
            for x in g_author_summary:
                author_summary = (x.find('i').get_text())
                #print(author_summary)
        except:
            author_summary = "none"

        try:
            image =  super_soup.find('img', class_="pi-image-thumbnail").get("src")
            #print(image)
        except:
            image = 'none'
        #print(bookname, author, narrator, release, publisher, run_time, previous, next, author_summary, image)

        #books_dict = {"Bookname":[], "Author":[], "Narrator":[], "Release":[], "Publisher":[], "RunTime":[], "Previous":[], "Next":[], "AuthorSummary":[], "Image":[]}
        books_dict["bookname"].append(bookname)
        books_dict["author"].append(author)
        books_dict["narrator"].append(narrator)
        books_dict["release"].append(release)
        books_dict["publisher"].append(publisher)
        books_dict["runtime"].append(run_time)
        books_dict["previous"].append(previous)
        books_dict["next"].append(next)
        books_dict["authorsummary"].append(author_summary)
        books_dict["image"].append(image)
    df = pd.DataFrame.from_dict(books_dict)
    df.to_sql(con=engine, name='books', if_exists='append', index=False)


def scrapeCharacters(engine):
    my_data = r.get('https://expeditionary-force-by-craig-alanson.fandom.com/wiki/Characters')
    soup = BeautifulSoup(my_data.content, "html.parser")
    g_find_characters = soup.find_all("div", class_="wds-tab__content")
    character_list = []
    ran = False
    for x in g_find_characters:
        find_a = x.find_all("a")
        for y in find_a:
            if y.get_text() == "Notable Characters" or y.get_text() == 'Verd-Kris' or y.get_text() == 'Jeraptha' or y.get_text() == 'Maxolhx' or y.get_text() == 'Kristang' or y.get_text() == 'Ruhar':
                pass
            elif y.get_text() == "Rindhalu" or y.get_text() == "Thuranin" or y.get_text() == 'Wurgalan' or y.get_text() == "Bosphuraq" or y.get_text() == "Keepers of the Faith" or y.get_text() == 'Verd-kris':
                pass
            elif y.get_text() == "Other Humans" or y.get_text() == "The Merry Band of Pirates" or y.get_text() == 'Spec Ops Teams' or y.get_text() == "STAR Team" or y.get_text() == "Alien Legion Commandos":
                pass
            elif y.get_text() == "Former Spec Ops Team" or y.get_text() == "Science Team" or y.get_text() == 'The Mavericks' or y.get_text() == "Alien Legion" or y.get_text() == "UNEF" or y.get_text() == "Valdez":
                pass
            else:
                character_list.append(y.get_text())
    #print(character_list)
    character_dict = {"name":[], "alias":[], "rank":[], "affiliation":[], "relationship":[], "species_name":[], "sex":[], "status":[], "first_appearence":[], "last_known_location":[]}
    for x in character_list:
        #try:
        print(x)
        if x == 'Captain Uhtavio "Big Score" Scorandum':
            x = "Uhtavio_Scorandum"
        elif x == 'Brevet Captain Illiath':
            x = 'Illiath'
        elif x == 'Admiral Jet-au-Bes Kekrando':
            x = 'Jet-au-Bes Kekrando'
        elif x == 'Jeremy Smythe':
            x = 'Jeremy_Ewan_Smythe'
        elif x == 'Major Kapoor':
            x = 'Kapoor_(MBoP)'
        elif x == 'Lieutenant Williams':
            x = 'Williams_(MBoP)'
        elif x == 'Lieutenant Hendricks':
            x = 'Hendricks_(MBoP)'
        elif x == 'Captain Xho':
            x = 'Xho_(MBoP)'
        elif x == 'Captain Chander':
            x = 'Chander_(MBoP)'
        elif x == 'Dr. Mark Friedlander':
            x = 'Dr._Mark_Friedlander_(MBoP)'
        elif x == 'Dr. Sarah Rose':
            x = 'Dr._Sarah_Rose_(MBoP)'
        elif x == 'Dr. Graziano':
            x = 'Dr._Graziano_(MBoP)'
        elif x == 'Dr. Mark Friedlander':
            x = 'Dr._Mark_Friedlander_(MBoP)'
        elif x == 'Dr. Mesker':
            x = 'Dr._Mesker_(MBoP)'
        elif x == 'Dr. Tanaka':
            x = 'Dr._Tanaka_(MBoP)'
        elif x == 'Dr. Kassner':
            x = 'Dr._Kassner_(MBoP)'
        elif x == 'Dr. Zheng':
            if ran == False:
                x = 'Dr._Zheng_(MBoP)'
                ran = True
            if ran == True:
                continue
        elif x == 'Dr. Suarez':
            x = 'Dr._Suarez_(MBoP)'
        elif x == 'Dr. Reinfall':
            x = 'Dr._Reinfall_(MBoP)'
        elif x == 'Amos Gonzales':
            continue
        
        sub_data = r.get(f'https://expeditionary-force-by-craig-alanson.fandom.com/wiki/{x}')
        super_soup = BeautifulSoup(sub_data.content, "html.parser")
        g_grab_aside = super_soup.find("aside")
        try:
            g_grab_first_name = g_grab_aside.find(attrs={"data-source": "first_name"})
            g_grab_first_name_div = g_grab_first_name.find("div", class_="pi-data-value pi-font")
            firstname = g_grab_first_name_div.get_text()
        except:
            firstname = "None"

        try:
            g_grab_last_name = g_grab_aside.find(attrs={"data-source": "last_name"})
            g_grab_last_name_div = g_grab_last_name.find("div", class_="pi-data-value pi-font")
            lastname = g_grab_last_name_div.get_text()
        except:
            lastname = "None"

        try:
            g_grab_alias = g_grab_aside.find(attrs={"data-source": "alias(s)"})
            g_grab_alias_div = g_grab_alias.find("div", class_="pi-data-value pi-font")
            alias = g_grab_alias_div.get_text()
        except:
            alias = "No Alias"

        try:
            g_grab_rank = g_grab_aside.find(attrs={"data-source": "rank_/_title"})
            g_grab_rank_div = g_grab_rank.find("div", class_="pi-data-value pi-font")
            rank = g_grab_rank_div.get_text()
        except:
            rank = "None"

        try:
            g_grab_affiliation = g_grab_aside.find(attrs={"data-source": "affiliation(s)"})
            g_grab_affiliation_div = g_grab_affiliation.find("div", class_="pi-data-value pi-font")
            affiliation = g_grab_affiliation_div.get_text()
        except:
            affiliation = "None"

        try:
            g_grab_relationship = g_grab_aside.find(attrs={"data-source": "relationship(s)"})
            g_grab_relationship_div = g_grab_relationship.find("div", class_="pi-data-value pi-font")
            relationship = g_grab_relationship_div.get_text()
        except:
            relationship = "None"

        try:
            g_grab_species = g_grab_aside.find(attrs={"data-source": "species"})
            g_grab_species_div = g_grab_species.find("div", class_="pi-data-value pi-font")
            species = g_grab_species_div.get_text()
            if species == "Human" or species == "human":
                species = "Humans"
            if species == "NA - Elder AI" or species == "NA - Elder AI-created":
                species = "Elders"
            elif species == "Elder AI (communications sub-mind)":
                species = "Elders"
        except:
            species = "None"

        try:
            g_grab_sex = g_grab_aside.find(attrs={"data-source": "sex"})
            g_grab_sex_div = g_grab_sex.find("div", class_="pi-data-value pi-font")
            sex = g_grab_sex_div.get_text()
        except:
            sex = "None"

        try:
            g_grab_status = g_grab_aside.find(attrs={"data-source": "status"})
            g_grab_status_div = g_grab_status.find("div", class_="pi-data-value pi-font")
            status = g_grab_status_div.get_text()
        except:
            status = "None"

        try:
            g_grab_first_appearance = g_grab_aside.find(attrs={"data-source": "first_appearance"})
            g_grab_first_appearance_div = g_grab_first_appearance.find("div", class_="pi-data-value pi-font")
            g_grab_first_appearence_a = g_grab_first_appearance_div.find("a")
            first_appearance = g_grab_first_appearence_a.get_text()
            if first_appearance == "Book 2: Spec Ops":
                first_appearance = "ExForce 2: Spec Ops"
            elif first_appearance == "ExForce 3.5: Trouble on Paradise":
                first_appearance = "Book 3.5: Trouble on Paradise (Novella)"
            
            
        except:
            first_appearance = "ExForce 1: Columbus Day"
        
        try:
            g_grab_last_known_location = g_grab_aside.find(attrs={"data-source": "last_known_location"})
            g_grab_last_known_location_div = g_grab_last_known_location.find("div", class_="pi-data-value pi-font")
            last_known_location = g_grab_last_known_location_div.get_text()
        except:
            last_known_location = "None"
        
        #character_dict = {"Name":[], "Alias":[], "Rank":[], "Affiliation":[], "Relationship":[], "Species":[], "Sex":[], "Status":[], "First_Appearence":[], "Last_Known_Location":[]}
        character_dict["name"].append(f'{firstname} {lastname}')
        character_dict["alias"].append(alias)
        character_dict["rank"].append(rank)
        character_dict["affiliation"].append(affiliation)
        character_dict["relationship"].append(relationship)
        character_dict["species_name"].append(species)
        character_dict["sex"].append(sex)
        character_dict["status"].append(status)
        character_dict["first_appearence"].append(first_appearance)
        character_dict["last_known_location"].append(last_known_location)
    df = pd.DataFrame.from_dict(character_dict)
    df.to_sql(con=engine, name='characters', if_exists='append', index=False)

#scrapeCharacters(engine)
#scrapeBooks(engine)
#scrapeFactions()
scrape_ships(engine)
#scrape_planets2(engine)
#scrape_planets()
#scrapinTime_SpeciesPage(getSpecies(), engine)
