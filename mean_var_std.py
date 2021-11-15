import numpy as np

def calculate(list):
  #checking the length of the list 
  if len(list)!=9:
    raise ValueError("List must contain nine numbers.")
  else:
  #converting list into a numpy array
    matrix=np.array(list).reshape(3,3)#reshaping the array to  3x3 matrix
  
  #getting the required statistics in nested list form
    mean=[(matrix.mean(axis=0).tolist()),(matrix.mean(axis=1).tolist()),(matrix.flatten().mean())]
  #the markdown example shows column wise calculation first thus axis=0
  #the .tolist() function is to match output requirmenets of value in the form of list in the dictionary 
    
    variance=[(matrix.var(axis=0).tolist()),(matrix.var(axis=1).tolist()),(matrix.flatten().var())]

    standard_deviation=[(matrix.std(axis=0).tolist()),(matrix.std(axis=1).tolist()),(matrix.flatten().std())]

    max_matrix=[(matrix.max(axis=0).tolist()),(matrix.max(axis=1).tolist()),(matrix.flatten().max())]

    min_matrix=[(matrix.min(axis=0).tolist()),(matrix.min(axis=1).tolist()),(matrix.flatten().min())]

    sum_matrix=[(matrix.sum(axis=0).tolist()),(matrix.sum(axis=1).tolist()),(matrix.flatten().sum())]

  #output in the form of dictionary 
  calculations= {
    'mean': mean,
    'variance':variance,
    'standard deviation': standard_deviation,
    'max': max_matrix,
    'min': min_matrix,
    'sum': sum_matrix,
  }

  return calculations
