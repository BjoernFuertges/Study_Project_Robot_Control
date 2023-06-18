import website.GUI as wcc
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Start the robot control system.')
    parser.add_argument('--name', type=str, default='IRobot',
                    help='Name of the robot for the connection to the webcontroller (default: IRobot)')
    parser.add_argument('--wc_ip', type=str, default='localhost',
                    help='IP address of the webcontroller (default: localhost)')
    parser.add_argument('--wc_port', type=int, default=50051,
                    help='Port number of the webcontroller (default: 50051)')
    parser.add_argument('--gui_debug', type=bool, default=True,
                    help='Activate debug modus (default: True --> debug modus is active)')
    parser.add_argument('--gui_ip', type=str, default='localhost',
                    help='IP address the GUI dev server should listen to (default: localhost)')
    parser.add_argument('--gui_port', type=int, default=5000,
                    help='Port number, the GUI dev server should listen to (default: 5000)')

    args = parser.parse_args()

    wcc.start(name=args.name, wc_ip=args.wc_ip, wc_port=args.wc_port, debug_modus=args.gui_debug, gui_ip=args.gui_ip, gui_port=args.gui_port)