ip_address = input("Enter a IP-address like 10.0.1.1: ")

try:
    octets = list(map(int, ip_address.split('.')))

    if len(octets) != 4 or any(o < 0 or o > 255 for o in octets):
        print("unused")
    else:
        first_octet = octets[0]

        if ip_address == "0.0.0.0":
            print("unassigned")
        elif ip_address == "255.255.255.255":
            print("local broadcast")
        elif 1 <= first_octet <= 127:
            print("unicast")
        elif 128 <= first_octet <= 191:
            print("unicast")
        elif 192 <= first_octet <= 223:
            print("unicast")
        elif 224 <= first_octet <= 239:
            print("multicast")
        else:
            print("unused")
except ValueError:
    print("unused")