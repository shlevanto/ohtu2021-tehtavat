from matchers import And, Or, HasAtLeast, HasFewerThan, PlaysIn, Not, All


from matchers import And, Or, HasAtLeast, HasFewerThan, PlaysIn, Not, All


class QueryBuilder:
    def __init__(self, matcher=All()):
        self._matcher = matcher
    
    def build(self):
        return self._matcher  
    
    def plays_in(self, team):
        return QueryBuilder(PlaysIn(team))
    
    def has_at_least(self, value, attr):
        return QueryBuilder(HasAtLeast(value, attr))
    
    