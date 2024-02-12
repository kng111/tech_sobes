# O: Open-Closed Principle (Принцип открытости-закрытости).

class NotificationSender:
    def send_notification(self, message, notifier):
        notifier.send(message)

class EmailNotifier:
    def send(self, message):
        # Логика отправки уведомления по электронной почте
        print(f"Sending email notification: {message}")

class SMSNotifier:
    def send(self, message):
        # Логика отправки уведомления по SMS
        print(f"Sending SMS notification: {message}")

class PushNotifier:
    def send(self, message):
        # Логика отправки уведомления через push-уведомления
        print(f"Sending push notification: {message}")

# Создаем экземпляры классов-нотификаторов
        
email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()
push_notifier = PushNotifier()

# Создаем экземпляр класса NotificationSender
notification_sender = NotificationSender()

# Отправляем уведомления
notification_sender.send_notification("Hello via email", email_notifier)
notification_sender.send_notification("Hi via SMS", sms_notifier)
notification_sender.send_notification("Hey via push", push_notifier)

''' КРАТКО:

Применение принципа открытости-закрытости способствует созданию гибкого,
 устойчивого к изменениям и легко поддерживаемого кода

* Программные сущности (классы, модули, функции) должны быть открыты для расширения,
 но не для модификации.
'''




''' ПЛЮСЫ:
    Расширяемость:
        Система, соответствующая OCP, легко расширяется с добавлением нового функционала. 

    Минимизация риска:
        Разделение изменений позволяет избежать внесения ошибок в существующий код.

    Улучшенная поддержка:
        Система построенная с учетом OCP, легче поддается сопровождению. 

    Гибкость кода:
        Код, соответствующий OCP, становится более гибким и адаптивным.

    Создание плагинов:
        OCP поддерживает создание плагинов и расширений

    Устойчивость к изменениям:
        Система, следующая OCP, остается стабильной при изменениях требований

    Улучшенная модульность:
        Компоненты системы могут быть разработаны и тестированы независимо друг от друга
 
'''

