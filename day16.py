class Packet:
    def __init__(self, version, typeid):
        self.version = version
        self.typeid = typeid

def parse_packet(bits, start=0):
    version = int(bits[start:start + 3], 2)
    typeid = int(bits[start + 3:start + 6], 2)

    result = Packet(version, typeid)

    if typeid == 4:
        num = ""
        parsed_until = start + 6

        while parsed_until < len(bits):
            num += bits[parsed_until + 1:parsed_until + 5]
            parsed_until += 5

            if bits[parsed_until - 5] == "0":
                break

        result.value = int(num, 2)
        return (result, parsed_until)

    result.length_type = int(bits[start + 6])

    if result.length_type:
        num_packets = int(bits[start + 7:start + 18], 2)

        result.sub_packets = []
        parsed_until = start + 18

        for _ in range(num_packets):
            p, parsed_until = parse_packet(bits, parsed_until)
            result.sub_packets.append(p)

        return (result, parsed_until)

    num_bits = int(bits[start + 7:start + 22], 2)

    result.sub_packets = []
    parsed_until = start + 22

    while parsed_until < start + 22 + num_bits:
        p, parsed_until = parse_packet(bits, parsed_until)
        result.sub_packets.append(p)

    return (result, parsed_until)

def total_versions(packet):
    if packet.typeid == 4:
        return packet.version

    return packet.version + sum(total_versions(p) for p in packet.sub_packets)

def hex_to_binary(s):
    htb = {"0": "0000", "1": "0001", "2": "0010", "3": "0011",
            "4": "0100", "5": "0101", "6": "0110", "7": "0111",
            "8": "1000", "9": "1001", "A": "1010", "B": "1011",
            "C": "1100", "D": "1101", "E": "1110", "F": "1111"}

    return "".join(htb[c] for c in s)

def main():
    with open("day16_input.txt") as f:
        bits = hex_to_binary(f.read().strip())
        print(f"Bits: {bits}")
        packet, _ = parse_packet(bits)
        print(f"Total version numbers are: {total_versions(packet)}")

if __name__ == "__main__":
    main()
