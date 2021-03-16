#MinSteps.py
# Alexa is given n piles of equal or unequal heights. In one step, Alexa can remove any number of boxes from the pile which has the maximum height and try to make it equal to the one which is just lower than the maximum height of the stack. Determine the minimum number of steps required to make all of the piles equal in height.

# Example 1:

# Input: piles = [5, 2, 1]
# Output: 3
# Explanation:
# Step 1: reducing 5 -> 2 [2, 2, 1]
# Step 2: reducing 2 -> 1 [2, 1, 1]
# Step 3: reducing 2 -> 1 [1, 1, 1]
# So final number of steps required is 3.

def minSteps(piles):
    # EDGE CASE
    if len(piles) < 2:
        return 0

    # SORT THE BLOCKS
    piles = sorted(piles, reverse=True)

    # COUNT THE STEPS WE NEED
    steps = 0

    # EACH TIME WE SEE A DIFFERENT ELEMENT, WE NEED TO SEE HOW MANY ELEMENTS ARE BEFORE IT
    for i in range(1, len(piles)):
        steps += i if piles[i - 1] != piles[i] else 0

    return steps


print(minSteps([5,2,1]))
