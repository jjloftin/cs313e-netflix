import json


#----------------
# netflix_predict
#----------------
def netflix_predict(m_avg, c_avg):
  '''
  c_id - customer id
  m_id - movie id
  p = prediction
  '''
  
  '''
  Give a base rating. Calculate difference of movie and customer averages from the base. Weight them and add to base rating.
  '''
  base = 3.6
  m_diff = m_avg - base
  c_diff = c_avg - base
  
  p = base + 0.7*m_diff + 0.3*c_diff
 
  
  return p
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

  
  probe_data.close()
  '''
  Calulate and return the RMSE
  '''
  sum = 0
  for key in p:
    sum += (p[key] - probe_dict[key])**2
  
  
  return (sum/len(p))**0.5

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
 
  c_avgs = open('zwf69-TCustRatings.txt','r') 
  c_avg_dict = {}
  
  i = 0
  
  for line in c_avgs:
    s = line.strip().split(',')
    c_avg_dict[s[0]] = eval(s[1])

  c_avgs.close()
   
  m_avgs = open('sp35972-MovieAvg.txt','r')
  m_avg_dict = {}
  
  for line in m_avgs:
    s = line.strip().split(':')
    m_avg_dict[s[0]] = eval(s[1])
  
  
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
    
    p = netflix_predict(m_avg_dict[m_id], c_avg_dict[c_id])
   
    prediction_dict[m_id,c_id] = p 
    
    w.write(str(p) + '\n')
    
  
  rmse = int(netflix_rmse(prediction_dict) * 100) / 100
  w.write(str(rmse))  
    
    
      
  
  
  
