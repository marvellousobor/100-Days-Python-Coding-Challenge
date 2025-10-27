#Nesting
travel_log = {
    "France": {"cities_visited": ["Paris", "Lillie", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 12}
}

#Nesting a Dictionary in a List

travel_log = {
    {
    "country": "France",
    "cities_visited": ["Paris", "Lillie", "Dijon"],
    "total_visits": 12
    },
    {
    "country": "Germany", 
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 12
    },
}