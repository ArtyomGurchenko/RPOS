def process_cam_table(filename, vlan_filter):
    entries = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.split()
                if len(parts) == 4 and parts[1].count('.') == 2:
                    vlan = int(parts[0])
                    mac_address = parts[1]
                    interface = parts[3]
                    entries.append((vlan, mac_address, interface))
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"Error: {e}")

    entries.sort()

    for vlan, mac_address, interface in entries:
        if vlan == vlan_filter:
            print(f"{vlan}\t{mac_address}\t{interface}")


if __name__ == "__main__":
    vlan_input = int(input("Enter VLAN's number: "))
    process_cam_table('CAM_table.txt', vlan_input)