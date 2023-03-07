import utils.windowmanager
import utils.window

manager = utils.windowmanager.WindowManager()

window = utils.window.Window(title="Test", height=100, width=500)
window.createWindow()
window.showWindow()

uuid = manager.addWindow(window)
print(uuid)

for i in range(1000):
    if False == True:
        print("h")