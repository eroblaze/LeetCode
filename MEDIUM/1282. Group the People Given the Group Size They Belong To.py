class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        """
        The group sizes is not more than the size of the array
        """
        o = {}

        for idx, el in enumerate(groupSizes):
            try:
                o[el].append(idx)
            except KeyError:
                o[el] = [idx]

        r = []
        for key, el in o.items():
            val = el
            while len(val) > 0:
                r.append(val[:key])
                val = val[key:]

        return r
