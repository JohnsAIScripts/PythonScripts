@echo off

echo Find Link
net use Z: \\NX1-22H2\Users\admin\Desktop\SHARE /user: <<[user] space [password]>>

echo Copy File
xcopy "C:\Users\Admin\Desktop\RebootTest\TimeDateReport.txt" "Z:\" /s /i /y

echo Delete
net use Z: /delete



rem C:\Users\admin\Desktop\SHARE