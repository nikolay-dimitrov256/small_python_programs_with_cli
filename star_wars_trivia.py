import requests


def get_film_names(list_urls: list) -> list:
    films = []
    for film_url in list_urls:
        film_data = requests.get(film_url)
        episode_id = film_data.json()['episode_id']
        title = film_data.json()['title']
        film_name = f'Episode {episode_id}: {title}'
        films.append(film_name)
    films.sort()

    return films


def get_character_names(list_urls: list) -> list:
    characters = []
    for character_url in list_urls:
        character_data = requests.get(character_url)
        character_name = character_data.json()['name']
        characters.append(character_name)
    characters.sort()

    return characters


def get_single_name(url: str) -> str:
    data = requests.get(url)
    name = data.json()['name']

    return name


def find_planet():

    planet_urls = {'Alderaan': 'https://swapi.dev/api/planets/2/', 'Aleen Minor': 'https://swapi.dev/api/planets/38/',
                   'Bespin': 'https://swapi.dev/api/planets/6/', 'Bestine IV': 'https://swapi.dev/api/planets/26/',
                   'Cato Neimoidia': 'https://swapi.dev/api/planets/18/', 'Cerea': 'https://swapi.dev/api/planets/43/',
                   'Champala': 'https://swapi.dev/api/planets/50/', 'Chandrila': 'https://swapi.dev/api/planets/32/',
                   'Concord Dawn': 'https://swapi.dev/api/planets/53/',
                   'Corellia': 'https://swapi.dev/api/planets/22/', 'Coruscant': 'https://swapi.dev/api/planets/9/',
                   'Dagobah': 'https://swapi.dev/api/planets/5/', 'Dantooine': 'https://swapi.dev/api/planets/25/',
                   'Dathomir': 'https://swapi.dev/api/planets/36/', 'Dorin': 'https://swapi.dev/api/planets/49/',
                   'Endor': 'https://swapi.dev/api/planets/7/', 'Eriadu': 'https://swapi.dev/api/planets/21/',
                   'Felucia': 'https://swapi.dev/api/planets/17/', 'Geonosis': 'https://swapi.dev/api/planets/11/',
                   'Glee Anselm': 'https://swapi.dev/api/planets/44/',
                   'Haruun Kal': 'https://swapi.dev/api/planets/42/', 'Hoth': 'https://swapi.dev/api/planets/4/',
                   'Iktotch': 'https://swapi.dev/api/planets/47/', 'Iridonia': 'https://swapi.dev/api/planets/45/',
                   'Kalee': 'https://swapi.dev/api/planets/59/', 'Kamino': 'https://swapi.dev/api/planets/10/',
                   'Kashyyyk': 'https://swapi.dev/api/planets/14/', 'Malastare': 'https://swapi.dev/api/planets/35/',
                   'Mirial': 'https://swapi.dev/api/planets/51/', 'Mon Cala': 'https://swapi.dev/api/planets/31/',
                   'Mustafar': 'https://swapi.dev/api/planets/13/', 'Muunilinst': 'https://swapi.dev/api/planets/57/',
                   'Mygeeto': 'https://swapi.dev/api/planets/16/', 'Naboo': 'https://swapi.dev/api/planets/8/',
                   'Nal Hutta': 'https://swapi.dev/api/planets/24/', 'Ojom': 'https://swapi.dev/api/planets/55/',
                   'Ord Mantell': 'https://swapi.dev/api/planets/27/',
                   'Polis Massa': 'https://swapi.dev/api/planets/15/', 'Quermia': 'https://swapi.dev/api/planets/48/',
                   'Rodia': 'https://swapi.dev/api/planets/23/', 'Ryloth': 'https://swapi.dev/api/planets/37/',
                   'Saleucami': 'https://swapi.dev/api/planets/19/', 'Serenno': 'https://swapi.dev/api/planets/52/',
                   'Shili': 'https://swapi.dev/api/planets/58/', 'Skako': 'https://swapi.dev/api/planets/56/',
                   'Socorro': 'https://swapi.dev/api/planets/30/', 'Stewjon': 'https://swapi.dev/api/planets/20/',
                   'Sullust': 'https://swapi.dev/api/planets/33/', 'Tatooine': 'https://swapi.dev/api/planets/1/',
                   'Tholoth': 'https://swapi.dev/api/planets/46/', 'Toydaria': 'https://swapi.dev/api/planets/34/',
                   'Trandosha': 'https://swapi.dev/api/planets/29/', 'Troiken': 'https://swapi.dev/api/planets/40/',
                   'Tund': 'https://swapi.dev/api/planets/41/', 'Umbara': 'https://swapi.dev/api/planets/60/',
                   'Utapau': 'https://swapi.dev/api/planets/12/', 'Vulpter': 'https://swapi.dev/api/planets/39/',
                   'Yavin IV': 'https://swapi.dev/api/planets/3/', 'Zolan': 'https://swapi.dev/api/planets/54/',
                   'unknown': 'https://swapi.dev/api/planets/28/'}

    all_planets = ['Alderaan', 'Aleen Minor', 'Bespin', 'Bestine IV', 'Cato Neimoidia', 'Cerea', 'Champala',
                   'Chandrila', 'Concord Dawn', 'Corellia', 'Coruscant', 'Dagobah', 'Dantooine', 'Dathomir', 'Dorin',
                   'Endor', 'Eriadu', 'Felucia', 'Geonosis', 'Glee Anselm', 'Haruun Kal', 'Hoth', 'Iktotch',
                   'Iridonia', 'Kalee', 'Kamino', 'Kashyyyk', 'Malastare', 'Mirial', 'Mon Cala', 'Mustafar',
                   'Muunilinst', 'Mygeeto', 'Naboo', 'Nal Hutta', 'Ojom', 'Ord Mantell', 'Polis Massa', 'Quermia',
                   'Rodia', 'Ryloth', 'Saleucami', 'Serenno', 'Shili', 'Skako', 'Socorro', 'Stewjon', 'Sullust',
                   'Tatooine', 'Tholoth', 'Toydaria', 'Trandosha', 'Troiken', 'Tund', 'Umbara', 'Utapau', 'Vulpter',
                   'Yavin IV', 'Zolan', 'unknown']

    print('\nWhich planet are you interested in?')

    while True:
        searched_planet = input('\nEnter a planet name, [l] to list all planet names, or [b] to go back: ')
        if searched_planet.lower() == 'b':
            break

        elif searched_planet.lower() == 'l':
            for planet_name in all_planets:
                print(planet_name)

        elif searched_planet in planet_urls.keys():
            url = planet_urls.get(searched_planet)
            if not url:
                print('Cannot find that planet.')
                continue

            print('\nLoading data...')
            result = requests.get(url)
            planet_data = result.json()

            planet_data['residents'] = get_character_names(planet_data['residents'])

            planet_data['films'] = get_film_names(planet_data['films'])

            display_data(planet_data, 'planet')

        else:
            print('Cannot find that planet.')


def find_starship():

    starship_urls = {'A-wing': 'https://swapi.dev/api/starships/28/',
                     'AA-9 Coruscant freighter': 'https://swapi.dev/api/starships/47/',
                     'B-wing': 'https://swapi.dev/api/starships/29/',
                     'Banking clan frigte': 'https://swapi.dev/api/starships/68/',
                     'Belbullab-22 starfighter': 'https://swapi.dev/api/starships/74/',
                     'CR90 corvette': 'https://swapi.dev/api/starships/2/',
                     'Calamari Cruiser': 'https://swapi.dev/api/starships/27/',
                     'Death Star': 'https://swapi.dev/api/starships/9/',
                     'Droid control ship': 'https://swapi.dev/api/starships/32/',
                     'EF76 Nebulon-B escort frigate': 'https://swapi.dev/api/starships/23/',
                     'Executor': 'https://swapi.dev/api/starships/15/',
                     'H-type Nubian yacht': 'https://swapi.dev/api/starships/49/',
                     'Imperial shuttle': 'https://swapi.dev/api/starships/22/',
                     'J-type diplomatic barge': 'https://swapi.dev/api/starships/43/',
                     'Jedi Interceptor': 'https://swapi.dev/api/starships/65/',
                     'Jedi starfighter': 'https://swapi.dev/api/starships/48/',
                     'Millennium Falcon': 'https://swapi.dev/api/starships/10/',
                     'Naboo Royal Starship': 'https://swapi.dev/api/starships/40/',
                     'Naboo fighter': 'https://swapi.dev/api/starships/39/',
                     'Naboo star skiff': 'https://swapi.dev/api/starships/64/',
                     'Rebel transport': 'https://swapi.dev/api/starships/17/',
                     'Republic Assault ship': 'https://swapi.dev/api/starships/52/',
                     'Republic Cruiser': 'https://swapi.dev/api/starships/31/',
                     'Republic attack cruiser': 'https://swapi.dev/api/starships/63/',
                     'Scimitar': 'https://swapi.dev/api/starships/41/',
                     'Sentinel-class landing craft': 'https://swapi.dev/api/starships/5/',
                     'Slave 1': 'https://swapi.dev/api/starships/21/',
                     'Solar Sailer': 'https://swapi.dev/api/starships/58/',
                     'Star Destroyer': 'https://swapi.dev/api/starships/3/',
                     'TIE Advanced x1': 'https://swapi.dev/api/starships/13/',
                     'Theta-class T-2c shuttle': 'https://swapi.dev/api/starships/61/',
                     'Trade Federation cruiser': 'https://swapi.dev/api/starships/59/',
                     'V-wing': 'https://swapi.dev/api/starships/75/', 'X-wing': 'https://swapi.dev/api/starships/12/',
                     'Y-wing': 'https://swapi.dev/api/starships/11/', 'arc-170': 'https://swapi.dev/api/starships/66/'}

    all_starships = [ship for ship in starship_urls.keys()]

    print('\nWhich spaceship are you interested in?')

    while True:
        searched_ship = input('Enter a ship name, [l] to list all spaceships, or [b] to go back: ')

        if searched_ship.lower() == 'b':
            break

        elif searched_ship.lower() == 'l':
            print()
            for ship_name in all_starships:
                print(ship_name)

        elif searched_ship in starship_urls.keys():
            print('\nLoading data...')

            url = starship_urls[searched_ship]
            response = requests.get(url)
            ship_data = response.json()

            ship_data['pilots'] = get_character_names(ship_data['pilots'])

            ship_data['films'] = get_film_names(ship_data['films'])

            display_data(ship_data, 'spaceship')

        else:
            print('Cannot find this spaceship.')


def find_vehicle():

    vehicles_urls = {'AT-AT': 'https://swapi.dev/api/vehicles/18/', 'AT-RT': 'https://swapi.dev/api/vehicles/76/',
                     'AT-ST': 'https://swapi.dev/api/vehicles/19/', 'AT-TE': 'https://swapi.dev/api/vehicles/53/',
                     'Armored Assault Tank': 'https://swapi.dev/api/vehicles/35/',
                     'Bantha-II cargo skiff': 'https://swapi.dev/api/vehicles/25/',
                     'C-9979 landing craft': 'https://swapi.dev/api/vehicles/37/',
                     'Clone turbo tank': 'https://swapi.dev/api/vehicles/71/',
                     'Corporate Alliance tank droid': 'https://swapi.dev/api/vehicles/72/',
                     'Droid gunship': 'https://swapi.dev/api/vehicles/73/',
                     'Droid tri-fighter': 'https://swapi.dev/api/vehicles/67/',
                     'Emergency Firespeeder': 'https://swapi.dev/api/vehicles/62/',
                     'Flitknot speeder': 'https://swapi.dev/api/vehicles/55/',
                     'Geonosian starfighter': 'https://swapi.dev/api/vehicles/57/',
                     'Imperial Speeder Bike': 'https://swapi.dev/api/vehicles/30/',
                     'Koro-2 Exodrive airspeeder': 'https://swapi.dev/api/vehicles/45/',
                     'LAAT/c': 'https://swapi.dev/api/vehicles/51/', 'LAAT/i': 'https://swapi.dev/api/vehicles/50/',
                     'Multi-Troop Transport': 'https://swapi.dev/api/vehicles/34/',
                     'Neimoidian shuttle': 'https://swapi.dev/api/vehicles/56/',
                     'Oevvaor jet catamaran': 'https://swapi.dev/api/vehicles/69/',
                     'Raddaugh Gnasp fluttercraft': 'https://swapi.dev/api/vehicles/70/',
                     'SPHA': 'https://swapi.dev/api/vehicles/54/', 'Sail barge': 'https://swapi.dev/api/vehicles/24/',
                     'Sand Crawler': 'https://swapi.dev/api/vehicles/4/',
                     'Single Trooper Aerial Platform': 'https://swapi.dev/api/vehicles/36/',
                     'Sith speeder': 'https://swapi.dev/api/vehicles/42/',
                     'Snowspeeder': 'https://swapi.dev/api/vehicles/14/',
                     'Storm IV Twin-Pod cloud car': 'https://swapi.dev/api/vehicles/20/',
                     'T-16 skyhopper': 'https://swapi.dev/api/vehicles/6/',
                     'TIE bomber': 'https://swapi.dev/api/vehicles/16/',
                     'TIE/IN interceptor': 'https://swapi.dev/api/vehicles/26/',
                     'TIE/LN starfighter': 'https://swapi.dev/api/vehicles/8/',
                     'Tribubble bongo': 'https://swapi.dev/api/vehicles/38/',
                     'Tsmeu-6 personal wheel bike': 'https://swapi.dev/api/vehicles/60/',
                     'Vulture Droid': 'https://swapi.dev/api/vehicles/33/',
                     'X-34 landspeeder': 'https://swapi.dev/api/vehicles/7/',
                     'XJ-6 airspeeder': 'https://swapi.dev/api/vehicles/46/',
                     'Zephyr-G swoop bike': 'https://swapi.dev/api/vehicles/44/'}

    all_vehicles = [name for name in vehicles_urls.keys()]

    print('\nWhich vehicle are you interested in?')
    while True:
        searched_vehicle = input('Enter a vehicle name, [l] to list all vehicles, or [b] to go back: ')

        if searched_vehicle.lower() == 'b':
            break

        elif searched_vehicle in vehicles_urls.keys():
            print('\nLoading data...')

            url = vehicles_urls[searched_vehicle]
            response = requests.get(url)
            vehicle_data = response.json()

            vehicle_data['pilots'] = get_character_names(vehicle_data['pilots'])

            vehicle_data['films'] = get_film_names(vehicle_data['films'])

            display_data(vehicle_data, 'vehicle')

        elif searched_vehicle.lower() == 'l':
            print()
            for vehicle in all_vehicles:
                print(vehicle)

        else:
            print('Cannot find that vehicle.')


def find_characters():
    character_urls = {'Ackbar': 'https://swapi.dev/api/people/27/', 'Adi Gallia': 'https://swapi.dev/api/people/55/',
                      'Anakin Skywalker': 'https://swapi.dev/api/people/11/',
                      'Arvel Crynyd': 'https://swapi.dev/api/people/29/',
                      'Ayla Secura': 'https://swapi.dev/api/people/46/',
                      'Bail Prestor Organa': 'https://swapi.dev/api/people/68/',
                      'Barriss Offee': 'https://swapi.dev/api/people/65/',
                      'Ben Quadinaros': 'https://swapi.dev/api/people/50/',
                      'Beru Whitesun lars': 'https://swapi.dev/api/people/7/',
                      'Bib Fortuna': 'https://swapi.dev/api/people/45/',
                      'Biggs Darklighter': 'https://swapi.dev/api/people/9/',
                      'Boba Fett': 'https://swapi.dev/api/people/22/', 'Bossk': 'https://swapi.dev/api/people/24/',
                      'C-3PO': 'https://swapi.dev/api/people/2/', 'Chewbacca': 'https://swapi.dev/api/people/13/',
                      'Cliegg Lars': 'https://swapi.dev/api/people/62/', 'Cordé': 'https://swapi.dev/api/people/61/',
                      'Darth Maul': 'https://swapi.dev/api/people/44/',
                      'Darth Vader': 'https://swapi.dev/api/people/4/',
                      'Dexter Jettster': 'https://swapi.dev/api/people/71/',
                      'Dooku': 'https://swapi.dev/api/people/67/', 'Dormé': 'https://swapi.dev/api/people/66/',
                      'Dud Bolt': 'https://swapi.dev/api/people/48/', 'Eeth Koth': 'https://swapi.dev/api/people/54/',
                      'Finis Valorum': 'https://swapi.dev/api/people/34/',
                      'Gasgano': 'https://swapi.dev/api/people/49/', 'Greedo': 'https://swapi.dev/api/people/15/',
                      'Gregar Typho': 'https://swapi.dev/api/people/60/',
                      'Grievous': 'https://swapi.dev/api/people/79/', 'Han Solo': 'https://swapi.dev/api/people/14/',
                      'IG-88': 'https://swapi.dev/api/people/23/',
                      'Jabba Desilijic Tiure': 'https://swapi.dev/api/people/16/',
                      'Jango Fett': 'https://swapi.dev/api/people/69/',
                      'Jar Jar Binks': 'https://swapi.dev/api/people/36/',
                      'Jek Tono Porkins': 'https://swapi.dev/api/people/19/',
                      'Jocasta Nu': 'https://swapi.dev/api/people/74/',
                      'Ki-Adi-Mundi': 'https://swapi.dev/api/people/52/',
                      'Kit Fisto': 'https://swapi.dev/api/people/53/', 'Lama Su': 'https://swapi.dev/api/people/72/',
                      'Lando Calrissian': 'https://swapi.dev/api/people/25/',
                      'Leia Organa': 'https://swapi.dev/api/people/5/', 'Lobot': 'https://swapi.dev/api/people/26/',
                      'Luke Skywalker': 'https://swapi.dev/api/people/1/',
                      'Luminara Unduli': 'https://swapi.dev/api/people/64/',
                      'Mace Windu': 'https://swapi.dev/api/people/51/',
                      'Mas Amedda': 'https://swapi.dev/api/people/59/',
                      'Mon Mothma': 'https://swapi.dev/api/people/28/',
                      'Nien Nunb': 'https://swapi.dev/api/people/31/',
                      'Nute Gunray': 'https://swapi.dev/api/people/33/',
                      'Obi-Wan Kenobi': 'https://swapi.dev/api/people/10/',
                      'Owen Lars': 'https://swapi.dev/api/people/6/',
                      'Padmé Amidala': 'https://swapi.dev/api/people/35/',
                      'Palpatine': 'https://swapi.dev/api/people/21/', 'Plo Koon': 'https://swapi.dev/api/people/58/',
                      'Poggle the Lesser': 'https://swapi.dev/api/people/63/',
                      'Quarsh Panaka': 'https://swapi.dev/api/people/42/',
                      'Qui-Gon Jinn': 'https://swapi.dev/api/people/32/', 'R2-D2': 'https://swapi.dev/api/people/3/',
                      'R4-P17': 'https://swapi.dev/api/people/75/', 'R5-D4': 'https://swapi.dev/api/people/8/',
                      'Ratts Tyerel': 'https://swapi.dev/api/people/47/',
                      'Raymus Antilles': 'https://swapi.dev/api/people/81/',
                      'Ric Olié': 'https://swapi.dev/api/people/39/',
                      'Roos Tarpals': 'https://swapi.dev/api/people/37/',
                      'Rugor Nass': 'https://swapi.dev/api/people/38/',
                      'Saesee Tiin': 'https://swapi.dev/api/people/56/',
                      'San Hill': 'https://swapi.dev/api/people/77/', 'Sebulba': 'https://swapi.dev/api/people/41/',
                      'Shaak Ti': 'https://swapi.dev/api/people/78/',
                      'Shmi Skywalker': 'https://swapi.dev/api/people/43/',
                      'Sly Moore': 'https://swapi.dev/api/people/82/', 'Tarfful': 'https://swapi.dev/api/people/80/',
                      'Taun We': 'https://swapi.dev/api/people/73/', 'Tion Medon': 'https://swapi.dev/api/people/83/',
                      'Wat Tambor': 'https://swapi.dev/api/people/76/', 'Watto': 'https://swapi.dev/api/people/40/',
                      'Wedge Antilles': 'https://swapi.dev/api/people/18/',
                      'Wicket Systri Warrick': 'https://swapi.dev/api/people/30/',
                      'Wilhuff Tarkin': 'https://swapi.dev/api/people/12/',
                      'Yarael Poof': 'https://swapi.dev/api/people/57/', 'Yoda': 'https://swapi.dev/api/people/20/',
                      'Zam Wesell': 'https://swapi.dev/api/people/70/'}

    all_characters = [name for name in character_urls.keys()]

    print('\nWhich character are you interested in?')

    while True:
        searched_character = input('Enter a character name, [l] to list all characters, or [b] to go back: ')

        if searched_character in character_urls:
            print('\nLoading data...')

            character_url = character_urls[searched_character]
            response = requests.get(character_url)
            character_data = response.json()

            character_data['homeworld'] = get_single_name(character_data['homeworld'])
            character_data['films'] = get_film_names(character_data['films'])
            character_data['species'] = get_character_names(character_data['species'])
            character_data['vehicles'] = get_character_names(character_data['vehicles'])
            character_data['starships'] = get_character_names(character_data['starships'])

            display_data(character_data, 'character')

        elif searched_character.lower() == 'b':
            break

        elif searched_character.lower() == 'l':
            for name in all_characters:
                print(name)

        else:
            print('Cannot find this character.')


def find_film():
    film_urls = {'Episode 1: The Phantom Menace': 'https://swapi.dev/api/films/4/',
                 'Episode 2: Attack of the Clones': 'https://swapi.dev/api/films/5/',
                 'Episode 3: Revenge of the Sith': 'https://swapi.dev/api/films/6/',
                 'Episode 4: A New Hope': 'https://swapi.dev/api/films/1/',
                 'Episode 5: The Empire Strikes Back': 'https://swapi.dev/api/films/2/',
                 'Episode 6: Return of the Jedi': 'https://swapi.dev/api/films/3/'}

    all_films = [name for name in film_urls.keys()]

    print('\nWhich film are you interested in?')

    while True:
        searched_film = input('Enter a film name, [l] to list all films, or [b] to go back: ')

        if searched_film in film_urls:
            print('\nLoading data... This may take a while.')
            response = requests.get(film_urls[searched_film])
            film_data = response.json()

            film_data['name'] = searched_film
            film_data['opening_crawl'] = film_data['opening_crawl'].replace('\\r', '')
            film_data['characters'] = get_character_names(film_data['characters'])
            film_data['planets'] = get_character_names(film_data['planets'])
            film_data['starships'] = get_character_names(film_data['starships'])
            film_data['vehicles'] = get_character_names(film_data['vehicles'])
            film_data['species'] = get_character_names(film_data['species'])

            display_data(film_data, 'film')

        elif searched_film.lower() == 'l':
            for name in all_films:
                print(name)

        elif searched_film.lower() == 'b':
            break

        else:
            print('Cannot find this film.')


def display_data(data: dict, category: str):
    if category == 'planet':
        print('\nName:', data['name'])
        print('Rotation period:', data['rotation_period'])
        print('Orbital period:', data['orbital_period'])
        print('Diameter:', data['diameter'])
        print('Climate:', data['climate'])
        print('Gravity:', data['gravity'])
        print('Terrain:', data['terrain'])
        print('Surface water:', data['surface_water'])
        print('Population:', data['population'])
        print('Famous residents:')
        for resident in data['residents']:
            print(f' - {resident}')
        print('Appears in:')
        for film in data['films']:
            print(f' - {film}')

    elif category == 'spaceship':
        print('\nName:', data['name'])
        print('Model:', data['model'])
        print('Manufacturer:', data['manufacturer'])
        print('Cost in credits:', data['cost_in_credits'])
        print('Length:', data['length'])
        print('Max atmosphering speed:', data['max_atmosphering_speed'])
        print('Crew:', data['crew'])
        print('Passengers:', data['passengers'])
        print('Cargo_capacity:', data['cargo_capacity'])
        print('Consumables:', data['consumables'])
        print('Hyperdrive rating:', data['hyperdrive_rating'])
        print('MGLT:', data['MGLT'])
        print('Starship class:', data['starship_class'])
        print('Piloted by:')
        for pilot in data['pilots']:
            print(f' - {pilot}')
        print('Appeared in films:')
        for film in data['films']:
            print(f' - {film}')

    elif category == 'vehicle':
        print('\nName:', data['name'])
        print('Model:', data['model'])
        print('Manufacturer:', data['manufacturer'])
        print('Cost in credits:', data['cost_in_credits'])
        print('Length:', data['length'])
        print('Max atmosphering speed:', data['max_atmosphering_speed'])
        print('Crew:', data['crew'])
        print('Passengers:', data['passengers'])
        print('Cargo capacity:', data['cargo_capacity'])
        print('Consumables:', data['consumables'])
        print('Vehicle class:', data['vehicle_class'])
        print('Piloted by:')
        for pilot in data['pilots']:
            print(f' - {pilot}')
        print('Appeared in films:')
        for film in data['films']:
            print(f' - {film}')

    elif category == 'character':
        print('\nName:', data['name'])
        print('Height:', data['height'])
        print('Mass:', data['mass'])
        print('Hair color:', data['hair_color'])
        print('Skin color:', data['skin_color'])
        print('Eyes color:', data['eye_color'])
        print('Year of birth:', data['birth_year'])
        print('Gender:', data['gender'])
        print('Homeworld:', data['homeworld'])
        print('Appeared in films:')
        for film in data['films']:
            print(f' - {film}')
        print('Species:')
        if data['species']:
            print(f' - {data["species"][0]}')
        print('Vehicles handled:')
        for vehicle in data['vehicles']:
            print(f' - {vehicle}')
        print('Spaceships piloted:')
        for ship in data['starships']:
            print(f' - {ship}')

    elif category == 'film':
        print('\nTitle:', data['name'])
        print('Opening crawl:')
        print(data['opening_crawl'])
        print()
        print('Director:', data['director'])
        print('Producer/s:', data['producer'])
        print('Release date:', data['release_date'])
        print('Characters:')
        for character in data['characters']:
            print(f' - {character}')
        print('Planets:')
        for planet in data['planets']:
            print(f' - {planet}')
        print('Starships:')
        for ship in data['starships']:
            print(f' - {ship}')
        print('Vehicles:')
        for vehicle in data['vehicles']:
            print(f' - {vehicle}')
        print('Species:')
        for person in data['species']:
            print(f' - {person}')


def main_function():
    while True:
        print('\nWhat are you interested in?')
        print('[1] Planets\n[2] Spaceships\n[3] Vehicles\n[4] Characters\n[5] Films\n[e] exit')

        command = input()

        if command == '1':
            find_planet()

        elif command == '2':
            find_starship()

        elif command == '3':
            find_vehicle()

        elif command == '4':
            find_characters()

        elif command == '5':
            find_film()

        elif command.lower() == 'e':
            break

        else:
            print('Please enter a valid command.')


print('Hi! I have some Star Wars trivia for you.')

main_function()
