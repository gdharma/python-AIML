import wikipedia

import sys
searchWIKI=searchquery=" ".join(sys.argv[1:])
print(wikipedia.summary(searchWIKI,sentences=2))
