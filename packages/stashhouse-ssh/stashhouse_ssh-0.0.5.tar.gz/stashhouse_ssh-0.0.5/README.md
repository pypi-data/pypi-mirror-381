<!--suppress HtmlDeprecatedAttribute-->
<div align="center">
   <h1>🖥️ StashHouse: SSH Plugin</h1>
</div>

<hr />

<div align="center">

[💼 Purpose](#purpose) | [🛡️ Security](#security) | [⚖️ License](#license)

</div>

<hr />

# Purpose

A plugin for [StashHouse](https://pypi.org/project/stashhouse/) to include a Secure Copy Protocol (SCP) and Secure File 
Transfer Protocol (SFTP) server without authentication.

Registers a plugin named `ssh` and provides a `--ssh.port` argument to configure the port to listen on.

# Usage

This package is a plugin for [StashHouse](https://pypi.org/project/stashhouse/). To install the program:

```shell
python3 -m pip install 'stashhouse[ssh]'
```

The following command-line arguments are available:
```
--ssh.port: The port to start the SCP/SFTP server on
--ssh.host-key-file: The host key file to use.
--ssh.disable-host-key-save: Disables saving a new host key file if one does not exist.
```

For example, to start the SCP/SFTP server on port 2222 and use the SSH host key file at `ssh-host-key`, generating it 
if it does not exist:
```bash
stashhouse -e ssh --ssh.port 2222 --ssh.host-key-file ssh-host-key
```

# Security

By default, this plugin should **not** be deployed in an internet-facing manner to prevent unwanted file uploads. Always 
deploy it with appropriate security restrictions such as, but not exclusively, firewall rules.

# License

This package contains code under multiple licenses. This package primarily consists of code under the MIT License with
certain derivative works under the Eclipse Public License v2.0.

<details>
<summary>MIT License</summary>

```
Copyright (c) 2025 Jayson Fong

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

</details>

<details>
<summary>Eclipse Public License v2.0</summary>

```
Copyright (c) 2013-2024 by Ron Frederick <ronf@timeheart.net> and others.

This program and the accompanying materials are made available under the terms of the Eclipse Public License v2.0 which 
accompanies this distribution and is available at:

http://www.eclipse.org/legal/epl-2.0/
This program may also be made available under the following secondary licenses when the conditions for such availability 
set forth in the Eclipse Public License v2.0 are satisfied:

GNU General Public License, Version 2.0, or any later versions of that license
SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later
```

</details>
