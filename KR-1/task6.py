class Message:
  def __init__(self, content):
    self.content = content

  def send(self):
    print(f'Уведомление отправлено: {self.content}')

class EmailMessage(Message):
  def __init__(self, content):
    super().__init__(content)

  def send(self):
    print(f'Уведомление отправлено на email: {self.content}')


class SMSMessage(Message):
  def __init__(self, content):
    super().__init__(content)

  def send(self):
    print(f'Уведомление отправлено на мобильный номер с текстом: {self.content}')


def handle_message(message):
    message.send()

message_content = 'Ваш заказ №500 подтвержден.'

email = EmailMessage(message_content)
handle_message(email)

sms = SMSMessage(message_content)
handle_message(sms)