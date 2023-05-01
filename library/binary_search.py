def binary_search(seq,key):
  left=0
  right=len(seq)-1
  
  while(left<=right):
    pivot=(right+left)//2
    if seq[pivot]==key:return pivot 
    elif seq[pivot]<key:
      left=pivot+1
    else:     
      right=pivot-1
      
    return -1
  