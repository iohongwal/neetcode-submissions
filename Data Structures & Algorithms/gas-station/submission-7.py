class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1

        tank = 0
        start = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i + 1
                continue

        return start

        # for i in range(len(gas)):
        #     tank = gas[i] - cost[i]

        #     if tank < 0:
        #         continue
            
        #     j = (i + 1) % len(gas)

        #     while i != j:
        #         tank += gas[j]
        #         tank -= cost[j]
        #         if tank < 0:
        #             break
                
        #         j += 1 
        #         j %= len(gas)

        #     if i == j:
        #         return i

        # return -1

        # for i in range(len(gas)):
        #     tank = gas[i]
        #     spend = cost[i] 
        #     if cost[i] > tank:
        #         continue
        #     j = 0 if (i + 1) >= len(gas) else i + 1
        #     tank = tank - spend + gas[j]
        #     spend = cost[j]
        #     while tank >= spend and i != j:
        #         j = 0 if (j + 1) >= len(gas) else j + 1
        #         tank = tank - spend + gas[j]
        #         spend = cost[j]
            
        #     if i == j:
        #         return i

        # return -1

