@echo off

wmic path win32_pnpsigneddriver get caption,description,deviceclass,deviceid,devicename,hardwareid,location,manufacturer,status,name /format:hform > PCIlist.html
