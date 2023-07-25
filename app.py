import flask
import csv

app = flask.Flask(__name__)
app.config['DEBUG'] = True
    

file_obj = open('/Users/bharathraj.karkera/Desktop/imp/Users.csv', 'r')
dict_obj = csv.DictReader(file_obj)
Users = [i for i in dict_obj]
file_obj.close()


@app.route('/users', methods=['GET'])
def get_users():
    return flask.jsonify(Users)


@app.errorhandler(404)
def not_found(error):
    return flask.make_response(flask.jsonify({'error': 'Not found'}),
                               404)

@app.route('/users/<int:id>', methods=['GET'])
def getUserById(id):
    requested_user = [i for i in Users if i['id'] == str(id)]
    if len(requested_user) == 0:
        flask.abort(404)
    else:
        return flask.jsonify(requested_user)


@app.route('/users', methods=['POST'])
def create_user():
    if not flask.request.json:
        flask.abort(400)

    required = {
        'name': str,
        'age': int,
        'JL': str,
        'Language': str
        }

    json_data = flask.request.get_json()
    missing_fields = [i for i in required.keys() if i not in json_data]

    if len(missing_fields) > 0:
        api_response = {'status': 'error',
                        'message': 'Json request is missing mandatory parameters',
                        'missing': missing_fields}
        return (flask.jsonify(api_response), 400)

    elif len(missing_fields) == 0:
       wrong_data_types = [i for i in required.keys() if not isinstance(json_data[i], required[i])]
       if len(wrong_data_types) > 0:
           api_response = {'status': 'error','message': 'Json request data type is not matching the required format','missing': wrong_data_types}
           return (flask.jsonify(api_response), 400)
    global Users 
    id_list=[]
    for i in Users:
       id_list.append(int(i['id'])) 
       
    id_list=list(set(id_list)) 
    id_value = max(id_list)+1

    new_entry = {
        'id': id_value,
        'name': flask.request.json['name'],
        'Language': flask.request.json['Language'],
        'JL': flask.request.json['JL'],
        'age': flask.request.json['age'],
        }
    Users.append(new_entry)
    file_obj = open('/Users/bharathraj.karkera/Desktop/imp/Users.csv',
                    'a+', newline='\n', encoding='utf-8')
    writer_obj = csv.writer(file_obj,lineterminator='\n')
    row_to_be_added = [id_value, flask.request.json['name'],
                       flask.request.json['Language'],
                       flask.request.json['JL'],
                       flask.request.json['age']]
    writer_obj.writerow(row_to_be_added)
    file_obj.close()

    return (flask.jsonify(new_entry), 200)


@app.route('/users/<int:id>',methods=['PUT'])
def update_user(id):
   global Users
   requested_user = [i for i in Users if i['id'] == str(id)]
   if len(requested_user) == 0:
      api_response = {'status': 'error','message': 'User does not exists','missing': id}
      return (flask.jsonify(api_response), 404)
   else:
      json_data = flask.request.get_json()
      passed_fields=[i for i in json_data.keys()]
      available_fields=['id', 'name', 'Language', 'age', 'JL']
      for i in passed_fields:
         if i not in available_fields:
            api_response = {'status': 'error','message': 'Invalid data field passed in the JSON request','invalid': i}
            return (flask.jsonify(api_response), 400)
         else:
            pass
      buffer_list=Users
      for i in passed_fields:
         for j in buffer_list:
            if j['id']==str(id):
               j[i]=json_data[i]
      Users=buffer_list
      file_obj=open('/Users/bharathraj.karkera/Desktop/imp/Users.csv','w')
      field_names=['id' , 'name' , 'Language' , 'JL' , 'age']
      dict_obj=csv.DictWriter(file_obj,field_names)
      dict_obj.writeheader()
      for i in Users:
         dict_obj.writerow(i)
      file_obj.close()
      requested_user = [i for i in Users if i['id'] == str(id)]
      return (flask.jsonify(requested_user) ,200)   


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
   print(id)
   global Users
   requested_user = [i for i in Users if i['id'] == str(id)]
   print(requested_user)
   if len(requested_user) == 0:
      api_response = {'status': 'error','message': 'User does not exists','missing': id}
      flask.abort(404)
   else:
      Users.remove(requested_user[0])
      api_response = {'status': 'success','message': 'User Data removed Successfully','removed id': id}
      return (flask.jsonify(api_response), 200)
      
app.run()

# curl -i http://127.0.0.1:5000/users
# curl -i -H "Content-Type: application/json" -X POST -d '{"name":"Aishwarya" , "JL": "SSE" , "Language": "Python" , "age":25 }' http://localhost:5000/users
# curl -i -H "Content-Type: application/json" -X POST -d '{"name":"Rohit" , "JL": "TL" , "Language": "Java" , "age":35 }' http://localhost:5000/users
# curl -i -H "Content-Type: application/json" -X POST -d '{"name":"Anil" , "JL": "TL" , "Language": "Java" }' http://localhost:5000/users
# curl -i -H "Content-Type: application/json" -X POST -d '{"name":"Anil" , "JL": "TL" , "Language": "Java" ,  "age":"25"}' http://localhost:5000/users
# curl -i -H "Accept: application/json"  -X GET http://127.0.0.1:5000/users
# curl -i -H "Content-Type: application/json" -X PUT -d '{"age":25,"name":"Bharath"}' http://localhost:5000/users/0
# curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/users/4
# Id, name, Language, age, JL
# 0, Bharath, Python, 26, TA
# 1, Shrini, Python, 28, TL
# 2, Naga, Java, 27, TA
# 3, Hitha, JS, 26, TA


#curl -i -H "Accept: application/json"  -X GET http://127.0.0.1:5000/users

#curl -i "http://localhost:5000/users" \
#-H "Accept: application/json" \
#-H "Content-Type:application/json" \
#--data @<(cat <<EOF
#{
#"name":"Maddy" , 
#"JL": "SSE" , 
#"Language": "Python" , 
#"age":25
#  }
#EOF
#)

#curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/users/7
