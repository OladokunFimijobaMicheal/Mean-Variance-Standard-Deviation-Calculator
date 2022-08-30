import numpy as np

def calculate(list):

    if len(list) != 9:
        raise  ValueError("List must contain nine numbers.")

    functions = {'mean': 'np.mean',
                'variance': 'np.var',
                'standard deviation': 'np.std',
                'max': 'np.max',
                'min': 'np.min',
                'sum': 'np.sum'}

    x = np.array(list).reshape((3,3))

    calculations = dict()
    for key, value in functions.items():
        calculations[key] = [eval(value + '(x, axis = 0)').tolist(), \
                             eval(value + '(x, axis = 1)').tolist(), \
                             eval(value + '(x)')]

    return calculations



   
    
    























    


    