from .Airport import Airport
from Route import Route
class DataSource:
    self.graph = Graph()
    def graph(self):
        return self.graph

class FlightPlan(DataSource):




    def __init__(self, inputList):
        self.visited = set([])
        self.input = inputList
        self.current = self.input.first()


dp = []

def build_dp(n, fr):
    dp[0] = 0
    for i in range(1, n):
        min_cost = uint(2 >> 63) + 1
        min_candidate = None
        for candidate in expand(fr.current, fr.visited, fr.input):
            cost = Route.calculate(fr.current, candidate)
            if min_cost > cost:
                min_cost = cost
                min_candidate = candidate
        ret_cost = Route.calculate_return_path(candidate, fr.route)
        clone_fr = clone(fr)
        clone_fr.route = clone_fr.route.add(min_candidate)
        clone_fr.visited.add(min_candidate)
        clone_fr.current = min_candidate
        last = fr.last
        home = fr.input.first()
        fr = clone_fr
        dp[i] = min(dp[i - 1] + ret_cost, dp[i - 1] + cost(candidate, last) + cost(last, home))

    
def DP(n, c, fr):
    return dp[n]
    
def main():
    build_dp(0, 0, FlightPlan())



def expand(current:Airport, done:set(Airport), avaiable:List[Airport]) -> List[Airport]:
    res = []
    for a in avaiable:
        if a not in done and a != current:
            res.append(a)
    return res


