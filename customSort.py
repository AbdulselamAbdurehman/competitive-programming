class Solution:
    def customSortString(self, order: str, s: str) -> str:
        custom_order = {order[i]: i for i in range(len(order))}
        result = sorted(s, key=lambda item: custom_order.get(item, 26))
        return ''.join(result)
