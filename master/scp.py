#-*- coding:utf-8 -*-
import paramiko,os,sys,time

port = 22
user = 'root'
def ssh_scp_put(ip,port,user,password,local_file,remote_file):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, 22, 'root', password)
    a = ssh.exec_command('date')
    stdin, stdout, stderr = a
    print stdout.read()
    sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
    sftp = ssh.open_sftp()
    sftp.put(local_file, remote_file)

def ssh_scp_get(ip, port, user, password, remote_file, local_file):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, 22, 'root', password)
    a = ssh.exec_command('date')
    stdin, stdout, stderr = a
    print stdout.read()
    sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
    sftp = ssh.open_sftp()
    sftp.get(remote_file, local_file)



ip = raw_input("请输入远端主机的IP地址：")
password = raw_input("请输入远端主机的密码：")

while True:
    print '''
    -------欢迎使用 scp software--------
    上传文件请输入  [ 1 ]:
    下载文件请输入  [ 2 ]:
    退出SCP请输入   [ q ]:
    ------------------------------------
    '''
    choice = raw_input("请输入 [ ]")
    if choice == "1":
        local_file = raw_input("请输入本地文件的绝对路径：")
        remote_file = raw_input("请输入文件上传的绝对路径：")
        ssh_scp_put(ip,port,user,password,local_file,remote_file)
    elif choice == "2":
        remote_file = raw_input("请输入远端文件的绝对路径：")
        local_file = raw_input("请输入要放到本地的绝对路径：")
        ssh_scp_get(ip,port,user,password,remote_file,local_file)
    elif choice == "q":
        print "感谢使用，再见"
        exit()
    else:
        print "输入错误，请重新输入："