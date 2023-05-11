import pyRAPL
import numpy as np
 
# input two matrices
mat1 = ([1, 6, 5,6,7,8,9],[1, 6, 5,6,7,8,9],[1, 6, 5,6,7,8,9],[1, 6, 5,6,7,8,9],[1, 6, 5,6,7,8,9],[1, 6, 5,6,7,8,9],[1, 6, 5,6,7,8,9])
mat2 = ([1, 6, 5,6,7,8,9],[1, 6, 5,6,7,8,9],[1, 6, 5,6,7,8,9],[1, 6, 5,6,7,8,9],[1, 6, 5,6,7,8,9],[1, 6, 5,6,7,8,9],[1, 6, 5,6,7,8,9])
mat3 = ([1, 6, 5,6,7,8,9],[1, 6, 5,6,7,8,9],[1, 6, 5,6,7,8,9],[1, 6, 5,6,7,8,9],[1, 6, 5,6,7,8,9],[1, 6, 5,6,7,8,9],[1, 6, 5,6,7,8,9])
 
# This will return dot product
#res = np.dot(mat1,mat2)

#pyRAPL.setup(devices=[pyRAPL.Device.PKG], socket_ids=[1,2])
pyRAPL.setup()
csv_output = pyRAPL.outputs.CSVOutput('result.csv')

@pyRAPL.measureit(output=csv_output)
def foo():
  # Instructions to be evaluated.
  res = np.dot(mat1,mat2)
  res =np.dot(res,mat3)
  return res
for _ in range(1000):
  foo()
csv_output.save()
