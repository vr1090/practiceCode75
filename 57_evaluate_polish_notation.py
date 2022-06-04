class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.i = len(tokens) -1
        print(tokens)
        
        def evaluate():    
            token = tokens[self.i]
            isOperator = token in ["+","-","*","/"]
            self.i = self.i - 1
            
            if not isOperator:
                return int(token)
            else:
                right = evaluate()
                left = evaluate()
                
                if token == "+":
                    return int(left + right)
                elif token == "-":
                    return int(left - right)
                elif token == "*":
                    return int(left * right)
                elif token == "/":
                    return int(left / right)
                else:
                    return 0
        
        return evaluate()
                
         