import ipaddress
import sys

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


if __name__ == "__main__":
    # Takes user inputted CIDR address
    if len(sys.argv) != 2:
        print("Usage: python3 ip_addressigma.py <CIDR address>")
        sys.exit(1)

    cidr_input = sys.argv[1]
    # Validate cidr_input
    try:
        network = ipaddress.ip_network(cidr_input)
    except ValueError:
        print("Invalid CIDR format. Please enter a valid CIDR address.")
        exit(1)

    # Convert CIDR to binary
    binary_submask = cidr_to_bin_submask(cidr_input)

    # Parse the IP address
    octets = parse_ip_address(cidr_input)
    bin_ip = ip_to_bin(octets)
    network_address = apply_subnet_mask(bin_ip, binary_submask)