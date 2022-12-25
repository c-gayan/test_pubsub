import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class MiniPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publishers_ = self.create_publisher(String, 'test_topic', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
 
    def timer_callback(self):
        msg = String()
        msg.data = 'Hello gayan, this is %d message' % self.i
        self.publishers_.publish(msg)
        self.get_logger().info('pub -> "%s"' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    mini_publisher = MiniPublisher()
    rclpy.spin(mini_publisher)

    mini_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()       