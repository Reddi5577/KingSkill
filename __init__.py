from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'Ram'

LOGGER = getLogger(__name__)

class KingSkill(MycroftSkill):

    def __init__(self):
        super(KingSkill, self).__init__(name="KingSkill")
    def initialize(self):
        king_intent = IntentBuilder("KingIntent").\
            require("KingKeyword").build()
        self.register_intent(king_intent, self.handle_king_intent)

    def handle_king_intent(self, message):
        self.speak_dialog("kingnames")

    def stop(self):
        pass


def create_skill():
    return KingSkill()
