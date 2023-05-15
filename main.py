{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "02995607",
   "metadata": {},
   "outputs": [],
   "source": [
    "from autokm import auto_km as ak\n",
    "from music_files import music_handle_mvp\n",
    "from email_handler import email as em\n",
    "\n",
    "import time\n",
    "import os\n",
    "import pyautogui\n",
    "from pytesseract import pytesseract\n",
    "from datetime import datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c4014428",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{\"file_name\": \"\",\"file_path\": \"\",\"to\": \"sebastian\",\"subject\": \"hello\",\"body\": \"\"}\n",
      "{'file_name': '', 'file_path': '', 'to': 'sbucarion1@babson.edu', 'subject': 'hello', 'body': ''}\n"
     ]
    }
   ],
   "source": [
    "import email_handler\n",
    "em.email_main(\"send an email to sebastian with the subjec saying hello\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "7888a162",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C:\\Users\\sbucarion1\\Documents\\code\\pierre\\music_files\\spotify_config.ini\n",
      "C:\\Users\\sbucarion1\\Documents\\code\\pierre\\music_files\\spotify_config.ini\n",
      "MUSIC:  play monkeys spinning monkeys\n"
     ]
    }
   ],
   "source": [
    "music_handle_mvp.spotify_controller(\"play monkeys spinning monkeys\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "36bc7ec2",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Listening\n",
      "result2:\n",
      "{   'alternative': [   {   'confidence': 0.88653308,\n",
      "                           'transcript': 'nope yeah play monkeys spitting '\n",
      "                                         'monkeys'},\n",
      "                       {   'transcript': 'nope Pierre play monkeys spitting '\n",
      "                                         'monkeys'},\n",
      "                       {'transcript': 'European play monkeys spitting monkeys'},\n",
      "                       {   'transcript': 'no Pierre play monkeys spitting '\n",
      "                                         'monkeys'},\n",
      "                       {   'transcript': 'nope yeah play monkey spitting '\n",
      "                                         'monkeys'}],\n",
      "    'final': True}\n",
      "End\n",
      "Listening\n",
      "result2:\n",
      "{   'alternative': [   {   'confidence': 0.95610243,\n",
      "                           'transcript': \"spitting monkeys so it won't work no \"\n",
      "                                         \"it'll work and I just need to fix \"\n",
      "                                         'cuz like I said I was testing it '\n",
      "                                         'when I had a mic and headphones I '\n",
      "                                         'need a wiggle around with the input '\n",
      "                                         \"it's not playing monkeys spending \"\n",
      "                                         \"monkeys oh no cuz it didn't read it \"\n",
      "                                         'was looking for monkey speed'},\n",
      "                       {   'transcript': \"spitting monkeys so it won't work no \"\n",
      "                                         \"it'll work and I just need to fix \"\n",
      "                                         'cuz like I said I was testing it '\n",
      "                                         'when I had a mic and headphones I '\n",
      "                                         'need a wiggle around with the input '\n",
      "                                         \"it's not playing monkeys spending \"\n",
      "                                         \"monkeys oh no cuz it didn't read \"\n",
      "                                         \"it's looking for monkey speed\"},\n",
      "                       {   'transcript': \"spitting monkeys so it won't work no \"\n",
      "                                         \"it'll work and I just need to fix \"\n",
      "                                         'cuz like I said I was testing it '\n",
      "                                         'when I had a mic and headphones I '\n",
      "                                         'need a wiggle around with the input '\n",
      "                                         \"it's not playing monkeys spending \"\n",
      "                                         \"monkeys oh no cuz it didn't read it \"\n",
      "                                         'was looking for monkey speaking'},\n",
      "                       {   'transcript': \"spitting monkeys so it won't work no \"\n",
      "                                         \"it'll work and I just need to fix \"\n",
      "                                         'cuz like I said I was testing it '\n",
      "                                         'when I had a mic and headphones I '\n",
      "                                         'need a wiggle around with the input '\n",
      "                                         \"it's not playing monkeys spending \"\n",
      "                                         \"monkeys oh no cuz it didn't read \"\n",
      "                                         \"it's looking for monkey speaking\"},\n",
      "                       {   'transcript': \"spitting monkeys so it won't work no \"\n",
      "                                         \"it'll work and I just need to fix \"\n",
      "                                         'cuz like I said I was testing it '\n",
      "                                         'when I had a mic and headphones I '\n",
      "                                         'need a wiggle around with the input '\n",
      "                                         \"it's not playing monkeys spending \"\n",
      "                                         \"monkeys oh no cuz it didn't read it \"\n",

      "    'final': True}\n",
      "End\n",
      "Listening\n",
      "result2:\n",
      "{   'alternative': [   {   'confidence': 0.92158312,\n",

      "    'final': True}\n",
      "End\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\ipykernel_15780\\2126155405.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;32mwhile\u001b[0m \u001b[1;32mTrue\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m     \u001b[0mcommand\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mak\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcommand_listener\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mcommand\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Documents\\code\\pierre\\autokm\\auto_km.py\u001b[0m in \u001b[0;36mcommand_listener\u001b[1;34m(activator)\u001b[0m\n\u001b[0;32m     94\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     95\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mcommand_listener\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mactivator\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m\"pierre\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 96\u001b[1;33m     \u001b[0mcommand\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0minput_detector\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mactivator\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     97\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mcommand\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     98\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Documents\\code\\pierre\\autokm\\input_listener.py\u001b[0m in \u001b[0;36minput_detector\u001b[1;34m(activator, quick_input)\u001b[0m\n\u001b[0;32m     78\u001b[0m     \u001b[1;31m#Code to detect noise\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     79\u001b[0m     \u001b[1;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1000\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 80\u001b[1;33m         \u001b[0mblock\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mstream\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mINPUT_FRAMES_PER_BLOCK\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     81\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     82\u001b[0m         \u001b[0mamplitude\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mget_rms\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mblock\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\site-packages\\pyaudio\\__init__.py\u001b[0m in \u001b[0;36mread\u001b[1;34m(self, num_frames, exception_on_overflow)\u001b[0m\n\u001b[0;32m    568\u001b[0m                 raise IOError(\"Not input stream\",\n\u001b[0;32m    569\u001b[0m                               paCanNotReadFromAnOutputOnlyStream)\n\u001b[1;32m--> 570\u001b[1;33m             return pa.read_stream(self._stream, num_frames,\n\u001b[0m\u001b[0;32m    571\u001b[0m                                   exception_on_overflow)\n\u001b[0;32m    572\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "source": [
    "#Write something in input listener to shutoff get_audio after certain length of silence\n",
    "#add something to pass in device id to spotify api\n",
    "\n",
    "while True:\n",
    "    command = ak.command_listener()\n",
    "    \n",
    "    if command is not None:\n",
    "        music_handle_mvp.spotify_controller(command)\n",
    "        #em.email_main(command)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "102f91ee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Music Command:  resume song\n",
      "C:\\Users\\sbuca\\Documents\\pierre\\music_files\\spotify_icons\\navbar_buttons\n",
      "Box(left=2870, top=962, width=20, height=22)\n"
     ]
    }
   ],
   "source": [
    "music_handle_mvp.main(\"resume song\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b2f7164b",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'auto_km' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\ipykernel_15780\\3745270719.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#while True\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mcommand\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mauto_km\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcommand_listener\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0mmusic_handle_mvp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmain\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcommand\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'auto_km' is not defined"
     ]
    }
   ],
   "source": [
    "#while True\n",
    "command = auto_km.command_listener()\n",
    "music_handle_mvp.main(command)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "63b63762",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'pierre open spotify'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "command"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4554ed5f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def pierre():\n",
    "    while True:\n",
    "        command = auto_km.command_listener()\n",
    "        \n",
    "        if \"spotify\" in command:\n",
    "            #Goto music handler\n",
    "            track = command.split()[2:-2]\n",
    "            track = \" \".join(track)\n",
    "            \n",
    "            coors = auto_km.click_on_command(track) \n",
    "            \n",
    "            if coors != (0,0):\n",
    "                print(coors)\n",
    "                pyautogui.click(coors)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "317eb5b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Listening\n",
      "result2:\n",
      "{   'alternative': [   {   'confidence': 0.87750065,\n",
      "                           'transcript': 'play songs that headlight Clarity on '\n",
      "                                         'Spotify'},\n",
      "                       {   'transcript': 'play songs that hit Lake Clarity on '\n",
      "                                         'Spotify'},\n",
      "                       {   'transcript': 'Pierre play songs that hit Lake '\n",
      "                                         'Clarity on Spotify'}],\n",
      "    'final': True}\n",
      "play songs that headlight Clarity on Spotify\n",
      "End\n",
      "Listening\n",
      "result2:\n",
      "{   'alternative': [   {'confidence': 0.70868462, 'transcript': 'Haiti'},\n",
      "                       {'transcript': 'Patriot'},\n",
      "                       {'transcript': 'hey.'},\n",
      "                       {'transcript': 'PayPal'},\n",
      "                       {'transcript': 'paytm'}],\n",
      "    'final': True}\n",
      "Haiti\n",
      "End\n",
      "Listening\n",
      "result2:\n",
      "{   'alternative': [   {   'confidence': 0.59610277,\n",
      "                           'transcript': 'tapir play songs that hit like '\n",
      "                                         'Clarity on Spotify'},\n",
      "                       {   'transcript': 'hey Pierre play songs that hit like '\n",
      "                                         'Clarity on Spotify'},\n",
      "                       {   'transcript': 'hey Pierre play songs I hit like '\n",
      "                                         'Clarity on Spotify'},\n",
      "                       {   'transcript': 'tapir play songs I hit like Clarity '\n",
      "                                         'on Spotify'},\n",
      "                       {   'transcript': 'play Pierre play songs that hit like '\n",
      "                                         'Clarity on Spotify'}],\n",
      "    'final': True}\n",
      "tapir play songs that hit like Clarity on Spotify\n",
      "tapir play songs that hit like clarity on spotify\n",
      "(47.0, 551.0)\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-5-f4c0596ba133>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mpierre\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-4-e7ef884ac364>\u001b[0m in \u001b[0;36mpierre\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mpierre\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m     \u001b[1;32mwhile\u001b[0m \u001b[1;32mTrue\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m         \u001b[0mcommand\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mauto_km\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcommand_listener\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[1;34m\"spotify\"\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mcommand\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Documents\\pierre\\autokm\\auto_km.py\u001b[0m in \u001b[0;36mcommand_listener\u001b[1;34m(activator)\u001b[0m\n\u001b[0;32m     66\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     67\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mcommand_listener\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mactivator\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m\"pierre\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 68\u001b[1;33m         \u001b[0mcommand\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0minput_detector\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mactivator\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     69\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mcommand\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     70\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Documents\\pierre\\autokm\\input_listener.py\u001b[0m in \u001b[0;36minput_detector\u001b[1;34m(activator)\u001b[0m\n\u001b[0;32m     68\u001b[0m     \u001b[1;31m#Code to detect noise\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     69\u001b[0m     \u001b[1;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1000\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 70\u001b[1;33m         \u001b[0mblock\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mstream\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mINPUT_FRAMES_PER_BLOCK\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     71\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     72\u001b[0m         \u001b[0mamplitude\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mget_rms\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mblock\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda33\\lib\\site-packages\\pyaudio.py\u001b[0m in \u001b[0;36mread\u001b[1;34m(self, num_frames, exception_on_overflow)\u001b[0m\n\u001b[0;32m    610\u001b[0m                           paCanNotReadFromAnOutputOnlyStream)\n\u001b[0;32m    611\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 612\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mpa\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread_stream\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_stream\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mnum_frames\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mexception_on_overflow\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    613\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    614\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mget_read_available\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "source": [
    "pierre()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cb3af252",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Spotify\n",
    "\n",
    "#Use autokm to listen for command\n",
    "#Route externally\n",
    "#Use autokm to locate song or playlist on spotify"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0b725e90",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['songs', 'that', 'hit', 'like', 'clarity']"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "['play', 'songs', 'that', 'hit', 'like', 'clarity', 'on', 'spotify'][1:-2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b0002525",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
