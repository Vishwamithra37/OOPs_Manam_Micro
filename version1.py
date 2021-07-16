#This works fine
import json
from nested_dictionaries import NestedDictionaries as nd
import flask
import pymongo as pym
from hashlib import sha256,md5
from Crypto.Random import get_random_bytes
from secrets import token_hex
import time
from bson.objectid import ObjectId


db=pym.MongoClient("mongodb://localhost:27017/") # connecting to the local Mongodb

class a1:
    def treader(me):
        me["auth"]["token"]=flask.request.cookies.get('token')
        me["auth"]["state"]=flask.request.cookies.get('state')
        assert type(me["auth"]["token"])==str and len(me["auth"]["token"])==26
        assert type(me["auth"]["state"])==str 
        a=flask.Response(json.dumps(me))  
        a.delete_cookie("token") #Key with name token gets deleted
        a.set_cookie('ola','chela') #Ola:chela cookie gets set
        return me

    def tcheker(me):
        #Required:
        #me["auth"]["token"] -->"m_question" or "d_question"
        #["auth"]["state"]
        #["auth"]["election circles"]
        
        
        dab=db["tokens"]
        dac=dab[me["auth"]["state"]]
        fire=dac.find_one({"auth.token":me["auth"]["token"]},
                          {"_id":1,"user.email":1,
                          "user.election circles":1,
                           "user.state":1,"user.name":1,"user.party":1})
        assert fire!=None
        assert me["auth"]["state"]==fire["user"]["state"]
        assert me["auth"]["election circles"] in fire["user"]["election circles"]
        fire["auth"]["token"]=me["auth"]["token"]                                 ##Use fire to create a token   
        return fire
    
    def tcreator(me):
           #Required:  #Use fire
           #me["auth"]["token"] 
           #["user"]["email"]
           #["user"]["election circles"]
           #["user"]["state"] -- email
           #["user"]["name"]
            a=token_hex(4)
            b=token_hex(4)
            c=str(a)+str(round(time.time()))+str(b)
            dab=db["tokens"]
            dac=dab[me["auth"]["state"]]
            me1=nd()
            me1["auth"]["token"]=c                         #The token that will be linked
            me1["user"]["email"]=me["user"]["email"]     #The email that will be linked
            me1["user"]["election circles"]=me["user"]["election circles"] #The election circles
            me1["user"]["state"]=me["user"]["state"]      #The state is stored
            me1["user"]["name"]=me["user"]["name"]
            dac.insert_one(me1)
            dac.delete_one({"auth.token":me["auth"]["token"]})

            return (me1["auth"]["token"]) #Returns a new token

    def qup(me):    #Question database update
        #Required:
        #me["edit"]["code"] -->"m_question" or "d_question"
        #["auth"]["state"]
        #["auth"]["election circles"]
        #["auth"]["user"] -- email
        #["edit"][me["edit"]["code"]]
        
        test=["m_question","d_question"]   


        assert me["edit"]["code"] in test
        dab=db["feed"]
        dac=dab[me["auth"]["state"]]
        fire=dac.find_one({"_id":ObjectId(me["q"]["hash"]),"election circles":me["auth"]["election circles"]},
                          {"_id":0,"auth.users":1})
        ########################################################################################
        assert me["user"]["email"] in fire["auth"]["users"]
        dac.update_one({"_id":ObjectId(me["q"]["hash"])},
                       {"$set":
                        {
                            ("q."+me["edit"]["code"]):me["edit"][me["edit"]["code"]],
                            "edit":{"timestamp":round(time.time())},
                            "edit":{"user":me["auth"]["user"]}
                        }
                       }
                      )
        #########################################################################################
        return "ok"           

    def sup(me):    #Solution database update
        
        test=["solution"]    
        
        
        assert me["edit"]["code"] in test
        dab=db["solutions"]
        dac=dab[me["auth"]["state"]]
        fire=dac.find_one({"s.hash":me["s"]["hash"],"election circles":me["auth"]["election circles"]},
                          {"_id":0,"auth.users":1})
        ########################################################################################
        assert me["user"]["email"] in fire["auth"]["users"]
        dac.update_one({"_id":ObjectId(me["q"]["hash"])},
                       {"$set":
                        {
                            ("s."+me["edit"]["code"]):me["edit"][me["edit"]["code"]],
                            "edit":{"timestamp":round(time.time())},
                            "edit":{"user":me["auth"]["user"]}
                        }
                       }
                      )
        #########################################################################################
        return "ok"
        
        
    def pup(me):    #Profile database update

        test=["password","phone","occupation"]    
        assert me["edit"]["code"] in test        
        
        count=0

        ##############Add captcha#####################################

        v2=me["edit"][me["edit"]["code"]]
        v3=me["edit"]["code"]

        for j in test:
            count=1+count
            if j==v3 and count==1:
                assert type(v2)==str and len(v2)==19 #password
                tes=md5((v2).encode('utf-8'))
                v4=tes.hexdigest()
            elif j==v3 and count==2:
                assert 8<len(v2)<=10 
                v4=v2
            elif j==v3 and count==3:
                assert type(v2)==str
                v4=v2

            dab=db["users"]                         #This is the database
            dac=dab[me["user"]["state"]]          #This is a collection        

            dac.update({"user.email":me["user"]["email"]},{"$set":{v3:v4}})    
        
            return {"Operation":"successful"}

class maker():
   def questionmaker(me):
        


class uad:
   def upvote(me):
       
    
    
    
    
        
        
        
       