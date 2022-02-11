import numpy as np

def calculate(list):

    if len(list) == 9:
        a = np.array(list).reshape(3,3)

        #Calculation mean across Row, Column and whole array
        m0 = a.mean(axis = 0).tolist()
        m1 = a.mean(axis = 1).tolist()
        m = a.mean()
        #Variance
        v0 = a.var(axis = 0).tolist()
        v1 = a.var(axis = 1).tolist()
        v = a.var()
        #Standar deviation
        s0 = a.std(axis = 0).tolist()
        s1 = a.std(axis = 1).tolist()
        s = a.std()
        #maximum
        mx0 = a.max(axis = 0).tolist()
        mx1 = a.max(axis = 1).tolist()
        mx = a.max()
        #minimum
        mn0 = a.min(axis = 0).tolist()
        mn1 = a.min(axis = 1).tolist()
        mn = a.min()
        #sum
        sm0 = a.sum(axis = 0).tolist()
        sm1 = a.sum(axis = 1).tolist()
        sm = a.sum()

        calculation = {'mean': [m0, m1, m],
                            'variance': [v0, v1, v],
                            'standard deviation': [s0, s1, s],
                            'max': [mx0, mx1, mx],
                            'min': [mn0, mn1, mn],
                            'sum': [sm0, sm1, sm]
                            }
        return calculation

    else:
        raise ValueError(f'List must contain nine numbers, mean_var_std.calculate, {list}')