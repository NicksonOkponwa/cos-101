def a():
    displacement=int(input("what is the displacement???"))
    time=int(input('what is time???'))
    #velocity=displacement/time
    output=str(displacement/time)
    print(output+"m/s")

def b():
    mass=float(input("input your mass:"))
    gravity=float(input("input your gravity:"))
    #weight=mass*gravity
    output=(mass*gravity)
    print(output+"N")
def c():
    force=int(input('what is force???'))
    distance=int(input("what is distance???"))
    #power=force*distance
    output=str(force*distance)
    print(output+'Watt')

def d():
    length=int(input("what is length???"))
    breadth=int(input("what is breadth???"))
    #area of rectangle=length*breadth
    output=str(length*breadth)
    print(output+"cm^2")

def e():
    distance=float(input("what is distance???"))
    time=float(input("what is time???"))
    #speed=distance/time
    output=str(distance/time)
    print(output+"m/s")

def main():
    user_choice=input("choose from a-e:")
    if user_choice == "a":
        a()
    elif user_choice == "b":
        b()
if __name__ == "__main__":
    main()


