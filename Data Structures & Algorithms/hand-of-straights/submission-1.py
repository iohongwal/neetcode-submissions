class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        hand_freq = Counter(hand)
        hand_minHeap = list(hand_freq.keys())
        heapq.heapify(hand_minHeap)

        while hand_minHeap:

            num = hand_minHeap[0]
            
            for i in range(num, num + groupSize):
                if i not in hand_freq:
                    return False
                hand_freq[i] -= 1

                if hand_freq[i] == 0:
                    if i != hand_minHeap[0]:
                        return False
                    heapq.heappop(hand_minHeap)
                

        return True

