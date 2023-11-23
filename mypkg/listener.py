import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from person_msgs.msg import Person   #通信の型（16ビットの符号付き整数）

def cb(msg):          #17行目で定期実行されるコールバック関数
    global node       #関数を抜けてもnがリセットされないようにしている
    node.get_logger().info("Listen: %s" %msg)

rclpy.init()
node = Node("listener")            #ノード作成（nodeという「オブジェクト」を作成）
sub = node.create_subscription(Person, "person", cb,10)   #パブリッシャのオブジェクト作成
rclpy.spin(node)            #実行（無限ループ）
