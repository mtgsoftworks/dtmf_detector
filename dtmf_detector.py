#!/usr/bin/python
import sys
from os import path
from DTMFdetector import DTMFdetector

def usage():
  print("")
  print("Wave audio file based DTMF detector")
  print("Outputs DTMF digits detected from wave audio file")
  print("")
  print("Usage:")
  print("")
  print("dtmf_detector -i pathToWavFile [-f frequency] [-d] [-h] [-?]")
  print("                      [-ss sample size] [-ch channels] [-e encoding]")
  print("")
  print("Notes:")
  print("       parameters in brackets are optional")
  print("")
  print("       filepath to wave audio file may be relative or absolute")
  print("")
  print("       Default supported & tested audio file formats are")
  print("       16-bit, mono, 8kHz, PCM encoding (default format)")
  print("       16-bit, mono, 16kHz, PCM encoding (doesn't work well)")
  print("")
  print("       For other sample sizes, frequencies, and encoding formats,")
  print("       you will have to modify the source code to support them.")
  print("")
  print("       For now, the code/tool will ignore unsupported sample sizes,")
  print("       frequencies, encodings, etc. when you supply them as inputs.")
  print("")
  print("       NOTE: If you try and supply a wave audio file w/ unsupported")
  print("       audio file format, code/tool will likely return an error or")
  print("       unreliable results.")
  print("")
  print("")
  print("       frequency = 8000, 16000, 11025, 22050, 44100, etc.")
  print("       sample size, in bits = 8, 16")
  print("       channels = 1 for mono, 2 for stereo")
  print("       encoding = PCM, ADPCM, mu-Law, a-Law, etc.")
  print("")
  print("       -d = enable debug mode:")
  print("            outputs additional info for DTMF detection analysis")
  print("       -h or -? = print this help contents")
  print("")


if len(sys.argv) < 2:
  usage()
  sys.exit(2)


wavfile = ""
debugFlag = False
freq = 8000


samplesize = 16
channels = 1
encoding = "PCM"


for i in range(len(sys.argv)):
  if sys.argv[i] == '-h':
    usage()                     
    sys.exit()                  
  elif sys.argv[i] == '-?':
    usage()                     
    sys.exit()
  elif sys.argv[i] == '-i':
    wavfile = sys.argv[i+1]
  elif sys.argv[i] == '-f':
    freq = sys.argv[i+1]
  elif sys.argv[i] == '-d':
    debugFlag = True
  elif sys.argv[i] == '-ss':
    samplesize = sys.argv[i+1]
  elif sys.argv[i] == '-ch':
    channels = sys.argv[i+1]
  elif sys.argv[i] == '-e':
    encoding = sys.argv[i+1]

if not path.exists(wavfile):
  print("")
  print("Wave audio file does not exist. Please verify file.")
  print("Run \"dtmf_detector -h\" for usage info.")
  print("")
  sys.exit(2)

dtmf = DTMFdetector(freq,debugFlag)
data = dtmf.getDTMFfromWAV(wavfile)
print(data)
