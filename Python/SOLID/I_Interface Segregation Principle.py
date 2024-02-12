"""
Создавайте узкоспециализированные интерфейсы,
 предназначенные для конкретного клиента.
   Клиенты не должны зависеть от интерфейсов,
     которые они не используют.
"""



"""
Ответ: Класс должен иметь только одну причину для изменения,
 то есть, он должен быть ответственным только за одну важную часть функциональности.
"""

from abc import ABC, abstractmethod

# Интерфейс для отправки уведомлений по электронной почте
class EmailSender(ABC):
    @abstractmethod
    def send_email(self, to, message):
        pass

# Интерфейс для отправки уведомлений по SMS
class SMSSender(ABC):
    @abstractmethod
    def send_sms(self, to, message):
        pass

# Реализация интерфейса отправки уведомлений по электронной почте и SMS
class EmailAndSMSSender(EmailSender, SMSSender):
    def send_email(self, to, message):
        # Реализация отправки по электронной почте
        print(f"Sending email to {to}: {message}")

    def send_sms(self, to, message):
        # Реализация отправки по SMS
        print(f"Sending SMS to {to}: {message}")

# Сервис для отправки уведомлений только по электронной почте
class EmailService:
    def __init__(self, email_sender):
        self.email_sender = email_sender

    def send_email_notification(self, to, message):
        self.email_sender.send_email(to, message)

# Создание экземпляра реализации интерфейса
email_and_sms_sender = EmailAndSMSSender()

# Создание экземпляра сервиса отправки уведомлений по электронной почте
email_service = EmailService(email_and_sms_sender)

# Использование сервиса для отправки уведомления по электронной почте
email_service.send_email_notification("user@example.com", "Hello from EmailService")

"""
В этом коде мы создаем два интерфейса (EmailSender и SMSSender),
 затем реализацию,
   поддерживающую оба интерфейса (EmailAndSMSSender).
     Затем мы создаем сервис (EmailService),
       который требует только интерфейс отправки уведомлений по электронной почте (EmailSender).
         Клиентский код (email_service.send_email_notification) использует только метод send_email,
           что соответствует принципу разделения интерфейса.
"""


"""
    ПЛЮСЫ:
    Плюсы Interface Segregation Principle (Принцип интерфейсов):

    Гибкость: 
        Клиенты зависят только от тех методов, 
            которые им необходимы, 
                что делает клиентский код более гибким.

    Ясная ответственность: 
        Интерфейсы имеют четко определенные обязанности,
            улучшая понимание кода и его поддержку.

    Легкость расширения: 
        Добавление новых методов в интерфейсы не требует изменений в существующем клиентском коде,
        что облегчает расширение функционала.
"""