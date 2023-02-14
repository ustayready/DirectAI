DirectAI
==================

## Overview ##
ChatGPT queries via OpenAI API in your terminal.

A quick utility you can keep in a terminal window to rapidly query OpenAI's ChatGPT via the API and receive the results. There are probably better, more fully featured alternatives out there but I got tired of looking and fighting with pre-reqs so I just threw this together. 

Follow me on Twitter ([Mike Felch - @ustayready](https://twitter.com/ustayready)) 

## Benefits ##

 * Uses an OpenAI API key instead of fighting other users on the web interface
 * Set the OpenAI API key in an environment variable (OPENAI_API_KEY) or as a flag
 * Just input `clear` to clear the terminal
 * Just input `quit` to exit the client back to the terminal

## Disclaimer ##
 * I'm not responsible for your ChatGPT addiction.
 * Be careful not to query ChatGPT with sensitive information.

## Basic Usage ##
### Requires OpenAI API key
```
usage: direct.py [-h] [--key KEY]

Directly query ChatGPT using the API

optional arguments:
  -h, --help  show this help message and exit
  --key KEY   OpenAI API key
  
DirectAI the ChatGPT terminal client
```
         
## Installation ##
You can install and run with the following command:

```bash
$ git clone https://github.com/ustayready/directai
$ cd directai
~/directai $ virtualenv -p python3 .
~/directai $ source bin/activate
(directai) ~/directai $ pip install -r requirements.txt
(directai) ~/directai $ python direct.py
```

Note that Python 3.6+ is required.

