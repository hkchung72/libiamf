import yaml
import inspect
import argparse

parser = argparse.ArgumentParser(description="test_000011 verification script")
parser.add_argument("--log",  type=str, required=True, help="decoder verification log output file")
parser.add_argument("--wav",  type=str, required=True, help="decoder verification wav output file")
parser.add_argument("--bitwise",  type=str, required=False, help="decoder verification bitwise comparison reference file")
parser.add_argument("--psnr",  type=str, required=False, help="decoder verification PSNR evaluation reference file")
args = parser.parse_args()

total_natoms = 0
total_nobus = 0
total_length_0 = 0
total_length_1 = 0
total_frames = 0
codec_samplerate_0 = 0

atom_list = []
obu_list = []
open_sharp0 = 0
open_sharp1 = 0
read_s = ""
with open(args.log,"r") as log_data:
    for line in log_data:
        if line == "#0\n":
            open_sharp0 = 1
        elif line == "#1\n":
            open_sharp1 = 1
        elif line == "##\n":
            if open_sharp0 == 1:
                open_sharp0 = 0
                json_o = yaml.load(read_s, Loader=yaml.FullLoader)
                obu_list.append(json_o)
                read_s = ""
                total_nobus += 1
            elif open_sharp1 == 1:
                open_sharp1 = 0
                json_a = yaml.load(read_s, Loader=yaml.FullLoader)
                atom_list.append(json_a)
                read_s = ""
                total_natoms += 1
        elif open_sharp0 == 1 or open_sharp1 == 1:
            read_s += line

print("*"*40)
print("* IAMF-ISOBMFF Syntax Check ")
print("*"*40)

pass_count = 0
if "ftyp_0000000000000000" in atom_list[0]:
	pass_count += 1
	atom = atom_list[0]["ftyp_0000000000000000"]
	if atom[0]["MajorBrands"] == "dash":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[1]["Version"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[2]["CompatibleBrands"] == "iso6iamf":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

if "moov_0000000000000018" in atom_list[1]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

if "mvhd_0000000000000020" in atom_list[2]:
	pass_count += 1
	atom = atom_list[2]["mvhd_0000000000000020"]
	if atom[0]["Version"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[1]["Flags"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[2]["CreationTime"] == "2023-04-19 00:00:00 UTC":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[3]["ModificationTime"] == "2023-04-19 00:00:00 UTC":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[4]["TimeScale"] == 16000:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[5]["Duration"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[6]["PreferedRate"] == 65536:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[7]["PreferedVolume"] == 256:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[8]["Reserved1"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[9]["Reserved2"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[10]["Reserved3"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[11]["MatrixStructure"] == "0x00010000 0x00000000 0x00000000 0x00000000 0x00010000 0x00000000 0x00000000 0x00000000 0x40000000":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[12]["PreviewTime"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[13]["PreviewDuration"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[14]["PosterTime"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[15]["SelectionTime"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

if "trak_00000000000000b4" in atom_list[3]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

if "tkhd_00000000000000bc" in atom_list[4]:
	pass_count += 1
	atom = atom_list[4]["tkhd_00000000000000bc"]
	if atom[0]["Version"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[1]["Flags"] == 3:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[2]["CreationTime"] == "2023-04-19 00:00:00 UTC":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[3]["ModificationTime"] == "2023-04-19 00:00:00 UTC":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[4]["TrackID"] == 1:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[5]["Reserved1"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[6]["Duration"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[7]["Reserved2"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[8]["Reserved3"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[9]["Layer"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[10]["AlternativeGroup"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[11]["Volume"] == 256:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[12]["Reserved4"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[13]["MatrixStructure"] == "0x00010000 0x00000000 0x00000000 0x00000000 0x00010000 0x00000000 0x00000000 0x00000000 0x40000000":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[14]["TrackWidth"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[15]["TrackHeight"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

if "mdhd_0000000000000120" in atom_list[5]:
	pass_count += 1
	atom = atom_list[5]["mdhd_0000000000000120"]
	if atom[0]["Version"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[1]["Flags"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[2]["CreationTime"] == "2023-04-19 00:00:00 UTC":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[3]["ModificationTime"] == "2023-04-19 00:00:00 UTC":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[4]["TimeScale"] == 16000:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[5]["Duration"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[6]["Language"] == 21956:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[7]["Quality"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

if "hdlr_0000000000000140" in atom_list[6]:
	pass_count += 1
	atom = atom_list[6]["hdlr_0000000000000140"]
	if atom[0]["Version"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[1]["Flags"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[2]["PreDefined"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[3]["ComponentSubtype"] == 1936684398:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[4]["Reserved1"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[5]["Reserved2"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[6]["Reserved3"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[7]["Name"] == "ISO Media file produced by Google Inc. Created on: 04/18/2023.":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

if "stbl_00000000000001cb" in atom_list[7]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

if "stsd_00000000000001d3" in atom_list[8]:
	pass_count += 1
	atom = atom_list[8]["stsd_00000000000001d3"]
	if atom[0]["Version"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[1]["Flags"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[2]["EntryCount"] == 1:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

if "iamf_00000000000001e3" in atom_list[9]:
	pass_count += 1
	atom = atom_list[9]["iamf_00000000000001e3"]
	if atom[0]["Reserved1"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[1]["Reserved2"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[2]["DataReferenceIndex"] == 1:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[3]["Reserved3"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[4]["Reserved4"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[5]["ChannelCount"] == 2:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[6]["SampleSize"] == 16:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[7]["Predefined"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[8]["Reserved5"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[9]["SampleRate"] == 16000:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

if "iamd_0000000000000207" in atom_list[10]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

if "stts_0000000000000288" in atom_list[11]:
	pass_count += 1
	atom = atom_list[11]["stts_0000000000000288"]
	if atom[0]["Version"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[1]["Flags"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[2]["EntryCount"] == 0:
		pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

if "stsc_0000000000000298" in atom_list[12]:
	pass_count += 1
	atom = atom_list[12]["stsc_0000000000000298"]
	if atom[0]["Version"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[1]["Flags"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[2]["EntryCount"] == 0:
		pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

if "stsz_00000000000002b8" in atom_list[13]:
	pass_count += 1
	atom = atom_list[13]["stsz_00000000000002b8"]
	if atom[0]["Version"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[1]["Flags"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[2]["SampleSize"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[3]["SampleCount"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

if "stco_00000000000002a8" in atom_list[14]:
	pass_count += 1
	atom = atom_list[14]["stco_00000000000002a8"]
	if atom[0]["Version"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[1]["Flags"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[2]["EntryCount"] == 0:
		pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

if "moof_00000000000002dc" in atom_list[15]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

if "traf_00000000000002f4" in atom_list[16]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

if "tfhd_00000000000002fc" in atom_list[17]:
	pass_count += 1
	atom = atom_list[17]["tfhd_00000000000002fc"]
	if atom[0]["Version"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[1]["Flags"] == 131106:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[2]["TrackID"] == 1:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[3]["SampleDescriptionIndex"] == 1:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[4]["DefaultSampleFlag"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

if "trun_0000000000000324" in atom_list[18]:
	pass_count += 1
	atom = atom_list[18]["trun_0000000000000324"]
	if atom[0]["Version"] == 1:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[1]["Flags"] == 769:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[2]["SampleCount"] == 126:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	SampleCount = atom[2]["SampleCount"]
	if atom[3]["DataOffset"] == 1134:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[4]["SampleDuration_0"] == 128:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[5]["SampleSize_0"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[6]["SampleDuration_1"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[7]["SampleSize_1"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[8]["SampleDuration_2"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[9]["SampleSize_2"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[10]["SampleDuration_3"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[11]["SampleSize_3"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[12]["SampleDuration_4"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[13]["SampleSize_4"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[14]["SampleDuration_5"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[15]["SampleSize_5"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[16]["SampleDuration_6"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[17]["SampleSize_6"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[18]["SampleDuration_7"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[19]["SampleSize_7"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[20]["SampleDuration_8"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[21]["SampleSize_8"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[22]["SampleDuration_9"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[23]["SampleSize_9"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[24]["SampleDuration_10"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[25]["SampleSize_10"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[26]["SampleDuration_11"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[27]["SampleSize_11"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[28]["SampleDuration_12"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[29]["SampleSize_12"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[30]["SampleDuration_13"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[31]["SampleSize_13"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[32]["SampleDuration_14"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[33]["SampleSize_14"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[34]["SampleDuration_15"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[35]["SampleSize_15"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[36]["SampleDuration_16"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[37]["SampleSize_16"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[38]["SampleDuration_17"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[39]["SampleSize_17"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[40]["SampleDuration_18"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[41]["SampleSize_18"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[42]["SampleDuration_19"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[43]["SampleSize_19"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[44]["SampleDuration_20"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[45]["SampleSize_20"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[46]["SampleDuration_21"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[47]["SampleSize_21"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[48]["SampleDuration_22"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[49]["SampleSize_22"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[50]["SampleDuration_23"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[51]["SampleSize_23"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[52]["SampleDuration_24"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[53]["SampleSize_24"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[54]["SampleDuration_25"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[55]["SampleSize_25"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[56]["SampleDuration_26"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[57]["SampleSize_26"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[58]["SampleDuration_27"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[59]["SampleSize_27"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[60]["SampleDuration_28"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[61]["SampleSize_28"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[62]["SampleDuration_29"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[63]["SampleSize_29"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[64]["SampleDuration_30"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[65]["SampleSize_30"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[66]["SampleDuration_31"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[67]["SampleSize_31"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[68]["SampleDuration_32"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[69]["SampleSize_32"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[70]["SampleDuration_33"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[71]["SampleSize_33"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[72]["SampleDuration_34"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[73]["SampleSize_34"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[74]["SampleDuration_35"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[75]["SampleSize_35"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[76]["SampleDuration_36"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[77]["SampleSize_36"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[78]["SampleDuration_37"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[79]["SampleSize_37"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[80]["SampleDuration_38"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[81]["SampleSize_38"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[82]["SampleDuration_39"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[83]["SampleSize_39"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[84]["SampleDuration_40"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[85]["SampleSize_40"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[86]["SampleDuration_41"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[87]["SampleSize_41"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[88]["SampleDuration_42"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[89]["SampleSize_42"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[90]["SampleDuration_43"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[91]["SampleSize_43"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[92]["SampleDuration_44"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[93]["SampleSize_44"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[94]["SampleDuration_45"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[95]["SampleSize_45"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[96]["SampleDuration_46"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[97]["SampleSize_46"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[98]["SampleDuration_47"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[99]["SampleSize_47"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[100]["SampleDuration_48"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[101]["SampleSize_48"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[102]["SampleDuration_49"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[103]["SampleSize_49"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[104]["SampleDuration_50"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[105]["SampleSize_50"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[106]["SampleDuration_51"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[107]["SampleSize_51"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[108]["SampleDuration_52"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[109]["SampleSize_52"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[110]["SampleDuration_53"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[111]["SampleSize_53"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[112]["SampleDuration_54"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[113]["SampleSize_54"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[114]["SampleDuration_55"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[115]["SampleSize_55"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[116]["SampleDuration_56"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[117]["SampleSize_56"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[118]["SampleDuration_57"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[119]["SampleSize_57"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[120]["SampleDuration_58"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[121]["SampleSize_58"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[122]["SampleDuration_59"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[123]["SampleSize_59"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[124]["SampleDuration_60"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[125]["SampleSize_60"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[126]["SampleDuration_61"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[127]["SampleSize_61"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[128]["SampleDuration_62"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[129]["SampleSize_62"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[130]["SampleDuration_63"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[131]["SampleSize_63"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[132]["SampleDuration_64"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[133]["SampleSize_64"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[134]["SampleDuration_65"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[135]["SampleSize_65"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[136]["SampleDuration_66"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[137]["SampleSize_66"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[138]["SampleDuration_67"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[139]["SampleSize_67"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[140]["SampleDuration_68"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[141]["SampleSize_68"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[142]["SampleDuration_69"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[143]["SampleSize_69"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[144]["SampleDuration_70"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[145]["SampleSize_70"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[146]["SampleDuration_71"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[147]["SampleSize_71"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[148]["SampleDuration_72"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[149]["SampleSize_72"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[150]["SampleDuration_73"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[151]["SampleSize_73"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[152]["SampleDuration_74"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[153]["SampleSize_74"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[154]["SampleDuration_75"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[155]["SampleSize_75"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[156]["SampleDuration_76"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[157]["SampleSize_76"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[158]["SampleDuration_77"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[159]["SampleSize_77"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[160]["SampleDuration_78"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[161]["SampleSize_78"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[162]["SampleDuration_79"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[163]["SampleSize_79"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[164]["SampleDuration_80"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[165]["SampleSize_80"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[166]["SampleDuration_81"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[167]["SampleSize_81"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[168]["SampleDuration_82"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[169]["SampleSize_82"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[170]["SampleDuration_83"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[171]["SampleSize_83"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[172]["SampleDuration_84"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[173]["SampleSize_84"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[174]["SampleDuration_85"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[175]["SampleSize_85"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[176]["SampleDuration_86"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[177]["SampleSize_86"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[178]["SampleDuration_87"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[179]["SampleSize_87"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[180]["SampleDuration_88"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[181]["SampleSize_88"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[182]["SampleDuration_89"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[183]["SampleSize_89"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[184]["SampleDuration_90"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[185]["SampleSize_90"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[186]["SampleDuration_91"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[187]["SampleSize_91"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[188]["SampleDuration_92"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[189]["SampleSize_92"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[190]["SampleDuration_93"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[191]["SampleSize_93"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[192]["SampleDuration_94"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[193]["SampleSize_94"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[194]["SampleDuration_95"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[195]["SampleSize_95"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[196]["SampleDuration_96"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[197]["SampleSize_96"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[198]["SampleDuration_97"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[199]["SampleSize_97"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[200]["SampleDuration_98"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[201]["SampleSize_98"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[202]["SampleDuration_99"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[203]["SampleSize_99"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[204]["SampleDuration_100"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[205]["SampleSize_100"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[206]["SampleDuration_101"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[207]["SampleSize_101"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[208]["SampleDuration_102"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[209]["SampleSize_102"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[210]["SampleDuration_103"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[211]["SampleSize_103"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[212]["SampleDuration_104"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[213]["SampleSize_104"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[214]["SampleDuration_105"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[215]["SampleSize_105"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[216]["SampleDuration_106"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[217]["SampleSize_106"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[218]["SampleDuration_107"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[219]["SampleSize_107"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[220]["SampleDuration_108"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[221]["SampleSize_108"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[222]["SampleDuration_109"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[223]["SampleSize_109"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[224]["SampleDuration_110"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[225]["SampleSize_110"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[226]["SampleDuration_111"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[227]["SampleSize_111"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[228]["SampleDuration_112"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[229]["SampleSize_112"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[230]["SampleDuration_113"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[231]["SampleSize_113"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[232]["SampleDuration_114"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[233]["SampleSize_114"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[234]["SampleDuration_115"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[235]["SampleSize_115"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[236]["SampleDuration_116"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[237]["SampleSize_116"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[238]["SampleDuration_117"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[239]["SampleSize_117"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[240]["SampleDuration_118"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[241]["SampleSize_118"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[242]["SampleDuration_119"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[243]["SampleSize_119"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[244]["SampleDuration_120"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[245]["SampleSize_120"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[246]["SampleDuration_121"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[247]["SampleSize_121"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[248]["SampleDuration_122"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[249]["SampleSize_122"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[250]["SampleDuration_123"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[251]["SampleSize_123"] == 261:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[252]["SampleDuration_124"] == 128:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[253]["SampleSize_124"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[254]["SampleDuration_125"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[255]["SampleSize_125"] == 261:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items = 357
if pass_count == no_of_check_items:
	print("%d item(s) of %d tests is/are passed."%(pass_count, no_of_check_items))
else:
	print("%d item(s) of %d tests is/are passed."%(pass_count, no_of_check_items))
	print("%d item(s) of %d tests is/are failed."%(no_of_check_items-pass_count, no_of_check_items))	    

print("*"*40)
print("* IAMF-OBU Syntax Check")
print("*"*40)

# Check DescriptorOBUs
pass_count = 0
if "MagicCodeOBU_0" in obu_list[0]:
	pass_count += 1
	obu = obu_list[0].get("MagicCodeOBU_0")[0]
	if obu.get("ia_code") == 1767992678:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if obu.get("version") == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if obu.get("profile_version") == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))
if "CodecConfigOBU_1" in obu_list[1]:
	pass_count += 1
	obu = obu_list[1].get("CodecConfigOBU_1")[0]
	if obu.get("codec_config_id") == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if obu.get("codec_config") is not None:
		pass_count += 1
		if obu["codec_config"].get("codec_id") == 1768973165:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if obu["codec_config"].get("num_samples_per_frame") == 128:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if obu["codec_config"].get("roll_distance") == 0:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if obu["codec_config"].get("decoder_config_lpcm") is not None:
			pass_count += 1
			if obu["codec_config"]["decoder_config_lpcm"].get("sample_format_flags") == 1: # LPCM_LITTLE_ENDIAN
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			if obu["codec_config"]["decoder_config_lpcm"].get("sample_size") == 16:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			if obu["codec_config"]["decoder_config_lpcm"].get("sample_rate") == 16000:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))
if "AudioElementOBU_2" in obu_list[2]:
	pass_count += 1
	obu = obu_list[2].get("AudioElementOBU_2")[0]
	if obu.get("audio_element_id") == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if obu.get("audio_element_type") == 0: # AUDIO_ELEMENT_CHANNEL_BASED
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if obu.get("codec_config_id") == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if obu.get("num_substreams") == 2:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if obu.get("audio_substream_ids") is not None:
		pass_count += 1
		audio_substream_ids = obu.get("audio_substream_ids")
		if audio_substream_ids[0] == 0:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if audio_substream_ids[1] == 1:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if obu.get("num_parameters") == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if obu.get("scalable_channel_layout_config") is not None:
		pass_count += 1
		if obu["scalable_channel_layout_config"].get("num_layers") == 1:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if obu["scalable_channel_layout_config"].get("channel_audio_layer_configs") is not None:
			pass_count += 1
			channel_audio_layer_configs = obu["scalable_channel_layout_config"].get("channel_audio_layer_configs")
			if channel_audio_layer_configs[0].get("loudspeaker_layout") == 1:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			if channel_audio_layer_configs[0].get("output_gain_is_present_flag") == 0:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			if channel_audio_layer_configs[0].get("recon_gain_is_present_flag") == 0:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			if channel_audio_layer_configs[0].get("substream_count") == 2:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			if channel_audio_layer_configs[0].get("coupled_substream_count") == 0:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))
if "MixPresentationOBU_3" in obu_list[3]:
	pass_count += 1
	obu = obu_list[3].get("MixPresentationOBU_3")[0]
	if obu.get("mix_presentation_id") == 42:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if obu.get("mix_presentation_annotations") is not None:
		pass_count += 1
		if obu["mix_presentation_annotations"].get("mix_presentation_friendly_label") == "test_mix_pres":
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if obu.get("num_sub_mixes") == 1:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if obu.get("sub_mixes") is not None:
		pass_count += 1
		sub_mixes = obu.get("sub_mixes")
		if sub_mixes[0].get("num_audio_elements") == 1:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if sub_mixes[0].get("audio_elements") is not None:
			pass_count += 1
			audio_elements = sub_mixes[0].get("audio_elements")
			if audio_elements[0].get("audio_element_id") == 0:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			if audio_elements[0].get("mix_presentation_element_annotations") is not None:
				pass_count += 1
				if audio_elements[0]["mix_presentation_element_annotations"].get("audio_element_friendly_label") == "test_sub_mix_0_audio_element_0":
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			if audio_elements[0].get("element_mix_config") is not None:
				pass_count += 1
				if audio_elements[0]["element_mix_config"].get("mix_gain") is not None:
					pass_count += 1
					if audio_elements[0]["element_mix_config"]["mix_gain"].get("param_definition") is not None:
						pass_count += 1
						if audio_elements[0]["element_mix_config"]["mix_gain"]["param_definition"].get("parameter_id") == 0:
							pass_count += 1
						else:
							frame = inspect.currentframe()
							print("failure line is #%d."%(frame.f_lineno))
						if audio_elements[0]["element_mix_config"]["mix_gain"]["param_definition"].get("parameter_rate") == 0:
							pass_count += 1
						else:
							frame = inspect.currentframe()
							print("failure line is #%d."%(frame.f_lineno))
						if audio_elements[0]["element_mix_config"]["mix_gain"]["param_definition"].get("param_definition_mode") == True:
							pass_count += 1
						else:
							frame = inspect.currentframe()
							print("failure line is #%d."%(frame.f_lineno))
					else:
						frame = inspect.currentframe()
						print("failure line is #%d."%(frame.f_lineno))
					if audio_elements[0]["element_mix_config"]["mix_gain"].get("default_mix_gain") == 0:
						pass_count += 1
					else:
						frame = inspect.currentframe()
						print("failure line is #%d."%(frame.f_lineno))
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if sub_mixes[0].get("output_mix_config") is not None:
			pass_count += 1
			if sub_mixes[0]["output_mix_config"].get("output_mix_gain") is not None:
				pass_count += 1
				if sub_mixes[0]["output_mix_config"]["output_mix_gain"].get("param_definition") is not None:
					pass_count += 1
					if sub_mixes[0]["output_mix_config"]["output_mix_gain"]["param_definition"].get("parameter_id") == 0:
						pass_count += 1
					else:
						frame = inspect.currentframe()
						print("failure line is #%d."%(frame.f_lineno))
					if sub_mixes[0]["output_mix_config"]["output_mix_gain"]["param_definition"].get("parameter_rate") == 0:
						pass_count += 1
					else:
						frame = inspect.currentframe()
						print("failure line is #%d."%(frame.f_lineno))
					if sub_mixes[0]["output_mix_config"]["output_mix_gain"]["param_definition"].get("param_definition_mode") == True:
						pass_count += 1
					else:
						frame = inspect.currentframe()
						print("failure line is #%d."%(frame.f_lineno))
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				if sub_mixes[0]["output_mix_config"]["output_mix_gain"].get("default_mix_gain") == 0:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if sub_mixes[0].get("num_layouts") == 1:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if sub_mixes[0].get("layouts") is not None:
			pass_count += 1
			layouts = sub_mixes[0].get("layouts")
			if layouts[0].get("loudness_layout") is not None:
				pass_count += 1
				if layouts[0]["loudness_layout"].get("layout_type") == 2: # LAYOUT_TYPE_LOUDSPEAKERS_SS_CONVENTION
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				if layouts[0]["loudness_layout"].get("ss_layout") is not None:
					pass_count += 1
					if layouts[0]["loudness_layout"]["ss_layout"].get("sound_system") == 0: # SOUND_SYSTEM_A_0_2_0
						pass_count += 1
					else:
						frame = inspect.currentframe()
						print("failure line is #%d."%(frame.f_lineno))
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			if layouts[0].get("loudness") is not None:
				pass_count += 1
				if layouts[0]["loudness"].get("info_type") == 0:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				if layouts[0]["loudness"].get("integrated_loudness") == -13513:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				if layouts[0]["loudness"].get("digital_peak") == -12879:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))
if "SyncOBU_4" in obu_list[4]:
	pass_count += 1
	obu = obu_list[4].get("SyncOBU_4")[0]
	if obu.get("global_offset") == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if obu.get("num_obu_ids") == 2:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if obu.get("sync_array") is not None:
		pass_count += 1
		sync_array = obu.get("sync_array")
		if sync_array[0].get("obu_id") == 0:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if sync_array[0].get("obu_data_type") == 0: # OBU_DATA_TYPE_SUBSTREAM
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if sync_array[0].get("reinitialize_decoder") == False:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if sync_array[0].get("relative_offset") == 192:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if sync_array[1].get("obu_id") == 1:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if sync_array[1].get("obu_data_type") == 0: # OBU_DATA_TYPE_SUBSTREAM
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if sync_array[1].get("reinitialize_decoder") == False:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if sync_array[1].get("relative_offset") == 0:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

# Check Audio Frame and Temporal Delimiter
import re
audio_frame_list = list()
temporal_delimiter_count = 0
substream_ids = list()
total_length = dict()

for obu in obu_list:
	key = next(iter(obu))
	if re.match(r'AudioFrameOBU_\d+',key):
		audio_frame = obu[key][0]
		substream_id = audio_frame.get("audio_substream_id")
		if substream_id not in substream_ids:
			substream_ids.append(substream_id)
			
		if total_length.get(substream_id) is None:
			total_length[substream_id] = 0
		else:
			total_length[substream_id] += audio_frame.get("size_of(audio_frame)")
		audio_frame_list.append(audio_frame)
	elif re.match(r'TemporalDelimiterOBU_\d+',key):
		temporal_delimiter_count += 1
num_samples_to_trim_at_end = audio_frame_list[-1].get("num_samples_to_trim_at_end")
num_samples_to_trim_at_start = audio_frame_list[0].get("num_samples_to_trim_at_start")

if num_samples_to_trim_at_end == 64:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))
if num_samples_to_trim_at_start == 0:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))
	
if substream_ids == [0, 1]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))
	obu = obu_list[0].get("MagicCodeOBU_0")[0]
profile_version = obu.get("profile_version")
if not (profile_version == 0 and temporal_delimiter_count > 0):
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

# AUDIO_ELEMENT_CHANNEL_BASED
audio_element_obu = obu_list[2].get("AudioElementOBU_2")[0]
channel_audio_layer_configs = audio_element_obu["scalable_channel_layout_config"].get("channel_audio_layer_configs")

# loudspekaer_layout_0: Stereo
substream_count_0 = channel_audio_layer_configs[0].get("substream_count")
coupled_substream_count_0 = channel_audio_layer_configs[0].get("coupled_substream_count")
if substream_count_0 == 1:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))
if coupled_substream_count_0 == 1:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items = 84
if pass_count == no_of_check_items:
	print("%d item(s) of %d tests is/are passed."%(pass_count, no_of_check_items))
else:
	print("%d item(s) of %d tests is/are passed."%(pass_count, no_of_check_items))
	print("%d item(s) of %d tests is/are failed."%(no_of_check_items-pass_count, no_of_check_items))
	
print("*"*40)
print("* Decoded Audio Signal Check")
print("*"*40)

pass_count = 0
# Calculate PSNR
def calc_psnr(ref_signal, signal) -> None:
	import numpy as np
	import math
	
	max_value = np.iinfo(ref_signal.dtype).max-np.iinfo(ref_signal.dtype).min
	
	mse = np.mean((ref_signal - signal)**2, axis=0, dtype = 'float64')
	
	num_channels = ref_signal.shape[1]
	for i in range(num_channels):
		if mse[i]==0:
			print(f'ch#{i} PSNR: inf')
		else:
			print(f'ch#{i} PSNR: {10*math.log10(max_value**2/mse[i])} dB')
			
	return
	
# Compare two signals
def bitwise_compare(ref_signal, signal) -> None:
	import numpy as np

	tot_diff = 0
	num_samples = ref_signal.shape[0]
	num_channels = ref_signal.shape[1]
	for i in range(num_channels):
		is_equal = np.equal(ref_signal[:,i],signal[:,i])
		diff = np.where(is_equal==False)
		diff_count = diff[0].size
		
		print(f'ch#{i} Matched: {num_samples-diff_count}/{num_samples}')
		
		if diff_count > 0:
			print(f'Unmatched Index: {diff[0][:100]}')
		tot_diff += diff_count
	return tot_diff, num_samples * num_channels
	
	
if args.psnr is not None:
	import scipy.io.wavfile as wavfile
	ref_file = args.psnr
	cmp_file = args.wav
	
	ref_samplerate, ref_data = wavfile.read(ref_file)	
	cmp_samplerate, cmp_data = wavfile.read(cmp_file)
	
	# Check sampling rate
	assert ref_samplerate == cmp_samplerate, "Sampling rate of reference file and comparison file are different."
	
	# Check number of channels
	assert ref_data.shape[1] == cmp_data.shape[1], "Number of channels of reference file and comparison file are different."
	
	# Check number of samples
	assert ref_data.shape[0] == cmp_data.shape[0], "Number of samples of reference file and comparison file are different."
	
	print("PSNR evaluation:")
	calc_psnr(ref_data, cmp_data)

if args.bitwise is not None:
	import scipy.io.wavfile as wavfile
	ref_file = args.bitwise
	cmp_file = args.wav
	
	ref_samplerate, ref_data = wavfile.read(ref_file)	
	cmp_samplerate, cmp_data = wavfile.read(cmp_file)
	
	# Check sampling rate
	assert ref_samplerate == cmp_samplerate, "Sampling rate of reference file and comparison file are different."
	
	# Check number of channels
	assert ref_data.shape[1] == cmp_data.shape[1], "Number of channels of reference file and comparison file are different."
	
	# Check number of samples
	assert ref_data.shape[0] == cmp_data.shape[0], "Number of samples of reference file and comparison file are different."
	
	print("bitwise comparison:")
	tot_diff, tot_sample = bitwise_compare(ref_data, cmp_data)
	if (tot_diff > 0):
		print("%d point(s) of %d comparisons is/are different."%(tot_diff, tot_sample))
		print("%d point(s) of %d comparisons is/are same."%(tot_sample-tot_diff, tot_sample))		
	else:
		print("%d point(s) of %d comparisons is/are same."%(tot_sample-tot_diff, tot_sample))
	
	
print("*"*40)
print("* log output file: %s"%(args.log))
print("* wav output file: %s"%(args.wav))
if args.psnr is not None or args.bitwise is not None:
	print("* reference wav file: %s"%(ref_file))
print("*"*40)
	