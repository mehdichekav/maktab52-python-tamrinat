from pymongo import MongoClient

client = MongoClient(port=27017)
db = client.call_note


def insert_new_phone_number(db):
    call_note = {}
    call_note["first_name"] = input("please enter first name: ")
    call_note["last_name"] = input("please enter last name: ")
    number_of_phone = int(input("please enter the number of phones: "))
    for i in range(number_of_phone):
        call_note[str(f"phone {i + 1}")] = input(f"please enter {i + 1} phone number: ")
    result = db.reviews.insert_one(call_note)
    return result


def show_all_data_base(db):
    for x in db.reviews.find():
        print(x)

def delete_element(db,key,value):
    myquery = {key: value}
    db.reviews.delete_one(myquery)
    return key
def update_element(db,key,old_value,new_value):
    myquery = {key: old_value}
    newvalues = {"$set": {key: new_value}}
    db.reviews.update_one(myquery, newvalues)
    return key


# # for add new row call insert_new_phone_number(db)
# insert_new_phone_number(db)
## for show all data base call show_all_data_base(db)
# show_all_data_base(db)
update_element(db,'first_name','sepehr','arman')
delete_element(db,"first_name","hadi")

show_all_data_base(db)
