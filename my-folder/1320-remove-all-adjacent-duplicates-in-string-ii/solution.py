class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1]+=1

                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char,1])
        
        result = "".join(char * count for char,count in stack)
        return result





























        # stack = [] #store [character,count] pairs

        # for char in s:
        #     # If stack is not empty and top character matches current
        #     if stack and stack[-1][0] == char:
        #         stack[-1][1]+=1

        #         # If count reaches k, remove this group
        #         if stack[-1][1] == k:
        #             stack.pop()
        #     else:
        #        # Different character, push new entry
        #         stack.append([char,1])

        # # Build result string from stack
        # result = (char *count for char, count in stack )
        # return result
        

            

        
