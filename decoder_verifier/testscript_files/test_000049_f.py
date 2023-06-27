import yaml
import inspect
import argparse

parser = argparse.ArgumentParser(description="/home/yongmin/Desktop/ymk/IAMF_RefSW/tools/script_merge/mp4_test_script/ verification script")
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

elst_MediaTime = 0
pass_count = 0
no_of_check_items = 0

no_of_check_items += 1
if "ftyp_0000000000000000" in atom_list[0]:
	pass_count += 1
	atom = atom_list[0]["ftyp_0000000000000000"]
	no_of_check_items += 1
	if atom[0]["MajorBrands"] == "dash":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1]["Version"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2]["CompatibleBrands"] == "iso6iamf":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "moov_0000000000000018" in atom_list[1]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "mvhd_0000000000000020" in atom_list[2]:
	pass_count += 1
	atom = atom_list[2]["mvhd_0000000000000020"]
	no_of_check_items += 1
	if atom[0]["Version"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1]["Flags"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2]["CreationTime"] == "2023-05-12 00:00:00 UTC":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3]["ModificationTime"] == "2023-05-12 00:00:00 UTC":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[4]["TimeScale"] == 48000:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[5]["Duration"] == 644971:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[6]["PreferedRate"] == 65536:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[7]["PreferedVolume"] == 256:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[8]["Reserved1"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[9]["Reserved2"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[10]["Reserved3"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[11]["MatrixStructure"] == "0x00010000 0x00000000 0x00000000 0x00000000 0x00010000 0x00000000 0x00000000 0x00000000 0x40000000":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[12]["PreviewTime"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[13]["PreviewDuration"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[14]["PosterTime"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[15]["SelectionTime"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "trak_00000000000000b4" in atom_list[3]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "tkhd_00000000000000bc" in atom_list[4]:
	pass_count += 1
	atom = atom_list[4]["tkhd_00000000000000bc"]
	no_of_check_items += 1
	if atom[0]["Version"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1]["Flags"] == 3:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2]["CreationTime"] == "2023-05-12 00:00:00 UTC":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3]["ModificationTime"] == "2023-05-12 00:00:00 UTC":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[4]["TrackID"] == 1:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[5]["Reserved1"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[6]["Duration"] == 644971:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[7]["Reserved2"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[8]["Reserved3"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[9]["Layer"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[10]["AlternativeGroup"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[11]["Volume"] == 256:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[12]["Reserved4"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[13]["MatrixStructure"] == "0x00010000 0x00000000 0x00000000 0x00000000 0x00010000 0x00000000 0x00000000 0x00000000 0x40000000":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[14]["TrackWidth"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[15]["TrackHeight"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "edts_0000000000000118" in atom_list[5]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "elst_0000000000000120" in atom_list[6]:
	pass_count += 1
	atom = atom_list[6]["elst_0000000000000120"]
	no_of_check_items += 1
	if atom[0]["Version"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1]["Flags"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	elst_EntryCount = atom[2]["EntryCount"]
	no_of_check_items += 1
	if atom[2]["EntryCount"] == 1:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3]["SegmentDuration_0"] == 644971:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[4]["MediaTime_0"] == 312:
		pass_count += 1
		elst_MediaTime = atom[4]["MediaTime_0"]
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[5]["MediaRateInteger_0"] == 1:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[6]["MediaRateFraction_0"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "mdhd_0000000000000144" in atom_list[7]:
	pass_count += 1
	atom = atom_list[7]["mdhd_0000000000000144"]
	no_of_check_items += 1
	if atom[0]["Version"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1]["Flags"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2]["CreationTime"] == "2023-05-12 00:00:00 UTC":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3]["ModificationTime"] == "2023-05-12 00:00:00 UTC":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
		mdhd_TimeScale = atom[4]["TimeScale"]
	no_of_check_items += 1
	if atom[4]["TimeScale"] == 48000:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	mdhd_Duration = atom[5]["Duration"]
	no_of_check_items += 1
	if atom[5]["Duration"] == 644971:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[6]["Language"] == 21956:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[7]["Quality"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "hdlr_0000000000000164" in atom_list[8]:
	pass_count += 1
	atom = atom_list[8]["hdlr_0000000000000164"]
	no_of_check_items += 1
	if atom[0]["Version"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1]["Flags"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2]["PreDefined"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3]["ComponentSubtype"] == 1936684398:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[4]["Reserved1"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[5]["Reserved2"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[6]["Reserved3"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[7]["Name"] == "ISO Media file produced by Google Inc. Created on: 05/11/2023.":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "stbl_00000000000001ef" in atom_list[9]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "stsd_00000000000001f7" in atom_list[10]:
	pass_count += 1
	atom = atom_list[10]["stsd_00000000000001f7"]
	no_of_check_items += 1
	if atom[0]["Version"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1]["Flags"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2]["EntryCount"] == 1:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "iamf_0000000000000207" in atom_list[11]:
	pass_count += 1
	atom = atom_list[11]["iamf_0000000000000207"]
	no_of_check_items += 1
	if atom[0]["Reserved1"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1]["Reserved2"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2]["DataReferenceIndex"] == 1:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3]["Reserved3"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[4]["Reserved4"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	iamf_ChannelCount = atom[5]["ChannelCount"]
	no_of_check_items += 1
	if atom[5]["ChannelCount"] == 6:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	iamf_SampleSize = atom[6]["SampleSize"]
	no_of_check_items += 1
	if atom[6]["SampleSize"] == 16:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[7]["Predefined"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[8]["Reserved5"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[9]["SampleRate"] == 48000:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "iamd_000000000000022b" in atom_list[12]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "stts_00000000000002d6" in atom_list[13]:
	pass_count += 1
	atom = atom_list[13]["stts_00000000000002d6"]
	no_of_check_items += 1
	if atom[0]["Version"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1]["Flags"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	stts_EntryCount = atom[2]["EntryCount"]
	no_of_check_items += 1
	if atom[2]["EntryCount"] == 0:
		pass_count += 1
		stts_SampleCountSum = 0
		stts_SampleDeltaSum = 0
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "stsc_00000000000002e6" in atom_list[14]:
	pass_count += 1
	atom = atom_list[14]["stsc_00000000000002e6"]
	no_of_check_items += 1
	if atom[0]["Version"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1]["Flags"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2]["EntryCount"] == 0:
		pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "stco_00000000000002f6" in atom_list[15]:
	pass_count += 1
	atom = atom_list[15]["stco_00000000000002f6"]
	no_of_check_items += 1
	if atom[0]["Version"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1]["Flags"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2]["EntryCount"] == 0:
		pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "stsz_0000000000000306" in atom_list[16]:
	pass_count += 1
	atom = atom_list[16]["stsz_0000000000000306"]
	no_of_check_items += 1
	if atom[0]["Version"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1]["Flags"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2]["SampleSize"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3]["SampleCount"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "moof_0000000000000362" in atom_list[17]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "traf_000000000000037a" in atom_list[18]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "tfhd_0000000000000382" in atom_list[19]:
	pass_count += 1
	atom = atom_list[19]["tfhd_0000000000000382"]
	no_of_check_items += 1
	if atom[0]["Version"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1]["Flags"] == 131114:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2]["TrackID"] == 1:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3]["SampleDescriptionIndex"] == 1:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[4]["DefaultSampleDuration"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[5]["DefaultSampleFlag"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "trun_00000000000003ae" in atom_list[20]:
	pass_count += 1
	atom = atom_list[20]["trun_00000000000003ae"]
	no_of_check_items += 1
	if atom[0]["Version"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1]["Flags"] == 513:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2]["SampleCount"] == 166:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	SampleCount = atom[2]["SampleCount"]
	no_of_check_items += 1
	if atom[3]["DataOffset"] == 794:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[4]["SampleSize_0"] == 1491:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[5]["SampleSize_1"] == 1471:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[6]["SampleSize_2"] == 1471:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[7]["SampleSize_3"] == 1471:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[8]["SampleSize_4"] == 1471:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[9]["SampleSize_5"] == 1471:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[10]["SampleSize_6"] == 808:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[11]["SampleSize_7"] == 687:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[12]["SampleSize_8"] == 783:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[13]["SampleSize_9"] == 890:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[14]["SampleSize_10"] == 951:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[15]["SampleSize_11"] == 1017:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[16]["SampleSize_12"] == 1120:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[17]["SampleSize_13"] == 1150:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[18]["SampleSize_14"] == 1207:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[19]["SampleSize_15"] == 1241:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[20]["SampleSize_16"] == 1256:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[21]["SampleSize_17"] == 1301:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[22]["SampleSize_18"] == 1298:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[23]["SampleSize_19"] == 1309:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[24]["SampleSize_20"] == 1348:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[25]["SampleSize_21"] == 1392:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[26]["SampleSize_22"] == 1293:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[27]["SampleSize_23"] == 1281:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[28]["SampleSize_24"] == 1291:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[29]["SampleSize_25"] == 1318:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[30]["SampleSize_26"] == 1310:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[31]["SampleSize_27"] == 1300:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[32]["SampleSize_28"] == 1307:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[33]["SampleSize_29"] == 1306:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[34]["SampleSize_30"] == 1300:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[35]["SampleSize_31"] == 1307:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[36]["SampleSize_32"] == 1301:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[37]["SampleSize_33"] == 1300:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[38]["SampleSize_34"] == 1305:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[39]["SampleSize_35"] == 1302:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[40]["SampleSize_36"] == 1310:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[41]["SampleSize_37"] == 1299:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[42]["SampleSize_38"] == 1308:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[43]["SampleSize_39"] == 1303:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[44]["SampleSize_40"] == 1326:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[45]["SampleSize_41"] == 1327:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[46]["SampleSize_42"] == 1316:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[47]["SampleSize_43"] == 1326:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[48]["SampleSize_44"] == 1319:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[49]["SampleSize_45"] == 1323:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[50]["SampleSize_46"] == 1305:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[51]["SampleSize_47"] == 1314:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[52]["SampleSize_48"] == 1317:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[53]["SampleSize_49"] == 1314:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[54]["SampleSize_50"] == 1307:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[55]["SampleSize_51"] == 1314:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[56]["SampleSize_52"] == 1302:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[57]["SampleSize_53"] == 1317:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[58]["SampleSize_54"] == 1320:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[59]["SampleSize_55"] == 1316:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[60]["SampleSize_56"] == 1324:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[61]["SampleSize_57"] == 1324:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[62]["SampleSize_58"] == 1313:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[63]["SampleSize_59"] == 1319:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[64]["SampleSize_60"] == 1318:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[65]["SampleSize_61"] == 1312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[66]["SampleSize_62"] == 1309:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[67]["SampleSize_63"] == 1306:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[68]["SampleSize_64"] == 1316:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[69]["SampleSize_65"] == 1352:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[70]["SampleSize_66"] == 1347:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[71]["SampleSize_67"] == 1355:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[72]["SampleSize_68"] == 1317:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[73]["SampleSize_69"] == 1346:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[74]["SampleSize_70"] == 1327:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[75]["SampleSize_71"] == 1341:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[76]["SampleSize_72"] == 1315:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[77]["SampleSize_73"] == 1317:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[78]["SampleSize_74"] == 1453:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[79]["SampleSize_75"] == 1365:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[80]["SampleSize_76"] == 1344:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[81]["SampleSize_77"] == 1312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[82]["SampleSize_78"] == 1301:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[83]["SampleSize_79"] == 1334:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[84]["SampleSize_80"] == 1318:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[85]["SampleSize_81"] == 1314:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[86]["SampleSize_82"] == 1339:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[87]["SampleSize_83"] == 1286:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[88]["SampleSize_84"] == 1282:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[89]["SampleSize_85"] == 1308:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[90]["SampleSize_86"] == 1286:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[91]["SampleSize_87"] == 1304:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[92]["SampleSize_88"] == 1303:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[93]["SampleSize_89"] == 1279:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[94]["SampleSize_90"] == 1334:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[95]["SampleSize_91"] == 1322:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[96]["SampleSize_92"] == 1315:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[97]["SampleSize_93"] == 1338:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[98]["SampleSize_94"] == 1347:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[99]["SampleSize_95"] == 1388:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[100]["SampleSize_96"] == 1334:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[101]["SampleSize_97"] == 1318:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[102]["SampleSize_98"] == 1310:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[103]["SampleSize_99"] == 1313:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[104]["SampleSize_100"] == 1324:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[105]["SampleSize_101"] == 1322:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[106]["SampleSize_102"] == 1326:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[107]["SampleSize_103"] == 1311:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[108]["SampleSize_104"] == 1290:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[109]["SampleSize_105"] == 1335:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[110]["SampleSize_106"] == 1326:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[111]["SampleSize_107"] == 1327:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[112]["SampleSize_108"] == 1323:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[113]["SampleSize_109"] == 1333:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[114]["SampleSize_110"] == 1299:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[115]["SampleSize_111"] == 1295:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[116]["SampleSize_112"] == 1301:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[117]["SampleSize_113"] == 1317:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[118]["SampleSize_114"] == 1282:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[119]["SampleSize_115"] == 1292:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[120]["SampleSize_116"] == 1285:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[121]["SampleSize_117"] == 1296:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[122]["SampleSize_118"] == 1327:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[123]["SampleSize_119"] == 1317:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[124]["SampleSize_120"] == 1314:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[125]["SampleSize_121"] == 1329:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[126]["SampleSize_122"] == 1310:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[127]["SampleSize_123"] == 1319:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[128]["SampleSize_124"] == 1328:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[129]["SampleSize_125"] == 1313:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[130]["SampleSize_126"] == 1331:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[131]["SampleSize_127"] == 1300:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[132]["SampleSize_128"] == 1302:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[133]["SampleSize_129"] == 1318:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[134]["SampleSize_130"] == 1324:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[135]["SampleSize_131"] == 1321:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[136]["SampleSize_132"] == 1337:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[137]["SampleSize_133"] == 1433:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[138]["SampleSize_134"] == 1337:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[139]["SampleSize_135"] == 1312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[140]["SampleSize_136"] == 1307:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[141]["SampleSize_137"] == 1368:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[142]["SampleSize_138"] == 1323:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[143]["SampleSize_139"] == 1316:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[144]["SampleSize_140"] == 1306:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[145]["SampleSize_141"] == 1289:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[146]["SampleSize_142"] == 1305:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[147]["SampleSize_143"] == 1272:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[148]["SampleSize_144"] == 1264:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[149]["SampleSize_145"] == 1257:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[150]["SampleSize_146"] == 1281:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[151]["SampleSize_147"] == 1290:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[152]["SampleSize_148"] == 1310:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[153]["SampleSize_149"] == 1301:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[154]["SampleSize_150"] == 1298:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[155]["SampleSize_151"] == 1297:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[156]["SampleSize_152"] == 1306:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[157]["SampleSize_153"] == 1314:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[158]["SampleSize_154"] == 1324:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[159]["SampleSize_155"] == 1325:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[160]["SampleSize_156"] == 1286:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[161]["SampleSize_157"] == 1425:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[162]["SampleSize_158"] == 1264:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[163]["SampleSize_159"] == 1279:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[164]["SampleSize_160"] == 1294:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[165]["SampleSize_161"] == 1308:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[166]["SampleSize_162"] == 1307:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[167]["SampleSize_163"] == 1330:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[168]["SampleSize_164"] == 1306:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[169]["SampleSize_165"] == 1322:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "moof_0000000000035267" in atom_list[21]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "traf_000000000003527f" in atom_list[22]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "tfhd_0000000000035287" in atom_list[23]:
	pass_count += 1
	atom = atom_list[23]["tfhd_0000000000035287"]
	no_of_check_items += 1
	if atom[0]["Version"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1]["Flags"] == 131106:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2]["TrackID"] == 1:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3]["SampleDescriptionIndex"] == 1:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[4]["DefaultSampleFlag"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "trun_00000000000352af" in atom_list[24]:
	pass_count += 1
	atom = atom_list[24]["trun_00000000000352af"]
	no_of_check_items += 1
	if atom[0]["Version"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1]["Flags"] == 769:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2]["SampleCount"] == 59:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	SampleCount = atom[2]["SampleCount"]
	no_of_check_items += 1
	if atom[3]["DataOffset"] == 598:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[4]["SampleDuration_0"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[5]["SampleSize_0"] == 1322:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[6]["SampleDuration_1"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[7]["SampleSize_1"] == 1290:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[8]["SampleDuration_2"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[9]["SampleSize_2"] == 1297:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[10]["SampleDuration_3"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[11]["SampleSize_3"] == 1331:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[12]["SampleDuration_4"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[13]["SampleSize_4"] == 1280:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[14]["SampleDuration_5"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[15]["SampleSize_5"] == 1299:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[16]["SampleDuration_6"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[17]["SampleSize_6"] == 1310:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[18]["SampleDuration_7"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[19]["SampleSize_7"] == 1314:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[20]["SampleDuration_8"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[21]["SampleSize_8"] == 1301:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[22]["SampleDuration_9"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[23]["SampleSize_9"] == 1303:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[24]["SampleDuration_10"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[25]["SampleSize_10"] == 1322:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[26]["SampleDuration_11"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[27]["SampleSize_11"] == 1399:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[28]["SampleDuration_12"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[29]["SampleSize_12"] == 1383:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[30]["SampleDuration_13"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[31]["SampleSize_13"] == 1310:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[32]["SampleDuration_14"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[33]["SampleSize_14"] == 1352:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[34]["SampleDuration_15"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[35]["SampleSize_15"] == 1359:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[36]["SampleDuration_16"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[37]["SampleSize_16"] == 1363:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[38]["SampleDuration_17"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[39]["SampleSize_17"] == 1275:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[40]["SampleDuration_18"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[41]["SampleSize_18"] == 1302:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[42]["SampleDuration_19"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[43]["SampleSize_19"] == 1269:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[44]["SampleDuration_20"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[45]["SampleSize_20"] == 1280:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[46]["SampleDuration_21"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[47]["SampleSize_21"] == 1343:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[48]["SampleDuration_22"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[49]["SampleSize_22"] == 1300:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[50]["SampleDuration_23"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[51]["SampleSize_23"] == 1319:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[52]["SampleDuration_24"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[53]["SampleSize_24"] == 1309:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[54]["SampleDuration_25"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[55]["SampleSize_25"] == 1300:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[56]["SampleDuration_26"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[57]["SampleSize_26"] == 1341:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[58]["SampleDuration_27"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[59]["SampleSize_27"] == 1313:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[60]["SampleDuration_28"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[61]["SampleSize_28"] == 1318:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[62]["SampleDuration_29"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[63]["SampleSize_29"] == 1306:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[64]["SampleDuration_30"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[65]["SampleSize_30"] == 1313:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[66]["SampleDuration_31"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[67]["SampleSize_31"] == 1318:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[68]["SampleDuration_32"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[69]["SampleSize_32"] == 1300:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[70]["SampleDuration_33"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[71]["SampleSize_33"] == 1310:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[72]["SampleDuration_34"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[73]["SampleSize_34"] == 1334:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[74]["SampleDuration_35"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[75]["SampleSize_35"] == 1307:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[76]["SampleDuration_36"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[77]["SampleSize_36"] == 1342:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[78]["SampleDuration_37"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[79]["SampleSize_37"] == 1322:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[80]["SampleDuration_38"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[81]["SampleSize_38"] == 1308:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[82]["SampleDuration_39"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[83]["SampleSize_39"] == 1288:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[84]["SampleDuration_40"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[85]["SampleSize_40"] == 1278:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[86]["SampleDuration_41"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[87]["SampleSize_41"] == 1315:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[88]["SampleDuration_42"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[89]["SampleSize_42"] == 1326:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[90]["SampleDuration_43"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[91]["SampleSize_43"] == 1326:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[92]["SampleDuration_44"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[93]["SampleSize_44"] == 1237:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[94]["SampleDuration_45"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[95]["SampleSize_45"] == 1252:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[96]["SampleDuration_46"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[97]["SampleSize_46"] == 1305:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[98]["SampleDuration_47"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[99]["SampleSize_47"] == 1259:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[100]["SampleDuration_48"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[101]["SampleSize_48"] == 1335:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[102]["SampleDuration_49"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[103]["SampleSize_49"] == 1245:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[104]["SampleDuration_50"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[105]["SampleSize_50"] == 1299:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[106]["SampleDuration_51"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[107]["SampleSize_51"] == 1307:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[108]["SampleDuration_52"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[109]["SampleSize_52"] == 1254:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[110]["SampleDuration_53"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[111]["SampleSize_53"] == 1291:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[112]["SampleDuration_54"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[113]["SampleSize_54"] == 1285:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[114]["SampleDuration_55"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[115]["SampleSize_55"] == 1287:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[116]["SampleDuration_56"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[117]["SampleSize_56"] == 1283:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[118]["SampleDuration_57"] == 2880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[119]["SampleSize_57"] == 1288:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[120]["SampleDuration_58"] == 163:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[121]["SampleSize_58"] == 719:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

if pass_count == no_of_check_items:
	print("%d item(s) of %d tests is/are passed."%(pass_count, no_of_check_items))
else:
	print("%d item(s) of %d tests is/are passed."%(pass_count, no_of_check_items))
	print("%d item(s) of %d tests is/are failed."%(no_of_check_items-pass_count, no_of_check_items))

print("*"*40)
print("* IAMF-OBU Syntax Check")
print("*"*40)

# Check DescriptorOBUs
no_of_check_items = 0
pass_count = 0
no_of_check_items += 1
if "IaSequenceHeaderOBU_0" in obu_list[0]:
	pass_count += 1
	obu = obu_list[0].get("IaSequenceHeaderOBU_0")[0]
	no_of_check_items += 1
	if obu.get("ia_code") == 1767992678:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if obu.get("profile_name") == 0: # PROFILE_VERSION_SIMPLE
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if obu.get("profile_compatible") == 0: # PROFILE_VERSION_SIMPLE
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))
no_of_check_items += 1
if "CodecConfigOBU_1" in obu_list[1]:
	pass_count += 1
	obu = obu_list[1].get("CodecConfigOBU_1")[0]
	no_of_check_items += 1
	if obu.get("codec_config_id") == 200:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if obu.get("codec_config") is not None:
		pass_count += 1
		no_of_check_items += 1
		if obu["codec_config"].get("codec_id") == 1332770163:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if obu["codec_config"].get("num_samples_per_frame") == 2880:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if obu["codec_config"].get("decoder_config_opus") is not None:
			pass_count += 1
			no_of_check_items += 1
			if obu["codec_config"]["decoder_config_opus"].get("version") == 1:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if obu["codec_config"]["decoder_config_opus"].get("output_channel_count") == 2:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if obu["codec_config"]["decoder_config_opus"].get("pre_skip") == 312:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if obu["codec_config"]["decoder_config_opus"].get("input_sample_rate") == 48000:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if obu["codec_config"]["decoder_config_opus"].get("output_gain") == 0:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if obu["codec_config"]["decoder_config_opus"].get("mapping_family") == 0:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if obu["codec_config"].get("audio_roll_distance") == -2:
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
no_of_check_items += 1
if "AudioElementOBU_2" in obu_list[2]:
	pass_count += 1
	obu = obu_list[2].get("AudioElementOBU_2")[0]
	no_of_check_items += 1
	if obu.get("audio_element_id") == 300:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if obu.get("audio_element_type") == 0: # AUDIO_ELEMENT_CHANNEL_BASED
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if obu.get("codec_config_id") == 200:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if obu.get("num_substreams") == 4:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if obu.get("audio_substream_ids") is not None:
		pass_count += 1
		audio_substream_ids = obu.get("audio_substream_ids")
		no_of_check_items += 1
		if audio_substream_ids[0] == 0:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if audio_substream_ids[1] == 1:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if audio_substream_ids[2] == 2:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if audio_substream_ids[3] == 3:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if obu.get("num_parameters") == 2:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if obu.get("audio_element_params") is not None:
		pass_count += 1
		audio_element_params = obu.get("audio_element_params")
		no_of_check_items += 1
		if audio_element_params[0].get("param_definition_type") == 1:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if audio_element_params[0].get("demixing_param") is not None:
			pass_count += 1
			no_of_check_items += 1
			if audio_element_params[0]["demixing_param"].get("param_definition") is not None:
				pass_count += 1
				no_of_check_items += 1
				if audio_element_params[0]["demixing_param"]["param_definition"].get("parameter_id") == 998:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if audio_element_params[0]["demixing_param"]["param_definition"].get("parameter_rate") == 48000:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if audio_element_params[0]["demixing_param"]["param_definition"].get("param_definition_mode") == False:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if audio_element_params[0]["demixing_param"]["param_definition"].get("duration") == 2880:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if audio_element_params[0]["demixing_param"]["param_definition"].get("num_subblocks") == 1:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if audio_element_params[0]["demixing_param"]["param_definition"].get("constant_subblock_duration") == 2880:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if audio_element_params[0]["demixing_param"].get("default_demixing_info_parameter_data") is not None:
				pass_count += 1
				no_of_check_items += 1
				if audio_element_params[0]["demixing_param"]["default_demixing_info_parameter_data"].get("dmixp_mode") == 1: # DMIXP_MODE_2
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if audio_element_params[0]["demixing_param"].get("default_w") == 0:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if audio_element_params[1].get("param_definition_type") == 2:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if audio_element_params[1].get("recon_gain_param") is not None:
			pass_count += 1
			no_of_check_items += 1
			if audio_element_params[1]["recon_gain_param"].get("param_definition") is not None:
				pass_count += 1
				no_of_check_items += 1
				if audio_element_params[1]["recon_gain_param"]["param_definition"].get("parameter_id") == 999:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if audio_element_params[1]["recon_gain_param"]["param_definition"].get("parameter_rate") == 48000:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if audio_element_params[1]["recon_gain_param"]["param_definition"].get("param_definition_mode") == False:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if audio_element_params[1]["recon_gain_param"]["param_definition"].get("duration") == 2880:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if audio_element_params[1]["recon_gain_param"]["param_definition"].get("num_subblocks") == 1:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if audio_element_params[1]["recon_gain_param"]["param_definition"].get("constant_subblock_duration") == 2880:
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
	no_of_check_items += 1
	if obu.get("scalable_channel_layout_config") is not None:
		pass_count += 1
		no_of_check_items += 1
		if obu["scalable_channel_layout_config"].get("num_layers") == 2:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if obu["scalable_channel_layout_config"].get("channel_audio_layer_configs") is not None:
			pass_count += 1
			channel_audio_layer_configs = obu["scalable_channel_layout_config"].get("channel_audio_layer_configs")
			no_of_check_items += 1
			if channel_audio_layer_configs[0].get("loudspeaker_layout") == 1:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if channel_audio_layer_configs[0].get("output_gain_is_present_flag") == 0:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if channel_audio_layer_configs[0].get("recon_gain_is_present_flag") == 0:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if channel_audio_layer_configs[0].get("substream_count") == 1:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if channel_audio_layer_configs[0].get("coupled_substream_count") == 1:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if channel_audio_layer_configs[1].get("loudspeaker_layout") == 2:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if channel_audio_layer_configs[1].get("output_gain_is_present_flag") == 0:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if channel_audio_layer_configs[1].get("recon_gain_is_present_flag") == 1:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if channel_audio_layer_configs[1].get("substream_count") == 3:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if channel_audio_layer_configs[1].get("coupled_substream_count") == 1:
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
no_of_check_items += 1
if "MixPresentationOBU_3" in obu_list[3]:
	pass_count += 1
	obu = obu_list[3].get("MixPresentationOBU_3")[0]
	no_of_check_items += 1
	if obu.get("mix_presentation_id") == 42:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if obu.get("num_sub_mixes") == 1:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if obu.get("sub_mixes") is not None:
		pass_count += 1
		sub_mixes = obu.get("sub_mixes")
		no_of_check_items += 1
		if sub_mixes[0].get("num_audio_elements") == 1:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sub_mixes[0].get("audio_elements") is not None:
			pass_count += 1
			audio_elements = sub_mixes[0].get("audio_elements")
			no_of_check_items += 1
			if audio_elements[0].get("audio_element_id") == 300:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if audio_elements[0].get("mix_presentation_element_annotations") is not None:
				pass_count += 1
				no_of_check_items += 1
				if audio_elements[0]["mix_presentation_element_annotations"].get("audio_element_friendly_label") == "test_sub_mix_0_audio_element_0":
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if audio_elements[0].get("element_mix_config") is not None:
				pass_count += 1
				no_of_check_items += 1
				if audio_elements[0]["element_mix_config"].get("mix_gain") is not None:
					pass_count += 1
					no_of_check_items += 1
					if audio_elements[0]["element_mix_config"]["mix_gain"].get("param_definition") is not None:
						pass_count += 1
						no_of_check_items += 1
						if audio_elements[0]["element_mix_config"]["mix_gain"]["param_definition"].get("parameter_id") == 100:
							pass_count += 1
						else:
							frame = inspect.currentframe()
							print("failure line is #%d."%(frame.f_lineno))
						no_of_check_items += 1
						if audio_elements[0]["element_mix_config"]["mix_gain"]["param_definition"].get("parameter_rate") == 48000:
							pass_count += 1
						else:
							frame = inspect.currentframe()
							print("failure line is #%d."%(frame.f_lineno))
						no_of_check_items += 1
						if audio_elements[0]["element_mix_config"]["mix_gain"]["param_definition"].get("param_definition_mode") == True:
							pass_count += 1
						else:
							frame = inspect.currentframe()
							print("failure line is #%d."%(frame.f_lineno))
					else:
						frame = inspect.currentframe()
						print("failure line is #%d."%(frame.f_lineno))
					no_of_check_items += 1
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
		no_of_check_items += 1
		if sub_mixes[0].get("output_mix_config") is not None:
			pass_count += 1
			no_of_check_items += 1
			if sub_mixes[0]["output_mix_config"].get("output_mix_gain") is not None:
				pass_count += 1
				no_of_check_items += 1
				if sub_mixes[0]["output_mix_config"]["output_mix_gain"].get("param_definition") is not None:
					pass_count += 1
					no_of_check_items += 1
					if sub_mixes[0]["output_mix_config"]["output_mix_gain"]["param_definition"].get("parameter_id") == 100:
						pass_count += 1
					else:
						frame = inspect.currentframe()
						print("failure line is #%d."%(frame.f_lineno))
					no_of_check_items += 1
					if sub_mixes[0]["output_mix_config"]["output_mix_gain"]["param_definition"].get("parameter_rate") == 48000:
						pass_count += 1
					else:
						frame = inspect.currentframe()
						print("failure line is #%d."%(frame.f_lineno))
					no_of_check_items += 1
					if sub_mixes[0]["output_mix_config"]["output_mix_gain"]["param_definition"].get("param_definition_mode") == True:
						pass_count += 1
					else:
						frame = inspect.currentframe()
						print("failure line is #%d."%(frame.f_lineno))
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
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
		no_of_check_items += 1
		if sub_mixes[0].get("num_layouts") == 2:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sub_mixes[0].get("layouts") is not None:
			pass_count += 1
			layouts = sub_mixes[0].get("layouts")
			no_of_check_items += 1
			if layouts[0].get("loudness_layout") is not None:
				pass_count += 1
				no_of_check_items += 1
				if layouts[0]["loudness_layout"].get("layout_type") == 2: # LAYOUT_TYPE_LOUDSPEAKERS_SS_CONVENTION
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if layouts[0]["loudness_layout"].get("ss_layout") is not None:
					pass_count += 1
					no_of_check_items += 1
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
			no_of_check_items += 1
			if layouts[0].get("loudness") is not None:
				pass_count += 1
				no_of_check_items += 1
				if layouts[0]["loudness"].get("info_type") == 0:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if layouts[0]["loudness"].get("integrated_loudness") == -6195:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if layouts[0]["loudness"].get("digital_peak") == -2865:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if layouts[1].get("loudness_layout") is not None:
				pass_count += 1
				no_of_check_items += 1
				if layouts[1]["loudness_layout"].get("layout_type") == 2: # LAYOUT_TYPE_LOUDSPEAKERS_SS_CONVENTION
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if layouts[1]["loudness_layout"].get("ss_layout") is not None:
					pass_count += 1
					no_of_check_items += 1
					if layouts[1]["loudness_layout"]["ss_layout"].get("sound_system") == 1: # SOUND_SYSTEM_B_0_5_0
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
			no_of_check_items += 1
			if layouts[1].get("loudness") is not None:
				pass_count += 1
				no_of_check_items += 1
				if layouts[1]["loudness"].get("info_type") == 0:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if layouts[1]["loudness"].get("integrated_loudness") == -6134:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if layouts[1]["loudness"].get("digital_peak") == -2865:
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
	no_of_check_items += 1
	if obu.get("count_label") == 1:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if obu.get("language_labels") is not None:
		pass_count += 1
		language_labels = obu.get("language_labels")
		no_of_check_items += 1
		if language_labels[0] == "en-us":
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if obu.get("mix_presentation_annotations_array") is not None:
		pass_count += 1
		mix_presentation_annotations_array = obu.get("mix_presentation_annotations_array")
		no_of_check_items += 1
		if mix_presentation_annotations_array[0].get("mix_presentation_friendly_label") == "test_mix_pres":
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

if pass_count == no_of_check_items:
	print("%d item(s) of %d tests is/are passed."%(pass_count, no_of_check_items))
else:
	print("%d item(s) of %d tests is/are passed."%(pass_count, no_of_check_items))
	print("%d item(s) of %d tests is/are failed."%(no_of_check_items-pass_count, no_of_check_items))
	
# Check Bitstream Validation
print("*"*40)
print("* IAMF-Bitstream Valid Check")
print("*"*40)

from iamf_validator import is_valid_bitstream
valid, message = is_valid_bitstream(obu_list)
if not valid:
	print("Invalid Bitstream!!!")
	print(message)
else:
	print("Valid Bitstream")
	print("*"*40)
	print("* Decoded Audio Signal Check")
	print("*"*40)

	# Calculate PSNR
	def calc_psnr(ref_signal, signal):
		import numpy as np
		import math
		
		max_value = np.iinfo(ref_signal.dtype).max-np.iinfo(ref_signal.dtype).min
		
		# To prevent overflow
		ref_signal = ref_signal.astype('int64')
		signal = signal.astype('int64')
		
		mse = np.mean((ref_signal - signal)**2, axis=0, dtype = 'float64')
		
		# To support mono signal
		num_channels = 1 if ref_signal.shape[1:] == () else ref_signal.shape[1]
		for i in range(num_channels):
			mse_value = mse[i] if num_channels > 1 else mse
			if mse_value==0:
				print(f'ch#{i} PSNR: inf')
			else:
				print(f'ch#{i} PSNR: {10*math.log10(max_value**2/mse_value)} dB')
				
		return
		
	# Compare two signals
	def bitwise_compare(ref_signal, signal):
		import numpy as np

		tot_diff = 0
		num_samples = ref_signal.shape[0]
		num_channels = 1 if ref_signal.shape[1:] == () else ref_signal.shape[1]
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
				
		print("PSNR evaluation:")
		
		try:
			ref_samplerate, ref_data = wavfile.read(ref_file)	
			cmp_samplerate, cmp_data = wavfile.read(cmp_file)
			
			# Check sampling rate
			if not (ref_samplerate == cmp_samplerate):
				raise Exception("Sampling rate of reference file and comparison file are different.")
			
			# Check number of channels
			if not (ref_data.shape[1:] == cmp_data.shape[1:]):
				raise Exception("Number of channels of reference file and comparison file are different.")
			
			# Check number of samples
			if not (ref_data.shape[0] == cmp_data.shape[0]):
				raise Exception("Number of samples of reference file and comparison file are different.")
			
			calc_psnr(ref_data, cmp_data)
			
		except Exception as err:
			print(str(err))

	if args.bitwise is not None:
		import scipy.io.wavfile as wavfile
		ref_file = args.bitwise
		cmp_file = args.wav
		
		print("bitwise comparison:")
		
		try:
			ref_samplerate, ref_data = wavfile.read(ref_file)	
			cmp_samplerate, cmp_data = wavfile.read(cmp_file)
					
			# Check sampling rate
			if not (ref_samplerate == cmp_samplerate):
				raise Exception("Sampling rate of reference file and comparison file are different.")
			
			# Check number of channels
			if not (ref_data.shape[1:] == cmp_data.shape[1:]):
				raise Exception("Number of channels of reference file and comparison file are different.")
				
			# Check number of samples
			if not (ref_data.shape[0] == cmp_data.shape[0]):
				raise Exception("Number of samples of reference file and comparison file are different.")
			
			tot_diff, tot_sample = bitwise_compare(ref_data, cmp_data)
			if (tot_diff > 0):
				print("%d point(s) of %d comparisons is/are different."%(tot_diff, tot_sample))
				print("%d point(s) of %d comparisons is/are same."%(tot_sample-tot_diff, tot_sample))		
			else:
				print("%d point(s) of %d comparisons is/are same."%(tot_sample-tot_diff, tot_sample))
			
		except Exception as err:
			print(str(err))
			
	
	print("*"*40)
	print("* log output file: %s"%(args.log))
	print("* wav output file: %s"%(args.wav))
	if args.psnr is not None or args.bitwise is not None:
		print("* reference wav file: %s"%(ref_file))
	print("*"*40)

print("*"*40)
print("description:")
print("""A 2-layer IAMF stream encoded using Opus with the last layer
being 5.1.""")
print("is_valid: True")
print("primary_tested_spec_sections: ['2.7.2/channel_audio_layer_config', '2.10', '2.12.1']")
print("*"*40)

