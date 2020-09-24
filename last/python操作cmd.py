import os
# 有返回值
# os.popen()
# print(result.read())
# os.system("jupyter notebook")
# print(os.path)


# 用户在服务器编辑个人文件夹，在Linux服务器开启独立的notebook服务
@api.route('/start_notebook', methods=['POST', 'GET'])
@cross_origin()
def Start_Notebook():
    """
    返回给前端用户notebook服务的地址
    服务器需安装jupyter notebook， pip install jupyter notebook
    服务器端是否存在/home/USERNAME/.jupyter/jupyter_notebook_config.py文件
    若不存在，jupyter notebook --generate-config
    不必要设置服务器的notebook密码
    ./notebook
        config1.py
        config2.py
        username1
            ...
        username2
            ...
    """
    # SOCKET_USER_FOLDER_PATH =  '/root/.jupyter'
    data = json.loads(request.get_data())
    username = data['username']
    # 再修改，存数据库较好
    collection = client['user']['index']
    user = collection.find({'username':username})
    port = user['port']
    
    path = SOCKET_USER_FOLDER_PATH + '/' + username
    if not os.path.exists(path):
        os.mkdir(path)
        with open(SOCKET_USER_FOLDER_PATH + '/jupyter_notebook_config.py', 'r') as f:
            lines = f.readlines()
          # 修改端口和启动地址，默认端口和地址在最后两行
        lines[-2] = 'c.NotebookApp.port = ' + port + '\n'
        lines[-1] = "c.NotebookApp.notebook_dir = '" + path + "'"
        with open(SOCKET_USER_FOLDER_PATH + '/jupyter_notebook_config_' + username + '.py', 'w') as f:
            new_config_str = ''.join(lines)
            f.write(new_config_str)

    # 在服务器指定用户文件夹用配置文件运行notebook服务
    os.chdir(SOCKET_USER_FOLDER_PATH)
    os.system("jupyter notebook --config jupyter_notebook_config_" + username + ".py")
    # notebook的服务端口在服务器的配置文件中
    data = {
        'url': 'http://' + SOCKET_IP + ':' + port,
        'status': 'start notebook sever successfully'
    }
    return jsonify(data)
