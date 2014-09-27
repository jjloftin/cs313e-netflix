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
  

  base = 3.65
  
  m_diff = m_avg - base
  c_diff = c_avg - base

  p = base + 0.7*m_diff + 0.3*c_diff
  
  if(p > 5):
    return 5
  elif(p < 1):
    return 1
  
  return p
#-------------
# netflix_rsme
#-------------

def netflix_rmse(p,a):
  '''
  p - iterable of preictions for ratings
  '''
  

  '''
  Calulate and return the RMSE
  '''
  
  assert len(p) <= len(a)
  
  sum = 0
  for key in p:
    sum += (p[key] - a[key])**2
  
  assert sum >= 0
  
  return (sum/len(p))**0.5


#--------------
# netflix_solve
#--------------
def netflix_solve(r, w):

  '''
  reads in from a reader, writes predictions to a writer
  r a reader
  w a writer
  '''
  
  #create dictionary of average customer ratings. dict[CustomerID] = average rating for customer ID
  c_avgs = open('/u/prat0318/netflix-tests/zwf69-TCustRatings.txt','r') 
  c_avg_dict = {}

  
  for line in c_avgs:
    s = line.strip().split(',')
    c_avg_dict[s[0]] = eval(s[1])

  c_avgs.close()
   
  #create dictionary of average movie ratings. dict[MovieID] = average rating for movie ID
  m_avgs = open('/u/prat0318/netflix-tests/sp35972-MovieAvg.txt','r')
  m_avg_dict = {}
  
  for line in m_avgs:
    s = line.strip().split(':')
    m_avg_dict[s[0]] = eval(s[1])
  
  #initiailize dictionary of movie rating predictions. dict[MovieID,CustomerID] = predicted rating of Movie ID for Customer ID
  prediction_dict = {}
  
  c_id = 0
  m_id = 0
  
  #Place predictions in prediction dict and write MovieID's and predictions to writer 
  
  for line in r:
  
    s = line.strip()
 
    #check to see if line is movie ID 
    if (':' in s):
      m_id = s[:-1]
      w.write(str(m_id) + ': \n')
      continue
    else:
      c_id = s
    
    
    
    p = netflix_predict(m_avg_dict[m_id], c_avg_dict[c_id])
    
    w.write(str(p) + '\n')
    
    
    prediction_dict[m_id,c_id] = p 
    
    
  
  #Make dictonary of actual ratings dict[movieID, customerID] = actual rating
  probe_data = open('/u/prat0318/netflix-tests/cct667-ProbeCacheAnswers.txt', 'r')
  probe_dict = {}
  for line in probe_data:
    s = line.strip().split()
    #associate [movieID,customerID] with rating
    probe_dict[s[0],s[1]] = eval(s[2])

  
  probe_data.close()
  
  rmse = int(netflix_rmse(prediction_dict, probe_dict) * 100) / 100
  w.write('RMSE: ' + str(rmse))  