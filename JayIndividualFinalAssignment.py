#Final Assignment
#Individual
# Jay Patel

class Doctor:
    
    #declares class objects of doctor class
    def _init_(self):
        self.id = "none"
        self.name = "none"
        self.speciality = "none"
        self.timing = "none"
        self.qualification = "none"
        self.room = "none"
    
    #Formats each doctos information in format used in text file
    def formatDrInfo(self,list_to_convert):
        self.converted_string = '_'.join(list_to_convert)
        return self.converted_string + '\n'

    #Asks user to enter doctor properties
    def enterDrInfo(self):
        self.id = input("Enter the doctor's ID:\n\n")
        self.name = input("Enter the doctor's name:\n\n")
        self.speciality = input("Enter the doctor's specility:\n\n")
        self.timing = input("Enter the doctor's timing (e.g., 7am-10pm):\n\n")
        self.qualification = input("Enter the doctor's qualification:\n\n")
        self.room = input("Enter the doctor's room number:\n\n")
        return [self.id,self.name,self.speciality,self.timing,self.qualification,self.room]

    #reads from doctors text file and fills the doctors object in the list
    def readDoctorsFile(self):
        self.file_open = open('doctors.txt', "r")
        self.element_list = self.file_open.readlines()
        self.file_open.close()
        return self.element_list

    #search doctor by id in list
    def searchDoctorById(self):
        self.doctor_list = self.readDoctorsFile()
        self.current_list = []
        
        for i in range(len(self.doctor_list)):
            self.current_list.append([])
            self.current_list[i] = self.doctor_list[i].split("_")

        self.query = input("\n Enter the doctor ID:\n\n")
        
        self.flag = False
        for i in range(len(self.current_list)):
            if self.current_list[i][0] == self.query:
                self.displayDoctorInfo(self.current_list[i])
                self.flag = True
        if self.flag == False:
            print("Can't find the doctor with the same ID on the system")

    #search doctor by name in list
    def searchDoctorByName(self):
        self.doctor_list = self.readDoctorsFile()
        self.current_list = []
        for i in range(len(self.doctor_list)):
            self.current_list.append([])
            self.current_list[i] = self.doctor_list[i].split("_")

        self.query = input("\n Enter the doctor name:\n\n")
        
        self.flag = False
        for i in range(len(self.current_list)):
            if self.current_list[i][1] == self.query:
                self.displayDoctorInfo(self.current_list[i])
                self.flag = True
        if self.flag == False:
            print("Can't find the doctor with the same name on the system")
    
    #displays doctors information in the line    
    def displayDoctorInfo(self,doctor_list):
        self.doctor_list = doctor_list
        self.doctor_list[4] = self.doctor_list[4].upper() #capitalizes qualifications due to file inconsistancy
        print(f"{'Id': <5}{'Name': <20}{'Specialty': <15}{'Timing': <15}{'Qualification': <15}{'Room Number': <0}"+'\n')
        print(f"{self.doctor_list[0]: <5}{self.doctor_list[1]: <20}{self.doctor_list[2]: <15}{self.doctor_list[3]: <15}{self.doctor_list[4]: <15}{self.doctor_list[5]: <0}")

    #asks the user to enter the id of the doctor to edit 
    def editDoctorInfo(self):
        self.doctor_list = self.readDoctorsFile()
        self.current_list = []
        for i in range(len(self.doctor_list)):
            self.current_list.append([])
            self.current_list[i] = self.doctor_list[i].split("_")

        self.query = input("Please enter the id of the doctor that you want to edit their information:\n\n")
        
        self.flag = False
        for i in range(len(self.current_list)):
            if self.current_list[i][0] == self.query:
                self.new_list[i][1] = input("\nEnter new Name:\n\n")
                self.new_list[i][2] = input("\nEnter new Specilist in:\n\n")
                self.new_list[i][3] = input("\nEnter new Timing: \n\n")
                self.new_list[i][4] = input("\nEnter new Qualification: \n\n")
                self.new_list[i][5] = input("\nEnter new Room number:\n\n")
                self.doctor_list[i] = self.formatDrInfo(self.current_list[i])
                self.writeListOfDoctorsToFile(self.doctor_list)
                self.flag = True
        if self.flag == False:
            print("Can't find the doctor with the same ID on the system\n")

    #displayes all the doctors information as a report/table
    def displayDoctorsList(self):
        self.doctor_list = self.readDoctorsFile()
        self.current_list = []

        for i in range(len(self.doctor_list)):
            self.current_list.append([])
            self.current_list[i] = self.doctor_list[i].split("_")
        
        del self.current_list[0] 
    
        print(f"{'Id': <5}{'Name': <20}{'Specialty': <15}{'Timing': <15}{'Qualification': <15}{'Room Number': <0}"+'\n')
        for i in range(len(self.current_list)):
            print(f"{self.current_list[i][0]: <5}{self.current_list[i][1]: <20}{self.current_list[i][2]: <15}{(self.current_list[i][3].lower()): <15}{(self.current_list[i][4].upper()): <15}{self.current_list[i][5]: <0}")

    #writes the files of docts to doctors file after formatting
    def writeListOfDoctorsToFile(self,doctor_list):
        self.file_open = open('doctors.txt', "w")
        self.index = 0
        for data in doctor_list:
            self.file_open.write(doctor_list[self.index])
            self.index +=1
        self.file_open.close()

    #writes doctors to text file after formating it correctly
    def addDrToFile(self):
        self.doctor_to_add = self.enterDrInfo()
        self.doctor_to_add = self.formatDrInfo(self.doctor_to_add)
        self.doctor_list = self.readDoctorsFile()
        
        self.index = 0
        for data in self.doctor_list:
            if self.doctor_list[self.index].endswith('\n') == False:
                self.doctor_list[self.index] = self.doctor_list[self.index] + '\n'
            self.index += 1

        self.doctor_list.append(self.doctor_to_add)
        self.writeListOfDoctorsToFile(self.doctor_list)

class Facility:
    
    #declare class objects of facility class
    def _init_(self):
        self.name = "none"

    #add facility to text file
    def addFacility(self):
        '''Adds and writes the facility name to the file'''
        self.open_file = open("facilities.txt", "r")
        self.facility_list = self.open_file.readlines()
        self.open_file.close()
        
        self.name = input("Enter Facility name: \n\n")
        
        self.facility_list.append(self.name)

        self.writeListOffacilitiesToFile(self.facility_list)

    #display facility from text line by line
    def displayFacilities(self):
        '''Displays the list of facilities'''
        self.open_file = open("facilities.txt", "r")
        self.facility_list = self.open_file.readlines()
        self.open_file.close()

        self.facility_list[0] = "The " + self.facility_list[0]
        
        for i in range(len(self.facility_list)):
            if self.facility_list[i].endswith('\n') == False:
                print(self.facility_list[i]+'\n')
            else:
                print(self.facility_list[i])

    #prints list of facility from file
    def writeListOffacilitiesToFile(self,new_entry):
        '''Writes the facilities list to facilities.txt'''
        self.open_file = open("facilities.txt", "w")
  
        self.index = 0
        for entries in new_entry:
            if new_entry[self.index].endswith('\n') == False:
                new_entry[self.index] = new_entry[self.index] + '\n'
            self.open_file.write(new_entry[self.index])
            self.index += 1

        self.open_file.close()
        

class Management:
    
    #displays main menu 
    def Display_Menu(self):
        self.loop = True
        while self.loop:
            menu_no = input('Welcome to Alberta Hospital (AH) Managment system\nSelect from the following options, or select 0 to stop:\n1 - 	Doctors\n2 - 	Facilities\n3 - 	Laboratories\n4 - 	Patients\n\n')
            
            if int(menu_no) == 1:
                self.cycle = True
                self.obj_handle = Doctor()
                while self.cycle:
                    menu_no = input('\nDoctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n\n')
                    if int(menu_no) == 1:
                        self.obj_handle.displayDoctorsList()
                        print("\nBack to the prevoius Menu") 
                    elif int(menu_no) == 2:
                        self.obj_handle.searchDoctorById()
                        print("\nBack to the prevoius Menu") 
                    elif int(menu_no) == 3:
                        self.obj_handle.searchDoctorByName()
                        print("\nBack to the prevoius Menu")
                    elif int(menu_no) == 4:
                        self.obj_handle.addDrToFile()
                        print("\nBack to the prevoius Menu")
                    elif int(menu_no) == 5:
                        self.obj_handle.editDoctorInfo()
                        print("\nBack to the prevoius Menu")
                    elif int(menu_no) == 6:
                        self.cycle = False
                        print("")

            elif int(menu_no) == 2:
                self.cycle = True
                self.obj_handle = Facility()
                while self.cycle:
                    menu_no = input('Facilities Menu:\n1 - Display Facilities list\n2 - Add Facility\n3 - Back to the Main Menu\n\n')
                    if int(menu_no) == 1:
                        self.obj_handle.displayFacilities()
                        print("Back to the prevoius Menu") 
                    elif int(menu_no) == 2:
                        self.obj_handle.addFacility()
                        print("\nBack to the prevoius Menu") 
                    elif int(menu_no) == 3:
                        self.cycle = False
                        print("")
          
            else:
                self.loop = False 

mainobject = Management()
mainobject.Display_Menu() 