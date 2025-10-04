<!--suppress HtmlDeprecatedAttribute-->
<div align="center">
   <h1>🐚 Netapult: SSH Plugin</h1>
</div>

<hr />

<div align="center">

[💼 Purpose](#purpose) | [🏁 Usage](#usage)

</div>

<hr />

# Purpose

This plugin provides the SSH protocol for [Netapult](https://pypi.org/project/netapult/), enabling scalable network 
automation and orchestration for network-connected devices.

# Usage

This package registers a `ssh` protocol handler for Netapult, usable from Netapult's dispatcher.

```python
import time

import netapult.dispatch

with netapult.dispatch.dispatch(
    "generic", # Use the generic client
    "ssh", # Use our SSH protocol
    protocol_options={
        "host": "your-host-here",
        "username": "your-username-here",
        "password": "your-password-here",
    },
) as client:
    # Allow time for the terminal to initialize
    time.sleep(3)

    # Acquire the banner
    banner: str = client.read(text=True)
    prompt_found, result = client.run_command("wall test1\n", text=True)

    print("Banner:", banner)
    print("Result:", result)

```