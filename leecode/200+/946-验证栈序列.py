class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        for i in pushed:
            stack.append(i)
            while popped and stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        return not popped
