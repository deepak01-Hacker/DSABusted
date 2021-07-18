class Solution(object):
    def myPow(self, x, y):
        if y < 0:
            y = -y
            x = 1/x
        
        result = 1;
        while (y > 0):
            if (y % 2 == 0):

                x = x * x;
                y = y / 2;
            else:

                result = result * x;
                y = y - 1;


        return result;
