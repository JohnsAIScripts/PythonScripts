@ECHO off 
REM Name your USB Drive: FIERYBIOS  (For AutoBoot ONLY)
TITLE WinPE Boot Config
CLS

ECHO *** Gathering Hardware Information ***
wmic cpu Get Name > C:\Users\Admin\Desktop\Automation_HW_Audit_StandAlone\HW_Info.csv
wmic MemoryChip Get DeviceLocator,Capacity,Speed,Manufacturer,PartNumber >> C:\Users\Admin\Desktop\Automation_HW_Audit_StandAlone\HW_Info.csv
wmic computersystem get name >> C:\Users\Admin\Desktop\Automation_HW_Audit_StandAlone\HW_Info.csv
wmic LogicalDisk get Name,Size,VolumeName,Description >> C:\Users\Admin\Desktop\Automation_HW_Audit_StandAlone\HW_Info.csv
wmic DiskDrive get SerialNumber,Caption,Description,FirmwareRevision,DeviceID,Size > DiskDriveInfo.txt

REM Wpeutil InitializeNetwork  (For AutoBoot ONLY)
wmic NIC Get name,manufacturer,MACAddress >> C:\Users\Admin\Desktop\Automation_HW_Audit_StandAlone\HW_Info.csv

REM Convert bat file to unicode
type HW_Info.csv > C:\Users\Admin\Desktop\Automation_HW_Audit_StandAlone\HW_Info.txt

ECHO *** Gathering Dump Information ***
Release--ExtractEfiBiosBlockParameters64.exe C:\Users\Admin\Desktop\Automation_HW_Audit_StandAlone\BIOSBlock.txt
DumpSystemConfiguration.exe /O:BIOSFrag.xml /f 
DumpSystemConfiguration.exe > C:\Users\Admin\Desktop\Automation_HW_Audit_StandAlone\DumpConfig.txt

ECHO *** Gathering Drive Information ***
echo IntelSSDsSummary > IntelSSDsSummary.txt
isdct.exe set -system EnableLSIAdapter = true
isdct.exe show -intelssd >> IntelSSDsSummary.txt
isdct.exe show -smart -intelssd > IntelSSDsSMART.txt
isdct.exe show -all -intelssd > IntelSSDsDetails.txt

ECHO *** Gathering LSI Information ***
storcli64.exe /c0 show all > C:\Users\Admin\Desktop\Automation_HW_Audit_StandAlone\LSI-Info0.txt
storcli64.exe /c0/ dall show all > C:\Users\Admin\Desktop\Automation_HW_Audit_StandAlone\LSIRAID-Info0.txt
storcli64.exe /c1 show all > C:\Users\Admin\Desktop\Automation_HW_Audit_StandAlone\LSI-Info1.txt
storcli64.exe /c1/ dall show all > C:\Users\Admin\Desktop\Automation_HW_Audit_StandAlone\LSIRAID-Info1.txt

ECHO *** Compiling Results ***
AutoCompileData_v002.exe


ECHO ** Exit the script
REM wpeutil shutdown   (For AutoBoot ONLY)
EXIT /B
