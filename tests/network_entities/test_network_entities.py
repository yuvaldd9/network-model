from scapy.all import Ether, IP, TCP, UDP

from network_model.network_entities import EthernetEntity, IPEntity, TCPEntity, UDPEntity


def test_ethernet_entity_sanity():
    assert EthernetEntity("ethernet_test", "AA:BB:CC:DD:EE:FF")


def test_ethernet_entity_base_packet(ethernet_entity):
    ethernet_entity._generate_base_packet()
    assert ethernet_entity._base_packet == Ether(src="AA:BB:CC:DD:EE:FF")


def test_ethernet_entity_send_packet_fields(ethernet_entity, basic_message):
    ethernet_entity._generate_base_packet()
    packet = ethernet_entity._generate_packet(basic_message)
    assert packet == Ether(src="AA:BB:CC:DD:EE:FF", dst="BB:AA:BB:AA:BB:AA")


def test_ip_entity_sanity():
    assert IPEntity("ip_test", "AA:BB:CC:DD:EE:FF", "1.1.1.1")


def test_ip_entity_base_packet(ip_entity):
    ip_entity._generate_base_packet()
    assert ip_entity._base_packet == Ether(src="AA:BB:CC:DD:EE:FF") / IP(src="1.1.1.1")


def test_ip_entity_send_packet_fields(ip_entity, basic_message):
    ip_entity._generate_base_packet()
    packet = ip_entity._generate_packet(basic_message)
    assert packet == Ether(src="AA:BB:CC:DD:EE:FF", dst="BB:AA:BB:AA:BB:AA") / IP(
        src="1.1.1.1", dst="0.0.0.0"
    )


def test_tcp_entity_sanity():
    assert TCPEntity("tcp_test", "AA:BB:CC:DD:EE:FF", "1.1.1.1", 5555)


def test_tcp_entity_base_packet(tcp_entity):
    tcp_entity._generate_base_packet()
    assert tcp_entity._base_packet == Ether(src="AA:BB:CC:DD:EE:FF") / IP(src="1.1.1.1") / TCP(sport=5555)


def test_tcp_entity_send_packet_fields(tcp_entity, basic_message):
    tcp_entity._generate_base_packet()
    packet = tcp_entity._generate_packet(basic_message)
    assert packet == Ether(src="AA:BB:CC:DD:EE:FF", dst="BB:AA:BB:AA:BB:AA") / IP(
        src="1.1.1.1", dst="0.0.0.0"
    ) / TCP(sport=5555, dport=8080)


def test_udp_entity_sanity():
    assert UDPEntity("udp_test", "AA:BB:CC:DD:EE:FF", "1.1.1.1", 5555)


def test_udp_entity_base_packet(udp_entity):
    udp_entity._generate_base_packet()
    assert udp_entity._base_packet == Ether(src="AA:BB:CC:DD:EE:FF") / IP(src="1.1.1.1") / UDP(sport=5555)


def test_udp_entity_send_packet_fields(udp_entity, basic_message):
    udp_entity._generate_base_packet()
    packet = udp_entity._generate_packet(basic_message)
    assert packet == Ether(src="AA:BB:CC:DD:EE:FF", dst="BB:AA:BB:AA:BB:AA") / IP(
        src="1.1.1.1", dst="0.0.0.0"
    ) / UDP(sport=5555, dport=8080)
