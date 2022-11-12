import json
def register(type,filename,name,mobile,email,password):
    
    if type.lower() == "manager":
        details = {
            "Name": name,
            "Mobile" : mobile,
            "Email" : email,
            "Password" : password
        }
        file = open(filename, "r+")
        try:
            data = []
            data = json.load(file)
            data.append(details)
            file.seek(0)
            file.truncate()
            json.dump(data,file)
            return True
        except json.decoder.JSONDecodeError as ex:
            print(ex)
            lst = []
            lst.append(details)
            json.dump(lst,file)
            return False
        finally:
            file.close()


if __name__ == "__main__":
    register("manager", "manager.json", "Nikhil", "1234567890", "nikhilmandlik@gmail.com", "123456")
    register("manager", "manager.json", "ADITYA", "1234567890", "nikhilmandlik@gmail.com", "123456")
    register("manager", "manager.json", "prashant", "1234567890", "prashantpayle@gmail.com", "123456")