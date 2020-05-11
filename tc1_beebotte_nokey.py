#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 RS Components Ltd
# SPDX-License-Identifier: MIT License

"""
Print the celsius reading out.
"""
from beebotte import *
import time
from DesignSpark.Pmod.HAT import createPmod

### Replace API_KEY and SECRET_KEY with those of your account
bbt = BBT('API key', 'Sercret key')

temp_resource   = Resource(bbt, 'Temp_raspberry', 'temp')

if __name__ == '__main__':
    
    therm = createPmod('TC1','JBA')
    time.sleep(0.1)
    
    try:
        while True:
            temp = therm.readCelcius()
            
            print(temp)
            temp_resource.write(temp)
            #intn = therm.readInternal()
            #print(intn)
            time.sleep(5)
    except KeyboardInterrupt:
        pass
    finally:
        therm.cleanup()
