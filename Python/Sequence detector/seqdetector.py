from seqdetectorlib import *
def main():
   x=seqdetector()
   n=0
   for i in words_list:
      status=x.evolve(i) 
      if status == True:
         print("Detected: end position is",n)
      n = n+1
   return True

words_list = ["here","","here","are","the","solutions","to","the","next","exam"]
main()

