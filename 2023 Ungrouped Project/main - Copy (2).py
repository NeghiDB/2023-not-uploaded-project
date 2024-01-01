import glob

print('Name of document:')

for name in glob.glob('*'):
    print(name)

input()
