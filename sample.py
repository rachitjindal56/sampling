import re
import string

x = "  Government of India  "
print(re.sub("\n+"," ",x.lower()).lstrip())