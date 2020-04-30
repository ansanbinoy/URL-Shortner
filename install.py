from subprocess import call
call(["pip", "install", "pyshorteners"])
call(["clear"])
call(["python3", "url-shortener.py", "-h"])