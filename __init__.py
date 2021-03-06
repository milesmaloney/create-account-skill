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
            
            last_name = self.get_response("What is your last name?")

            name = user_name + " " + last_name
            
            phone = self.get_response("What is your phone number?")
            dbphone = int(phone.replace("-", ""))

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
            

            self.speak("A new account will be created with the following information: Name: {}, Phone Number: {}, User I.D.: {}".format(name,phone,convertid))
            confirm = self.ask_yesno("Is this information correct? Please say yes or no.")

            if confirm == "yes":
                cur.execute("INSERT INTO Customer(CustomerID, Name, Balance, PhoneNo) VALUES(?,?,?,?)", (userid, name, 0, dbphone))
                conn.commit()
                self.speak("Your account has been created. Thank you!") 
                return
            elif confirm == "no":
                self.speak("Okay. Let's try with your information again")
    
        conn.close()


def create_skill():
    return CreateAccount()

