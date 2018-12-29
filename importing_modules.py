# importing mymodule

import mymodule
import os


subjects = ['hindi', 'math', 'english', 'physics']


ind = mymodule.find_index(subjects, 'telugu')
print(ind)

print(dir(os))