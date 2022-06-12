class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res_com = []
        def backtracking(left,right,com_list):
            if len(com_list) == 2*n:
                res_com.append("".join(com_list))
            else:
                #先添加左括号
                if left < n:
                    com_list.append("(")
                    backtracking(left+1,right,com_list)
                    com_list.pop()
                #当左括号的数量大于右括号的时候再添加右括号
                if left > right:
                    com_list.append(")")
                    backtracking(left,right+1,com_list)
                    com_list.pop()
        backtracking(0,0,[])
        return res_com

solution = Solution()
print(solution.generateParenthesis(3))
