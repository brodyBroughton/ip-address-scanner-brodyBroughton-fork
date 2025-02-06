[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/cYbEVSqo)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17976891)
# IP Address Scanner

A simple Python tool that converts CIDR notation into a binary subnet mask, parses the IP address, applies the subnet mask, calculates the network range, and pings each IP address in the range.

## Features
- Converts CIDR notation to binary subnet mask.
- Parses and converts the IP address to binary.
- Applies the subnet mask to compute the network address.
- Calculates the range of available IP addresses (excluding network and broadcast addresses).
- Pings all active IP addresses in the determined range and shows their response times.

## Prerequisites
- Python 3
- Network access permissions (for executing ping commands)

## Installation
1. Clone the repository:
    ```
    git clone https://github.com/brodyBroughton/ip-address-scanner-brodybroughton-fork.git
    ```
2. Change directory:
    ```
    cd ip-address-scanner-brodybroughton-fork
    ```

## Usage
Run the script with the required CIDR address:
```
python3 ip_addressigma.py <CIDR address>
```
For example:
```
python3 ip_addressigma.py 192.168.1.0/24
```

## How It Works
- The script converts the CIDR notation into a binary subnet mask.
- It extracts the IP address and its octets from the CIDR input.
- The IP address is translated into its binary form.
- A subnet mask is applied via a bitwise operation to identify the network address.
- The script then calculates the usable host IP range.
- Each IP within the range is pinged individually, and the output displays whether the host is UP or DOWN along with the response time if applicable.
