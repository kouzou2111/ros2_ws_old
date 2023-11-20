import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from std_msgs.msg import Int16   #通信の型（16ビットの符号付き整数）

def cb(msg):          #17行目で定期実行されるコールバック関数
    global node       #関数を抜けてもnがリセットされないようにしている
    node.get_logger().info("Listen: %d" %msg.data)

rclpy.init()
node = Node("listener")            #ノード作成（nodeという「オブジェクト」を作成）
sub = node.create_subscription(Int16, "countup", cb,10)   #パブリッシャのオブジェクト作成
rclpy.spin(node)            #実行（無限ループ）
