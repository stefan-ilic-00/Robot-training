import rtde_control

# Setup robot with robot IP address
rtde_c = rtde_control.RTDEControlInterface("192.168.1.20")


rtde_c.teachMode()
input('Press Enter stop Teach (Freedrive) mode...')
rtde_c.endTeachMode()

# Stop the RTDE control script
rtde_c.stopScript()