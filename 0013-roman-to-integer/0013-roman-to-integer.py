class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    # Initialize the total value and previous value to zero
        total = 0
        prev_value = 0
    
    # Iterate through the input string in reverse
        for c in s[::-1]:
        # Get the integer value of the current numeral
            curr_value = roman_values[c]
        
        # If the current value is less than the previous value, subtract it from the total
            if curr_value < prev_value:
                total -= curr_value
        # Otherwise, add it to the total
            else:
                total += curr_value
        
        # Update the previous value for the next iteration
            prev_value = curr_value
    
    # Return the total value
        return total