import yaml
import inspect
import argparse

parser = argparse.ArgumentParser(description="test_000009 verification script")
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
	if atom[1]["Flags"] == 131114:
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
	if atom[4]["DefaultSampleDuration"] == 64:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[5]["DefaultSampleFlag"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

if "trun_0000000000000328" in atom_list[18]:
	pass_count += 1
	atom = atom_list[18]["trun_0000000000000328"]
	if atom[0]["Version"] == 1:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[1]["Flags"] == 513:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[2]["SampleCount"] == 125:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	SampleCount = atom[2]["SampleCount"]
	if atom[3]["DataOffset"] == 630:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[4]["SampleSize_0"] == 259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[5]["SampleSize_1"] == 269:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[6]["SampleSize_2"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[7]["SampleSize_3"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[8]["SampleSize_4"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[9]["SampleSize_5"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[10]["SampleSize_6"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[11]["SampleSize_7"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[12]["SampleSize_8"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[13]["SampleSize_9"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[14]["SampleSize_10"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[15]["SampleSize_11"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[16]["SampleSize_12"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[17]["SampleSize_13"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[18]["SampleSize_14"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[19]["SampleSize_15"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[20]["SampleSize_16"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[21]["SampleSize_17"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[22]["SampleSize_18"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[23]["SampleSize_19"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[24]["SampleSize_20"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[25]["SampleSize_21"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[26]["SampleSize_22"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[27]["SampleSize_23"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[28]["SampleSize_24"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[29]["SampleSize_25"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[30]["SampleSize_26"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[31]["SampleSize_27"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[32]["SampleSize_28"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[33]["SampleSize_29"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[34]["SampleSize_30"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[35]["SampleSize_31"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[36]["SampleSize_32"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[37]["SampleSize_33"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[38]["SampleSize_34"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[39]["SampleSize_35"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[40]["SampleSize_36"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[41]["SampleSize_37"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[42]["SampleSize_38"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[43]["SampleSize_39"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[44]["SampleSize_40"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[45]["SampleSize_41"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[46]["SampleSize_42"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[47]["SampleSize_43"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[48]["SampleSize_44"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[49]["SampleSize_45"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[50]["SampleSize_46"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[51]["SampleSize_47"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[52]["SampleSize_48"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[53]["SampleSize_49"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[54]["SampleSize_50"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[55]["SampleSize_51"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[56]["SampleSize_52"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[57]["SampleSize_53"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[58]["SampleSize_54"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[59]["SampleSize_55"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[60]["SampleSize_56"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[61]["SampleSize_57"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[62]["SampleSize_58"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[63]["SampleSize_59"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[64]["SampleSize_60"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[65]["SampleSize_61"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[66]["SampleSize_62"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[67]["SampleSize_63"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[68]["SampleSize_64"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[69]["SampleSize_65"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[70]["SampleSize_66"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[71]["SampleSize_67"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[72]["SampleSize_68"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[73]["SampleSize_69"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[74]["SampleSize_70"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[75]["SampleSize_71"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[76]["SampleSize_72"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[77]["SampleSize_73"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[78]["SampleSize_74"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[79]["SampleSize_75"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[80]["SampleSize_76"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[81]["SampleSize_77"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[82]["SampleSize_78"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[83]["SampleSize_79"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[84]["SampleSize_80"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[85]["SampleSize_81"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[86]["SampleSize_82"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[87]["SampleSize_83"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[88]["SampleSize_84"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[89]["SampleSize_85"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[90]["SampleSize_86"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[91]["SampleSize_87"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[92]["SampleSize_88"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[93]["SampleSize_89"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[94]["SampleSize_90"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[95]["SampleSize_91"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[96]["SampleSize_92"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[97]["SampleSize_93"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[98]["SampleSize_94"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[99]["SampleSize_95"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[100]["SampleSize_96"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[101]["SampleSize_97"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[102]["SampleSize_98"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[103]["SampleSize_99"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[104]["SampleSize_100"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[105]["SampleSize_101"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[106]["SampleSize_102"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[107]["SampleSize_103"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[108]["SampleSize_104"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[109]["SampleSize_105"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[110]["SampleSize_106"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[111]["SampleSize_107"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[112]["SampleSize_108"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[113]["SampleSize_109"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[114]["SampleSize_110"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[115]["SampleSize_111"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[116]["SampleSize_112"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[117]["SampleSize_113"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[118]["SampleSize_114"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[119]["SampleSize_115"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[120]["SampleSize_116"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[121]["SampleSize_117"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[122]["SampleSize_118"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[123]["SampleSize_119"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[124]["SampleSize_120"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[125]["SampleSize_121"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[126]["SampleSize_122"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[127]["SampleSize_123"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[128]["SampleSize_124"] == 268:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items = 231
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
	if obu.get("codec_config_id") == 200:
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
		if obu["codec_config"].get("num_samples_per_frame") == 64:
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
	if obu.get("audio_element_id") == 300:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if obu.get("audio_element_type") == 0: # AUDIO_ELEMENT_CHANNEL_BASED
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if obu.get("codec_config_id") == 200:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if obu.get("num_substreams") == 1:
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
			if channel_audio_layer_configs[0].get("substream_count") == 1:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			if channel_audio_layer_configs[0].get("coupled_substream_count") == 1:
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
			if audio_elements[0].get("audio_element_id") == 300:
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
						if audio_elements[0]["element_mix_config"]["mix_gain"]["param_definition"].get("parameter_id") == 100:
							pass_count += 1
						else:
							frame = inspect.currentframe()
							print("failure line is #%d."%(frame.f_lineno))
						if audio_elements[0]["element_mix_config"]["mix_gain"]["param_definition"].get("parameter_rate") == 16000:
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
					if sub_mixes[0]["output_mix_config"]["output_mix_gain"]["param_definition"].get("parameter_id") == 100:
						pass_count += 1
					else:
						frame = inspect.currentframe()
						print("failure line is #%d."%(frame.f_lineno))
					if sub_mixes[0]["output_mix_config"]["output_mix_gain"]["param_definition"].get("parameter_rate") == 16000:
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
		if sync_array[0].get("relative_offset") == 0:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if sync_array[1].get("obu_id") == 100:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if sync_array[1].get("obu_data_type") == 1: # OBU_DATA_TYPE_PARAMETER
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if sync_array[1].get("reinitialize_decoder") == False:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if sync_array[1].get("relative_offset") == 100:
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

if num_samples_to_trim_at_end == 0:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))
if num_samples_to_trim_at_start == 0:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))
	
if substream_ids == [0]:
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

no_of_check_items = 83
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
	