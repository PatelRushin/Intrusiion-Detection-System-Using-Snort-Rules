@echo off
echo Pinging the Victim:
start ping 192.168.56.101
echo %time%
timeout 10 > NUL
echo %time%
start ssh ubuntu01@192.168.56.101
echo %time%
timeout 10 > NUL
echo %time%
start nmap -p0-65535 192.168.56.101
