travel_log = []
add_new_travel_log = True
while add_new_travel_log:
    name_of_country = input("Name of country visited: ")
    number_of_visits = input("Number of visits: ")
    cities_visited = input("Number of cities visited. Seperate by a comma(,): ").split(", ")

    def add_new_country(country, visits, cities):
        new_log = {
                "country": country,
                "visits": visits,
                "cities": cities,
            }
        
        travel_log.append(new_log)
        print(travel_log)

    add_new_country(country = name_of_country, visits = number_of_visits, cities = cities_visited)

    add_new_log = input("Would you like to add new travel log, 'yes' or 'no': ").lower()
    if add_new_log == "yes":
        add_new_travel_log = True
    else:
        print("Have a nice day")
        add_new_travel_log = False