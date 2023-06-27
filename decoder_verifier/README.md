## Usage<BR>

> iamfplayer.exe -i0 -o2 -r 16000 -v ./test_000000_3.log -s0 test_000000_3.iamf<BR>
--> 000000_3.log is written.<BR>
    ss0_000000_3.wav is written.<BR>

> iamfplayer.exe -i1 -o2 -r 16000 -v ./test_000000_3_f.log -s0 test_000000_3_f.mp4<BR>
--> test_000000_3_f.log is written.<BR>
    ss0_000000_3_f.wav is written.<BR>

> iamfplayer.exe -i1 -o2 -r 16000 -v ./test_000000_3_s.log -s0 test_000000_3_s.mp4<BR>
--> test_000000_3_s.log is written.<BR>
    ss0_000000_3_s.wav is written.<BR>

> python.exe test_000019_s.py --log test_000019_s.log --wav ss0_test_000019_s.wav --psnr ref_ss0_test_000019_s.wav<BR>
--> call test_000019_s.py for verifying test_000019_s.log and ss0_test_000019_s.wav.<BR>

please see the 4 directories to see verfication result.<BR>

"decoder_verifier/log_output_files"<BR>
"decoder_verifier/wav_output_files"<BR>
"decoder_verifier/ref_audio_files"<BR>
"decoder_verifier/testscript_files"<BR>


