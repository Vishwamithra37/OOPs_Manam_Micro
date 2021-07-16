
from version2 import a1
import json
from nested_dictionaries import NestedDictionaries as nd
me=nd()
me["auth"]["token"]="telanganga"
me["auth"]["number"]="15623580"
me["auth"]["state"]="biharis"
r=a1.tcheker(me)
print(r)