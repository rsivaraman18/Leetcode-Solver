print("Ready")
name = "siva"
job = "Python developer"

print(f'My name is {name} and job is {job}')
print("My name is {1} and job is {0}".format(job,name))
print("My name is {a} and job is {b}".format(a=job,b=name))

data = {
            'name':'siva',
            'job':'Developer',
            'car':'scropio'

}

for item in data.items():
    x,y = item
    print(x,'-->',y)

for item in data.values():
    print(item)

for item in data.keys():
    print(item)

print()

def greet(**data):
    print(data)

greet(hello=124,nanban=232)