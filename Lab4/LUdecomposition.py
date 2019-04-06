import numpy as np
class LuDecomposition:
    #A = [[2, -1, -2],
    #     [-4, 6, 3],
    #     [-4, -2, 8]]
    def GaussianElimination(self, A):
        #temp = np.zeros((3, 3))
        temp=A
        t=0
        for i in range(len(A)-1):
            for row in range(t, len(A)):
                t0 = temp[row][t] / temp[t][t]

                for column in range(len(A[0])):
                    if(row>t):
                        #print("row ", row, "---column", column, "temp",temp[row][t]/temp[t][t] )
                        temp[row][column] = temp[row][column] - ((t0)*temp[t][column])
                        #print(temp[row])
            #print(temp)
            t=t+1
        return(temp)



