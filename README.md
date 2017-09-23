![Electrum-MORNINGSTAR](https://raw.githubusercontent.com/morningStar/electrum-morningstar/master/electrumlogo.png)
electrum-morningstar-server
=========================================
  * Language: Python
  * Authors: ThomasV (original ltc fork) bitspill & sunerok 

Features
--------

  * The server indexes UTXOs by address, in a Patricia tree structure
    described by Alan Reiner (see the 'ultimate blockchain
    compression' thread in the Bitcointalk forum)

  * The server requires morningstard, leveldb and plyvel

  * The server code is open source. Anyone can run a server, removing
    single points of failure concerns.

  * The server knows which set of MorningStar addresses belong to the same
    wallet, which might raise concerns about anonymity. However, it
    should be possible to write clients capable of using several
    servers. An i2p electrum server, as well as tor based electrum server 
    are soon to come.

Installation
------------

  1. To install and run a server, see INSTALL. For greater
     detail on the installation process, see HOWTO.md.

  2. To start and stop the server, use the 'electrum-morningstar-server' script



License
-------

electrum-morningstar-server is made available under the terms of the [GNU Affero General
Public License](http://www.gnu.org/licenses/agpl.html), version 3. See the 
included `LICENSE` for more details.


