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
                        #if(temp[row][column]==0):
                            #temp[row][column] = np.nan
                            #print(temp[row])
            #print(temp)
            t=t+1
        return(temp)

    def FindL(self, A, L):
        #temp = np.zeros((3, 3))
        temp=A
        t=0
        t3=-1
        for i in range(len(A)-1):

            for row in range(t, len(A)):

                t0 = temp[row][t] / temp[t][t]
                t3 = t3+1
                for column in range(len(A[0])):
                    if(row>t):
                        #print("row ", row, "---column", column, "temp",temp[row][t]/temp[t][t] )
                        #L[row][column] = temp[row][column] / temp[row-1][column]
                        if(temp[row][column] - ((t0)*temp[t][column])==0):
                            if(L[row][column]==0):
                                L[row][column] = temp[row][column]/temp[row-t3][column]
                        temp[row][column] = temp[row][column] - ((t0)*temp[t][column])
                #print("temp",temp)
            t = t + 1

        return(L)

