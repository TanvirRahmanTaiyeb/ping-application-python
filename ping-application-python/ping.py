import os
import socket
import struct
import select
import time

# Function to calculate checksum (error-checking value)
def calculate_checksum(data):
    total_sum = 0
    count_to = (len(data) // 2) * 2
    count = 0

    while count < count_to:
        val = data[count + 1] * 256 + data[count]
        total_sum += val
        total_sum &= 0xffffffff
        count += 2

    if count_to < len(data):
        total_sum += data[-1]
        total_sum &= 0xffffffff

    total_sum = (total_sum >> 16) + (total_sum & 0xffff)
    total_sum += (total_sum >> 16)
    checksum = ~total_sum
    checksum &= 0xffff
    checksum = checksum >> 8 | ((checksum & 0xff) << 8)
    return checksum

# Function to create ICMP packet (ping request)
def create_icmp_packet(packet_id, sequence):
    header = struct.pack('bbHHh', 8, 0, 0, packet_id, sequence)
    data = struct.pack('d', time.time())
    packet_checksum = calculate_checksum(header + data)
    header = struct.pack('bbHHh', 8, 0, socket.htons(packet_checksum), packet_id, sequence)
    return header + data

# Function to send ICMP packet
def send_icmp_packet(sock, dest_addr, packet_id, sequence):
    packet = create_icmp_packet(packet_id, sequence)
    sock.sendto(packet, (dest_addr, 1))

# Function to receive ICMP reply
def receive_icmp_packet(sock, packet_id, sequence, timeout=1):
    time_remaining = timeout
    while True:
        start_time = time.time()
        readable = select.select([sock], [], [], time_remaining)
        elapsed_time = time.time() - start_time

        if not readable[0]:
            return None, None

        time_received = time.time()
        received_packet, addr = sock.recvfrom(1024)
        icmp_header = received_packet[20:28]
        pkt_type, code, checksum, pkt_id, seq = struct.unpack("bbHHh", icmp_header)

        if pkt_id == packet_id and seq == sequence:
            bytes_in_double = struct.calcsize("d")
            time_sent = struct.unpack("d", received_packet[28:28 + bytes_in_double])[0]
            ttl = struct.unpack("B", received_packet[8:9])[0]
            return time_received - time_sent, ttl

        time_remaining -= elapsed_time
        if time_remaining <= 0:
            return None, None

# Function to display ping result
def display_ping_statistics(dest_addr, sequence, delay, ttl):
    if delay is None:
        print(f"Request timeout for icmp_seq {sequence}")
    else:
        print(f"64 bytes from {dest_addr}: icmp_seq={sequence} ttl={ttl} time={delay * 1000:.3f} ms")

# Main function to run ping
def my_ping(host, count=4):
    try:
        dest_addr = socket.gethostbyname(host)
        print(f"PING {host} ({dest_addr}): 56 data bytes\n")

        with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname("icmp")) as sock:
            for sequence in range(count):
                send_icmp_packet(sock, dest_addr, os.getpid() & 0xFFFF, sequence)
                delay, ttl = receive_icmp_packet(sock, os.getpid() & 0xFFFF, sequence)
                display_ping_statistics(dest_addr, sequence, delay, ttl)
                time.sleep(1)

    except socket.error as err:
        print("Socket error:", err)
        print("This script must be run as root/Administrator.")

# Entry point
if __name__ == '__main__':
    host_to_ping = input("Enter a host to ping: ")
    my_ping(host_to_ping)
