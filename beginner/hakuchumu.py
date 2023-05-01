S=input()

tmp_index=0
flag="YES"
while(tmp_index<len(S)):
  
  if S[tmp_index:tmp_index+6]=="eraser":
    tmp_index+=6
  elif S[tmp_index:tmp_index+5]=="erase" :
    tmp_index+=5
  elif S[tmp_index:tmp_index+7]=="dreamer"  and S[tmp_index+7]!="a":
    tmp_index+=7
  elif S[tmp_index:tmp_index+5]=="dream"  :
    tmp_index+=5
  else:
    flag="NO"
    break
print(flag)