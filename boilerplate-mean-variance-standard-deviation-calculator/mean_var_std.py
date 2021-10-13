import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers")

  arr = np.reshape(list, (3,3))
  calculations = {'mean':[],'variance':[],'standard deviation':[],'max':[],'min':[],'sum':[]}

## calculating for axis1
  axis1_mean = []
  axis1_var = []
  axis1_sd = []
  axis1_max = []
  axis1_min = []
  axis1_sum = []
  for a in range(3):
    val = arr[:,a]
    axis1_mean.append(np.mean(val))
    axis1_var.append(np.var(val))
    axis1_sd.append(np.std(val))
    axis1_max.append(np.amax(val))
    axis1_min.append(np.amin(val))
    axis1_sum.append(np.sum(val))

  ## calculating for axis2
  axis2_mean = []
  axis2_var = []
  axis2_sd = []
  axis2_max = []
  axis2_min = []
  axis2_sum = []
  for a in range(3):
    val = arr[a,:]
    axis2_mean.append(np.mean(val))
    axis2_var.append(np.var(val))
    axis2_sd.append(np.std(val))
    axis2_max.append(np.amax(val))
    axis2_min.append(np.amin(val))
    axis2_sum.append(np.sum(val))

  #calculating for flattened
  flat_mean = np.mean(arr)
  flat_var = np.var(arr)
  flat_sd = np.std(arr)
  flat_max = np.amax(arr)
  flat_min = np.amin(arr)
  flat_sum = np.sum(arr)

  #updating the values in my calculations dictionary
  calculations['mean'] = [axis1_mean, axis2_mean, flat_mean]
  calculations['variance'] = [axis1_var, axis2_var, flat_var]
  calculations['standard deviation'] = [axis1_sd, axis2_sd, flat_sd]
  calculations['max'] = [axis1_max, axis2_max, flat_max]
  calculations['min'] = [axis1_min, axis2_min, flat_min]
  calculations['sum'] = [axis1_sum, axis2_sum, flat_sum]

  
  return calculations