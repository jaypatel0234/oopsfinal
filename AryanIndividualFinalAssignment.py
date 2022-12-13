#Final Assignment
#Group 5
# Aryan Patel


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

class Patient:
    
    #declares class objects of patient
    def _init_(self):
        self.id = "none"
        self.name = "none"
        self.disease = "none"
        self.gender = "none"
        self.age = "none"
    
    #formats patient info for text file
    def formatPatientInfo(self):
        return f"{self.id}_{self.name}_{self.disease}_{self.gender}_{self.age}"

    #asks user for patient info
    def enterPatientInfo(self):
        self.id = input("Enter Patient ID: \n")
        self.name = input("Enter Patient Name: \n")
        self.disease = input("Enter Patient Disease: \n")
        self.gender = input("Enter Patient Gender: \n")
        self.age = input("Enter Patient Age: \n")

    #read patients text file
    def readPatientsFile(self, file_name):
        patients_list = []
        with open(file_name, "r") as file:
            for line in file:
                patient_info = line.split("_")
                patients_list.append(self._init_(patient_info[0], patient_info[1], patient_info[2], patient_info[3], patient_info[4]))
        return patients_list
    
    #display patient list from text file
    def displayPatientsList():
        print("{:<4} {:<15} {:<15} {:<15} {:<15}\n ".format('Id','Name','Disease','Gender','Age'))
        f=open("patients.txt","r")
        next(f)
        while(True):
            p=f.readline()
            l=len(p)
            if(l==0):
                break
            linevar=p.split('_')
            print("{:<4} {:<15} {:<15} {:<15} {:<15}".format(linevar[0],linevar[1],linevar[2],linevar[3],linevar[4]))
        f.close()
    
    #search patient by id in text file            
    def searchPatientById():
        searchid=input("Enter the Doctor Id:\n")
        f=open("patients.txt","r")
        flag=0
        while(True):
            t=f.readline()
            l=len(t)
            if(l==0):
                break
            linevar=t.split('_')
            if(linevar[0]==searchid):
                print("{:<4} {:<15} {:<15} {:<15} {:<15} \n ".format('Id','Name','Disease','Gender','Age'))
                print("{:<4} {:<15} {:<15} {:<15} {:<15} ".format(linevar[0],linevar[1],linevar[2],linevar[3],linevar[4]))
                flag=1
                break
        if(flag==0):
            print("Can't find the doctor with the same ID on the system\n")   
        f.close()            
     
    #search patient by name in text file     
    def addPatientToFile():
        id=input("Enter Patient id: \n")
        name=input("Enter Patient Name: \n") 
        disease=input("Enter Patient Disease: \n")
        gender=input("Enter Patient Gender: \n")
        age=input("Enter Patient Age: \n")
        f=open("FinalAssignment\patients.txt","a")
        f.write(id+"_"+name+"_"+disease+"_"+gender+"_"+age+"\n")
        f.close   
    
    #display patient info from text file    
    def displayPatientInfo(self):
        print(f"Patient ID: {self.id}\n")
        print(f"Patient Name: {self.name}\n")
        print(f"Patient Disease: {self.disease}\n")
        print(f"Patient Gender: {self.gender}\n")
        print(f"Patient Age: {self.age}\n")    
    
    #edit patient info    
    def editPatientInfo():
        changeid=input("Please enter the id of the Patient that you want to edit their information:\n")
        newname=input("Enter New Name: \n")
        newdisease=input("Enter New Disease: \n")
        newgender=input("Enter New Gender: \n")
        newage=input("Enter New Age: \n")
                #t.write("\n"+g[0]+"-"+newname+"-"+newdisease+"-"+newgender+"-"+newage)
                
    #writes list of patient to file            
    def writeListOfPatientsToFile(self, patients_list, file_name):
        with open("patients.txt", "w") as file:
            for patient in patients_list:
                file.write(patient.formatPatientInfo() + "\n")        
  
class Management:
    
    #displays main menu 
    def Display_Menu(self):
        self.loop = True
        while self.loop:
            menu_no = input('Welcome to Alberta Hospital (AH) Managment system\nSelect from the following options, or select 0 to stop:\n1 - 	Doctors\n2 - 	Facilities\n3 - 	Laboratories\n4 - 	Patients\n\n')
            
            if int(menu_no) == 2:
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
            
            elif int(menu_no) == 4:
                self.cycle = True
                self.obj_handle = Patient()
                while self.cycle:
                    menu_no = input('Patients Menu:\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n\n')
                    if int(menu_no) == 1:
                        Patient.displayPatientsList()
                    elif int(menu_no) == 2:
                        Patient.searchPatientById()
                    elif int(menu_no) == 3:
                        Patient.addPatientToFile()
                    elif int(menu_no) == 4:
                        Patient.editPatientInfo()
                    elif int(menu_no) == 5:
                        self.cycle = False
                    print("")   
            
            else:
                self.loop = False 

mainobject = Management()
mainobject.Display_Menu() 