# The_Muezzin

The_Muezzin is project that takes wav files from folder
- save its metadata with its transcription into elasticsearch
  with hash from its metadata with transcription
- save wave file itself in mongoDB
  with the hash from metadata with transcription

## processing_data

### manager

Get foler path and trough glob library receive all wav files.

### metadata

Create dictionary with metadata
- file path
- name
- creation datetime
- modification datetime
- size
through os library.

### transcription

Transcript wav file trough speech_recognition library 
and adding this to the dictionary of metadata.

The transcription goes here becouse it part of processing.

### kafka

Send it with kafka producer with "processed" topic.

## store_data

### manager

Get the massage with kafka consumer with "processed" topic.
