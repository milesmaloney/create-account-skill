from mycroft import MycroftSkill, intent_file_handler
#do we need the database here too?
import random 

class CreateAccount(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('account.create.intent')
    def handle_account_create(self, message):
        self.speak("Let's create an account. Please provide your information.")
        confirm = "no"
        while confirm == "no":
            user_name = self.get_response("What is your first name?")
            #TODO ask for middle name?
            last_name = self.get_response("What is your last name?")
            #other information suggestions: preferred station, regular modes of transport, most frequent routes?
            self.speak("Creating customer I.D., hold on....")
            userid = random.randint(1,9999999999) #probably will change this range later
            self.speak("Your user I.D. is {}.".format(userid))
            self.speak("A new account will be created with the following information: Name: {}, Last Name: {}, User I.D.: {}".format(user_name,last_name,userid))
            confirm = self.get_response("Confirm if this information is correct, please say yes or no.")
            if confirm == "yes":
                self.speak("Your account has been created. Thank you!") #might change this
                break
            elif confirm == "no":
                self.speak("Okay. Let's try with your information again")
                #NOTE this is just a placeholder, might make it more complex later on and rather than having the user say everything be specific for which thing is wrong
            
            #NOTE the below code is for error checking, might make it too complex though
            #else:
                #self.speak("Sorry, I didn't get that. Could you repeat that again?")

            #TODO if need there be add the customer to the database

        #self.speak_dialog('account.create')


def create_skill():
    return CreateAccount()

