import pyautogui
import pywinauto

# 将指定目录下的单个md文件转换为html文件
def ConvertMdToHtml(typoraApp, inFileCoor, fileMenuCoor, outFileCoor, quitFileCoor, mdFile):
    # 打开Typora应用程序
    pywinauto.application.Application(backend="uia").start(typoraApp)
    # 打开md文件
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'o')
    time.sleep(2)
    pyautogui.click(inFileCoor[0], inFileCoor[1])
    pyautogui.typewrite(mdFile)
    pyautogui.press('enter', presses=1, interval=0.5)
    # 导出html
    time.sleep(5)
    pyautogui.click(fileMenuCoor[0], fileMenuCoor[1])
    time.sleep(0.5)
    pyautogui.press('down', presses=14, interval=0.1)
    pyautogui.press('right', presses=1, interval=0.1)
    pyautogui.press('down', presses=1, interval=0.1)
    pyautogui.press('enter', presses=1, interval=0.5)
    time.sleep(2)
    pyautogui.doubleClick(outFileCoor[0], outFileCoor[1])
    pyautogui.typewrite(mdFile[:-2] + FileFormat.HtmlFileSuffix())
    pyautogui.press('enter', presses=1, interval=0.5)
    pyautogui.press('left', presses=1, interval=0.1)
    pyautogui.press('enter', presses=1, interval=0.5)
    # 关闭Typora
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(1)
    pyautogui.click(quitFileCoor[0], quitFileCoor[1])
    time.sleep(5)
    
# 将指定目录下的所有md文件转换为html文件
def ConvertAllMdToHtml(typoraApp, inFileCoor, fileMenuCoor, outFileCoor, quitFileCoor, mdFilesDir):
    # 筛选指定目录下的文件
    for root, dirs, files in os.walk(mdFilesDir):
        for name in files:
            if FileFormat.IsMdFile(name):
                mdFile = os.path.join(root, name)
                ConvertMdToHtml(typoraApp, inFileCoor, fileMenuCoor, outFileCoor, quitFileCoor, mdFile)


