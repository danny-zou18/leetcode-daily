from types import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        res = 0

        for num in derived:
            res ^= num
        
        return res == 0
    
# Time Complexity: O(n), where n is the length of derived

# Space Complexity: O(1)

#Intuition
# Observe the following equations that represent the relationship between the elements of the derived and original arrays:

# derived[0] = original[0] XOR original[1]
# derived[1] = original[1] XOR original[2]
# derived[2] = original[2] XOR original[3]
# derived[3] = original[3] XOR original[4]

# ...

# derived[n-1] = original[n-1] XOR original[0]
# Each element in original appears exactly twice in the equations: once as original[i] and once as original[i+1]. For example:

# original[0] appears in derived[0] (original[0] XOR original[1])
# original[0] also appears in derived[n-1] (original[n-1] XOR original[0])
# Since XOR is both commutative and associative, the order doesn’t matter. When all occurrences of original[i] are XORed together, they cancel each other out: original[0] XOR original[0] XOR original[1] XOR original[1] ... = 0

# If the derived array is valid (i.e., it was generated from some original), then the XOR of all elements in derived must be 0. This is because all elements of original cancel out when XORed.

# Algorithm
# Initialize a variable XOR to 0. This will store the cumulative XOR of elements in the derived array.

# Iterate through each element in the derived array:

# For each element, compute the XOR with the current value of XOR and update XOR.
# After the loop, check the value of XOR:

# If XOR == 0, return true (indicating the array is valid).
# Otherwise, return false.