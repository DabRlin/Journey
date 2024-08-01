#用于SSH协议的库，支持远程服务器的操作
import paramiko

#创建SSH客户端实例
ssh = paramiko.SSHClient()

#设置缺少主机密钥的策略
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#l连接到ssh服务器
ssh.connect('hostname',username = 'user',password='passwd')

#exec_command返回标准输入流，输出流，错误流
stdin,stdout,stderr = ssh.exec_command('ls')
#打印输出
print(stdout.read().decode())
#关闭ssh连接
ssh.close()