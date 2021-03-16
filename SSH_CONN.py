import paramiko, time


def ssh_conn(ip, user, pwd, cmd):
    #print("Creating SSH Client..")
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #print("Connection..")
    ssh_client.connect(hostname=ip, username=user, password=pwd)
    #print("Command execution..")
    ssh_client.exec_command(cmd)
    time.sleep(2)
    ssh_client.close()




