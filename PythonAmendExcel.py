import openpyxl

# = PROMPT USER
# Prompt user for name, age, and goal
pn = input("Enter the Part Number: ")
project = input("Enter the affected projects: ")
version = input("Enter the BIOS version: ")
agile = input("Enter the Agile description: ")
checksum = input("Enter the BIOS checksum: ")
mobo = input("Enter the motherboard baseboard product name: ")
relnote = input("Enter the BIOS release notes file name: ")
link = input("Enter the network BIOS approval link: ")
xmlFile = input("Enter the name of the XML file: ")

# ======================================
# = WRITE PROMPTED DATA TO SETUP EMAIL
    
# Write sentence to file
with open("ApprovalEmail.txt", "w") as f:
    f.write(f""'\n')
    f.write(f"SUBJECT: BIOS Approval ({pn})"'\n')
    f.write(f""'\n')
    f.write(f"Person1,"'\n')
    f.write(f"")
    f.write(f"Here is the {project} BIOS {version} release. Please see the attachments and information below."'\n')
    f.write(f""'\n')
    f.write(f"{pn} - {agile}{checksum}"'\n')
    f.write(f""'\n')
    f.write(f"Please attach the following into Agile:"'\n')
    f.write(f"{mobo}{version}_{pn}.ROM - Source code (zip file)"'\n')
    f.write(f"{relnote} - Release Notes"'\n')
    f.write(f"{pn}_{mobo}{version}.pdf - Approval form"'\n')
    f.write(f"{mobo}{version}_{pn}.xml - XML Fragment"'\n')
    f.write(f""'\n')
    f.write(f"LINK:"'\n')
    f.write(f"{link}"'\n')
    f.write(f""'\n')
    f.write(f"Thank you"'\n')
    f.write(f""'\n')
    f.write(f"-Person2"'\n')
    f.write(f""'\n')


# ====================================
# Load Excel file and select active sheet
workbook = openpyxl.load_workbook(filename="TEMPLATE.xlsx")
worksheet = workbook.active


# = WRITE PROMPTED DATA TO EXCEL
# Write user information to cells A1, B1, and C1
worksheet["D9"] = version
worksheet["D22"] = project
worksheet["D24"] = checksum


# = GET DATA FROM ANOTHER FILE
# Open the text file
with open(xmlFile, 'r') as f:
    data = f.read()

# Select the sheet and cell to write to
worksheet = workbook.active
cell = worksheet['A13']

# = WRITE FILE DATA TO EXCEL
# Write the data to the cell
cell.value = data


# Save changes to Excel file
filenameXlsx = pn + ".xlsx"
workbook.save(filenameXlsx)

print(f"User information written to Excel file {pn}.xlsx.")
