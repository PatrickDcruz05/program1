print('WELCOME TO AREA AND VOLUME CALCULATOR')
x=input("ENTER YOUR DESIRED OPERATION(VOLUME/AREA):").upper()
if x=="AREA":
    print("1.CIRCLE")
    print("2.SQUARE")
    print("3.TRIANGLE")
    print("4.RECTANGLE")
    print("5.TRAPEZIUM")
    print("6.PARALLELOGRAM")
    choice=input("ENTER YOUR SHAPE:").upper()
    if choice=="CIRCLE":
         Radius=float(input('ENTER THE RADIUS OF THE CIRCLE:'))
         area_of_the_circle= (3.14*(Radius**2))
         print("THE AREA OF THE CIRCLE IS",area_of_the_circle)
    elif choice=="SQUARE":
         length=float(input("ENTER THE LENGTH OF THE SIDE OF A SQUARE:"))
         area_of_the_square=(length**2)
         print("THE AREA OF THE SQUARE IS",area_of_the_square)
    elif choice=="TRIANGLE":
         length=float(input("ENTER THE LENGTH OF THE TRIANGLE:"))
         breadth=float(input("ENTER THE BREADTH OF THE TRIANGLE:"))
         area_of_the_triangle=(0.5*(length*breadth))
         print("THE AREA OF THE TRIANGLE IS",area_of_the_triangle)
    elif choice=="RECTANGLE":
         length=float(input("ENTER THE LENGTH OF THE  RECTANGLE:"))
         breadth=float(input("ENTER THE BREADTH OF THE RECTANGLE:"))
         area_of_the_rectangle=(length*breadth)
         print("THE AREA OF THE RECTANGLE IS",area_of_the_rectangle)
    elif choice=="TRAPEZIUM":
         base1=float(input("ENTER THE BASE 1 OF THE TRAPEZIUM:"))
         base2=float(input("ENTER THE BASE 2 OF THE TRAPEZIUM:"))
         height=float(input("ENTER THE HEIGHT OF THE TRAPEZIUM:"))
         area_of_the_trapezium=(((base1+base2)/2)*height)
         print("THE AREA OF THE TRAPEZIUM IS",area_of_the_trapezium)
    elif choice=="PARALLELOGRAM":
         base=float(input("ENTER THE BASE OF THE PARALLELOGRAM:"))
         height=float(input("ENTER THE HEIGHT OF THE PARALLELOGRAM:"))
         area_of_the_parallelogram=(base*height)
         print("THE AREA OF THE PARALLELOGRAM IS",area_of_the_parallelogram)
    else:
         print("PLEASE ENTER THE CORRECT INPUT")
elif x=="VOLUME":
    print("1.CUBE")
    print("2.CUBOID")
    print("3.CONE")
    print("4.SPHERE")
    print("5.CYLINDER")
    choice=input("ENTER YOUR SHAPE:").upper()
    if choice=="CUBE":
         A=float(input("ENTER THE VALUE FOR A:"))
         volume_of_the_cube=(A**3)
         print("THE VOLUME OF THE CUBE IS",volume_of_the_cube)
    elif choice=="CUBOID":
         length=float(input("ENTER THE LENGTH OF CUBOID:"))
         width=float(input("ENTER THE WIDTH OF CUBOID:"))
         height=float(input("ENTER THE HEIGHT OF CUBOID:"))
         volume_of_the_cuboid= (width*length*height)
         print("THE VOLUME OF THE CUBOID IS",volume_of_the_cuboid) 
    elif choice=="CONE":
         radius=float(input("ENTER THE RADIUS OF THE CONE:"))
         height=float(input("ENTER THE HEIGHT OF THE CONE:"))
         volume_of_the_cone=((1/3)* 3.14* radius**2 * height)  
         print("THE VOLUME OF THE CONE IS",volume_of_the_cone)    
    elif choice=="SPHERE":
         radius=float(input("ENTER THE RADIUS OF THE SPHERE:"))
         volume_of_the_sphere=(((4/3)*3.14)*radius**3)
         print("THE VOLUME OF THE SPHERE IS",volume_of_the_sphere)
    elif choice=="CYLINDER":
         radius=float(input("ENTER THE RADIUS OF THE CYLINDER:"))
         height=float(input("ENTER THE HEIGHT OF THE CYLINDER:"))
         volume_of_the_cylinder=((3.14*radius**2) *height)
         print("THE VOLUME OF THE CYLINDER IS",volume_of_the_cylinder)
    else:
         print("PLEASE ENTER THE CORRECT INPUT")
else:
    print("SELECT THE CORRECT FUNCTION TO EXECUTE")
