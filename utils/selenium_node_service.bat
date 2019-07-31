::在另一台奴隶机中启动一个node，jar包放在bat、driver同级目录下面

start java -jar selenium-server-standalone-3.9.1.jar -role node -port 6666 -hub http://192.168.0.21:4444/grid/register