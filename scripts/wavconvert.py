import sys
import time
import argparse
import os
import logging

parser = argparse.ArgumentParser(description = "Wav file converter for Qun mk2")

parser.add_argument("--input", type=str, required = True, help = "Input file name. Required")
parser.add_argument("--output_dir", type=str, required = True, help = "Output folder name. Required")
parser.add_argument("--separate_channels", action="store_true", help = "Separate channels")
parser.add_argument("--allmix", action="store_true", help = "Output mix and separated channels data")
parser.add_argument("--debug", action = "store_true", help = "Print incoming / outgoing MIDI signals")

args = parser.parse_args()

if args.allmix:
    args.separate_channels = True

if args.debug:
    logging.basicConfig(level = logging.DEBUG)
else:
    logging.basicConfig(level = logging.INFO)



base_name = os.path.basename(args.input)

if args.output_dir[-1] != "/":
    args.output_dir = args.output_dir + "/"

output_filename = args.output_dir + base_name

if args.separate_channels:
    output_filename_r = args.output_dir + "r_" + base_name
    output_filename_l = args.output_dir + "l_" + base_name

logging.debug("filename = " + output_filename)

command_common = "sox " + args.input + " "
common_option = " -r 48000 -b 16 -c 1 "
if args.separate_channels:
    command = command_common + common_option + output_filename_l + " remix 1"
    logging.debug(command)
    os.system(command)
    command = command_common + common_option + output_filename_r + " remix 2"
    logging.debug(command)
    os.system(command)

if args.separate_channels == False or args.allmix:
    #mixdown
    command = command_common + common_option + output_filename
    logging.debug(command)
    os.system(command)


print("Finished")
