#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 17:34:22 2022

@author: stellarremnants
"""

import argparse
import os
import platform

DEFAULT_ADDRESS = "127.0.0.1"
DEFAULT_PORT="32330"
DEFAULT_PASSWORD = "DINOSAUR OFFICE"
DEFAULT_EXECUTABLE = "rcon"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Send a command to an RCON compatible server."
        )
    parser.add_argument("--address", "-a", nargs="?", dest="address", default=DEFAULT_ADDRESS)
    parser.add_argument("--port", "-p", nargs="?", dest="port", default=DEFAULT_PORT)
    parser.add_argument("--password", "-P", nargs="?", dest="password", default=DEFAULT_PASSWORD)
    parser.add_argument("--executable", "-e", nargs="?", dest="executable", default=DEFAULT_EXECUTABLE)
    parser.add_argument("--verbose", "-v", action="count", dest="verbose", default=0)
    parser.add_argument("rcon_command", nargs="*", type=str)
    
    args = parser.parse_args()
    
    rcon_command = " ".join(args.rcon_command)
    
    operating_system = platform.platform()
    
    executable_prefix=""
    
    if "linux" in operating_system.lower():
        if args.verbose >= 2:
            print(f"Operating on Linux ({operating_system})")
        executable_prefix="./"
    elif "windows" in operating_system.lower():
        if args.verbose >= 2:
            print(f"Operating on Windows ({operating_system})")
        executable_prefix=""
    else:
        if args.verbose >= 1:
            print(f"Operating on unknown or unsupported OS: {operating_system}")
        executable_prefix="./"
        
    
    if args.verbose >= 2:
        print(
            f"Sending an RCON command using the following settings:\n"
            f"Address:      {args.address}\n"
            f"Port:         {args.port}\n"
            f"Password:     {args.password}\n"
            f"Executable:   {args.executable}\n"
            f"RCON command: {rcon_command}\n"
            )
    
    command = f"./{args.executable} -a{args.address} -p{args.port} -P\"{args.password}\" {rcon_command}"
    if args.verbose >= 1:
        print(f"Executing command:\n{command}\n")
    os.system(command)
