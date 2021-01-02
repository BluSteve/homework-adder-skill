from mycroft import MycroftSkill, intent_file_handler


class HomeworkAdder(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('adder.homework.intent')
    def handle_adder_homework(self, message):
        self.speak_dialog('adder.homework')


def create_skill():
    return HomeworkAdder()

