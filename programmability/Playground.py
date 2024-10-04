from pywin32_system32 import *

exe_name = r"C:\Windows\System32\control.exe"

si = wproc.STARTUPINFO()
si.dwFlags = wcon.STARTF_USESHOWWINDOW
si.wShowWindow = wcon.SW_MAXIMIZE
h_proc, h_thr, pid, tid, = wproc.CreateProcess(None, exe_name, None, None, False, 0, None, None, si)
print(h_proc, h_thr, pid, tid)
