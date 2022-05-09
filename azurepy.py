# -*- coding: utf-8 -*-

import azure.cognitiveservices.speech as speechsdk


class Azu:
    def __init__(self, azu_setting, options):
        self.setting = azu_setting
        self.options = options
        self.token = self.setting.get("token")
        self.region = self.setting.get("region")
     
      

    def process(self, text, audio_name):
        audioSaveFile = audio_name
        processPOSTRequest(self.appKey, self.token, text, audioSaveFile, self.options)

   



def processPOSTRequest(subscriptiontoken, subregion, text, audioSaveFile, options):


    speech_config = speechsdk.SpeechConfig(subscriptiontoken, region=subregion)
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    
    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name='zh-CN-YunyangNeural'
    
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    
    # Get text from the console and synthesize to the default speaker.
    print("Enter some text that you want to speak >")
    text = input()
    
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
    
    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(text))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")