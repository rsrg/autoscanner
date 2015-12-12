"""
Created on 29 nov. 2015

@author: Valtyr Farshield
"""

import requests
import json

from PySide import QtCore

class PushBullet(QtCore.QObject):
    """
    Push Notification System
    """

    finished = QtCore.Signal(bool)

    def __init__(self, parent=None):
        super(PushBullet, self).__init__(parent)

        self.access_token = None
        self.title = None
        self.body = None

    def set_message(self, access_token, title, body):
        """
        Constructs the notification to be sent
        :param access_token: API Key
        :param title: Title of message
        :param body: Body of message
        :return: None
        """
        self.access_token = access_token
        self.title = title
        self.body = body

    def _send_notification(self):
        """
        Send notification via PushBullet
        :return: True if the message was successfully sent
        """

        if self.access_token != None and self.title != None and self.body != None:
            data_send = {"type": "note", "title": self.title, "body": self.body}

            resp = requests.post(
                'https://api.pushbullet.com/v2/pushes',
                data=json.dumps(data_send),
                headers={'Authorization': 'Bearer ' + self.access_token, 'Content-Type': 'application/json'}
            )

            if resp.status_code == 200:
                return True

        return False

    def process(self):
        response = self._send_notification()
        self.finished.emit(response)


def main():
    ACCESS_TOKEN = "your-api-key-here"
    push_bullet = PushBullet()
    push_bullet.set_message(ACCESS_TOKEN, "Test", "Test")
    push_bullet.process()

if __name__ == "__main__":
    main()
