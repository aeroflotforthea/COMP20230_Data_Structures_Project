'''

Intention: 

Write a recursive algorithm that adds all possible routes to a list, calculating the score as you go 


e.g Dublin, London, Madrid, Dublin

Dublin to London to Madrid is the same as Dublin to London + London to Madrid

'''

trips = {
    'London': ['Madrid','Dublin'],
    'Dublin': ['London', 'Madrid'],
    'Madrid': ['London', 'Dublin']
}




def getCost(start_airport_index, end_airport_index, chart):
    # list of airports changes, it gets smaller each time?
    key_name = list(trips)[start_airport_index] + ":" + trips[list(trips)[start_airport_index]][end_airport_index]

    if key_name in chart:
        return chart[key_name]
    if end_airport_index < 0:
        start_airport_index -= 1
        end_airport_index = 1
        print(chart)
        return chart
    else: 
        chart[key_name] = 1
        getCost(start_airport_index, end_airport_index -1, chart)
    
    
    


getCost(len(trips)-1, 1, {})