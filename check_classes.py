from helium import *
from flask import Flask, render_template, request

app = Flask(__name__)

class_list = {}
email = ''

@app.route("/", methods=['post', 'get'])
def email_form():
    if request.method == 'POST':
        parse_course_input(request.form.get('course1'), request.form.get('section1'), request.form.get('course2'), request.form.get('section2'), request.form.get('course3'), request.form.get('section3'), request.form.get('course4'), request.form.get('section4'), request.form.get('course5'), request.form.get('section5'), request.form.get('course6'), request.form.get('section6'))
        get_seats(class_list)
        return "<h>Test</h>"
    else:
        return render_template('form.html')

def parse_course_input(c1, s1, c2, s2, c3, s3, c4, s4, c5, s5, c6, s6):
    if c1 != '':
        class_list[c1] = s1.split(",")
    if c2 != '':
        class_list[c2] = s2.split(",")
    if c3 != '':
        class_list[c3] = s3.split(",")
    if c4 != '':
        class_list[c4] = s4.split(",")
    if c5 != '':
        class_list[c5] = s5.split(",")
    if c6 != '':
        class_list[c6] = s6.split(",")

def get_seats(class_list):
    #class_list = {"CMSC330" : ["0101", "0103"], "CMSC351" : ["0201"], "INAG110" : ["0501", "0505"]}
    print(class_list)
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