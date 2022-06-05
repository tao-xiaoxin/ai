class Solution:
    def plusOne(self, digits):
        number = 0
        lst = []
        n = len(digits)
        for i in range(n):
            if i != n - 1:
                number += digits[i] * (10 ** ((n - 1) - i))
            else:
                number += digits[i] + 1

        for j in range(len(str(number))):
            lst.append(int(str(number)[j]))
        return lst


if __name__ == '__main__':
    s = Solution()
    c = [4, 3, 2, 1]
    print(s.plusOne(c))
