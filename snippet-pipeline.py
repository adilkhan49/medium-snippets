import pandas as pd

def logTime():
  print(pd.to_datetime('now'),end='\t')

def MoveToDev(mv=False, source = '/mnt/ftp/', debug=False):

# Initialise file counter

  count = 0
  
# Log start of process
  
  logTime()
  print('{0} from {1}...'.format('Moving' if mv else 'Copying', source))
  
# Loop through all files in directory

  for i in dbutils.fs.ls(source)[:]:
    
# Parse metadata

    name = i.name
    path = i.path
    destination = 'mnt/ftp-dev'
    month = name[-21:-15]
    date = name[-21:-13]  
    target = '/{0}/{1}/{2}/{3}'.format(destination,month,date,name)

# File transfer (mv removes files from source, cp does not)

    if mv:
      try:
        dbutils.fs.mv(path,target)
      except:
        logTime()
        print('Failed to move file {}'.format(path))
        raise Exception ('Failed to move file {}'.format(path))
      
    else:
      try:
        dbutils.fs.cp(path,target)
      except:
        logTime()
        print('Failed to copy file {}'.format(path))
        raise Exception ('Failed to copy file {}'.format(path))
      
    if debug:
      logTime()
      print('{0} file {1}'.format('Moved' if mv else 'Copied', name))      
    count+=1
    
# Log number of files transfered  

  logTime()
  print('{0} files {1} from {2}.'.format(count,'moved' if mv else 'copied',source))
