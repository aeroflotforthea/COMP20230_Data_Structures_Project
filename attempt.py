from Airport import Airport
from Route import Route
from Aircraft import Aircraft

madrid = Airport("Madrid", 3.7038, 40.4168, 0.84)
london = Airport("London", 0.1278, 51.5074, 1.17)
dublin = Airport("Dublin", 6.2603, 53.3498, 1)
berlin = Airport("Berlin", 13.4050, 13.4050, 1.99) 


stops = {
    "Madrid": [london, dublin, madrid],
    "Dublin": [london, madrid, dublin],
    "London": [madrid, dublin, london]
}

flight_record = {
    "previously_visited": [],
    "current_airport": None,
    "previous_airport": None,
    "accumulated_score": 0
}


what_we_want = Route.calculate_score(madrid, london) + Route.calculate_score(london, dublin)


def traverse(start_node, subset, flight_record):

    

    # next time through, start_node is next in subset if not in visited

    flight_record["previously_visited"].append(start_node.getName())

    if flight_record["previous_airport"] == None:
        flight_record["previous_airport"] = start_node
    else: 
        flight_record["previous_airport"] = flight_record["current_airport"]
    flight_record["current_airport"] = start_node

    if len(subset) == 0:
        start = flight_record["current_airport"]
        previous = flight_record["previous_airport"]
        score = Route.calculate_score(flight_record["previous_airport"], flight_record["current_airport"])
        flight_record["accumulated_score"] = flight_record["accumulated_score"] + score
        return flight_record

    for airport in subset:
        start = flight_record["current_airport"]
        previous = flight_record["previous_airport"]
        flight_record = traverse(airport, [x for x in stops[airport.getName()] if x.getName() not in flight_record["previously_visited"]], flight_record)
        score = Route.calculate_score(previous, start)
        flight_record["accumulated_score"] = flight_record["accumulated_score"] + score
        
        return flight_record


print(traverse(madrid, stops["Madrid"], flight_record))
print(what_we_want)