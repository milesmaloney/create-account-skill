from mycroft import MycroftSkill, intent_file_handler


class CreateAccount(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('account.create.intent')
    def handle_account_create(self, message):
        self.speak_dialog('account.create')


def create_skill():
    return CreateAccount()

