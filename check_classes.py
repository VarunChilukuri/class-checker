from helium import *
from time import sleep

class_list = {"CMSC330" : ["0101", "0103"], "CMSC351" : ["0201"], "INAG110" : ["0501", "0505"]}
seat_list = {}
start_firefox("https://app.testudo.umd.edu/soc/", headless=True)

for a in class_list.keys():
    write(a, into="Course:")
    for b in class_list.get(a):
        write(b, into="Section:")
        press(ENTER)
        wait_until(lambda: Text(to_right_of="Open:").exists or Text("No courses matched your search filters above.").exists)
        if Text("No courses matched your search filters above.").exists():
            print("Section or Course doesn't exist.")
            seat_list[a+"-"+b] = 0
        else:
            print(Text(to_right_of="Open:").value)
            seat_list[a+"-"+b] = int(Text(to_right_of="Open:").value)
kill_browser()
print(seat_list)