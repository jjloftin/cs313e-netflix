import json


#----------------
# netflix_predict
#----------------
def netflix_predict(m_id,c_id):
  '''
  c_id - customer id
  m_id - movie id
  '''
  base = 3.7
  
  
  
  return 3.65
#-------------
# netflix_rsme
#-------------

def netflix_rmse(p):
  '''
  p - iterable of preictions for ratings
  '''
  
  '''
  Make the necessary lists from the probe data
  '''
  probe_data = open('cct667-ProbeCacheAnswers.txt', 'r')
  probe_dict = {}
  for line in probe_data:
    s = line.strip().split()
    #associate [movieID,customerID] with rating
    probe_dict[s[0],s[1]] = eval(s[2])

  
  '''
  Calulate and return the RMSE
  '''
  sum = 0
  for key in p:
    sum += (p[key] - probe_dict[key])**2
  
  
  return (sum/len(p))**0.5
#-------------
# netflix_read
#-------------
def netflix_read(r):
   return r.readline().strip()

#-------------
# netlix_print
#-------------
def netflix_print(w, pc):
   '''
   w - writer
   p - prediction or customer id
   write prediction to writer
   '''
   
   w.write(str(pc) + '\n')

#--------------
# netflix_solve
#--------------
def netflix_solve(r, w):

  '''
  reads in from a reader, writes predictions to a writer
  r a reader
  w a writer
  '''
 
  prediction_dict = {}
  
  c_id = 0
  m_id = 0
  
  while True:
  
    s = r.readline().strip()
    
    if len(s) == 0:
       break 
    #check to see if line is movie ID 
    if (':' in s):
      m_id = s[:-1]
      w.write(str(m_id) + ': \n')
      continue
    else:
      c_id = s
    
    p = netflix_predict(m_id, c_id)
   
    prediction_dict[m_id,c_id] = p 
    
    w.write(str(p) + '\n')
    
  
  rmse = netflix_rmse(prediction_dict)
  w.write(str(rmse))  
    
    
      
  
  
  
