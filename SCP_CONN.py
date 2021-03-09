import paramiko

def scp_conn(ip = None, user = None, pwd = None, action = None, filename = None):

    print("Creating SSH Client..")
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=user, password=pwd)
    sftp_client = ssh_client.open_sftp()
    print("File transferring")
    if action.lower() == "put":
        #sftp_client.put(f"C:/Users/kliens01/{filename}", f"C:/Users/{user}/{filename}")
        sftp_client.put(f"C:/Users/teszt/Device tools/moduls/{filename}", f"C:/Users/Device_tools/Devicetools/{filename}")
    elif action.lower() == "get":
        #sftp_client.get(f"C:/Users/{user}/{filename}", f"C:/Users/kliens01/{filename}")
        sftp_client.get(f"C:/Users/Device_tools/Devicetools/{filename}", f"C:/Users/teszt/Device tools/data/{filename}")
    else:
        print("Enter valid action (put or get) :")
        scp_conn(ip, user, pwd, None, filename)
    sftp_client.close()
    ssh_client.close()