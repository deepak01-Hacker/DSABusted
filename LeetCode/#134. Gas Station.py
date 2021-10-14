class Solution(object):
       
    def canCompleteCircuit(self, gas, cost):
        temp = 0
        size = 0

        for i in range(len(gas)):

            temp += gas[i]-cost[i]

            if temp > gas[i]-cost[i]:
                size += 1
            else:
                size = 1

            temp = max(temp,gas[i]-cost[i])

            if i == len(cost)-1 :

                if temp < 0 and gas[i]-cost[i] < 0:
                    return -1

        if size == len(cost):
            return 0

        for i in range(len(cost)-size):

            temp += gas[i]

            if temp < cost[i]:
                return -1

            temp -= cost[i]

        return len(cost)-size
