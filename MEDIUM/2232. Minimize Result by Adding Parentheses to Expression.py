class Solution:
    def minimizeResult(self, expression: str) -> str:
        if len(expression) == 3: return "(" + expression + ")"
        
        my_dict = {}
        left, right = expression.split("+")
        # get the bigger side
        big, small = left, right
        l_left, l_right = len(left), len(right)
        # work with my bigger side
        for i in range(len(big)-1, -1, -1):
            for j in range(len(small)):
                if i != 0:
                    left_side = int(big[:i])
                    if j != len(small) -1:
                        right_side = int(small[j+1:])
                        # there is a left_side and a right_side
                        ans = left_side * (int(big[i:]) + int(small[:j+1])) * right_side
                        my_dict[ans] = f"{left_side}({big[i:]}+{small[:j+1]}){right_side}"
                    else:
                        # Right side is the whole of small
                        ans = left_side * (int(big[i:]) + int(small))                                   
                        my_dict[ans] = f"{left_side}({big[i:]}+{small})"                        
                else:
                    # left side is the whole of big
                    left_side = int(big)
                    if j != len(small) -1:
                        right_side = int(small[j+1:])
                        ans = (left_side + int(small[:j+1])) * right_side
                        my_dict[ans] = f"({left_side}+{small[:j+1]}){right_side}"
                    else:
                        # Right side is the whole of small
                        ans = left_side + int(small)
                        my_dict[ans] = f"({left_side}+{small})"   

        smallest = min(my_dict.keys())
        return my_dict[smallest]
