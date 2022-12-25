import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MiniSubscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'test_topic',
            self.listner_callback,
            10
        )
        self.subscription

    def listner_callback(self, msg):
        self.get_logger().info('sub <- "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)
    mini_subscriber = MiniSubscriber()
    rclpy.spin(mini_subscriber)

    mini_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()