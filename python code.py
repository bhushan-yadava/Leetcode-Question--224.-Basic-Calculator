class Solution:
    def calculate(self, s: str) -> int:

        stack = []  # Initialize an empty list to be used as a stack
        result, operator = 0, 1  # Initialize result to 0 and operator to 1 ('+' sign)
        index, length = 0, len(s)  # Initialize loop variables
      
        # Iterate over the input string
        while index < length:
            # If the current character is a digit
            if s[index].isdigit():
                number = 0
                # Continue until a non-digit is found, building the number
                while index < length and s[index].isdigit():
                    number = number * 10 + int(s[index])
                    index += 1
                # Update the result with the current number and the preceding operator
                result += operator * number
                # Compensate for the index increment in the loop
                index -= 1
            # If the current character is a plus, set operator to 1
            elif s[index] == "+":
                operator = 1
            # If the current character is a minus, set operator to -1
            elif s[index] == "-":
                operator = -1
            # Handle opening parentheses
            elif s[index] == "(":
                # Push the current result and operator to the stack
                stack.append(result)
                stack.append(operator)
                # Reset the result and operator for the new expression within the parentheses
                result, operator = 0, 1
            # Handle closing parentheses
            elif s[index] == ")":
                # The result inside the parentheses is multiplied by the operator before the parentheses
                result *= stack.pop()
                # Add the result inside the parentheses to the result before the parentheses
                result += stack.pop()
            # Move to the next character
            index += 1
      
        return result  # Return the evaluated result
