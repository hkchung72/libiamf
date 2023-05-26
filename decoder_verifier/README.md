## Usage<BR>

> iamfplayer.exe -i1 -o2 -s0 test_000019_s.mp4 -v test_000019_s.log -r 16000<BR>
--> test_000019_s.log is written.<BR>
    ss0_test_000019_s.wav is written.<BR>

> python.exe test_000019_s.py --log test_000019_s.log --wav ss0_test_000019_s.wav --psnr ref_ss0_test_000019_s.wav<BR>
--> call test_000019_s.py for verifying test_000019_s.log and ss0_test_000019_s.wav.<BR>

please see the 4 directories to see verfication result.<BR>

"decoder_verifier/log_output_files"<BR>
"decoder_verifier/wav_output_files"<BR>
"decoder_verifier/ref_audio_files"<BR>
"decoder_verifier/testscript_files"<BR>


