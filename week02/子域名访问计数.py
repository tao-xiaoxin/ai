# 子域名访问计数
from collections import Counter


class Solution:
    def subdomainVisits(self, cpdomains):
        def cpdomain_counter(cpdomain):
            count, domain = cpdomain.split(' ')  # 拆分次数和域名
            substr = domain.split('.')
            domain_list = ['.'.join(substr[i:]) for i in reversed(range(len(substr)))]  # 获得所有子域名
            return Counter({domain: int(count) for domain in domain_list})

        counter = Counter({})
        for cpdomain in cpdomains:
            counter += cpdomain_counter(cpdomain)

        return [str(c) + ' ' + d for d, c in counter.items()]
