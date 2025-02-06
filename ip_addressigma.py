import ipaddress
import sys
import subprocess

def cidr_to_bin_submask(cidr_input):
    # Convert CIDR to binary
    cidr = int(cidr_input.split('/')[1])
    binary_submask = '1' * cidr + '0' * (32 - cidr)
    print("Binary Subnet Mask:", binary_submask)
    return binary_submask

def parse_ip_address(cidr_input):
    # Remove the CIDR notation
    ip_str = cidr_input.split('/')[0]
    # Split the IP address into its octets
    octets = ip_str.split('.')
    print("IP Address:", ip_str)
    return octets

def ip_to_bin(octets):
    # Convert each octet to its binary representation
    binary_octets = [format(int(octet), '08b') for octet in octets]
    print("Binary IP Address:", '.'.join(binary_octets))
    return binary_octets

def apply_subnet_mask(bin_ip, binary_submask):
    # Combine the list of binary octets into a single string
    bin_ip_str = ''.join(bin_ip)
    
    # Perform bitwise AND
    network_bits = ''.join(['1' if bin_ip_str[i] == '1' and binary_submask[i] == '1' else '0' for i in range(32)])
    
    # Split the result back into octets
    network_octets = [network_bits[i:i+8] for i in range(0, 32, 8)]
    print("Binary Network Address:", '.'.join(network_octets))
    
    # Convert binary network address to decimal format
    network_address = '.'.join([str(int(octet, 2)) for octet in network_octets])
    print("Network Address:", network_address)
    return network_address

def calculate_network_range(cidr_input, network_address):
    cidr = int(cidr_input.split('/')[1])
    host_bits = 32 - cidr
    total_addresses = 2 ** host_bits

    network_int = int(ipaddress.IPv4Address(network_address))
    broadcast_int = network_int + total_addresses - 1

    # Exclude the first and last IP addresses
    start_ip = str(ipaddress.IPv4Address(network_int + 1))
    broadcast_ip = str(ipaddress.IPv4Address(broadcast_int - 1))
    
    print("Network Range (excluding first and last):", start_ip, "-", broadcast_ip)
    return start_ip, broadcast_ip

def ping_network_range(start_ip, broadcast_ip):
    # Ping the network range and provide detailed output
    print("Pinging network range...")
    for i in range(int(ipaddress.IPv4Address(start_ip)), int(ipaddress.IPv4Address(broadcast_ip)) + 1):
        ip = str(ipaddress.IPv4Address(i))
        try:
            result = subprocess.run(
                ["ping", "-c", "1", "-W", "1", ip],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
        except Exception as e:
            print(f"{ip} - ERROR: {str(e)}")
            continue

        if result.returncode == 0:
            # Parse the response time from the ping output
            response_time = "N/A"
            for line in result.stdout.splitlines():
                if "time=" in line:
                    try:
                        # Extract the value after 'time=' and before ' ms'
                        part = line.split("time=")[1]
                        response_time = part.split()[0]
                    except Exception as e:
                        response_time = "N/A"
                    break
            print(f"{ip} - UP    - Response time: {response_time} ms")
        else:
            error_message = result.stderr.strip() or "(No response)"
            print(f"{ip} - DOWN  - ERROR: {error_message}")


if __name__ == "__main__":
    # Takes user inputted CIDR address
    if len(sys.argv) != 2:
        print("Usage: python3 ip_addressigma.py <CIDR address>")
        sys.exit(1)

    cidr_input = sys.argv[1]
    # Validate cidr_input
    try:
        network = ipaddress.ip_network(cidr_input, strict=False)
    except ValueError:
        print("Invalid CIDR format. Please enter a valid CIDR address.")
        exit(1)

    # Convert CIDR to binary
    binary_submask = cidr_to_bin_submask(cidr_input)

    # Parse the IP address
    octets = parse_ip_address(cidr_input)

    # Convert IP address to binary
    bin_ip = ip_to_bin(octets)

    # Apply the subnet mask
    network_address = apply_subnet_mask(bin_ip, binary_submask)

    # Calculate network range based on subnet mask
    start_ip, broadcast_ip = calculate_network_range(cidr_input, network_address)
    # Ping the calculated network range
    ping_network_range(start_ip, broadcast_ip)