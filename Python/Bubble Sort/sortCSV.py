# python argtest.py --fin datain --fout dataout


import sys

def genSortKey(col,up):
   def key(x):
      if up == '+':
         return x[col]
      elif up == '-':
         return -x[col]
   return key

def main():
   FIN=""
   FOUT=""
   COL=""
   DIR=""
   nargs=len(sys.argv)
   skip=False
   for i in range(1,nargs):
      if not skip:
         arg=sys.argv[i]
         print("INFO: processing",arg)
         if arg == "--fin":
            if i != nargs-1:
               FIN=sys.argv[i+1]
               skip=True
         elif arg == "--fout":
            if i != nargs-1:
               FOUT=sys.argv[i+1]
               skip=True
         elif arg == "--col":
            if i != nargs-1:
               COL=sys.argv[i+1]
               skip=True
         elif arg == "--dir":
            if i != nargs-1:
               DIR=sys.argv[i+1]
               skip=True
         else:
            print("ERR: unknown arg:",arg)
      else:
         skip=False

   print("INFO: FIN",FIN)
   print("INFO: FOUT",FOUT)
   print("INFO: COL",COL)
   print("INFO: DIR",DIR)
   accum = []
   try:
      f=open(FIN,'r')
   except:
      print("ERR: file",FIN,"does not exist or cannot be opened")
      return False
   try:
      g=open(FOUT,'w')
   except:
      print("ERR: file",FOUT,"could not be created")
   try:
      COL = int(COL)
   except:
      print("ERR: input",COL,"is a non-integer")
      return False
   if ((DIR != "+") and (DIR != "-")):
      print("ERR: dir",DIR,"is invalid")
      return False
   sortKey = genSortKey(COL,DIR)

   #try:
   #   f=open(FIN,'r')
   #except:
   #   print("ERR: file",FIN,"does not exist or cannot be opened")
   #   return False
   lines = f.readlines()
   try:
      for line in lines:
         j = line.split('\n')[0]
         k = j.split(',')
         r = []
         for i in k:
            r += [float(i)]
         accum += [r]
   except:
      print("ERR: non-numeric values in",FIN)
      return False
   #try:
   #   g = open(FOUT,'w')
   #except:
   #   print("ERR: file",FOUT,"could not be created")
   #   return False
   for i in accum:
      if COL > len(i)-1:
         print("ERR: --col",COL,"out of range")
         g.write("")
         return False
   
   sortedList = sorted(accum,key=sortKey)
   csv = []
   for row in range(0,len(sortedList),1):
      csv += [""]
      for i in sortedList[row]:
         csv[row] += str(i) + ","
      csv[row]=csv[row][0:len(csv[row])-1]
      csv[row] += "\n"
   for i in csv:
      g.write(str(i))
   return True

main()
