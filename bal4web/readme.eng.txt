Balabolka (Command Line Utility for Online Text-To-Speech Using), version 1.11
Copyright (c) 2019-2021 Ilya Morozov
All Rights Reserved

WWW: http://balabolka.site/bconsole.htm
E-mail: crossa@list.ru

Licence: Freeware
Operating System: Microsoft Windows XP/Vista/7/8/10



*** Usage ***

bal4web [options ...]


*** Command Line Options ***

-s <service_name>
   Sets the name of the online TTS service ("google", "baidu", "youdao"). The default is "google".

-l <language_name>
   Sets the language name for online TTS service. The name is a combination of an ISO 639 two-letter lowercase culture code associated with a language and an ISO 3166 two-letter uppercase subculture code associated with a country or region.
   For example: en-US, de-DE, ru-RU. The default is "en-US".

-g <gender>
   Sets the gender for the online TTS service (if supported). The available values: "female" or "f", "male" or "m". The default value is not defined.
   Now the Google TTS supports this paratmeter only.

-m
   Prints the list of supported languages (and genders, if available) for the online TTS service.

-f <file_name>
   Sets the name of the input text file. The command line may contain few options [-f].

-w <file_name>
   Sets the name of the output file in WAV format.

-c
   Takes the text input from clipboard.

-t <text>
   Takes the text from the command line. The command line may contain few options [-t].

-i
   Takes the text input from STDIN.

--encoding <encoding> or -enc <encoding>
   Sets the input text encoding ("ansi", "utf8" or "unicode"). The default encoding for STDIN is "ansi".

-ln <integer>
   Selects a line from the text file by using of a line number. The line numbering starts at "1".
   The interval of numbers can be used for selecting of more than one line (for example, "26-34").
   The command line may contain few options [-ln].

-d <file_name>
   Applies a dictionary for pronunciation correction (*.BXD, *.DIC or *.REX). The command line may contain few options [-d].
   You may use the desktop application 'Balabolka' to edit a dictionary.

-lrc
   Creates the LRC file. Lyrics will be synchronized with the speech in the output audio file.

-srt
   Creates the SRT file. Subtitles will be synchronized with the speech in the output audio file.

-sub
   Input text will be processed as subtitles. The option may be useful, when the options [-i] or [-c] are specified.

-host <host_name>
   Sets the hostname of the proxy server.

-port <integer>
   Sets the port number of the proxy server.

-p
   Display progress information in a console window.

--ignore-square-brackets or -isb
   Ignore text in [square brackets].

--ignore-curly-brackets or -icb
   Ignore text in {curly brackets}.

--ignore-angle-brackets or -iab
   Ignore text in <angle brackets>.

--ignore-round-brackets or -irb
   Ignore text in (round brackets).

--ignore-url or -iu
   Ignore URLs.

--ignore-comments or -ic
   Ignore comments in text. Single-line comments start with // and continue until the end of the line. Multiline comments start with /* and end with */.

-? or -h
   Prints the list of available command line options.

--lrc-length <integer>
   Sets the maximal length of text lines for the LRC file (in characters).

--lrc-fname <file_name>
   Sets the name of the LRC file that will be created. The option may be useful, when the option [-o] is specified.

--lrc-enc <encoding>
   Sets the encoding for the LRC file ("ansi", "utf8" or "unicode"). The default is "ansi".

--lrc-offset <integer>
   Sets the time shift for the LRC file (in milliseconds).

--lrc-artist <text>
   Sets the ID tag for the LRC file: artist.

--lrc-album <text>
   Sets the ID tag for the LRC file: album.

--lrc-title <text>
   Sets the ID tag for the LRC file: title.

--lrc-author <text>
   Sets the ID tag for the LRC file: author.

--lrc-creator <text>
   Sets the ID tag for the LRC file: creator of the LRC file.

--srt-length <integer>
   Sets the maximal length of text lines for the SRT file (in characters).

--srt-fname <file_name>
   Sets the name of the SRT file. The option may be useful, when the option [-o] is specified.

--srt-enc <encoding>
   Sets the encoding for the SRT file ("ansi", "utf8" or "unicode"). The default is "ansi".

--sub-format <text>
   Sets the format of input subtitles ("srt", "lrc", "ssa", "ass", "smi" or "vtt"). If the option is not specified, the format will be determined through the file extension.


*** Examples ***

Create the text file LANGUAGE.TXT with the list of the supported languages and genders for the Google TTS service:

bal4web -s Google -m > language.txt


Convert text from BOOK.TXT to speech and save as BOOK.WAV:

bal4web -f "d:\Text\book.txt" -w "d:\Sound\book.wav" -s Google -l en-US


*** Configuration File ***

The command line options can be stored as a configuration file "bal4web.cfg" in the same folder as the utility.

The sample configuration file:
===============
-f d:\Text\book.txt
-w d:\Sound\book.wav
-s Google
-l de-DE
-d d:\Dict\rules.bxd
-lrc
--lrc-length 75
--lrc-enc utf8
===============

The utility may combine options from the configuration file and the command line.


*** Audio Clips ***

The application allows to insert links to external WAV files (audio clips) into text. Audio clip tag will look like:

{{Audio=C:\Sounds\ring.wav}}

The audio clip will be embedded in the audio file created by the application.


*** "Lang" Tag ***

If it is necessary to change the language during the text converting, a special tag can be used:

Read the English text. {{Lang=de-DE}} Lesen Sie den deutschen Text.

The tag is valid until the next tag or the end of text.

For Google TTS that tag may contain information about a gender ("f" or "m") and a speech rate (the rate values range from "0.1" to "3.0"; the average human speech rate is "1.0").

{{Lang=de-DE;f}}

{{Lang=fr-FR;m;1.2}}


*** "Pause" Tag ***

A specified number of milliseconds of silence can be inserted into the output audio file. For example:

One hundred twenty milliseconds of silence {{Pause=120}} just occurred.


*** Licence ***

You are free to use and distribute software for noncommercial purposes. For commercial use or distribution, you need to get permission from the copyright holder. The application can not be used on the territory of Belarus, Cuba, Iran, North Korea, Syria, and the Crimea Region.

###