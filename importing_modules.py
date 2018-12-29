#importing mymodule
import mymodule
import sys
subjects = ['hindi', 'math', 'english', 'physics']

ind = mymodule.find_index(subjects, 'telugu')
print(ind)

print(sys.path)