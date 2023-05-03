## Usage

> iamfplayer.exe -i1 -o2 -s0 test_000019_s.mp4 -v test_000019_s.log -r 16000
--> test_000019_s.log is written.
    ss0_test_000019_s.wav is written.

> python.exe test_000019_s.py --log test_000019_s.log --wav ss0_test_000019_s.wav --bitwise ref_test_000019_s.wav
--> call test_000019_s.py for verifying test_000019_s.log and ss0_test_000019_s.wav.

please see the 4 directories to see verfication result.

"decoder_verifier/log_output_files"
"decoder_verifier/wav_output_files"
"decoder_verifier/ref_audio_files"
"decoder_verifier/testscript_files"


