===========
Process PCAP
===========

Process PCAP provides functions to parse a provided PCAP file to extract all of the DST IP addresses contained in it. It also includes a function to retreive the geoloc information on a provided IP address::

    #!/usr/bin/env python

    from towelstuff import location
    from towelstuff import utils

    if utils.has_towel():
        print "Your towel is located:", location.where_is_my_towel()

(Note the double-colon and 4-space indent formatting above.)

Paragraphs are separated by blank lines. *Italics*, **bold**,
and ``monospace`` look like this.