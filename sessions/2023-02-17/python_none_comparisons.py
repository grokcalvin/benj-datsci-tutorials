
# Technically works
if None == None:
    print("True")

if not (None != None):
    print("False")

# Pythonic way to compare "None"
if None is None:
    print("True")

if not (None != None):
    print("False")
