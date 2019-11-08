#!/usr/local/bin/python3
import logging
import os


def testinfo():
    print("calling shots from test info")

def logForScript():
    hostname= "newcomp.interac.local"
    location= "equinix"
    builtdate= "13 sept 2019"
    if not os.path.exists("/Users/ashukla/Documents/Scripts/execution.log"):
        with open("/Users/ashukla/Documents/Scripts/execution.log", 'w'):
            logging.basicConfig(filename="/Users/ashukla/Documents/Scripts/execution.log", level=logging.ERROR)
            logging.error("hostname {} not found".format(hostname))
            logging.exception("the location {} does not exist".format(location))
            logging.fatal("the built data is {}".format(builtdate))

if __name__ == "__main__":
    testinfo()
    logForScript()




