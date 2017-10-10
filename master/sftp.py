#-*- coding:utf-8 -*-
import paramiko
import time

class ScpAssistant(object):
    def __init__(self):
        print  '''
        -------欢迎使用 scp assistant--------
        '''
        self.remote_ips = {"10.5.79.2"}
        self.remote_password = "123456@com"
        self.service_port = 22
        self.username = "root"
        self.sshClient = paramiko.SSHClient()

    def scp_put(self, ip, local_file, remote_file):
        self.sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.sshClient.connect(ip, self.service_port, self.username, self.remote_password)
            print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            sftp = self.sshClient.open_sftp()
            print "scp ", local_file, " to ", ip, ":", remote_file
            sftp.put(local_file, remote_file)
        except Exception as ex:
            print ex


    def scp_get(self, ip, remote_file, local_file):
        self.sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.sshClient.connect(ip, self.service_port, self.username, self.remote_password)
            print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            sftp = self.sshClient.open_sftp()
            print "scp ", ip, ":", remote_file, " to ",  local_file
            sftp.get(remote_file, local_file)
        except Exception as ex:
            print ex


def main():
    assistant = ScpAssistant()

    local_file = "/root/share/test/hello"
    remote_file = "/root/hello"

    local_file2 = "/root/share/test/world"
    remote_file2 = "/root/world"

    for ip in assistant.remote_ips:

        assistant.scp_get(ip, remote_file, local_file)
        print "-------------------------------------"

        assistant.scp_put(ip, local_file2, remote_file2)
        print "-------------------------------------\n"
    exit()

if __name__ == '__main__':
    main()