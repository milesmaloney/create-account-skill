from mycroft import MycroftSkill, intent_file_handler
import sqlite3
import random 

class CreateAccount(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('account.create.intent')
    def handle_account_create(self, message):
        conn = sqlite3.connect("cubic.sql") 
        cur = conn.cursor()

        self.speak("Let's create an account. Please provide your information.")

        confirm = "no"

        while confirm == "no":
            user_name = self.get_response("What is your first name?")

            #TODO ask for middle name?
            
            last_name = self.get_response("What is your last name?")

            name = user_name + " " + last_name
            
            #other information suggestions: preferred station, regular modes of transport, most frequent routes?
            
            self.speak("Creating customer I.D., hold on....")

            userid = 0
            taken = 1
            while(taken == 1):
                userid = random.randint(1,999999)

                cur.execute("SELECT * FROM Customer WHERE CustomerID = ?", (userid,))
                customer = cur.fetchone()

                if (customer == None):
                    taken = 0

            convertid = str(userid).replace("", " ")
            self.speak("Your user I.D. is {}.".format(convertid))
            

            self.speak("A new account will be created with the following information: Name: {}, User I.D.: {}".format(name,convertid))
            confirm = self.ask_yesno("Is this information correct? Please say yes or no.")

            if confirm == "yes":
                cur.execute("INSERT INTO Customer(CustomerID, Name, Balance) VALUES(?,?,?)", (userid, name, 0))
                conn.commit()
                self.speak("Your account has been created. Thank you!") #might change this
                return
            elif confirm == "no":
                self.speak("Okay. Let's try with your information again")
                #NOTE this is just a placeholder, might make it more complex later on and rather than having the user say everything be specific for which thing is wrong
            
            #NOTE the below code is for error checking, might make it too complex though
            #else:
                #self.speak("Sorry, I didn't get that. Could you repeat that again?")

            #TODO if need there be add the customer to the database

        conn.close()
        #self.speak_dialog('account.create')


def create_skill():
    return CreateAccount()

