class Abbrevs:

    def __init__(self):
        self.collection = [
            'gov', 'msc' 'pres', 'sen', 'prof', 'inc', 'rep', 'reps',
            'rev', 'dem', 'adm', 'dr', 'arc', 'u.s', 'u.s.a', 'u.k',
            'p.m', 'a.m', 'mr', 'mrs', 'ms', 'co', 'vs', 'corp', 'no',
            ' n', 'u.n', 'jan', 'feb', 'mar', 'apr', 'jun', 'jul',
            'ago', 'sept', 'sep', 'oct', 'nov', 'dec'
        ]
    
    def get(self) -> list:
        """
        Get all the abbreviations.
        """
        return list(set(self.collection)) # set to list, to remove duplicates

