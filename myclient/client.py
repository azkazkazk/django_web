

from admin import Admin

import time
import pickle
import os
import requests

import json


def main():
    admin = Admin()

    while True:
        admin.adminView()
        option = input("Please choose to login or register")
        if option == '1' or option == 'login':
            student_name = input("Please input the Username：")
            password = input("Please input the password：")
            url = "http://192.168.1.84:8080/login/"

            headers = {'content-type': 'application/x-www-form-urlencoded'}
            requestsDate = {"username": student_name, "password": password}
            ret = requests.post(url, data=requestsDate, headers=headers)
            if ret.status_code == 200:
                text = json.loads(ret.text)
                # print(text,flush=True)
                status = text['status']
                if status == -1:
                    print("Password mismatch")
                if status == -2:
                    print("The username does not exist")
                if status == 0:
                    print("Login successful,wait two seconds to enter the scoring system")

                    time.sleep(2)
                    break
                # print(text)
            if ret.status_code == 500:
                print("Server error")
        if option == '2' or option == 'Submit':
            name = input("Please input the Username：")
            password = input("Please input the Password：")
            email = input("Please input the email：")
            url = "http://192.168.1.84:8080/register/"

            headers = {'content-type': 'application/x-www-form-urlencoded'}
            requestsDate = {"username": name, "password": password, "email": email}
            ret = requests.post(url, data=requestsDate, headers=headers)
            if ret.status_code == 200:
                text = json.loads(ret.text)
                status = text['status']
                if status == -1:
                    print("This user already exists, please log in directly")
                if status == 0:
                    print("Register successfully, please login")

                    time.sleep(2)

            # print(text)
            if ret.status_code == 500:
                print("Server error")
    print("************")

    while True:
        admin.interFaceView()
        option = input("Please operate")
        if option == "1" or option == 'rate':

            code = input("Please input code：")
            name = input("Please input name：")
            year = input("Please input year：")
            semester = input("请输入semester：")
            teacher = input("请输入teacher：")
            score = input("请输入score：")
            url = "http://192.168.1.84:8080/rate/"

            headers = {'content-type': 'application/x-www-form-urlencoded'}
            requestsDate = {"student_name": student_name, "code": code, "name": name, "year": year,
                            "semester": semester, "teacher": teacher, "score": score}
            ret = requests.post(url, data=requestsDate, headers=headers)
            if ret.status_code == 200:
                text = json.loads(ret.text)
                status = text['status']
                if status == -1:
                    print("The rating is repeated ")
                if status == 0:
                    print("Submitted successfully ")
                    time.sleep(0.5)

            if ret.status_code == 500:
                print("Server error")
        elif option == "2" or option == "list":
            code = input("Please enter code and press enter directly for all course codes：")
            year = input("Please enter year and press enter directly for all course year：")
            semester = input("Please enter semester and press enter directly for all semester：")
            url = "http://192.168.1.84:8080/list/"

            headers = {'content-type': 'application/x-www-form-urlencoded'}
            requestsDate = {"code": code, "year": year, "semester": semester}
            ret = requests.get(url, params=requestsDate, headers=headers)
            if ret.status_code == 200:
                text = json.loads(ret.text)

                print(text)
                time.sleep(0.5)

            if ret.status_code == 500:
                print("Server error")
        elif option == "3" or option == "view":
            teacher_id = input("Please input teacher_id(For all professors,please press enter directly)：")
            url = "http://192.168.1.84:8080/view/"

            headers = {'content-type': 'application/x-www-form-urlencoded'}
            requestsDate = {"teacher_id": teacher_id}
            ret = requests.get(url, params=requestsDate, headers=headers)
            if ret.status_code == 200:
                text = json.loads(ret.text)

                print(text)
                time.sleep(0.5)

            if ret.status_code == 500:
                print("Server error")
        elif option == "4" or option == "average":
            teacher_id = input("Please input teacher_id(For all professors,please press enter directly)：")
            code = input("Please input code(For all codes,please press enter directly)：")
            url = "http://192.168.1.84:8080/average/"

            headers = {'content-type': 'application/x-www-form-urlencoded'}
            requestsDate = {"teacher_id": teacher_id, "code": code}
            ret = requests.get(url, params=requestsDate, headers=headers)
            if ret.status_code == 200:
                text = json.loads(ret.text)

                print(text)
                time.sleep(0.5)

            if ret.status_code == 500:
                print("Server error")
        elif option == "5" or option == "Change passwords":
            print("You are about to make a password change")
            old_password = input("Please enter your original password：")
            new_password = input("Please enter your new password：")
            re_ne_password = input("Please reconfirm your new password：")
            url = "http://192.168.1.84:8080/repassword/"

            headers = {'content-type': 'application/x-www-form-urlencoded'}
            requestsDate = {"username": student_name, "old_password": old_password, "new_password": new_password,
                            "re_new_password": re_ne_password}
            ret = requests.post(url, data=requestsDate, headers=headers)
            if ret.status_code == 200:
                text = json.loads(ret.text)
                status = text.status
                if status == -1:
                    print("Incorrect password")
                if status == -2:
                    print("The two passwords do not match")
                if status == 0:
                    print("Modify the success")
                    time.sleep(0.5)

            if ret.status_code == 500:
                print("Server error")
            pass
        elif option == "6":
            pass

        elif option == "t":
            # 退出
            print("see you next time")
            main()
            pass

        time.sleep(2)


if __name__ == "__main__":
    main()
