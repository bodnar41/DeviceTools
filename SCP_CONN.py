import paramiko

def scp_conn(ip, user, pwd, action, filename):
    #print("Creating SSH Client..")
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=user, password=pwd)
    sftp_client = ssh_client.open_sftp()
    #print("File transferring")
    if action.lower() == "put":
        #sftp_client.put(f"C:/Users/kliens01/{filename}", f"C:/Users/{user}/{filename}")
        sftp_client.put(f"C:/Users/Device_tools/Devicetools/moduls/{filename}", f"C:/Users/Device_tools/Devicetools/{filename}")
    elif action.lower() == "get":
        #sftp_client.get(f"C:/Users/{user}/{filename}", f"C:/Users/kliens01/{filename}")
        sftp_client.get(f"C:/Users/Device_tools/Devicetools/{filename}", f"C:/Users/Device_tools/Devicetools/data/{filename}")

    sftp_client.close()
    ssh_client.close()