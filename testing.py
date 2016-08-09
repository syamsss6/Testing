import prgm

total=0
passed=0
failed=0
for i in dir(prgm):
 f=getattr(prgm,i)
 if(callable(f) and f.__name__.startswith('test_')):
   if f():
     passed+=1
  
   else:
      failed+=1
print "Total:",passed+failed
print "passed:",passed
print "failed:",failed
