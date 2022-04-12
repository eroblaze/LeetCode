class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        # Capacity is the volume of the watering can
        steps = 0
        vol = capacity
        for (idx, plant) in enumerate(plants):
            if vol >= plant:
                steps += 1
                # it can water this plant
                vol -= plant
            else:
                # walking back to river is idx and walking back to the plant is idx+1
                steps += idx # go back to river
                vol = capacity # refill
                steps += idx+1 # go back to plant
                vol -= plant
                
        return steps                
