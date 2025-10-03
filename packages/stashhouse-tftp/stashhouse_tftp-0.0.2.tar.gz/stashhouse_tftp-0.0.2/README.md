<!--suppress HtmlDeprecatedAttribute-->
<div align="center">
   <h1>🌴 StashHouse: TFTP Plugin</h1>
</div>

<hr />

<div align="center">

[💼 Purpose](#purpose) | [🛡️ Security](#security)

</div>

<hr />

# Purpose

A plugin for [StashHouse](https://pypi.org/project/stashhouse/) to offer the Trivial File Transfer Protocol (TFTP).

Registers a plugin named `tftp` and provides a `--tftp.port` argument to configure the port to listen on. The plugin
will prevent read access to files and only enable writing.

# Usage

This package is a plugin for [StashHouse](https://pypi.org/project/stashhouse/). To install the program:

```shell
python3 -m pip install 'stashhouse[tftp]'
```

The following command-line arguments are available:
```
--tftp.port: Port to listen on (default: 9069)
--tftp.ack-timeout: Timeout for each ACK. (default: 0.5)
--tftp.conn-timeout: Timeout before aborting a connection. (default: 3)
```

For example, to start the TFTP server on port 8069
```shell
stashhouse -e tftp --tftp.port 8069
```

# Security

The TFTP protocol lacks modern security mechanisms, such as authentication and encryption. Any file transfers involving
TFTP may traverse through the network in a plain-text form. It is not recommended to use or expose TFTP over an insecure
network such as the internet.
