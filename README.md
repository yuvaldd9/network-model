```markdown
# Network Model v1.0.0

Welcome to Network Model v1.0.0! This project allows you to model network activity by parsing a configuration file in YAML format and implementing the described network model using Scapy.
```

## Installation

### 1. Clone the Repository

```bash
git clone <repository_url>
cd network-model
```

### 2. Install Dependencies

Ensure you have Python installed (preferably Python 3.x). Then, install the package along with its dependencies using pip:

```bash
pip install .
```

This command will read the `pyproject.toml` file and install the required dependencies.

## Known Issues

- Currently, Network Model has only been tested on Linux systems.
- TCP acknowledgment (ack) and sequence (seq) sessions are not implemented in this version. However, they will be available in version 1.1.0.

## Features Coming in 1.1.0

In the upcoming version 1.1.0, we plan to introduce the following features:

- Virtual Interface support.
- Implementation of TCP session with acknowledgment (ack) and sequence (seq).
- Support for protocols: ARP and ICMP.
- Pytest plugin for easier testing.

Stay tuned for these exciting additions!

## Usage

After installing the package, you can execute Network Model using the following command:

```bash
network_model -f <file_descriptor>
```

Replace `<file_descriptor>` with the path to your configuration file in YAML format.

## Configuration File

Below is an example of a configuration file (`example_model.yml`) that describes the network model:

```yaml
name: "Example Model Descriptor"
interface: eth0
entities:
  -
      name: Alice
      protocol: tcp
      hw_address: "AA:AA:AA:AA:AA:AA"
      ip: 10.0.0.1
      port: 50001
  -
      name: Bob
      protocol: udp
      hw_address: "BB:BB:BB:BB:BB:BB"
      ip: 10.0.0.2
      port: 50002

sessions:
  -
      session_name: example1
      template: "custom"
      messages:
        - "Alice->Bob | Hello"
        - "Bob->Alice | Hi"
```

In this configuration:
- `name`: Descriptive name of the model.
- `interface`: Network interface to be used.
- `entities`: List of entities participating in the network model, including their names, protocols, hardware addresses, IPs, and ports.
- `sessions`: List of sessions defining the communication patterns between entities, including session name, template, and messages with sender, receiver, and data.

## Message Patterns

The messages in the configuration file follow the pattern:

```
sender->receiver | data
```

Where:
- `sender`: Name of the entity sending the message.
- `receiver`: Name of the entity receiving the message.
- `data`: Content of the message being transmitted.

Feel free to customize the configuration file to model your desired network activity.

## Contributing

We welcome contributions from the community! If you encounter any issues or have suggestions for improvements, please feel free to open an issue on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).

Happy networking with Network Model v1.0.0!
```