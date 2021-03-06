#!/usr/bin/python

import pyvisa as visa

from instruments import px100


class Instruments:
    def __init__(self):
        self.rm = visa.ResourceManager()
        self.instruments = []
        self.discover()

    def list(self):
        return self.instruments

    def instr(self):
        if self.instruments:
            return self.instruments[0]

    def discover(self):
        print("Detecting instruments...")
        for i in self.rm.list_resources():
            print(i)
            inst = self.rm.open_resource(i)
            try:
                driver = px100.PX100(
                    inst)  #Todo: loop over drivers if multiple
                if (driver.probe()):
                    self.instruments.append(driver)
                    print("found " + driver.name)
                else:
                    print("ko")
            except:
                print("err")
                inst.close()
        else:
            if len(self.instruments) == 0:
                print("No instruments found")
