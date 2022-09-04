from mycroft import MycroftSkill, intent_file_handler


class CallMycroft(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('mycroft.call.intent')
    def handle_mycroft_call(self, message):
        self.speak_dialog('mycroft.call')


def create_skill():
    return CallMycroft()

