#----------------
# netflix_predict
#----------------
def netflix_predict(c_id,m_id):
  '''
  c_id - customer id
  m_id - movie id
  '''
  
  
  return 0
#-------------
# netflix_rsme
#-------------

def netflix_rmse(p,a):
  '''
  p - iterable of preictions for ratings
  a - iterable of actual ratings
  '''
  
  return 0
  
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
 
  while True:
    s = r.readline().strip()
    
    m_id = 0
    
    if len(s) == 0:
       break 
    
    if (':' in s):
      m_id = s
    else:
      c_id = s
    
    p = netflix_predict(c_id, m_id)
    
    w.write(str(p) + '\n')   
    
    
      
  
  
  
