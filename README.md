immunity_dbg_plugins
====================

Plugins created to work with Immunity Debugger

bchunter.py: Bad Character Hunter. So you got EIP and (lets say) ESP. Put a breakpoint on JMP ESP. Fill the ESP with byte array of '\x00\x01..\xff'. Use byteArray() from the code to your python exploit PoC. Once done, execute bchunter as

!bchunter ESP

It will flash a message displaying the badchar it found. Lets say '\x00' (very common).
Next, send bytearray with badchar removed. You can use filterBC() from code to your exploit PoC.

!bchunter ESP '\x00'

One badchar in each turn. Keep doing it till all badchars get removed.
