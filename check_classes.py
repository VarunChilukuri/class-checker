from helium import *
from time import sleep

class_list = {"CMSC132" : ["0101", "0102"], "CMSC216" : ["0301", "0909"], "CMSC000" : ["0101"]}

start_firefox("https://app.testudo.umd.edu/soc/", headless=True)

for a in class_list.keys():
    write(a, into="Course:")
    for b in class_list.get(a):
        write(b, into="Section:")
        press(ENTER)
        wait_until(lambda: Text(to_right_of="Open:").exists or Text("No courses matched your search filters above.").exists)
        if Text("No courses matched your search filters above.").exists():
            print("Section or Course doesn't exist.")
        else:
            print(Text(to_right_of="Open:").value)
kill_browser()