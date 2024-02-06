class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        commons_index_sum = {word: 0 for word in set(list1).intersection(set(list2))}
        for i in range(len(list1)):
            if list1[i] in commons_index_sum:
                commons_index_sum[list1[i]] += i
        for j in range(len(list2)):
            if list2[j] in commons_index_sum:
                commons_index_sum[list2[j]] += j
        least_index_commons = []
        index_sum = len(list1) + len(list2)
        for common in commons_index_sum:
            if commons_index_sum[common] < index_sum:
                least_index_commons = [common]
                index_sum = commons_index_sum[common]
            elif commons_index_sum[common] == index_sum:
                least_index_commons.append(common)
        return least_index_commons
