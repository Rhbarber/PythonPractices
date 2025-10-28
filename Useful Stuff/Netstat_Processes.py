import subprocess
import psutil
import platform


def list_connections():
    try:
        # Detect the OS platform
        if platform.system() == "Windows":
            cmd = ['netstat', '-ano']
        else:
            cmd = ['ss', '-p']

        # Run the appropriate command
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode != 0:
            print(f"Error running command: {result.stderr}")
            return

        # Print header
        print(
            f"{'Proto':<6} {'Local Address':<25} {'Foreign Address':<25} {'State':<15} {'PID':<6} {'Process Name':<20}")

        # Parse the output line by line
        for line in result.stdout.splitlines():
            # Windows specific parsing for 'netstat -ano'
            if platform.system() == "Windows":
                if line.startswith(('TCP', 'UDP')):
                    parts = line.split()
                    if len(parts) >= 5:
                        proto = parts[0]
                        local_address = parts[1]
                        foreign_address = parts[2]
                        state = parts[3] if proto == 'TCP' else 'N/A'
                        pid = parts[-1]

                        # Get the process name using the PID
                        process_name = 'Unknown'
                        try:
                            process = psutil.Process(int(pid))
                            process_name = process.name()
                        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                            pass

                        print(
                            f"{proto:<6} {local_address:<25} {foreign_address:<25} {state:<15} {pid:<6} {process_name:<20}")

            # Linux specific parsing for 'ss -p'
            else:
                if line.startswith(('tcp', 'udp')):
                    parts = line.split()
                    proto = parts[0]
                    local_address = parts[4]
                    foreign_address = parts[5]
                    state = parts[1] if proto == 'tcp' else 'N/A'
                    pid_info = parts[-1] if 'pid=' in parts[-1] else 'pid=N/A'

                    pid = pid_info.split('pid=')[1].split(',')[0] if 'pid=' in pid_info else 'N/A'
                    process_name = 'Unknown'

                    if pid != 'N/A':
                        try:
                            process = psutil.Process(int(pid))
                            process_name = process.name()
                        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                            pass

                    print(
                        f"{proto:<6} {local_address:<25} {foreign_address:<25} {state:<15} {pid:<6} {process_name:<20}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    list_connections()
