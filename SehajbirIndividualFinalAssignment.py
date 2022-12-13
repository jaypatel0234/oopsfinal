#Final Assignment
#Individual
#Sehajbir Singh

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
        
class Laboratory:  
    
    #declare class objects of laboratory class
    def _init_(self):
        self.name = "none"
        self.cost = "none"
    
    #formats datain text format as shown in file
    def formatLabInfo(self):
        return f"{self.name}_{self.cost}"

    #asks laboratory detail from user
    def enterLaboratoryInfo(self):
        self.name = input("Enter Laboratory Name: ")
        self.cost = input("Enter Laboratory Cost: ")
    
    #reads laboratory from text file    
    def readLaboratoriesFiles(self):
        self.open_file = open("laboratories.txt", "r")
        self.test_list = self.open_file.readlines()
        self.open_file.close()
        return self.test_list      
    
    #displays laboratory in form of table
    def displayLabsList():
        print("{:<4} {:<15}\n ".format('Lab','Cost'))
        f=open("laboratories.txt","r")
        next(f)
        while(True):
            d=f.readline()
            l=len(d)
            if(l==0):
                break
            linevar=d.split('_')
            print("{:<4} {:<15}".format(linevar[0],linevar[1]))
        f.close()
        
    #writes laoratory to files    
    def addLabToFile():
        lab=input("Enter Laboratory facility:")
        cost=input("Enter Laboratory cost:") 
        f=open("laboratories.txt","a")
        f.write(lab+"_"+cost+"\n")
        f.close
    
    #writes list of lab to file    
    def writeListOfLabsToFile(self, labs_list, file_name):
        with open(file_name, "w") as file:
            for lab in labs_list:
                file.write(lab.formatLabInfo() + "\n")

class Management:
    
    #displays main menu 
    def DisplayMenu(self):
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
            
            elif int(menu_no) == 3:
                self.cycle = True
                self.obj_handle = Laboratory()
                while self.cycle:
                    menu_no = input('Laboratories Menu:\n1 - Display laboratories list\n2 - Add laboratory\n3 - Back to the Main Menu\n\n')
                    if int(menu_no) == 1:
                        Laboratory.displayLabsList()
                    elif int(menu_no) == 2:
                        Laboratory.addLabToFile()
                    elif int(menu_no) == 3:
                        self.cycle = False
                    print("Back to the prevoius Menu\n") 
            

mainobject = Management()
mainobject.DisplayMenu() 