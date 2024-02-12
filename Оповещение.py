import time

from plyer  import notification

if __name__ == "__main__":
    while True:
        time.sleep(1)
        notification.notify(
            title="Alert",
            message="Соабку кормить",
            # app_icon="icon.png",
            timeout=10
        )
        time.sleep(10)
    