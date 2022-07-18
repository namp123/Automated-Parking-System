#automated parking system
import re
pattern1 = re.compile(r"Create_parking_lot\s\d+")
pattern2 = re.compile(r"Park\s[A-Z]{2}-\d{2}-[A-Z]{2}-\d{4}\sdriver_age\s\d{2}")
pattern3 = re.compile(r"Slot_numbers_for_driver_of_age\s\d{2}")
pattern4 = re.compile(r"Slot_number_for_car_with_number\s[A-Z]{2}-\d{2}-[A-Z]{2}-\d{4}")
pattern5 = re.compile(r"Leave\s\d+")
pattern6 = re.compile(r"Vehicle_registration_number_for_driver_of_age\s\d{2}")
obj1 = re.compile(pattern1)
obj2 = re.compile(pattern2)
obj3 = re.compile(pattern3)
obj4 = re.compile(pattern4)
obj5 = re.compile(pattern5)
obj6 = re.compile(pattern6)

flag = 0
ageslotreg = []
slots = []

with open('input.txt') as f:
    lines = f.readlines()
    for i in lines:
      if obj1.match(i): #Create_parking_lot 6
        num = str(re.sub("\D", "", i))
        print("Created parking of "+num+" slots")
        
      elif obj2.match(i): #Park KA-01-HH-1234 driver_age 21
        flag = flag+1
        reg_no = i[5:18]
        age = i[29:len(i)-1]
        ageslotreg.append([int(age),flag,reg_no])
        print("Car with vehicle registration number "+reg_no+" has been parked at slot number "+str(flag))
        
      elif obj3.match(i): #Slot_numbers_for_driver_of_age 21
        #print("found")
        age = re.sub("\D", "", i)
        for i in ageslotreg:
          for j in i:
            if j == int(age):
              slots.append(i[1])
              break
        print(slots)

      elif obj4.match(i): #Slot_number_for_car_with_number PB-01-HH-1234
        reg_no = i[32:45]
        for i in ageslotreg:
          if reg_no in i:
            print(i[1])
            break

      elif obj5.match(i): #Leave 2
        flag = 0
        num = re.sub("\D", "", i)
        for i in ageslotreg:
          if int(num) == i[1]:
            flag = 1
            print("Slot number "+str(i[1])+" vacated, the car with vehicle registration number "+i[2]+" left the space, the driver of the car was of age "+str(i[0]))
            ageslotreg.remove(i)
            break

        if flag == 0:
          print("Slot already vacant")

      elif obj6.match(i): #Vehicle_registration_number_for_driver_of_age 18
        flag = 0
        age = re.sub("\D", "", i)
        for i in ageslotreg:
          if i[0] == int(age):
            flag = 1
            print(i[2])
        if flag == 0:
          print("Vehicle registration number for driver of age "+age+" not found")

            
            
        
    
        
              
          
        
        
        
        
        
        
        
      
      
  