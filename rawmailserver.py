import smtpd
import asyncore

server = smtpd.DebuggingServer(('0.0.0.0', 25), None)

asyncore.loop()