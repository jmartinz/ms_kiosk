#!/bin/bash

mpc -h 192.168.1.111 -p 6600 clear
mpc -h 192.168.1.111 -p 6600 load nenes
mpc -h 192.168.1.111 -p 6600 play