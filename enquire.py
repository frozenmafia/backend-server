import json

class Enquire():
    def __init__(self,userId):
        self.userId=userId
        self.readfile()


    def readfile(self):
        with open('user_data.json') as f:
            data=json.load(f) 
        f.close
        self.data = data
    
    def existence_of_user_in_the_register(self):
        user_list = self.data['Users']
        for i in range(len(user_list)):
            if(self.userId==user_list[i]['user'+str(i+1)]['userId']):
                return i
                break
        return False

    