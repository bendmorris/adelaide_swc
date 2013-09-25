# tag ID: A8025
# size (oz)
# sightings per month
# {1: 5}

# is_large (large means > 5 oz)
# is_small (small means < 3 oz)
# capture(month) 

class Rodent:
    def __init__(self, tag_id, size ):
        self.tag_id = tag_id
        self.size = size
        self.sightings_per_month = {}
    
    def is_large(self):
        # return True if size is > 5oz
        return (self.size > 5)
    
    def is_small(self):
        # return True if size is < 3oz
        return (self.size < 3)
    
    def plot(self):
        # return the letter of the plot at which
        # this rodent was first captured
        return self.tag_id[0]

    def capture(self, month):
        # we captured this rodent once in this month
        if month not in self.sightings_per_month:
            self.sightings_per_month[month] = 0
        self.sightings_per_month[month] += 1
