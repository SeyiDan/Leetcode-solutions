class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = [] #store indices of '('
        to_remove = set() #store indices for parenthesis to remove

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            if char == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)
            
        to_remove.update(stack)

        result = ''.join(char for i, char in enumerate(s) if i not in to_remove)
        return result


            












































        # stack = [] #store indices of the unmatch '('
        # to_remove = set() #indices to remove

        # #pass 1: Find all invalid parenthesis
        # for i, char in enumerate(s):
        #     if char == '(':
        #         stack.append(i) #Track opening parenthesis index
        #     elif char == ')':
        #         if stack:
        #             stack.pop() # Matched! Remove the '(' from stack
        #         else:
        #             to_remove.add(i)  # Unmatched ')' - mark for removal

        # # After pass 1, stack contains unmatched '(' indices            
        # to_remove.update(stack) # Mark all unmatched '(' for removal

        # result = ''.join(char for i, char in enumerate(s) if i not in to_remove)
        # return result
        
