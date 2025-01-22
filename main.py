import time
from plyer import notification

if __name__=="__main__":
    notification.notify(
        title = "PLzz... DRINK WATER",
        message = "Drink water live Hydrated and glow the Skin",
        app_icon= "D:\python\drinking water\icon.ico",
        timeout=10
    )
    time.sleep(60)

    #to run continue: pythonw .\main.py