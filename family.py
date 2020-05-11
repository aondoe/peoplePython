
    
class Person:
    def __init__(self, firstName, lastName):
        self.lastName=lastName;
        self.firstName=firstName;
        self.age=36;

    def getLast(self):
        print(self.lastName);

class Family:
    def __init__(self, lastName):
        self.lastName=lastName;

    def related(self, *args):
        famList=list(args);

        for x in famList:
            try:
                if x.lastName.casefold()==self.lastName.casefold():
                    famList.append(x.firstName+" "+x.lastName);
                    print("*****Yeah, WE HAVE A WINNER. ",x.firstName+" "+x.lastName+" might be related to the ",self.lastName,"family.");
                else:
                    print(x.firstName+" "+x.lastName+" is not related to the ",self.lastName,"family.");
            except AttributeError as e:
                pass;

##############  Below is the program    #####################
justiceFam=Family("Justice");   #New family object.

jason=Person("Jason","Jacobs"); #New Person object
jessie=Person("Jessie", "Justice");   #New Person object
jacklyn=Person("Jacklyn","Pakman");   #New Person object

justiceFam.related(jason,jessie,jacklyn);
