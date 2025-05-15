class multiplefunctions():
 def Subfields():
    subfieldlist=[
                  "Machine Learning",
                  "Neural Networks", 
                  "Vision",
                  "Robotics",
                  "Speech Processing",
                  "Natural Language Processing"
                 ]
    print("Sub-fields in AI are:")
 for subfields in subfieldlist:
     print(subfields)

 def OddEven(num):
    if ((num%2)==0):
        print("Enter a number:",num)
        print(num,"is even number")
    else:
         print(num,"is odd number")

 def Elegible():
     gender="Male"
     age=18
     print("Your Gender:",gender)
     print("Your Age:",age)
     if (gender=="Male"and age>=21) or(gender=="Female"and age>=18):
         print("ELIGIBLE")
     else:
         print("NOT ELIGIBLE")   

 def percentage():
    subject1 = 23
    subject2 = 45
    subject3 = 34
    subject4 = 23
    subject5 = 23
    print("Enter marks for Subject 1:",subject1)
    print("Enter marks for Subject 2:",subject2)
    print("Enter marks for Subject 3:",subject3)
    print("Enter marks for Subject 4:",subject4)
    print("Enter marks for Subject 5:",subject5)
    total = subject1 + subject2 + subject3 + subject4 + subject5
    percentage = (total / 500) * 100
    print("Total:", total)
    print("Percentage:", percentage)

 def triangle():
    height = 3
    breadth = 4
    print("height=",height)
    print("breadth=",breadth)
    Areaformula=(height*breadth)/2
    print("Area formula: (Height*Breadth)/2 ")
    print("Area of triangle:",Areaformula)
    height1 =3
    height2 =4
    breadth =45
    print("height1 =",height1)
    print("height2=",height2)
    print("breadth=",breadth)
    perimeter = height1 + height2 + breadth
    print("Perimeter formula: Height1+Height2+Breadth")
    print("Perimeter of Triangle:", perimeter)
    