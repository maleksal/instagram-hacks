# Instagram Hacks

Watch Instagram story's and read Direct messages without getting marked as seen. This is can be achieved by using Mitmproxy that allows us to intercept HTTP traffic and tamper data, but in this example it's only blocking some internal API calls.

## Installation

* **Install**:

```console
# clone the repo
$ git clone https://github.com/maleksal/instagram-hacks

# install requirements
$ python3 -m pip install -r requirements.txt

```

- **Configure system proxy settings :**

  If you are using ubuntu, go settings > network > network proxy > click manual. Then in http proxy put 127.0.0.1 and http port  8080

* **Install certificate :**

  run main.py, then in your browser go to mitm.it download the certificate and follow the 2 steps instruction.

### You're ready to go :)

> full documentation of Mitmproxy is available [here](https://github.com/mitmproxy/mitmproxy)

## Usage

```console
$ python3 main.py
```

> use control-c to exit



