from abc import ABC, abstractmethod

class AbstractMessage(ABC):
    def __init__(self, content):
        self.content = content

    @abstractmethod
    def send(self):
        pass


class EmailMessage(AbstractMessage):
    def send(self):
        print(f"Sending email with content: {self.content}")


class SMSMessage(AbstractMessage):
    def send(self):
        print(f"Sending SMS with content: {self.content}")


class PushNotification(AbstractMessage):
    def send(self):
        print(f"Sending push notification with content: {self.content}")


class MessageFactory:
    def create_message(self, type, content):
        if type == "email":
            return EmailMessage(content)
        elif type == "sms":
            return SMSMessage(content)
        elif type == "push":
            return PushNotification(content)
        else:
            return None


# Create a message factory
factory = MessageFactory()

# Create different types of messages
email = factory.create_message("email", "Hello, how are you?")
sms = factory.create_message("sms", "Meeting at 3 PM.")
push = factory.create_message("push", "New message received!")

# Send the messages
email.send()
sms.send()
push.send()