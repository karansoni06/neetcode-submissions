
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        most_common = count.most_common(k)

        result = []

        for item in most_common:
            result.append(item[0])

        return result