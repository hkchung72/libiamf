## Build iamfplayer to support verifier<BR>

Build iamfplayer with SUPPORT_VERIFIER=1 option.<BR>
> 1. open code/win32/VS2015/iamf.sln in Visual Studio IDE <BR>
> 2. add SUPPORT_VERIFIER=1 to preprocessor definition property of iamf project  <BR>
> 3. add SUPPORT_VERIFIER=1 to preprocessor definition property of iamfplayer project  <BR>
> 4. build all <BR>
<BR>

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

please see the 5 directories to see the verification result.<BR>

"decoder_verifier/log_output_files"<BR>
"decoder_verifier/wav_output_files"<BR>
"decoder_verifier/report_files"<BR>
"decoder_verifier/testscript_files"<BR>

## How to perform full verification<BR>

> cd decoder_verifier
> mkdir tests
> copy ..\tests\*.* .
> runtest

When full verification is completed, report files for all test cases are created in the report_files directory.

