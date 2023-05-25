import yaml
import inspect
import argparse

parser = argparse.ArgumentParser(description="test_000050_f verification script")
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
	if atom[5]["Duration"] == 0:
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
	if atom[6]["Duration"] == 0:
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
	if atom[3]["SegmentDuration_0"] == 0:
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
	if atom[5]["Duration"] == 0:
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
	if atom[5]["ChannelCount"] == 12:
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
if "stts_00000000000002e6" in atom_list[13]:
	pass_count += 1
	atom = atom_list[13]["stts_00000000000002e6"]
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
if "stsc_00000000000002f6" in atom_list[14]:
	pass_count += 1
	atom = atom_list[14]["stsc_00000000000002f6"]
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
if "stco_0000000000000306" in atom_list[15]:
	pass_count += 1
	atom = atom_list[15]["stco_0000000000000306"]
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
if "stsz_0000000000000316" in atom_list[16]:
	pass_count += 1
	atom = atom_list[16]["stsz_0000000000000316"]
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
if "moof_0000000000000366" in atom_list[17]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "traf_000000000000037e" in atom_list[18]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "tfhd_0000000000000386" in atom_list[19]:
	pass_count += 1
	atom = atom_list[19]["tfhd_0000000000000386"]
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
	if atom[1]["Flags"] == 2817:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2]["SampleCount"] == 1140:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	SampleCount = atom[2]["SampleCount"]
	no_of_check_items += 1
	if atom[3]["DataOffset"] == 13806:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[4]["SampleDuration_0"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[5]["SampleSize_0"] == 536:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[6]["SampleCompositionTimeOffset_0"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[7]["SampleDuration_1"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[8]["SampleSize_1"] == 480:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[9]["SampleCompositionTimeOffset_1"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[10]["SampleDuration_2"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[11]["SampleSize_2"] == 558:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[12]["SampleCompositionTimeOffset_2"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[13]["SampleDuration_3"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[14]["SampleSize_3"] == 616:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[15]["SampleCompositionTimeOffset_3"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[16]["SampleDuration_4"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[17]["SampleSize_4"] == 739:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[18]["SampleCompositionTimeOffset_4"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[19]["SampleDuration_5"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[20]["SampleSize_5"] == 897:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[21]["SampleCompositionTimeOffset_5"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[22]["SampleDuration_6"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[23]["SampleSize_6"] == 922:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[24]["SampleCompositionTimeOffset_6"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[25]["SampleDuration_7"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[26]["SampleSize_7"] == 987:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[27]["SampleCompositionTimeOffset_7"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[28]["SampleDuration_8"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[29]["SampleSize_8"] == 884:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[30]["SampleCompositionTimeOffset_8"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[31]["SampleDuration_9"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[32]["SampleSize_9"] == 863:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[33]["SampleCompositionTimeOffset_9"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[34]["SampleDuration_10"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[35]["SampleSize_10"] == 848:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[36]["SampleCompositionTimeOffset_10"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[37]["SampleDuration_11"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[38]["SampleSize_11"] == 840:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[39]["SampleCompositionTimeOffset_11"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[40]["SampleDuration_12"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[41]["SampleSize_12"] == 831:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[42]["SampleCompositionTimeOffset_12"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[43]["SampleDuration_13"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[44]["SampleSize_13"] == 846:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[45]["SampleCompositionTimeOffset_13"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[46]["SampleDuration_14"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[47]["SampleSize_14"] == 1031:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[48]["SampleCompositionTimeOffset_14"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[49]["SampleDuration_15"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[50]["SampleSize_15"] == 926:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[51]["SampleCompositionTimeOffset_15"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[52]["SampleDuration_16"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[53]["SampleSize_16"] == 908:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[54]["SampleCompositionTimeOffset_16"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[55]["SampleDuration_17"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[56]["SampleSize_17"] == 859:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[57]["SampleCompositionTimeOffset_17"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[58]["SampleDuration_18"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[59]["SampleSize_18"] == 849:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[60]["SampleCompositionTimeOffset_18"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[61]["SampleDuration_19"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[62]["SampleSize_19"] == 839:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[63]["SampleCompositionTimeOffset_19"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[64]["SampleDuration_20"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[65]["SampleSize_20"] == 829:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[66]["SampleCompositionTimeOffset_20"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[67]["SampleDuration_21"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[68]["SampleSize_21"] == 911:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[69]["SampleCompositionTimeOffset_21"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[70]["SampleDuration_22"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[71]["SampleSize_22"] == 885:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[72]["SampleCompositionTimeOffset_22"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[73]["SampleDuration_23"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[74]["SampleSize_23"] == 909:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[75]["SampleCompositionTimeOffset_23"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[76]["SampleDuration_24"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[77]["SampleSize_24"] == 866:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[78]["SampleCompositionTimeOffset_24"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[79]["SampleDuration_25"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[80]["SampleSize_25"] == 1084:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[81]["SampleCompositionTimeOffset_25"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[82]["SampleDuration_26"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[83]["SampleSize_26"] == 878:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[84]["SampleCompositionTimeOffset_26"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[85]["SampleDuration_27"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[86]["SampleSize_27"] == 884:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[87]["SampleCompositionTimeOffset_27"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[88]["SampleDuration_28"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[89]["SampleSize_28"] == 882:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[90]["SampleCompositionTimeOffset_28"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[91]["SampleDuration_29"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[92]["SampleSize_29"] == 885:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[93]["SampleCompositionTimeOffset_29"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[94]["SampleDuration_30"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[95]["SampleSize_30"] == 874:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[96]["SampleCompositionTimeOffset_30"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[97]["SampleDuration_31"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[98]["SampleSize_31"] == 877:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[99]["SampleCompositionTimeOffset_31"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[100]["SampleDuration_32"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[101]["SampleSize_32"] == 877:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[102]["SampleCompositionTimeOffset_32"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[103]["SampleDuration_33"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[104]["SampleSize_33"] == 873:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[105]["SampleCompositionTimeOffset_33"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[106]["SampleDuration_34"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[107]["SampleSize_34"] == 871:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[108]["SampleCompositionTimeOffset_34"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[109]["SampleDuration_35"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[110]["SampleSize_35"] == 908:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[111]["SampleCompositionTimeOffset_35"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[112]["SampleDuration_36"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[113]["SampleSize_36"] == 876:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[114]["SampleCompositionTimeOffset_36"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[115]["SampleDuration_37"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[116]["SampleSize_37"] == 875:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[117]["SampleCompositionTimeOffset_37"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[118]["SampleDuration_38"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[119]["SampleSize_38"] == 880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[120]["SampleCompositionTimeOffset_38"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[121]["SampleDuration_39"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[122]["SampleSize_39"] == 1407:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[123]["SampleCompositionTimeOffset_39"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[124]["SampleDuration_40"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[125]["SampleSize_40"] == 978:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[126]["SampleCompositionTimeOffset_40"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[127]["SampleDuration_41"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[128]["SampleSize_41"] == 914:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[129]["SampleCompositionTimeOffset_41"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[130]["SampleDuration_42"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[131]["SampleSize_42"] == 890:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[132]["SampleCompositionTimeOffset_42"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[133]["SampleDuration_43"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[134]["SampleSize_43"] == 898:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[135]["SampleCompositionTimeOffset_43"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[136]["SampleDuration_44"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[137]["SampleSize_44"] == 885:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[138]["SampleCompositionTimeOffset_44"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[139]["SampleDuration_45"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[140]["SampleSize_45"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[141]["SampleCompositionTimeOffset_45"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[142]["SampleDuration_46"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[143]["SampleSize_46"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[144]["SampleCompositionTimeOffset_46"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[145]["SampleDuration_47"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[146]["SampleSize_47"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[147]["SampleCompositionTimeOffset_47"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[148]["SampleDuration_48"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[149]["SampleSize_48"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[150]["SampleCompositionTimeOffset_48"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[151]["SampleDuration_49"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[152]["SampleSize_49"] == 866:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[153]["SampleCompositionTimeOffset_49"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[154]["SampleDuration_50"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[155]["SampleSize_50"] == 851:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[156]["SampleCompositionTimeOffset_50"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[157]["SampleDuration_51"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[158]["SampleSize_51"] == 846:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[159]["SampleCompositionTimeOffset_51"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[160]["SampleDuration_52"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[161]["SampleSize_52"] == 787:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[162]["SampleCompositionTimeOffset_52"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[163]["SampleDuration_53"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[164]["SampleSize_53"] == 808:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[165]["SampleCompositionTimeOffset_53"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[166]["SampleDuration_54"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[167]["SampleSize_54"] == 828:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[168]["SampleCompositionTimeOffset_54"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[169]["SampleDuration_55"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[170]["SampleSize_55"] == 834:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[171]["SampleCompositionTimeOffset_55"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[172]["SampleDuration_56"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[173]["SampleSize_56"] == 1088:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[174]["SampleCompositionTimeOffset_56"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[175]["SampleDuration_57"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[176]["SampleSize_57"] == 890:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[177]["SampleCompositionTimeOffset_57"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[178]["SampleDuration_58"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[179]["SampleSize_58"] == 876:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[180]["SampleCompositionTimeOffset_58"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[181]["SampleDuration_59"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[182]["SampleSize_59"] == 841:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[183]["SampleCompositionTimeOffset_59"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[184]["SampleDuration_60"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[185]["SampleSize_60"] == 936:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[186]["SampleCompositionTimeOffset_60"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[187]["SampleDuration_61"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[188]["SampleSize_61"] == 897:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[189]["SampleCompositionTimeOffset_61"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[190]["SampleDuration_62"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[191]["SampleSize_62"] == 835:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[192]["SampleCompositionTimeOffset_62"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[193]["SampleDuration_63"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[194]["SampleSize_63"] == 827:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[195]["SampleCompositionTimeOffset_63"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[196]["SampleDuration_64"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[197]["SampleSize_64"] == 835:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[198]["SampleCompositionTimeOffset_64"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[199]["SampleDuration_65"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[200]["SampleSize_65"] == 833:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[201]["SampleCompositionTimeOffset_65"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[202]["SampleDuration_66"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[203]["SampleSize_66"] == 1014:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[204]["SampleCompositionTimeOffset_66"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[205]["SampleDuration_67"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[206]["SampleSize_67"] == 874:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[207]["SampleCompositionTimeOffset_67"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[208]["SampleDuration_68"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[209]["SampleSize_68"] == 882:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[210]["SampleCompositionTimeOffset_68"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[211]["SampleDuration_69"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[212]["SampleSize_69"] == 882:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[213]["SampleCompositionTimeOffset_69"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[214]["SampleDuration_70"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[215]["SampleSize_70"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[216]["SampleCompositionTimeOffset_70"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[217]["SampleDuration_71"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[218]["SampleSize_71"] == 871:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[219]["SampleCompositionTimeOffset_71"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[220]["SampleDuration_72"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[221]["SampleSize_72"] == 873:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[222]["SampleCompositionTimeOffset_72"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[223]["SampleDuration_73"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[224]["SampleSize_73"] == 874:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[225]["SampleCompositionTimeOffset_73"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[226]["SampleDuration_74"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[227]["SampleSize_74"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[228]["SampleCompositionTimeOffset_74"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[229]["SampleDuration_75"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[230]["SampleSize_75"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[231]["SampleCompositionTimeOffset_75"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[232]["SampleDuration_76"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[233]["SampleSize_76"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[234]["SampleCompositionTimeOffset_76"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[235]["SampleDuration_77"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[236]["SampleSize_77"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[237]["SampleCompositionTimeOffset_77"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[238]["SampleDuration_78"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[239]["SampleSize_78"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[240]["SampleCompositionTimeOffset_78"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[241]["SampleDuration_79"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[242]["SampleSize_79"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[243]["SampleCompositionTimeOffset_79"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[244]["SampleDuration_80"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[245]["SampleSize_80"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[246]["SampleCompositionTimeOffset_80"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[247]["SampleDuration_81"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[248]["SampleSize_81"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[249]["SampleCompositionTimeOffset_81"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[250]["SampleDuration_82"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[251]["SampleSize_82"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[252]["SampleCompositionTimeOffset_82"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[253]["SampleDuration_83"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[254]["SampleSize_83"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[255]["SampleCompositionTimeOffset_83"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[256]["SampleDuration_84"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[257]["SampleSize_84"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[258]["SampleCompositionTimeOffset_84"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[259]["SampleDuration_85"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[260]["SampleSize_85"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[261]["SampleCompositionTimeOffset_85"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[262]["SampleDuration_86"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[263]["SampleSize_86"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[264]["SampleCompositionTimeOffset_86"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[265]["SampleDuration_87"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[266]["SampleSize_87"] == 870:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[267]["SampleCompositionTimeOffset_87"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[268]["SampleDuration_88"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[269]["SampleSize_88"] == 868:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[270]["SampleCompositionTimeOffset_88"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[271]["SampleDuration_89"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[272]["SampleSize_89"] == 871:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[273]["SampleCompositionTimeOffset_89"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[274]["SampleDuration_90"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[275]["SampleSize_90"] == 863:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[276]["SampleCompositionTimeOffset_90"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[277]["SampleDuration_91"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[278]["SampleSize_91"] == 860:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[279]["SampleCompositionTimeOffset_91"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[280]["SampleDuration_92"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[281]["SampleSize_92"] == 894:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[282]["SampleCompositionTimeOffset_92"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[283]["SampleDuration_93"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[284]["SampleSize_93"] == 864:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[285]["SampleCompositionTimeOffset_93"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[286]["SampleDuration_94"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[287]["SampleSize_94"] == 846:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[288]["SampleCompositionTimeOffset_94"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[289]["SampleDuration_95"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[290]["SampleSize_95"] == 848:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[291]["SampleCompositionTimeOffset_95"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[292]["SampleDuration_96"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[293]["SampleSize_96"] == 938:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[294]["SampleCompositionTimeOffset_96"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[295]["SampleDuration_97"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[296]["SampleSize_97"] == 845:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[297]["SampleCompositionTimeOffset_97"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[298]["SampleDuration_98"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[299]["SampleSize_98"] == 850:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[300]["SampleCompositionTimeOffset_98"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[301]["SampleDuration_99"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[302]["SampleSize_99"] == 828:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[303]["SampleCompositionTimeOffset_99"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[304]["SampleDuration_100"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[305]["SampleSize_100"] == 843:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[306]["SampleCompositionTimeOffset_100"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[307]["SampleDuration_101"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[308]["SampleSize_101"] == 843:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[309]["SampleCompositionTimeOffset_101"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[310]["SampleDuration_102"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[311]["SampleSize_102"] == 835:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[312]["SampleCompositionTimeOffset_102"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[313]["SampleDuration_103"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[314]["SampleSize_103"] == 1071:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[315]["SampleCompositionTimeOffset_103"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[316]["SampleDuration_104"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[317]["SampleSize_104"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[318]["SampleCompositionTimeOffset_104"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[319]["SampleDuration_105"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[320]["SampleSize_105"] == 835:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[321]["SampleCompositionTimeOffset_105"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[322]["SampleDuration_106"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[323]["SampleSize_106"] == 821:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[324]["SampleCompositionTimeOffset_106"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[325]["SampleDuration_107"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[326]["SampleSize_107"] == 874:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[327]["SampleCompositionTimeOffset_107"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[328]["SampleDuration_108"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[329]["SampleSize_108"] == 965:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[330]["SampleCompositionTimeOffset_108"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[331]["SampleDuration_109"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[332]["SampleSize_109"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[333]["SampleCompositionTimeOffset_109"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[334]["SampleDuration_110"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[335]["SampleSize_110"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[336]["SampleCompositionTimeOffset_110"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[337]["SampleDuration_111"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[338]["SampleSize_111"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[339]["SampleCompositionTimeOffset_111"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[340]["SampleDuration_112"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[341]["SampleSize_112"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[342]["SampleCompositionTimeOffset_112"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[343]["SampleDuration_113"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[344]["SampleSize_113"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[345]["SampleCompositionTimeOffset_113"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[346]["SampleDuration_114"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[347]["SampleSize_114"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[348]["SampleCompositionTimeOffset_114"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[349]["SampleDuration_115"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[350]["SampleSize_115"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[351]["SampleCompositionTimeOffset_115"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[352]["SampleDuration_116"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[353]["SampleSize_116"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[354]["SampleCompositionTimeOffset_116"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[355]["SampleDuration_117"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[356]["SampleSize_117"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[357]["SampleCompositionTimeOffset_117"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[358]["SampleDuration_118"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[359]["SampleSize_118"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[360]["SampleCompositionTimeOffset_118"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[361]["SampleDuration_119"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[362]["SampleSize_119"] == 860:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[363]["SampleCompositionTimeOffset_119"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[364]["SampleDuration_120"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[365]["SampleSize_120"] == 855:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[366]["SampleCompositionTimeOffset_120"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[367]["SampleDuration_121"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[368]["SampleSize_121"] == 854:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[369]["SampleCompositionTimeOffset_121"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[370]["SampleDuration_122"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[371]["SampleSize_122"] == 802:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[372]["SampleCompositionTimeOffset_122"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[373]["SampleDuration_123"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[374]["SampleSize_123"] == 788:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[375]["SampleCompositionTimeOffset_123"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[376]["SampleDuration_124"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[377]["SampleSize_124"] == 793:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[378]["SampleCompositionTimeOffset_124"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[379]["SampleDuration_125"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[380]["SampleSize_125"] == 823:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[381]["SampleCompositionTimeOffset_125"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[382]["SampleDuration_126"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[383]["SampleSize_126"] == 927:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[384]["SampleCompositionTimeOffset_126"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[385]["SampleDuration_127"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[386]["SampleSize_127"] == 869:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[387]["SampleCompositionTimeOffset_127"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[388]["SampleDuration_128"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[389]["SampleSize_128"] == 889:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[390]["SampleCompositionTimeOffset_128"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[391]["SampleDuration_129"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[392]["SampleSize_129"] == 906:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[393]["SampleCompositionTimeOffset_129"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[394]["SampleDuration_130"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[395]["SampleSize_130"] == 894:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[396]["SampleCompositionTimeOffset_130"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[397]["SampleDuration_131"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[398]["SampleSize_131"] == 905:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[399]["SampleCompositionTimeOffset_131"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[400]["SampleDuration_132"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[401]["SampleSize_132"] == 895:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[402]["SampleCompositionTimeOffset_132"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[403]["SampleDuration_133"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[404]["SampleSize_133"] == 877:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[405]["SampleCompositionTimeOffset_133"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[406]["SampleDuration_134"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[407]["SampleSize_134"] == 854:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[408]["SampleCompositionTimeOffset_134"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[409]["SampleDuration_135"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[410]["SampleSize_135"] == 801:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[411]["SampleCompositionTimeOffset_135"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[412]["SampleDuration_136"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[413]["SampleSize_136"] == 951:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[414]["SampleCompositionTimeOffset_136"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[415]["SampleDuration_137"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[416]["SampleSize_137"] == 851:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[417]["SampleCompositionTimeOffset_137"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[418]["SampleDuration_138"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[419]["SampleSize_138"] == 835:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[420]["SampleCompositionTimeOffset_138"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[421]["SampleDuration_139"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[422]["SampleSize_139"] == 787:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[423]["SampleCompositionTimeOffset_139"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[424]["SampleDuration_140"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[425]["SampleSize_140"] == 793:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[426]["SampleCompositionTimeOffset_140"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[427]["SampleDuration_141"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[428]["SampleSize_141"] == 801:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[429]["SampleCompositionTimeOffset_141"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[430]["SampleDuration_142"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[431]["SampleSize_142"] == 812:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[432]["SampleCompositionTimeOffset_142"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[433]["SampleDuration_143"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[434]["SampleSize_143"] == 828:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[435]["SampleCompositionTimeOffset_143"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[436]["SampleDuration_144"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[437]["SampleSize_144"] == 1102:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[438]["SampleCompositionTimeOffset_144"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[439]["SampleDuration_145"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[440]["SampleSize_145"] == 1014:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[441]["SampleCompositionTimeOffset_145"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[442]["SampleDuration_146"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[443]["SampleSize_146"] == 894:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[444]["SampleCompositionTimeOffset_146"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[445]["SampleDuration_147"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[446]["SampleSize_147"] == 882:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[447]["SampleCompositionTimeOffset_147"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[448]["SampleDuration_148"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[449]["SampleSize_148"] == 923:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[450]["SampleCompositionTimeOffset_148"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[451]["SampleDuration_149"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[452]["SampleSize_149"] == 911:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[453]["SampleCompositionTimeOffset_149"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[454]["SampleDuration_150"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[455]["SampleSize_150"] == 862:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[456]["SampleCompositionTimeOffset_150"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[457]["SampleDuration_151"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[458]["SampleSize_151"] == 843:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[459]["SampleCompositionTimeOffset_151"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[460]["SampleDuration_152"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[461]["SampleSize_152"] == 827:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[462]["SampleCompositionTimeOffset_152"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[463]["SampleDuration_153"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[464]["SampleSize_153"] == 928:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[465]["SampleCompositionTimeOffset_153"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[466]["SampleDuration_154"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[467]["SampleSize_154"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[468]["SampleCompositionTimeOffset_154"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[469]["SampleDuration_155"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[470]["SampleSize_155"] == 905:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[471]["SampleCompositionTimeOffset_155"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[472]["SampleDuration_156"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[473]["SampleSize_156"] == 858:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[474]["SampleCompositionTimeOffset_156"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[475]["SampleDuration_157"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[476]["SampleSize_157"] == 891:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[477]["SampleCompositionTimeOffset_157"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[478]["SampleDuration_158"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[479]["SampleSize_158"] == 899:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[480]["SampleCompositionTimeOffset_158"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[481]["SampleDuration_159"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[482]["SampleSize_159"] == 893:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[483]["SampleCompositionTimeOffset_159"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[484]["SampleDuration_160"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[485]["SampleSize_160"] == 889:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[486]["SampleCompositionTimeOffset_160"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[487]["SampleDuration_161"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[488]["SampleSize_161"] == 877:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[489]["SampleCompositionTimeOffset_161"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[490]["SampleDuration_162"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[491]["SampleSize_162"] == 876:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[492]["SampleCompositionTimeOffset_162"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[493]["SampleDuration_163"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[494]["SampleSize_163"] == 875:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[495]["SampleCompositionTimeOffset_163"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[496]["SampleDuration_164"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[497]["SampleSize_164"] == 874:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[498]["SampleCompositionTimeOffset_164"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[499]["SampleDuration_165"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[500]["SampleSize_165"] == 875:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[501]["SampleCompositionTimeOffset_165"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[502]["SampleDuration_166"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[503]["SampleSize_166"] == 871:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[504]["SampleCompositionTimeOffset_166"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[505]["SampleDuration_167"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[506]["SampleSize_167"] == 866:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[507]["SampleCompositionTimeOffset_167"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[508]["SampleDuration_168"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[509]["SampleSize_168"] == 866:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[510]["SampleCompositionTimeOffset_168"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[511]["SampleDuration_169"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[512]["SampleSize_169"] == 866:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[513]["SampleCompositionTimeOffset_169"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[514]["SampleDuration_170"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[515]["SampleSize_170"] == 860:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[516]["SampleCompositionTimeOffset_170"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[517]["SampleDuration_171"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[518]["SampleSize_171"] == 854:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[519]["SampleCompositionTimeOffset_171"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[520]["SampleDuration_172"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[521]["SampleSize_172"] == 844:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[522]["SampleCompositionTimeOffset_172"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[523]["SampleDuration_173"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[524]["SampleSize_173"] == 852:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[525]["SampleCompositionTimeOffset_173"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[526]["SampleDuration_174"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[527]["SampleSize_174"] == 847:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[528]["SampleCompositionTimeOffset_174"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[529]["SampleDuration_175"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[530]["SampleSize_175"] == 844:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[531]["SampleCompositionTimeOffset_175"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[532]["SampleDuration_176"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[533]["SampleSize_176"] == 849:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[534]["SampleCompositionTimeOffset_176"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[535]["SampleDuration_177"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[536]["SampleSize_177"] == 829:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[537]["SampleCompositionTimeOffset_177"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[538]["SampleDuration_178"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[539]["SampleSize_178"] == 859:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[540]["SampleCompositionTimeOffset_178"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[541]["SampleDuration_179"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[542]["SampleSize_179"] == 836:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[543]["SampleCompositionTimeOffset_179"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[544]["SampleDuration_180"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[545]["SampleSize_180"] == 870:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[546]["SampleCompositionTimeOffset_180"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[547]["SampleDuration_181"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[548]["SampleSize_181"] == 1147:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[549]["SampleCompositionTimeOffset_181"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[550]["SampleDuration_182"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[551]["SampleSize_182"] == 877:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[552]["SampleCompositionTimeOffset_182"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[553]["SampleDuration_183"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[554]["SampleSize_183"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[555]["SampleCompositionTimeOffset_183"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[556]["SampleDuration_184"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[557]["SampleSize_184"] == 865:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[558]["SampleCompositionTimeOffset_184"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[559]["SampleDuration_185"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[560]["SampleSize_185"] == 873:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[561]["SampleCompositionTimeOffset_185"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[562]["SampleDuration_186"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[563]["SampleSize_186"] == 878:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[564]["SampleCompositionTimeOffset_186"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[565]["SampleDuration_187"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[566]["SampleSize_187"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[567]["SampleCompositionTimeOffset_187"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[568]["SampleDuration_188"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[569]["SampleSize_188"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[570]["SampleCompositionTimeOffset_188"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[571]["SampleDuration_189"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[572]["SampleSize_189"] == 869:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[573]["SampleCompositionTimeOffset_189"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[574]["SampleDuration_190"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[575]["SampleSize_190"] == 866:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[576]["SampleCompositionTimeOffset_190"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[577]["SampleDuration_191"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[578]["SampleSize_191"] == 862:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[579]["SampleCompositionTimeOffset_191"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[580]["SampleDuration_192"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[581]["SampleSize_192"] == 864:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[582]["SampleCompositionTimeOffset_192"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[583]["SampleDuration_193"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[584]["SampleSize_193"] == 853:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[585]["SampleCompositionTimeOffset_193"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[586]["SampleDuration_194"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[587]["SampleSize_194"] == 834:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[588]["SampleCompositionTimeOffset_194"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[589]["SampleDuration_195"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[590]["SampleSize_195"] == 804:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[591]["SampleCompositionTimeOffset_195"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[592]["SampleDuration_196"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[593]["SampleSize_196"] == 788:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[594]["SampleCompositionTimeOffset_196"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[595]["SampleDuration_197"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[596]["SampleSize_197"] == 800:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[597]["SampleCompositionTimeOffset_197"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[598]["SampleDuration_198"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[599]["SampleSize_198"] == 794:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[600]["SampleCompositionTimeOffset_198"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[601]["SampleDuration_199"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[602]["SampleSize_199"] == 802:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[603]["SampleCompositionTimeOffset_199"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[604]["SampleDuration_200"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[605]["SampleSize_200"] == 1058:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[606]["SampleCompositionTimeOffset_200"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[607]["SampleDuration_201"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[608]["SampleSize_201"] == 891:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[609]["SampleCompositionTimeOffset_201"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[610]["SampleDuration_202"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[611]["SampleSize_202"] == 827:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[612]["SampleCompositionTimeOffset_202"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[613]["SampleDuration_203"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[614]["SampleSize_203"] == 827:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[615]["SampleCompositionTimeOffset_203"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[616]["SampleDuration_204"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[617]["SampleSize_204"] == 823:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[618]["SampleCompositionTimeOffset_204"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[619]["SampleDuration_205"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[620]["SampleSize_205"] == 819:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[621]["SampleCompositionTimeOffset_205"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[622]["SampleDuration_206"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[623]["SampleSize_206"] == 836:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[624]["SampleCompositionTimeOffset_206"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[625]["SampleDuration_207"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[626]["SampleSize_207"] == 846:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[627]["SampleCompositionTimeOffset_207"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[628]["SampleDuration_208"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[629]["SampleSize_208"] == 1070:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[630]["SampleCompositionTimeOffset_208"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[631]["SampleDuration_209"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[632]["SampleSize_209"] == 931:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[633]["SampleCompositionTimeOffset_209"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[634]["SampleDuration_210"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[635]["SampleSize_210"] == 892:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[636]["SampleCompositionTimeOffset_210"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[637]["SampleDuration_211"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[638]["SampleSize_211"] == 868:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[639]["SampleCompositionTimeOffset_211"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[640]["SampleDuration_212"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[641]["SampleSize_212"] == 875:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[642]["SampleCompositionTimeOffset_212"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[643]["SampleDuration_213"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[644]["SampleSize_213"] == 868:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[645]["SampleCompositionTimeOffset_213"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[646]["SampleDuration_214"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[647]["SampleSize_214"] == 890:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[648]["SampleCompositionTimeOffset_214"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[649]["SampleDuration_215"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[650]["SampleSize_215"] == 884:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[651]["SampleCompositionTimeOffset_215"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[652]["SampleDuration_216"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[653]["SampleSize_216"] == 873:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[654]["SampleCompositionTimeOffset_216"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[655]["SampleDuration_217"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[656]["SampleSize_217"] == 866:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[657]["SampleCompositionTimeOffset_217"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[658]["SampleDuration_218"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[659]["SampleSize_218"] == 858:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[660]["SampleCompositionTimeOffset_218"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[661]["SampleDuration_219"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[662]["SampleSize_219"] == 870:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[663]["SampleCompositionTimeOffset_219"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[664]["SampleDuration_220"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[665]["SampleSize_220"] == 877:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[666]["SampleCompositionTimeOffset_220"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[667]["SampleDuration_221"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[668]["SampleSize_221"] == 866:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[669]["SampleCompositionTimeOffset_221"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[670]["SampleDuration_222"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[671]["SampleSize_222"] == 897:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[672]["SampleCompositionTimeOffset_222"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[673]["SampleDuration_223"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[674]["SampleSize_223"] == 908:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[675]["SampleCompositionTimeOffset_223"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[676]["SampleDuration_224"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[677]["SampleSize_224"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[678]["SampleCompositionTimeOffset_224"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[679]["SampleDuration_225"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[680]["SampleSize_225"] == 989:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[681]["SampleCompositionTimeOffset_225"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[682]["SampleDuration_226"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[683]["SampleSize_226"] == 877:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[684]["SampleCompositionTimeOffset_226"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[685]["SampleDuration_227"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[686]["SampleSize_227"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[687]["SampleCompositionTimeOffset_227"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[688]["SampleDuration_228"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[689]["SampleSize_228"] == 840:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[690]["SampleCompositionTimeOffset_228"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[691]["SampleDuration_229"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[692]["SampleSize_229"] == 810:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[693]["SampleCompositionTimeOffset_229"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[694]["SampleDuration_230"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[695]["SampleSize_230"] == 832:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[696]["SampleCompositionTimeOffset_230"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[697]["SampleDuration_231"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[698]["SampleSize_231"] == 823:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[699]["SampleCompositionTimeOffset_231"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[700]["SampleDuration_232"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[701]["SampleSize_232"] == 956:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[702]["SampleCompositionTimeOffset_232"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[703]["SampleDuration_233"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[704]["SampleSize_233"] == 918:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[705]["SampleCompositionTimeOffset_233"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[706]["SampleDuration_234"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[707]["SampleSize_234"] == 865:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[708]["SampleCompositionTimeOffset_234"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[709]["SampleDuration_235"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[710]["SampleSize_235"] == 822:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[711]["SampleCompositionTimeOffset_235"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[712]["SampleDuration_236"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[713]["SampleSize_236"] == 845:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[714]["SampleCompositionTimeOffset_236"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[715]["SampleDuration_237"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[716]["SampleSize_237"] == 852:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[717]["SampleCompositionTimeOffset_237"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[718]["SampleDuration_238"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[719]["SampleSize_238"] == 838:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[720]["SampleCompositionTimeOffset_238"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[721]["SampleDuration_239"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[722]["SampleSize_239"] == 834:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[723]["SampleCompositionTimeOffset_239"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[724]["SampleDuration_240"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[725]["SampleSize_240"] == 832:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[726]["SampleCompositionTimeOffset_240"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[727]["SampleDuration_241"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[728]["SampleSize_241"] == 823:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[729]["SampleCompositionTimeOffset_241"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[730]["SampleDuration_242"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[731]["SampleSize_242"] == 818:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[732]["SampleCompositionTimeOffset_242"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[733]["SampleDuration_243"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[734]["SampleSize_243"] == 821:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[735]["SampleCompositionTimeOffset_243"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[736]["SampleDuration_244"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[737]["SampleSize_244"] == 820:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[738]["SampleCompositionTimeOffset_244"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[739]["SampleDuration_245"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[740]["SampleSize_245"] == 821:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[741]["SampleCompositionTimeOffset_245"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[742]["SampleDuration_246"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[743]["SampleSize_246"] == 823:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[744]["SampleCompositionTimeOffset_246"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[745]["SampleDuration_247"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[746]["SampleSize_247"] == 827:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[747]["SampleCompositionTimeOffset_247"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[748]["SampleDuration_248"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[749]["SampleSize_248"] == 837:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[750]["SampleCompositionTimeOffset_248"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[751]["SampleDuration_249"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[752]["SampleSize_249"] == 1379:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[753]["SampleCompositionTimeOffset_249"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[754]["SampleDuration_250"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[755]["SampleSize_250"] == 925:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[756]["SampleCompositionTimeOffset_250"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[757]["SampleDuration_251"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[758]["SampleSize_251"] == 871:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[759]["SampleCompositionTimeOffset_251"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[760]["SampleDuration_252"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[761]["SampleSize_252"] == 831:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[762]["SampleCompositionTimeOffset_252"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[763]["SampleDuration_253"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[764]["SampleSize_253"] == 823:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[765]["SampleCompositionTimeOffset_253"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[766]["SampleDuration_254"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[767]["SampleSize_254"] == 823:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[768]["SampleCompositionTimeOffset_254"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[769]["SampleDuration_255"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[770]["SampleSize_255"] == 834:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[771]["SampleCompositionTimeOffset_255"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[772]["SampleDuration_256"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[773]["SampleSize_256"] == 824:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[774]["SampleCompositionTimeOffset_256"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[775]["SampleDuration_257"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[776]["SampleSize_257"] == 791:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[777]["SampleCompositionTimeOffset_257"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[778]["SampleDuration_258"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[779]["SampleSize_258"] == 761:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[780]["SampleCompositionTimeOffset_258"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[781]["SampleDuration_259"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[782]["SampleSize_259"] == 772:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[783]["SampleCompositionTimeOffset_259"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[784]["SampleDuration_260"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[785]["SampleSize_260"] == 791:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[786]["SampleCompositionTimeOffset_260"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[787]["SampleDuration_261"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[788]["SampleSize_261"] == 821:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[789]["SampleCompositionTimeOffset_261"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[790]["SampleDuration_262"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[791]["SampleSize_262"] == 869:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[792]["SampleCompositionTimeOffset_262"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[793]["SampleDuration_263"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[794]["SampleSize_263"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[795]["SampleCompositionTimeOffset_263"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[796]["SampleDuration_264"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[797]["SampleSize_264"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[798]["SampleCompositionTimeOffset_264"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[799]["SampleDuration_265"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[800]["SampleSize_265"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[801]["SampleCompositionTimeOffset_265"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[802]["SampleDuration_266"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[803]["SampleSize_266"] == 1059:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[804]["SampleCompositionTimeOffset_266"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[805]["SampleDuration_267"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[806]["SampleSize_267"] == 912:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[807]["SampleCompositionTimeOffset_267"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[808]["SampleDuration_268"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[809]["SampleSize_268"] == 846:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[810]["SampleCompositionTimeOffset_268"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[811]["SampleDuration_269"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[812]["SampleSize_269"] == 946:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[813]["SampleCompositionTimeOffset_269"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[814]["SampleDuration_270"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[815]["SampleSize_270"] == 875:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[816]["SampleCompositionTimeOffset_270"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[817]["SampleDuration_271"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[818]["SampleSize_271"] == 853:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[819]["SampleCompositionTimeOffset_271"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[820]["SampleDuration_272"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[821]["SampleSize_272"] == 806:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[822]["SampleCompositionTimeOffset_272"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[823]["SampleDuration_273"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[824]["SampleSize_273"] == 793:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[825]["SampleCompositionTimeOffset_273"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[826]["SampleDuration_274"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[827]["SampleSize_274"] == 809:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[828]["SampleCompositionTimeOffset_274"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[829]["SampleDuration_275"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[830]["SampleSize_275"] == 842:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[831]["SampleCompositionTimeOffset_275"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[832]["SampleDuration_276"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[833]["SampleSize_276"] == 860:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[834]["SampleCompositionTimeOffset_276"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[835]["SampleDuration_277"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[836]["SampleSize_277"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[837]["SampleCompositionTimeOffset_277"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[838]["SampleDuration_278"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[839]["SampleSize_278"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[840]["SampleCompositionTimeOffset_278"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[841]["SampleDuration_279"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[842]["SampleSize_279"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[843]["SampleCompositionTimeOffset_279"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[844]["SampleDuration_280"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[845]["SampleSize_280"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[846]["SampleCompositionTimeOffset_280"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[847]["SampleDuration_281"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[848]["SampleSize_281"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[849]["SampleCompositionTimeOffset_281"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[850]["SampleDuration_282"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[851]["SampleSize_282"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[852]["SampleCompositionTimeOffset_282"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[853]["SampleDuration_283"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[854]["SampleSize_283"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[855]["SampleCompositionTimeOffset_283"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[856]["SampleDuration_284"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[857]["SampleSize_284"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[858]["SampleCompositionTimeOffset_284"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[859]["SampleDuration_285"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[860]["SampleSize_285"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[861]["SampleCompositionTimeOffset_285"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[862]["SampleDuration_286"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[863]["SampleSize_286"] == 951:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[864]["SampleCompositionTimeOffset_286"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[865]["SampleDuration_287"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[866]["SampleSize_287"] == 856:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[867]["SampleCompositionTimeOffset_287"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[868]["SampleDuration_288"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[869]["SampleSize_288"] == 841:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[870]["SampleCompositionTimeOffset_288"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[871]["SampleDuration_289"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[872]["SampleSize_289"] == 935:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[873]["SampleCompositionTimeOffset_289"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[874]["SampleDuration_290"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[875]["SampleSize_290"] == 837:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[876]["SampleCompositionTimeOffset_290"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[877]["SampleDuration_291"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[878]["SampleSize_291"] == 914:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[879]["SampleCompositionTimeOffset_291"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[880]["SampleDuration_292"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[881]["SampleSize_292"] == 920:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[882]["SampleCompositionTimeOffset_292"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[883]["SampleDuration_293"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[884]["SampleSize_293"] == 883:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[885]["SampleCompositionTimeOffset_293"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[886]["SampleDuration_294"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[887]["SampleSize_294"] == 908:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[888]["SampleCompositionTimeOffset_294"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[889]["SampleDuration_295"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[890]["SampleSize_295"] == 877:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[891]["SampleCompositionTimeOffset_295"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[892]["SampleDuration_296"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[893]["SampleSize_296"] == 1085:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[894]["SampleCompositionTimeOffset_296"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[895]["SampleDuration_297"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[896]["SampleSize_297"] == 931:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[897]["SampleCompositionTimeOffset_297"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[898]["SampleDuration_298"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[899]["SampleSize_298"] == 891:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[900]["SampleCompositionTimeOffset_298"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[901]["SampleDuration_299"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[902]["SampleSize_299"] == 900:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[903]["SampleCompositionTimeOffset_299"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[904]["SampleDuration_300"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[905]["SampleSize_300"] == 917:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[906]["SampleCompositionTimeOffset_300"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[907]["SampleDuration_301"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[908]["SampleSize_301"] == 909:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[909]["SampleCompositionTimeOffset_301"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[910]["SampleDuration_302"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[911]["SampleSize_302"] == 907:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[912]["SampleCompositionTimeOffset_302"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[913]["SampleDuration_303"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[914]["SampleSize_303"] == 907:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[915]["SampleCompositionTimeOffset_303"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[916]["SampleDuration_304"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[917]["SampleSize_304"] == 897:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[918]["SampleCompositionTimeOffset_304"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[919]["SampleDuration_305"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[920]["SampleSize_305"] == 919:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[921]["SampleCompositionTimeOffset_305"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[922]["SampleDuration_306"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[923]["SampleSize_306"] == 917:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[924]["SampleCompositionTimeOffset_306"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[925]["SampleDuration_307"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[926]["SampleSize_307"] == 907:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[927]["SampleCompositionTimeOffset_307"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[928]["SampleDuration_308"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[929]["SampleSize_308"] == 903:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[930]["SampleCompositionTimeOffset_308"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[931]["SampleDuration_309"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[932]["SampleSize_309"] == 891:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[933]["SampleCompositionTimeOffset_309"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[934]["SampleDuration_310"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[935]["SampleSize_310"] == 881:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[936]["SampleCompositionTimeOffset_310"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[937]["SampleDuration_311"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[938]["SampleSize_311"] == 874:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[939]["SampleCompositionTimeOffset_311"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[940]["SampleDuration_312"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[941]["SampleSize_312"] == 878:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[942]["SampleCompositionTimeOffset_312"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[943]["SampleDuration_313"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[944]["SampleSize_313"] == 867:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[945]["SampleCompositionTimeOffset_313"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[946]["SampleDuration_314"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[947]["SampleSize_314"] == 859:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[948]["SampleCompositionTimeOffset_314"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[949]["SampleDuration_315"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[950]["SampleSize_315"] == 891:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[951]["SampleCompositionTimeOffset_315"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[952]["SampleDuration_316"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[953]["SampleSize_316"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[954]["SampleCompositionTimeOffset_316"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[955]["SampleDuration_317"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[956]["SampleSize_317"] == 867:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[957]["SampleCompositionTimeOffset_317"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[958]["SampleDuration_318"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[959]["SampleSize_318"] == 797:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[960]["SampleCompositionTimeOffset_318"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[961]["SampleDuration_319"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[962]["SampleSize_319"] == 791:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[963]["SampleCompositionTimeOffset_319"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[964]["SampleDuration_320"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[965]["SampleSize_320"] == 802:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[966]["SampleCompositionTimeOffset_320"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[967]["SampleDuration_321"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[968]["SampleSize_321"] == 815:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[969]["SampleCompositionTimeOffset_321"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[970]["SampleDuration_322"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[971]["SampleSize_322"] == 1138:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[972]["SampleCompositionTimeOffset_322"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[973]["SampleDuration_323"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[974]["SampleSize_323"] == 903:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[975]["SampleCompositionTimeOffset_323"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[976]["SampleDuration_324"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[977]["SampleSize_324"] == 870:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[978]["SampleCompositionTimeOffset_324"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[979]["SampleDuration_325"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[980]["SampleSize_325"] == 863:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[981]["SampleCompositionTimeOffset_325"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[982]["SampleDuration_326"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[983]["SampleSize_326"] == 859:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[984]["SampleCompositionTimeOffset_326"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[985]["SampleDuration_327"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[986]["SampleSize_327"] == 877:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[987]["SampleCompositionTimeOffset_327"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[988]["SampleDuration_328"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[989]["SampleSize_328"] == 885:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[990]["SampleCompositionTimeOffset_328"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[991]["SampleDuration_329"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[992]["SampleSize_329"] == 876:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[993]["SampleCompositionTimeOffset_329"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[994]["SampleDuration_330"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[995]["SampleSize_330"] == 873:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[996]["SampleCompositionTimeOffset_330"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[997]["SampleDuration_331"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[998]["SampleSize_331"] == 873:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[999]["SampleCompositionTimeOffset_331"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1000]["SampleDuration_332"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1001]["SampleSize_332"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1002]["SampleCompositionTimeOffset_332"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1003]["SampleDuration_333"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1004]["SampleSize_333"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1005]["SampleCompositionTimeOffset_333"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1006]["SampleDuration_334"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1007]["SampleSize_334"] == 871:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1008]["SampleCompositionTimeOffset_334"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1009]["SampleDuration_335"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1010]["SampleSize_335"] == 870:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1011]["SampleCompositionTimeOffset_335"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1012]["SampleDuration_336"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1013]["SampleSize_336"] == 868:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1014]["SampleCompositionTimeOffset_336"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1015]["SampleDuration_337"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1016]["SampleSize_337"] == 866:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1017]["SampleCompositionTimeOffset_337"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1018]["SampleDuration_338"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1019]["SampleSize_338"] == 865:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1020]["SampleCompositionTimeOffset_338"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1021]["SampleDuration_339"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1022]["SampleSize_339"] == 865:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1023]["SampleCompositionTimeOffset_339"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1024]["SampleDuration_340"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1025]["SampleSize_340"] == 862:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1026]["SampleCompositionTimeOffset_340"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1027]["SampleDuration_341"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1028]["SampleSize_341"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1029]["SampleCompositionTimeOffset_341"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1030]["SampleDuration_342"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1031]["SampleSize_342"] == 904:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1032]["SampleCompositionTimeOffset_342"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1033]["SampleDuration_343"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1034]["SampleSize_343"] == 879:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1035]["SampleCompositionTimeOffset_343"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1036]["SampleDuration_344"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1037]["SampleSize_344"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1038]["SampleCompositionTimeOffset_344"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1039]["SampleDuration_345"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1040]["SampleSize_345"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1041]["SampleCompositionTimeOffset_345"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1042]["SampleDuration_346"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1043]["SampleSize_346"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1044]["SampleCompositionTimeOffset_346"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1045]["SampleDuration_347"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1046]["SampleSize_347"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1047]["SampleCompositionTimeOffset_347"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1048]["SampleDuration_348"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1049]["SampleSize_348"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1050]["SampleCompositionTimeOffset_348"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1051]["SampleDuration_349"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1052]["SampleSize_349"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1053]["SampleCompositionTimeOffset_349"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1054]["SampleDuration_350"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1055]["SampleSize_350"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1056]["SampleCompositionTimeOffset_350"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1057]["SampleDuration_351"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1058]["SampleSize_351"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1059]["SampleCompositionTimeOffset_351"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1060]["SampleDuration_352"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1061]["SampleSize_352"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1062]["SampleCompositionTimeOffset_352"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1063]["SampleDuration_353"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1064]["SampleSize_353"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1065]["SampleCompositionTimeOffset_353"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1066]["SampleDuration_354"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1067]["SampleSize_354"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1068]["SampleCompositionTimeOffset_354"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1069]["SampleDuration_355"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1070]["SampleSize_355"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1071]["SampleCompositionTimeOffset_355"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1072]["SampleDuration_356"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1073]["SampleSize_356"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1074]["SampleCompositionTimeOffset_356"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1075]["SampleDuration_357"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1076]["SampleSize_357"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1077]["SampleCompositionTimeOffset_357"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1078]["SampleDuration_358"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1079]["SampleSize_358"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1080]["SampleCompositionTimeOffset_358"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1081]["SampleDuration_359"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1082]["SampleSize_359"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1083]["SampleCompositionTimeOffset_359"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1084]["SampleDuration_360"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1085]["SampleSize_360"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1086]["SampleCompositionTimeOffset_360"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1087]["SampleDuration_361"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1088]["SampleSize_361"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1089]["SampleCompositionTimeOffset_361"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1090]["SampleDuration_362"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1091]["SampleSize_362"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1092]["SampleCompositionTimeOffset_362"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1093]["SampleDuration_363"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1094]["SampleSize_363"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1095]["SampleCompositionTimeOffset_363"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1096]["SampleDuration_364"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1097]["SampleSize_364"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1098]["SampleCompositionTimeOffset_364"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1099]["SampleDuration_365"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1100]["SampleSize_365"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1101]["SampleCompositionTimeOffset_365"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1102]["SampleDuration_366"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1103]["SampleSize_366"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1104]["SampleCompositionTimeOffset_366"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1105]["SampleDuration_367"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1106]["SampleSize_367"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1107]["SampleCompositionTimeOffset_367"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1108]["SampleDuration_368"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1109]["SampleSize_368"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1110]["SampleCompositionTimeOffset_368"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1111]["SampleDuration_369"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1112]["SampleSize_369"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1113]["SampleCompositionTimeOffset_369"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1114]["SampleDuration_370"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1115]["SampleSize_370"] == 869:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1116]["SampleCompositionTimeOffset_370"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1117]["SampleDuration_371"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1118]["SampleSize_371"] == 875:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1119]["SampleCompositionTimeOffset_371"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1120]["SampleDuration_372"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1121]["SampleSize_372"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1122]["SampleCompositionTimeOffset_372"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1123]["SampleDuration_373"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1124]["SampleSize_373"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1125]["SampleCompositionTimeOffset_373"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1126]["SampleDuration_374"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1127]["SampleSize_374"] == 847:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1128]["SampleCompositionTimeOffset_374"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1129]["SampleDuration_375"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1130]["SampleSize_375"] == 838:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1131]["SampleCompositionTimeOffset_375"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1132]["SampleDuration_376"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1133]["SampleSize_376"] == 834:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1134]["SampleCompositionTimeOffset_376"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1135]["SampleDuration_377"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1136]["SampleSize_377"] == 857:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1137]["SampleCompositionTimeOffset_377"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1138]["SampleDuration_378"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1139]["SampleSize_378"] == 973:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1140]["SampleCompositionTimeOffset_378"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1141]["SampleDuration_379"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1142]["SampleSize_379"] == 867:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1143]["SampleCompositionTimeOffset_379"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1144]["SampleDuration_380"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1145]["SampleSize_380"] == 855:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1146]["SampleCompositionTimeOffset_380"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1147]["SampleDuration_381"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1148]["SampleSize_381"] == 868:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1149]["SampleCompositionTimeOffset_381"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1150]["SampleDuration_382"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1151]["SampleSize_382"] == 883:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1152]["SampleCompositionTimeOffset_382"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1153]["SampleDuration_383"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1154]["SampleSize_383"] == 878:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1155]["SampleCompositionTimeOffset_383"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1156]["SampleDuration_384"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1157]["SampleSize_384"] == 879:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1158]["SampleCompositionTimeOffset_384"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1159]["SampleDuration_385"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1160]["SampleSize_385"] == 874:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1161]["SampleCompositionTimeOffset_385"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1162]["SampleDuration_386"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1163]["SampleSize_386"] == 871:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1164]["SampleCompositionTimeOffset_386"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1165]["SampleDuration_387"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1166]["SampleSize_387"] == 864:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1167]["SampleCompositionTimeOffset_387"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1168]["SampleDuration_388"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1169]["SampleSize_388"] == 856:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1170]["SampleCompositionTimeOffset_388"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1171]["SampleDuration_389"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1172]["SampleSize_389"] == 842:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1173]["SampleCompositionTimeOffset_389"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1174]["SampleDuration_390"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1175]["SampleSize_390"] == 851:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1176]["SampleCompositionTimeOffset_390"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1177]["SampleDuration_391"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1178]["SampleSize_391"] == 847:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1179]["SampleCompositionTimeOffset_391"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1180]["SampleDuration_392"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1181]["SampleSize_392"] == 844:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1182]["SampleCompositionTimeOffset_392"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1183]["SampleDuration_393"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1184]["SampleSize_393"] == 843:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1185]["SampleCompositionTimeOffset_393"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1186]["SampleDuration_394"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1187]["SampleSize_394"] == 831:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1188]["SampleCompositionTimeOffset_394"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1189]["SampleDuration_395"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1190]["SampleSize_395"] == 1095:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1191]["SampleCompositionTimeOffset_395"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1192]["SampleDuration_396"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1193]["SampleSize_396"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1194]["SampleCompositionTimeOffset_396"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1195]["SampleDuration_397"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1196]["SampleSize_397"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1197]["SampleCompositionTimeOffset_397"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1198]["SampleDuration_398"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1199]["SampleSize_398"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1200]["SampleCompositionTimeOffset_398"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1201]["SampleDuration_399"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1202]["SampleSize_399"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1203]["SampleCompositionTimeOffset_399"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1204]["SampleDuration_400"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1205]["SampleSize_400"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1206]["SampleCompositionTimeOffset_400"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1207]["SampleDuration_401"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1208]["SampleSize_401"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1209]["SampleCompositionTimeOffset_401"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1210]["SampleDuration_402"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1211]["SampleSize_402"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1212]["SampleCompositionTimeOffset_402"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1213]["SampleDuration_403"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1214]["SampleSize_403"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1215]["SampleCompositionTimeOffset_403"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1216]["SampleDuration_404"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1217]["SampleSize_404"] == 866:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1218]["SampleCompositionTimeOffset_404"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1219]["SampleDuration_405"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1220]["SampleSize_405"] == 853:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1221]["SampleCompositionTimeOffset_405"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1222]["SampleDuration_406"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1223]["SampleSize_406"] == 814:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1224]["SampleCompositionTimeOffset_406"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1225]["SampleDuration_407"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1226]["SampleSize_407"] == 810:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1227]["SampleCompositionTimeOffset_407"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1228]["SampleDuration_408"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1229]["SampleSize_408"] == 796:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1230]["SampleCompositionTimeOffset_408"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1231]["SampleDuration_409"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1232]["SampleSize_409"] == 762:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1233]["SampleCompositionTimeOffset_409"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1234]["SampleDuration_410"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1235]["SampleSize_410"] == 757:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1236]["SampleCompositionTimeOffset_410"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1237]["SampleDuration_411"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1238]["SampleSize_411"] == 764:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1239]["SampleCompositionTimeOffset_411"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1240]["SampleDuration_412"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1241]["SampleSize_412"] == 775:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1242]["SampleCompositionTimeOffset_412"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1243]["SampleDuration_413"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1244]["SampleSize_413"] == 813:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1245]["SampleCompositionTimeOffset_413"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1246]["SampleDuration_414"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1247]["SampleSize_414"] == 788:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1248]["SampleCompositionTimeOffset_414"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1249]["SampleDuration_415"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1250]["SampleSize_415"] == 844:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1251]["SampleCompositionTimeOffset_415"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1252]["SampleDuration_416"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1253]["SampleSize_416"] == 857:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1254]["SampleCompositionTimeOffset_416"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1255]["SampleDuration_417"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1256]["SampleSize_417"] == 869:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1257]["SampleCompositionTimeOffset_417"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1258]["SampleDuration_418"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1259]["SampleSize_418"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1260]["SampleCompositionTimeOffset_418"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1261]["SampleDuration_419"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1262]["SampleSize_419"] == 873:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1263]["SampleCompositionTimeOffset_419"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1264]["SampleDuration_420"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1265]["SampleSize_420"] == 871:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1266]["SampleCompositionTimeOffset_420"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1267]["SampleDuration_421"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1268]["SampleSize_421"] == 1078:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1269]["SampleCompositionTimeOffset_421"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1270]["SampleDuration_422"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1271]["SampleSize_422"] == 848:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1272]["SampleCompositionTimeOffset_422"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1273]["SampleDuration_423"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1274]["SampleSize_423"] == 827:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1275]["SampleCompositionTimeOffset_423"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1276]["SampleDuration_424"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1277]["SampleSize_424"] == 812:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1278]["SampleCompositionTimeOffset_424"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1279]["SampleDuration_425"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1280]["SampleSize_425"] == 810:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1281]["SampleCompositionTimeOffset_425"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1282]["SampleDuration_426"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1283]["SampleSize_426"] == 863:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1284]["SampleCompositionTimeOffset_426"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1285]["SampleDuration_427"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1286]["SampleSize_427"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1287]["SampleCompositionTimeOffset_427"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1288]["SampleDuration_428"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1289]["SampleSize_428"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1290]["SampleCompositionTimeOffset_428"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1291]["SampleDuration_429"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1292]["SampleSize_429"] == 1078:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1293]["SampleCompositionTimeOffset_429"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1294]["SampleDuration_430"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1295]["SampleSize_430"] == 803:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1296]["SampleCompositionTimeOffset_430"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1297]["SampleDuration_431"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1298]["SampleSize_431"] == 1075:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1299]["SampleCompositionTimeOffset_431"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1300]["SampleDuration_432"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1301]["SampleSize_432"] == 853:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1302]["SampleCompositionTimeOffset_432"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1303]["SampleDuration_433"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1304]["SampleSize_433"] == 883:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1305]["SampleCompositionTimeOffset_433"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1306]["SampleDuration_434"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1307]["SampleSize_434"] == 922:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1308]["SampleCompositionTimeOffset_434"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1309]["SampleDuration_435"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1310]["SampleSize_435"] == 974:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1311]["SampleCompositionTimeOffset_435"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1312]["SampleDuration_436"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1313]["SampleSize_436"] == 962:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1314]["SampleCompositionTimeOffset_436"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1315]["SampleDuration_437"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1316]["SampleSize_437"] == 932:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1317]["SampleCompositionTimeOffset_437"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1318]["SampleDuration_438"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1319]["SampleSize_438"] == 922:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1320]["SampleCompositionTimeOffset_438"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1321]["SampleDuration_439"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1322]["SampleSize_439"] == 908:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1323]["SampleCompositionTimeOffset_439"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1324]["SampleDuration_440"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1325]["SampleSize_440"] == 899:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1326]["SampleCompositionTimeOffset_440"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1327]["SampleDuration_441"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1328]["SampleSize_441"] == 892:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1329]["SampleCompositionTimeOffset_441"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1330]["SampleDuration_442"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1331]["SampleSize_442"] == 898:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1332]["SampleCompositionTimeOffset_442"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1333]["SampleDuration_443"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1334]["SampleSize_443"] == 901:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1335]["SampleCompositionTimeOffset_443"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1336]["SampleDuration_444"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1337]["SampleSize_444"] == 893:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1338]["SampleCompositionTimeOffset_444"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1339]["SampleDuration_445"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1340]["SampleSize_445"] == 882:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1341]["SampleCompositionTimeOffset_445"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1342]["SampleDuration_446"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1343]["SampleSize_446"] == 879:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1344]["SampleCompositionTimeOffset_446"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1345]["SampleDuration_447"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1346]["SampleSize_447"] == 869:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1347]["SampleCompositionTimeOffset_447"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1348]["SampleDuration_448"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1349]["SampleSize_448"] == 864:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1350]["SampleCompositionTimeOffset_448"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1351]["SampleDuration_449"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1352]["SampleSize_449"] == 855:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1353]["SampleCompositionTimeOffset_449"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1354]["SampleDuration_450"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1355]["SampleSize_450"] == 839:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1356]["SampleCompositionTimeOffset_450"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1357]["SampleDuration_451"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1358]["SampleSize_451"] == 816:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1359]["SampleCompositionTimeOffset_451"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1360]["SampleDuration_452"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1361]["SampleSize_452"] == 797:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1362]["SampleCompositionTimeOffset_452"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1363]["SampleDuration_453"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1364]["SampleSize_453"] == 775:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1365]["SampleCompositionTimeOffset_453"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1366]["SampleDuration_454"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1367]["SampleSize_454"] == 742:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1368]["SampleCompositionTimeOffset_454"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1369]["SampleDuration_455"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1370]["SampleSize_455"] == 736:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1371]["SampleCompositionTimeOffset_455"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1372]["SampleDuration_456"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1373]["SampleSize_456"] == 743:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1374]["SampleCompositionTimeOffset_456"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1375]["SampleDuration_457"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1376]["SampleSize_457"] == 775:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1377]["SampleCompositionTimeOffset_457"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1378]["SampleDuration_458"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1379]["SampleSize_458"] == 1094:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1380]["SampleCompositionTimeOffset_458"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1381]["SampleDuration_459"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1382]["SampleSize_459"] == 831:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1383]["SampleCompositionTimeOffset_459"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1384]["SampleDuration_460"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1385]["SampleSize_460"] == 799:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1386]["SampleCompositionTimeOffset_460"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1387]["SampleDuration_461"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1388]["SampleSize_461"] == 801:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1389]["SampleCompositionTimeOffset_461"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1390]["SampleDuration_462"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1391]["SampleSize_462"] == 827:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1392]["SampleCompositionTimeOffset_462"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1393]["SampleDuration_463"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1394]["SampleSize_463"] == 853:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1395]["SampleCompositionTimeOffset_463"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1396]["SampleDuration_464"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1397]["SampleSize_464"] == 892:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1398]["SampleCompositionTimeOffset_464"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1399]["SampleDuration_465"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1400]["SampleSize_465"] == 863:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1401]["SampleCompositionTimeOffset_465"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1402]["SampleDuration_466"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1403]["SampleSize_466"] == 1159:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1404]["SampleCompositionTimeOffset_466"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1405]["SampleDuration_467"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1406]["SampleSize_467"] == 996:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1407]["SampleCompositionTimeOffset_467"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1408]["SampleDuration_468"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1409]["SampleSize_468"] == 973:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1410]["SampleCompositionTimeOffset_468"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1411]["SampleDuration_469"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1412]["SampleSize_469"] == 887:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1413]["SampleCompositionTimeOffset_469"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1414]["SampleDuration_470"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1415]["SampleSize_470"] == 952:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1416]["SampleCompositionTimeOffset_470"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1417]["SampleDuration_471"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1418]["SampleSize_471"] == 978:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1419]["SampleCompositionTimeOffset_471"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1420]["SampleDuration_472"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1421]["SampleSize_472"] == 971:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1422]["SampleCompositionTimeOffset_472"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1423]["SampleDuration_473"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1424]["SampleSize_473"] == 925:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1425]["SampleCompositionTimeOffset_473"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1426]["SampleDuration_474"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1427]["SampleSize_474"] == 878:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1428]["SampleCompositionTimeOffset_474"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1429]["SampleDuration_475"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1430]["SampleSize_475"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1431]["SampleCompositionTimeOffset_475"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1432]["SampleDuration_476"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1433]["SampleSize_476"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1434]["SampleCompositionTimeOffset_476"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1435]["SampleDuration_477"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1436]["SampleSize_477"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1437]["SampleCompositionTimeOffset_477"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1438]["SampleDuration_478"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1439]["SampleSize_478"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1440]["SampleCompositionTimeOffset_478"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1441]["SampleDuration_479"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1442]["SampleSize_479"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1443]["SampleCompositionTimeOffset_479"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1444]["SampleDuration_480"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1445]["SampleSize_480"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1446]["SampleCompositionTimeOffset_480"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1447]["SampleDuration_481"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1448]["SampleSize_481"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1449]["SampleCompositionTimeOffset_481"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1450]["SampleDuration_482"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1451]["SampleSize_482"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1452]["SampleCompositionTimeOffset_482"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1453]["SampleDuration_483"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1454]["SampleSize_483"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1455]["SampleCompositionTimeOffset_483"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1456]["SampleDuration_484"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1457]["SampleSize_484"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1458]["SampleCompositionTimeOffset_484"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1459]["SampleDuration_485"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1460]["SampleSize_485"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1461]["SampleCompositionTimeOffset_485"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1462]["SampleDuration_486"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1463]["SampleSize_486"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1464]["SampleCompositionTimeOffset_486"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1465]["SampleDuration_487"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1466]["SampleSize_487"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1467]["SampleCompositionTimeOffset_487"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1468]["SampleDuration_488"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1469]["SampleSize_488"] == 871:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1470]["SampleCompositionTimeOffset_488"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1471]["SampleDuration_489"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1472]["SampleSize_489"] == 869:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1473]["SampleCompositionTimeOffset_489"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1474]["SampleDuration_490"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1475]["SampleSize_490"] == 868:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1476]["SampleCompositionTimeOffset_490"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1477]["SampleDuration_491"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1478]["SampleSize_491"] == 864:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1479]["SampleCompositionTimeOffset_491"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1480]["SampleDuration_492"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1481]["SampleSize_492"] == 857:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1482]["SampleCompositionTimeOffset_492"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1483]["SampleDuration_493"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1484]["SampleSize_493"] == 905:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1485]["SampleCompositionTimeOffset_493"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1486]["SampleDuration_494"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1487]["SampleSize_494"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1488]["SampleCompositionTimeOffset_494"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1489]["SampleDuration_495"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1490]["SampleSize_495"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1491]["SampleCompositionTimeOffset_495"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1492]["SampleDuration_496"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1493]["SampleSize_496"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1494]["SampleCompositionTimeOffset_496"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1495]["SampleDuration_497"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1496]["SampleSize_497"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1497]["SampleCompositionTimeOffset_497"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1498]["SampleDuration_498"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1499]["SampleSize_498"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1500]["SampleCompositionTimeOffset_498"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1501]["SampleDuration_499"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1502]["SampleSize_499"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1503]["SampleCompositionTimeOffset_499"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1504]["SampleDuration_500"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1505]["SampleSize_500"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1506]["SampleCompositionTimeOffset_500"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1507]["SampleDuration_501"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1508]["SampleSize_501"] == 871:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1509]["SampleCompositionTimeOffset_501"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1510]["SampleDuration_502"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1511]["SampleSize_502"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1512]["SampleCompositionTimeOffset_502"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1513]["SampleDuration_503"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1514]["SampleSize_503"] == 873:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1515]["SampleCompositionTimeOffset_503"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1516]["SampleDuration_504"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1517]["SampleSize_504"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1518]["SampleCompositionTimeOffset_504"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1519]["SampleDuration_505"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1520]["SampleSize_505"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1521]["SampleCompositionTimeOffset_505"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1522]["SampleDuration_506"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1523]["SampleSize_506"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1524]["SampleCompositionTimeOffset_506"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1525]["SampleDuration_507"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1526]["SampleSize_507"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1527]["SampleCompositionTimeOffset_507"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1528]["SampleDuration_508"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1529]["SampleSize_508"] == 871:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1530]["SampleCompositionTimeOffset_508"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1531]["SampleDuration_509"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1532]["SampleSize_509"] == 870:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1533]["SampleCompositionTimeOffset_509"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1534]["SampleDuration_510"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1535]["SampleSize_510"] == 869:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1536]["SampleCompositionTimeOffset_510"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1537]["SampleDuration_511"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1538]["SampleSize_511"] == 878:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1539]["SampleCompositionTimeOffset_511"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1540]["SampleDuration_512"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1541]["SampleSize_512"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1542]["SampleCompositionTimeOffset_512"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1543]["SampleDuration_513"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1544]["SampleSize_513"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1545]["SampleCompositionTimeOffset_513"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1546]["SampleDuration_514"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1547]["SampleSize_514"] == 866:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1548]["SampleCompositionTimeOffset_514"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1549]["SampleDuration_515"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1550]["SampleSize_515"] == 864:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1551]["SampleCompositionTimeOffset_515"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1552]["SampleDuration_516"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1553]["SampleSize_516"] == 864:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1554]["SampleCompositionTimeOffset_516"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1555]["SampleDuration_517"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1556]["SampleSize_517"] == 873:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1557]["SampleCompositionTimeOffset_517"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1558]["SampleDuration_518"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1559]["SampleSize_518"] == 863:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1560]["SampleCompositionTimeOffset_518"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1561]["SampleDuration_519"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1562]["SampleSize_519"] == 904:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1563]["SampleCompositionTimeOffset_519"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1564]["SampleDuration_520"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1565]["SampleSize_520"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1566]["SampleCompositionTimeOffset_520"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1567]["SampleDuration_521"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1568]["SampleSize_521"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1569]["SampleCompositionTimeOffset_521"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1570]["SampleDuration_522"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1571]["SampleSize_522"] == 860:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1572]["SampleCompositionTimeOffset_522"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1573]["SampleDuration_523"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1574]["SampleSize_523"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1575]["SampleCompositionTimeOffset_523"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1576]["SampleDuration_524"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1577]["SampleSize_524"] == 880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1578]["SampleCompositionTimeOffset_524"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1579]["SampleDuration_525"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1580]["SampleSize_525"] == 874:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1581]["SampleCompositionTimeOffset_525"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1582]["SampleDuration_526"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1583]["SampleSize_526"] == 874:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1584]["SampleCompositionTimeOffset_526"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1585]["SampleDuration_527"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1586]["SampleSize_527"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1587]["SampleCompositionTimeOffset_527"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1588]["SampleDuration_528"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1589]["SampleSize_528"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1590]["SampleCompositionTimeOffset_528"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1591]["SampleDuration_529"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1592]["SampleSize_529"] == 871:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1593]["SampleCompositionTimeOffset_529"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1594]["SampleDuration_530"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1595]["SampleSize_530"] == 866:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1596]["SampleCompositionTimeOffset_530"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1597]["SampleDuration_531"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1598]["SampleSize_531"] == 858:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1599]["SampleCompositionTimeOffset_531"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1600]["SampleDuration_532"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1601]["SampleSize_532"] == 857:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1602]["SampleCompositionTimeOffset_532"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1603]["SampleDuration_533"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1604]["SampleSize_533"] == 852:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1605]["SampleCompositionTimeOffset_533"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1606]["SampleDuration_534"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1607]["SampleSize_534"] == 849:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1608]["SampleCompositionTimeOffset_534"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1609]["SampleDuration_535"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1610]["SampleSize_535"] == 844:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1611]["SampleCompositionTimeOffset_535"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1612]["SampleDuration_536"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1613]["SampleSize_536"] == 845:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1614]["SampleCompositionTimeOffset_536"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1615]["SampleDuration_537"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1616]["SampleSize_537"] == 1010:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1617]["SampleCompositionTimeOffset_537"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1618]["SampleDuration_538"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1619]["SampleSize_538"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1620]["SampleCompositionTimeOffset_538"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1621]["SampleDuration_539"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1622]["SampleSize_539"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1623]["SampleCompositionTimeOffset_539"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1624]["SampleDuration_540"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1625]["SampleSize_540"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1626]["SampleCompositionTimeOffset_540"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1627]["SampleDuration_541"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1628]["SampleSize_541"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1629]["SampleCompositionTimeOffset_541"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1630]["SampleDuration_542"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1631]["SampleSize_542"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1632]["SampleCompositionTimeOffset_542"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1633]["SampleDuration_543"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1634]["SampleSize_543"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1635]["SampleCompositionTimeOffset_543"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1636]["SampleDuration_544"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1637]["SampleSize_544"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1638]["SampleCompositionTimeOffset_544"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1639]["SampleDuration_545"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1640]["SampleSize_545"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1641]["SampleCompositionTimeOffset_545"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1642]["SampleDuration_546"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1643]["SampleSize_546"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1644]["SampleCompositionTimeOffset_546"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1645]["SampleDuration_547"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1646]["SampleSize_547"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1647]["SampleCompositionTimeOffset_547"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1648]["SampleDuration_548"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1649]["SampleSize_548"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1650]["SampleCompositionTimeOffset_548"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1651]["SampleDuration_549"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1652]["SampleSize_549"] == 871:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1653]["SampleCompositionTimeOffset_549"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1654]["SampleDuration_550"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1655]["SampleSize_550"] == 840:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1656]["SampleCompositionTimeOffset_550"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1657]["SampleDuration_551"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1658]["SampleSize_551"] == 765:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1659]["SampleCompositionTimeOffset_551"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1660]["SampleDuration_552"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1661]["SampleSize_552"] == 741:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1662]["SampleCompositionTimeOffset_552"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1663]["SampleDuration_553"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1664]["SampleSize_553"] == 724:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1665]["SampleCompositionTimeOffset_553"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1666]["SampleDuration_554"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1667]["SampleSize_554"] == 709:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1668]["SampleCompositionTimeOffset_554"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1669]["SampleDuration_555"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1670]["SampleSize_555"] == 720:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1671]["SampleCompositionTimeOffset_555"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1672]["SampleDuration_556"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1673]["SampleSize_556"] == 790:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1674]["SampleCompositionTimeOffset_556"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1675]["SampleDuration_557"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1676]["SampleSize_557"] == 883:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1677]["SampleCompositionTimeOffset_557"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1678]["SampleDuration_558"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1679]["SampleSize_558"] == 839:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1680]["SampleCompositionTimeOffset_558"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1681]["SampleDuration_559"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1682]["SampleSize_559"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1683]["SampleCompositionTimeOffset_559"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1684]["SampleDuration_560"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1685]["SampleSize_560"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1686]["SampleCompositionTimeOffset_560"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1687]["SampleDuration_561"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1688]["SampleSize_561"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1689]["SampleCompositionTimeOffset_561"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1690]["SampleDuration_562"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1691]["SampleSize_562"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1692]["SampleCompositionTimeOffset_562"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1693]["SampleDuration_563"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1694]["SampleSize_563"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1695]["SampleCompositionTimeOffset_563"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1696]["SampleDuration_564"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1697]["SampleSize_564"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1698]["SampleCompositionTimeOffset_564"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1699]["SampleDuration_565"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1700]["SampleSize_565"] == 938:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1701]["SampleCompositionTimeOffset_565"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1702]["SampleDuration_566"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1703]["SampleSize_566"] == 915:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1704]["SampleCompositionTimeOffset_566"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1705]["SampleDuration_567"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1706]["SampleSize_567"] == 937:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1707]["SampleCompositionTimeOffset_567"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1708]["SampleDuration_568"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1709]["SampleSize_568"] == 922:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1710]["SampleCompositionTimeOffset_568"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1711]["SampleDuration_569"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1712]["SampleSize_569"] == 1018:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1713]["SampleCompositionTimeOffset_569"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1714]["SampleDuration_570"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1715]["SampleSize_570"] == 887:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1716]["SampleCompositionTimeOffset_570"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1717]["SampleDuration_571"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1718]["SampleSize_571"] == 749:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1719]["SampleCompositionTimeOffset_571"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1720]["SampleDuration_572"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1721]["SampleSize_572"] == 658:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1722]["SampleCompositionTimeOffset_572"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1723]["SampleDuration_573"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1724]["SampleSize_573"] == 848:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1725]["SampleCompositionTimeOffset_573"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1726]["SampleDuration_574"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1727]["SampleSize_574"] == 1142:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1728]["SampleCompositionTimeOffset_574"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1729]["SampleDuration_575"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1730]["SampleSize_575"] == 762:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1731]["SampleCompositionTimeOffset_575"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1732]["SampleDuration_576"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1733]["SampleSize_576"] == 829:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1734]["SampleCompositionTimeOffset_576"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1735]["SampleDuration_577"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1736]["SampleSize_577"] == 866:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1737]["SampleCompositionTimeOffset_577"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1738]["SampleDuration_578"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1739]["SampleSize_578"] == 983:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1740]["SampleCompositionTimeOffset_578"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1741]["SampleDuration_579"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1742]["SampleSize_579"] == 958:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1743]["SampleCompositionTimeOffset_579"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1744]["SampleDuration_580"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1745]["SampleSize_580"] == 987:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1746]["SampleCompositionTimeOffset_580"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1747]["SampleDuration_581"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1748]["SampleSize_581"] == 989:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1749]["SampleCompositionTimeOffset_581"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1750]["SampleDuration_582"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1751]["SampleSize_582"] == 962:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1752]["SampleCompositionTimeOffset_582"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1753]["SampleDuration_583"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1754]["SampleSize_583"] == 1032:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1755]["SampleCompositionTimeOffset_583"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1756]["SampleDuration_584"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1757]["SampleSize_584"] == 907:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1758]["SampleCompositionTimeOffset_584"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1759]["SampleDuration_585"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1760]["SampleSize_585"] == 892:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1761]["SampleCompositionTimeOffset_585"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1762]["SampleDuration_586"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1763]["SampleSize_586"] == 888:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1764]["SampleCompositionTimeOffset_586"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1765]["SampleDuration_587"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1766]["SampleSize_587"] == 888:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1767]["SampleCompositionTimeOffset_587"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1768]["SampleDuration_588"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1769]["SampleSize_588"] == 887:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1770]["SampleCompositionTimeOffset_588"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1771]["SampleDuration_589"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1772]["SampleSize_589"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1773]["SampleCompositionTimeOffset_589"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1774]["SampleDuration_590"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1775]["SampleSize_590"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1776]["SampleCompositionTimeOffset_590"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1777]["SampleDuration_591"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1778]["SampleSize_591"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1779]["SampleCompositionTimeOffset_591"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1780]["SampleDuration_592"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1781]["SampleSize_592"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1782]["SampleCompositionTimeOffset_592"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1783]["SampleDuration_593"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1784]["SampleSize_593"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1785]["SampleCompositionTimeOffset_593"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1786]["SampleDuration_594"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1787]["SampleSize_594"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1788]["SampleCompositionTimeOffset_594"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1789]["SampleDuration_595"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1790]["SampleSize_595"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1791]["SampleCompositionTimeOffset_595"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1792]["SampleDuration_596"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1793]["SampleSize_596"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1794]["SampleCompositionTimeOffset_596"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1795]["SampleDuration_597"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1796]["SampleSize_597"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1797]["SampleCompositionTimeOffset_597"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1798]["SampleDuration_598"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1799]["SampleSize_598"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1800]["SampleCompositionTimeOffset_598"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1801]["SampleDuration_599"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1802]["SampleSize_599"] == 870:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1803]["SampleCompositionTimeOffset_599"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1804]["SampleDuration_600"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1805]["SampleSize_600"] == 868:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1806]["SampleCompositionTimeOffset_600"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1807]["SampleDuration_601"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1808]["SampleSize_601"] == 861:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1809]["SampleCompositionTimeOffset_601"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1810]["SampleDuration_602"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1811]["SampleSize_602"] == 859:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1812]["SampleCompositionTimeOffset_602"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1813]["SampleDuration_603"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1814]["SampleSize_603"] == 849:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1815]["SampleCompositionTimeOffset_603"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1816]["SampleDuration_604"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1817]["SampleSize_604"] == 850:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1818]["SampleCompositionTimeOffset_604"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1819]["SampleDuration_605"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1820]["SampleSize_605"] == 840:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1821]["SampleCompositionTimeOffset_605"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1822]["SampleDuration_606"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1823]["SampleSize_606"] == 844:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1824]["SampleCompositionTimeOffset_606"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1825]["SampleDuration_607"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1826]["SampleSize_607"] == 841:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1827]["SampleCompositionTimeOffset_607"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1828]["SampleDuration_608"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1829]["SampleSize_608"] == 1014:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1830]["SampleCompositionTimeOffset_608"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1831]["SampleDuration_609"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1832]["SampleSize_609"] == 902:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1833]["SampleCompositionTimeOffset_609"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1834]["SampleDuration_610"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1835]["SampleSize_610"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1836]["SampleCompositionTimeOffset_610"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1837]["SampleDuration_611"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1838]["SampleSize_611"] == 871:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1839]["SampleCompositionTimeOffset_611"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1840]["SampleDuration_612"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1841]["SampleSize_612"] == 873:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1842]["SampleCompositionTimeOffset_612"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1843]["SampleDuration_613"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1844]["SampleSize_613"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1845]["SampleCompositionTimeOffset_613"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1846]["SampleDuration_614"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1847]["SampleSize_614"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1848]["SampleCompositionTimeOffset_614"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1849]["SampleDuration_615"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1850]["SampleSize_615"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1851]["SampleCompositionTimeOffset_615"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1852]["SampleDuration_616"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1853]["SampleSize_616"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1854]["SampleCompositionTimeOffset_616"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1855]["SampleDuration_617"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1856]["SampleSize_617"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1857]["SampleCompositionTimeOffset_617"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1858]["SampleDuration_618"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1859]["SampleSize_618"] == 865:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1860]["SampleCompositionTimeOffset_618"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1861]["SampleDuration_619"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1862]["SampleSize_619"] == 855:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1863]["SampleCompositionTimeOffset_619"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1864]["SampleDuration_620"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1865]["SampleSize_620"] == 791:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1866]["SampleCompositionTimeOffset_620"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1867]["SampleDuration_621"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1868]["SampleSize_621"] == 749:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1869]["SampleCompositionTimeOffset_621"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1870]["SampleDuration_622"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1871]["SampleSize_622"] == 731:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1872]["SampleCompositionTimeOffset_622"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1873]["SampleDuration_623"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1874]["SampleSize_623"] == 750:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1875]["SampleCompositionTimeOffset_623"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1876]["SampleDuration_624"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1877]["SampleSize_624"] == 761:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1878]["SampleCompositionTimeOffset_624"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1879]["SampleDuration_625"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1880]["SampleSize_625"] == 769:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1881]["SampleCompositionTimeOffset_625"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1882]["SampleDuration_626"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1883]["SampleSize_626"] == 1055:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1884]["SampleCompositionTimeOffset_626"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1885]["SampleDuration_627"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1886]["SampleSize_627"] == 888:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1887]["SampleCompositionTimeOffset_627"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1888]["SampleDuration_628"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1889]["SampleSize_628"] == 811:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1890]["SampleCompositionTimeOffset_628"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1891]["SampleDuration_629"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1892]["SampleSize_629"] == 775:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1893]["SampleCompositionTimeOffset_629"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1894]["SampleDuration_630"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1895]["SampleSize_630"] == 1161:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1896]["SampleCompositionTimeOffset_630"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1897]["SampleDuration_631"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1898]["SampleSize_631"] == 811:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1899]["SampleCompositionTimeOffset_631"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1900]["SampleDuration_632"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1901]["SampleSize_632"] == 801:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1902]["SampleCompositionTimeOffset_632"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1903]["SampleDuration_633"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1904]["SampleSize_633"] == 797:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1905]["SampleCompositionTimeOffset_633"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1906]["SampleDuration_634"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1907]["SampleSize_634"] == 801:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1908]["SampleCompositionTimeOffset_634"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1909]["SampleDuration_635"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1910]["SampleSize_635"] == 823:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1911]["SampleCompositionTimeOffset_635"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1912]["SampleDuration_636"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1913]["SampleSize_636"] == 1085:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1914]["SampleCompositionTimeOffset_636"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1915]["SampleDuration_637"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1916]["SampleSize_637"] == 914:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1917]["SampleCompositionTimeOffset_637"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1918]["SampleDuration_638"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1919]["SampleSize_638"] == 898:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1920]["SampleCompositionTimeOffset_638"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1921]["SampleDuration_639"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1922]["SampleSize_639"] == 873:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1923]["SampleCompositionTimeOffset_639"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1924]["SampleDuration_640"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1925]["SampleSize_640"] == 882:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1926]["SampleCompositionTimeOffset_640"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1927]["SampleDuration_641"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1928]["SampleSize_641"] == 894:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1929]["SampleCompositionTimeOffset_641"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1930]["SampleDuration_642"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1931]["SampleSize_642"] == 899:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1932]["SampleCompositionTimeOffset_642"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1933]["SampleDuration_643"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1934]["SampleSize_643"] == 939:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1935]["SampleCompositionTimeOffset_643"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1936]["SampleDuration_644"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1937]["SampleSize_644"] == 989:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1938]["SampleCompositionTimeOffset_644"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1939]["SampleDuration_645"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1940]["SampleSize_645"] == 936:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1941]["SampleCompositionTimeOffset_645"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1942]["SampleDuration_646"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1943]["SampleSize_646"] == 899:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1944]["SampleCompositionTimeOffset_646"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1945]["SampleDuration_647"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1946]["SampleSize_647"] == 883:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1947]["SampleCompositionTimeOffset_647"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1948]["SampleDuration_648"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1949]["SampleSize_648"] == 891:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1950]["SampleCompositionTimeOffset_648"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1951]["SampleDuration_649"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1952]["SampleSize_649"] == 939:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1953]["SampleCompositionTimeOffset_649"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1954]["SampleDuration_650"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1955]["SampleSize_650"] == 894:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1956]["SampleCompositionTimeOffset_650"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1957]["SampleDuration_651"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1958]["SampleSize_651"] == 886:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1959]["SampleCompositionTimeOffset_651"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1960]["SampleDuration_652"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1961]["SampleSize_652"] == 877:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1962]["SampleCompositionTimeOffset_652"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1963]["SampleDuration_653"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1964]["SampleSize_653"] == 873:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1965]["SampleCompositionTimeOffset_653"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1966]["SampleDuration_654"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1967]["SampleSize_654"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1968]["SampleCompositionTimeOffset_654"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1969]["SampleDuration_655"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1970]["SampleSize_655"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1971]["SampleCompositionTimeOffset_655"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1972]["SampleDuration_656"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1973]["SampleSize_656"] == 871:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1974]["SampleCompositionTimeOffset_656"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1975]["SampleDuration_657"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1976]["SampleSize_657"] == 866:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1977]["SampleCompositionTimeOffset_657"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1978]["SampleDuration_658"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1979]["SampleSize_658"] == 865:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1980]["SampleCompositionTimeOffset_658"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1981]["SampleDuration_659"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1982]["SampleSize_659"] == 852:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1983]["SampleCompositionTimeOffset_659"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1984]["SampleDuration_660"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1985]["SampleSize_660"] == 858:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1986]["SampleCompositionTimeOffset_660"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1987]["SampleDuration_661"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1988]["SampleSize_661"] == 893:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1989]["SampleCompositionTimeOffset_661"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1990]["SampleDuration_662"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1991]["SampleSize_662"] == 858:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1992]["SampleCompositionTimeOffset_662"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1993]["SampleDuration_663"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1994]["SampleSize_663"] == 851:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1995]["SampleCompositionTimeOffset_663"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1996]["SampleDuration_664"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1997]["SampleSize_664"] == 838:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1998]["SampleCompositionTimeOffset_664"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1999]["SampleDuration_665"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2000]["SampleSize_665"] == 924:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2001]["SampleCompositionTimeOffset_665"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2002]["SampleDuration_666"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2003]["SampleSize_666"] == 841:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2004]["SampleCompositionTimeOffset_666"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2005]["SampleDuration_667"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2006]["SampleSize_667"] == 863:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2007]["SampleCompositionTimeOffset_667"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2008]["SampleDuration_668"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2009]["SampleSize_668"] == 877:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2010]["SampleCompositionTimeOffset_668"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2011]["SampleDuration_669"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2012]["SampleSize_669"] == 834:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2013]["SampleCompositionTimeOffset_669"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2014]["SampleDuration_670"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2015]["SampleSize_670"] == 827:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2016]["SampleCompositionTimeOffset_670"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2017]["SampleDuration_671"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2018]["SampleSize_671"] == 817:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2019]["SampleCompositionTimeOffset_671"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2020]["SampleDuration_672"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2021]["SampleSize_672"] == 816:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2022]["SampleCompositionTimeOffset_672"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2023]["SampleDuration_673"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2024]["SampleSize_673"] == 1159:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2025]["SampleCompositionTimeOffset_673"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2026]["SampleDuration_674"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2027]["SampleSize_674"] == 845:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2028]["SampleCompositionTimeOffset_674"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2029]["SampleDuration_675"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2030]["SampleSize_675"] == 821:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2031]["SampleCompositionTimeOffset_675"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2032]["SampleDuration_676"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2033]["SampleSize_676"] == 839:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2034]["SampleCompositionTimeOffset_676"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2035]["SampleDuration_677"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2036]["SampleSize_677"] == 835:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2037]["SampleCompositionTimeOffset_677"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2038]["SampleDuration_678"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2039]["SampleSize_678"] == 1014:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2040]["SampleCompositionTimeOffset_678"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2041]["SampleDuration_679"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2042]["SampleSize_679"] == 882:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2043]["SampleCompositionTimeOffset_679"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2044]["SampleDuration_680"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2045]["SampleSize_680"] == 876:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2046]["SampleCompositionTimeOffset_680"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2047]["SampleDuration_681"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2048]["SampleSize_681"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2049]["SampleCompositionTimeOffset_681"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2050]["SampleDuration_682"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2051]["SampleSize_682"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2052]["SampleCompositionTimeOffset_682"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2053]["SampleDuration_683"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2054]["SampleSize_683"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2055]["SampleCompositionTimeOffset_683"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2056]["SampleDuration_684"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2057]["SampleSize_684"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2058]["SampleCompositionTimeOffset_684"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2059]["SampleDuration_685"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2060]["SampleSize_685"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2061]["SampleCompositionTimeOffset_685"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2062]["SampleDuration_686"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2063]["SampleSize_686"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2064]["SampleCompositionTimeOffset_686"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2065]["SampleDuration_687"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2066]["SampleSize_687"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2067]["SampleCompositionTimeOffset_687"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2068]["SampleDuration_688"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2069]["SampleSize_688"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2070]["SampleCompositionTimeOffset_688"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2071]["SampleDuration_689"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2072]["SampleSize_689"] == 850:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2073]["SampleCompositionTimeOffset_689"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2074]["SampleDuration_690"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2075]["SampleSize_690"] == 850:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2076]["SampleCompositionTimeOffset_690"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2077]["SampleDuration_691"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2078]["SampleSize_691"] == 813:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2079]["SampleCompositionTimeOffset_691"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2080]["SampleDuration_692"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2081]["SampleSize_692"] == 779:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2082]["SampleCompositionTimeOffset_692"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2083]["SampleDuration_693"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2084]["SampleSize_693"] == 774:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2085]["SampleCompositionTimeOffset_693"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2086]["SampleDuration_694"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2087]["SampleSize_694"] == 794:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2088]["SampleCompositionTimeOffset_694"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2089]["SampleDuration_695"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2090]["SampleSize_695"] == 811:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2091]["SampleCompositionTimeOffset_695"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2092]["SampleDuration_696"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2093]["SampleSize_696"] == 917:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2094]["SampleCompositionTimeOffset_696"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2095]["SampleDuration_697"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2096]["SampleSize_697"] == 850:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2097]["SampleCompositionTimeOffset_697"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2098]["SampleDuration_698"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2099]["SampleSize_698"] == 873:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2100]["SampleCompositionTimeOffset_698"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2101]["SampleDuration_699"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2102]["SampleSize_699"] == 874:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2103]["SampleCompositionTimeOffset_699"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2104]["SampleDuration_700"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2105]["SampleSize_700"] == 920:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2106]["SampleCompositionTimeOffset_700"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2107]["SampleDuration_701"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2108]["SampleSize_701"] == 904:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2109]["SampleCompositionTimeOffset_701"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2110]["SampleDuration_702"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2111]["SampleSize_702"] == 884:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2112]["SampleCompositionTimeOffset_702"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2113]["SampleDuration_703"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2114]["SampleSize_703"] == 852:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2115]["SampleCompositionTimeOffset_703"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2116]["SampleDuration_704"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2117]["SampleSize_704"] == 816:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2118]["SampleCompositionTimeOffset_704"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2119]["SampleDuration_705"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2120]["SampleSize_705"] == 911:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2121]["SampleCompositionTimeOffset_705"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2122]["SampleDuration_706"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2123]["SampleSize_706"] == 787:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2124]["SampleCompositionTimeOffset_706"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2125]["SampleDuration_707"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2126]["SampleSize_707"] == 818:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2127]["SampleCompositionTimeOffset_707"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2128]["SampleDuration_708"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2129]["SampleSize_708"] == 776:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2130]["SampleCompositionTimeOffset_708"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2131]["SampleDuration_709"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2132]["SampleSize_709"] == 807:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2133]["SampleCompositionTimeOffset_709"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2134]["SampleDuration_710"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2135]["SampleSize_710"] == 814:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2136]["SampleCompositionTimeOffset_710"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2137]["SampleDuration_711"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2138]["SampleSize_711"] == 836:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2139]["SampleCompositionTimeOffset_711"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2140]["SampleDuration_712"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2141]["SampleSize_712"] == 850:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2142]["SampleCompositionTimeOffset_712"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2143]["SampleDuration_713"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2144]["SampleSize_713"] == 1060:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2145]["SampleCompositionTimeOffset_713"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2146]["SampleDuration_714"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2147]["SampleSize_714"] == 1007:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2148]["SampleCompositionTimeOffset_714"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2149]["SampleDuration_715"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2150]["SampleSize_715"] == 900:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2151]["SampleCompositionTimeOffset_715"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2152]["SampleDuration_716"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2153]["SampleSize_716"] == 879:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2154]["SampleCompositionTimeOffset_716"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2155]["SampleDuration_717"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2156]["SampleSize_717"] == 913:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2157]["SampleCompositionTimeOffset_717"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2158]["SampleDuration_718"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2159]["SampleSize_718"] == 871:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2160]["SampleCompositionTimeOffset_718"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2161]["SampleDuration_719"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2162]["SampleSize_719"] == 847:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2163]["SampleCompositionTimeOffset_719"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2164]["SampleDuration_720"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2165]["SampleSize_720"] == 819:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2166]["SampleCompositionTimeOffset_720"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2167]["SampleDuration_721"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2168]["SampleSize_721"] == 810:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2169]["SampleCompositionTimeOffset_721"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2170]["SampleDuration_722"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2171]["SampleSize_722"] == 842:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2172]["SampleCompositionTimeOffset_722"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2173]["SampleDuration_723"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2174]["SampleSize_723"] == 1125:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2175]["SampleCompositionTimeOffset_723"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2176]["SampleDuration_724"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2177]["SampleSize_724"] == 864:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2178]["SampleCompositionTimeOffset_724"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2179]["SampleDuration_725"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2180]["SampleSize_725"] == 865:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2181]["SampleCompositionTimeOffset_725"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2182]["SampleDuration_726"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2183]["SampleSize_726"] == 880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2184]["SampleCompositionTimeOffset_726"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2185]["SampleDuration_727"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2186]["SampleSize_727"] == 946:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2187]["SampleCompositionTimeOffset_727"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2188]["SampleDuration_728"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2189]["SampleSize_728"] == 904:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2190]["SampleCompositionTimeOffset_728"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2191]["SampleDuration_729"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2192]["SampleSize_729"] == 953:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2193]["SampleCompositionTimeOffset_729"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2194]["SampleDuration_730"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2195]["SampleSize_730"] == 893:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2196]["SampleCompositionTimeOffset_730"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2197]["SampleDuration_731"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2198]["SampleSize_731"] == 887:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2199]["SampleCompositionTimeOffset_731"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2200]["SampleDuration_732"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2201]["SampleSize_732"] == 895:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2202]["SampleCompositionTimeOffset_732"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2203]["SampleDuration_733"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2204]["SampleSize_733"] == 876:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2205]["SampleCompositionTimeOffset_733"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2206]["SampleDuration_734"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2207]["SampleSize_734"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2208]["SampleCompositionTimeOffset_734"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2209]["SampleDuration_735"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2210]["SampleSize_735"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2211]["SampleCompositionTimeOffset_735"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2212]["SampleDuration_736"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2213]["SampleSize_736"] == 857:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2214]["SampleCompositionTimeOffset_736"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2215]["SampleDuration_737"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2216]["SampleSize_737"] == 870:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2217]["SampleCompositionTimeOffset_737"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2218]["SampleDuration_738"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2219]["SampleSize_738"] == 859:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2220]["SampleCompositionTimeOffset_738"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2221]["SampleDuration_739"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2222]["SampleSize_739"] == 850:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2223]["SampleCompositionTimeOffset_739"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2224]["SampleDuration_740"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2225]["SampleSize_740"] == 845:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2226]["SampleCompositionTimeOffset_740"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2227]["SampleDuration_741"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2228]["SampleSize_741"] == 836:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2229]["SampleCompositionTimeOffset_741"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2230]["SampleDuration_742"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2231]["SampleSize_742"] == 836:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2232]["SampleCompositionTimeOffset_742"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2233]["SampleDuration_743"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2234]["SampleSize_743"] == 839:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2235]["SampleCompositionTimeOffset_743"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2236]["SampleDuration_744"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2237]["SampleSize_744"] == 850:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2238]["SampleCompositionTimeOffset_744"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2239]["SampleDuration_745"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2240]["SampleSize_745"] == 827:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2241]["SampleCompositionTimeOffset_745"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2242]["SampleDuration_746"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2243]["SampleSize_746"] == 859:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2244]["SampleCompositionTimeOffset_746"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2245]["SampleDuration_747"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2246]["SampleSize_747"] == 837:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2247]["SampleCompositionTimeOffset_747"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2248]["SampleDuration_748"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2249]["SampleSize_748"] == 862:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2250]["SampleCompositionTimeOffset_748"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2251]["SampleDuration_749"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2252]["SampleSize_749"] == 836:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2253]["SampleCompositionTimeOffset_749"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2254]["SampleDuration_750"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2255]["SampleSize_750"] == 852:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2256]["SampleCompositionTimeOffset_750"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2257]["SampleDuration_751"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2258]["SampleSize_751"] == 1166:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2259]["SampleCompositionTimeOffset_751"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2260]["SampleDuration_752"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2261]["SampleSize_752"] == 923:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2262]["SampleCompositionTimeOffset_752"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2263]["SampleDuration_753"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2264]["SampleSize_753"] == 880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2265]["SampleCompositionTimeOffset_753"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2266]["SampleDuration_754"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2267]["SampleSize_754"] == 886:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2268]["SampleCompositionTimeOffset_754"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2269]["SampleDuration_755"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2270]["SampleSize_755"] == 878:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2271]["SampleCompositionTimeOffset_755"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2272]["SampleDuration_756"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2273]["SampleSize_756"] == 882:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2274]["SampleCompositionTimeOffset_756"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2275]["SampleDuration_757"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2276]["SampleSize_757"] == 887:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2277]["SampleCompositionTimeOffset_757"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2278]["SampleDuration_758"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2279]["SampleSize_758"] == 874:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2280]["SampleCompositionTimeOffset_758"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2281]["SampleDuration_759"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2282]["SampleSize_759"] == 875:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2283]["SampleCompositionTimeOffset_759"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2284]["SampleDuration_760"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2285]["SampleSize_760"] == 862:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2286]["SampleCompositionTimeOffset_760"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2287]["SampleDuration_761"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2288]["SampleSize_761"] == 855:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2289]["SampleCompositionTimeOffset_761"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2290]["SampleDuration_762"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2291]["SampleSize_762"] == 852:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2292]["SampleCompositionTimeOffset_762"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2293]["SampleDuration_763"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2294]["SampleSize_763"] == 837:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2295]["SampleCompositionTimeOffset_763"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2296]["SampleDuration_764"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2297]["SampleSize_764"] == 814:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2298]["SampleCompositionTimeOffset_764"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2299]["SampleDuration_765"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2300]["SampleSize_765"] == 792:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2301]["SampleCompositionTimeOffset_765"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2302]["SampleDuration_766"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2303]["SampleSize_766"] == 774:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2304]["SampleCompositionTimeOffset_766"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2305]["SampleDuration_767"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2306]["SampleSize_767"] == 776:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2307]["SampleCompositionTimeOffset_767"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2308]["SampleDuration_768"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2309]["SampleSize_768"] == 771:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2310]["SampleCompositionTimeOffset_768"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2311]["SampleDuration_769"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2312]["SampleSize_769"] == 1104:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2313]["SampleCompositionTimeOffset_769"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2314]["SampleDuration_770"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2315]["SampleSize_770"] == 828:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2316]["SampleCompositionTimeOffset_770"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2317]["SampleDuration_771"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2318]["SampleSize_771"] == 818:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2319]["SampleCompositionTimeOffset_771"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2320]["SampleDuration_772"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2321]["SampleSize_772"] == 833:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2322]["SampleCompositionTimeOffset_772"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2323]["SampleDuration_773"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2324]["SampleSize_773"] == 823:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2325]["SampleCompositionTimeOffset_773"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2326]["SampleDuration_774"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2327]["SampleSize_774"] == 822:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2328]["SampleCompositionTimeOffset_774"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2329]["SampleDuration_775"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2330]["SampleSize_775"] == 837:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2331]["SampleCompositionTimeOffset_775"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2332]["SampleDuration_776"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2333]["SampleSize_776"] == 828:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2334]["SampleCompositionTimeOffset_776"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2335]["SampleDuration_777"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2336]["SampleSize_777"] == 1160:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2337]["SampleCompositionTimeOffset_777"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2338]["SampleDuration_778"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2339]["SampleSize_778"] == 921:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2340]["SampleCompositionTimeOffset_778"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2341]["SampleDuration_779"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2342]["SampleSize_779"] == 892:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2343]["SampleCompositionTimeOffset_779"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2344]["SampleDuration_780"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2345]["SampleSize_780"] == 867:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2346]["SampleCompositionTimeOffset_780"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2347]["SampleDuration_781"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2348]["SampleSize_781"] == 853:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2349]["SampleCompositionTimeOffset_781"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2350]["SampleDuration_782"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2351]["SampleSize_782"] == 870:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2352]["SampleCompositionTimeOffset_782"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2353]["SampleDuration_783"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2354]["SampleSize_783"] == 899:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2355]["SampleCompositionTimeOffset_783"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2356]["SampleDuration_784"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2357]["SampleSize_784"] == 900:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2358]["SampleCompositionTimeOffset_784"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2359]["SampleDuration_785"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2360]["SampleSize_785"] == 903:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2361]["SampleCompositionTimeOffset_785"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2362]["SampleDuration_786"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2363]["SampleSize_786"] == 874:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2364]["SampleCompositionTimeOffset_786"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2365]["SampleDuration_787"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2366]["SampleSize_787"] == 848:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2367]["SampleCompositionTimeOffset_787"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2368]["SampleDuration_788"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2369]["SampleSize_788"] == 854:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2370]["SampleCompositionTimeOffset_788"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2371]["SampleDuration_789"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2372]["SampleSize_789"] == 869:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2373]["SampleCompositionTimeOffset_789"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2374]["SampleDuration_790"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2375]["SampleSize_790"] == 863:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2376]["SampleCompositionTimeOffset_790"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2377]["SampleDuration_791"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2378]["SampleSize_791"] == 855:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2379]["SampleCompositionTimeOffset_791"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2380]["SampleDuration_792"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2381]["SampleSize_792"] == 857:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2382]["SampleCompositionTimeOffset_792"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2383]["SampleDuration_793"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2384]["SampleSize_793"] == 849:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2385]["SampleCompositionTimeOffset_793"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2386]["SampleDuration_794"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2387]["SampleSize_794"] == 1107:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2388]["SampleCompositionTimeOffset_794"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2389]["SampleDuration_795"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2390]["SampleSize_795"] == 879:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2391]["SampleCompositionTimeOffset_795"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2392]["SampleDuration_796"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2393]["SampleSize_796"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2394]["SampleCompositionTimeOffset_796"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2395]["SampleDuration_797"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2396]["SampleSize_797"] == 833:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2397]["SampleCompositionTimeOffset_797"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2398]["SampleDuration_798"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2399]["SampleSize_798"] == 795:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2400]["SampleCompositionTimeOffset_798"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2401]["SampleDuration_799"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2402]["SampleSize_799"] == 800:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2403]["SampleCompositionTimeOffset_799"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2404]["SampleDuration_800"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2405]["SampleSize_800"] == 800:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2406]["SampleCompositionTimeOffset_800"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2407]["SampleDuration_801"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2408]["SampleSize_801"] == 963:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2409]["SampleCompositionTimeOffset_801"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2410]["SampleDuration_802"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2411]["SampleSize_802"] == 818:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2412]["SampleCompositionTimeOffset_802"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2413]["SampleDuration_803"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2414]["SampleSize_803"] == 848:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2415]["SampleCompositionTimeOffset_803"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2416]["SampleDuration_804"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2417]["SampleSize_804"] == 812:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2418]["SampleCompositionTimeOffset_804"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2419]["SampleDuration_805"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2420]["SampleSize_805"] == 824:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2421]["SampleCompositionTimeOffset_805"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2422]["SampleDuration_806"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2423]["SampleSize_806"] == 854:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2424]["SampleCompositionTimeOffset_806"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2425]["SampleDuration_807"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2426]["SampleSize_807"] == 840:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2427]["SampleCompositionTimeOffset_807"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2428]["SampleDuration_808"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2429]["SampleSize_808"] == 833:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2430]["SampleCompositionTimeOffset_808"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2431]["SampleDuration_809"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2432]["SampleSize_809"] == 830:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2433]["SampleCompositionTimeOffset_809"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2434]["SampleDuration_810"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2435]["SampleSize_810"] == 828:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2436]["SampleCompositionTimeOffset_810"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2437]["SampleDuration_811"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2438]["SampleSize_811"] == 829:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2439]["SampleCompositionTimeOffset_811"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2440]["SampleDuration_812"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2441]["SampleSize_812"] == 849:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2442]["SampleCompositionTimeOffset_812"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2443]["SampleDuration_813"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2444]["SampleSize_813"] == 851:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2445]["SampleCompositionTimeOffset_813"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2446]["SampleDuration_814"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2447]["SampleSize_814"] == 850:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2448]["SampleCompositionTimeOffset_814"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2449]["SampleDuration_815"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2450]["SampleSize_815"] == 855:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2451]["SampleCompositionTimeOffset_815"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2452]["SampleDuration_816"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2453]["SampleSize_816"] == 860:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2454]["SampleCompositionTimeOffset_816"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2455]["SampleDuration_817"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2456]["SampleSize_817"] == 855:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2457]["SampleCompositionTimeOffset_817"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2458]["SampleDuration_818"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2459]["SampleSize_818"] == 862:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2460]["SampleCompositionTimeOffset_818"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2461]["SampleDuration_819"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2462]["SampleSize_819"] == 1105:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2463]["SampleCompositionTimeOffset_819"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2464]["SampleDuration_820"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2465]["SampleSize_820"] == 871:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2466]["SampleCompositionTimeOffset_820"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2467]["SampleDuration_821"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2468]["SampleSize_821"] == 839:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2469]["SampleCompositionTimeOffset_821"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2470]["SampleDuration_822"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2471]["SampleSize_822"] == 805:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2472]["SampleCompositionTimeOffset_822"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2473]["SampleDuration_823"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2474]["SampleSize_823"] == 818:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2475]["SampleCompositionTimeOffset_823"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2476]["SampleDuration_824"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2477]["SampleSize_824"] == 837:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2478]["SampleCompositionTimeOffset_824"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2479]["SampleDuration_825"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2480]["SampleSize_825"] == 845:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2481]["SampleCompositionTimeOffset_825"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2482]["SampleDuration_826"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2483]["SampleSize_826"] == 862:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2484]["SampleCompositionTimeOffset_826"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2485]["SampleDuration_827"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2486]["SampleSize_827"] == 869:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2487]["SampleCompositionTimeOffset_827"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2488]["SampleDuration_828"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2489]["SampleSize_828"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2490]["SampleCompositionTimeOffset_828"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2491]["SampleDuration_829"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2492]["SampleSize_829"] == 888:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2493]["SampleCompositionTimeOffset_829"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2494]["SampleDuration_830"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2495]["SampleSize_830"] == 857:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2496]["SampleCompositionTimeOffset_830"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2497]["SampleDuration_831"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2498]["SampleSize_831"] == 936:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2499]["SampleCompositionTimeOffset_831"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2500]["SampleDuration_832"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2501]["SampleSize_832"] == 812:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2502]["SampleCompositionTimeOffset_832"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2503]["SampleDuration_833"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2504]["SampleSize_833"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2505]["SampleCompositionTimeOffset_833"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2506]["SampleDuration_834"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2507]["SampleSize_834"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2508]["SampleCompositionTimeOffset_834"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2509]["SampleDuration_835"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2510]["SampleSize_835"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2511]["SampleCompositionTimeOffset_835"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2512]["SampleDuration_836"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2513]["SampleSize_836"] == 1057:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2514]["SampleCompositionTimeOffset_836"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2515]["SampleDuration_837"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2516]["SampleSize_837"] == 852:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2517]["SampleCompositionTimeOffset_837"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2518]["SampleDuration_838"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2519]["SampleSize_838"] == 851:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2520]["SampleCompositionTimeOffset_838"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2521]["SampleDuration_839"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2522]["SampleSize_839"] == 868:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2523]["SampleCompositionTimeOffset_839"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2524]["SampleDuration_840"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2525]["SampleSize_840"] == 875:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2526]["SampleCompositionTimeOffset_840"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2527]["SampleDuration_841"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2528]["SampleSize_841"] == 816:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2529]["SampleCompositionTimeOffset_841"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2530]["SampleDuration_842"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2531]["SampleSize_842"] == 822:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2532]["SampleCompositionTimeOffset_842"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2533]["SampleDuration_843"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2534]["SampleSize_843"] == 854:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2535]["SampleCompositionTimeOffset_843"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2536]["SampleDuration_844"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2537]["SampleSize_844"] == 861:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2538]["SampleCompositionTimeOffset_844"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2539]["SampleDuration_845"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2540]["SampleSize_845"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2541]["SampleCompositionTimeOffset_845"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2542]["SampleDuration_846"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2543]["SampleSize_846"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2544]["SampleCompositionTimeOffset_846"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2545]["SampleDuration_847"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2546]["SampleSize_847"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2547]["SampleCompositionTimeOffset_847"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2548]["SampleDuration_848"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2549]["SampleSize_848"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2550]["SampleCompositionTimeOffset_848"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2551]["SampleDuration_849"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2552]["SampleSize_849"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2553]["SampleCompositionTimeOffset_849"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2554]["SampleDuration_850"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2555]["SampleSize_850"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2556]["SampleCompositionTimeOffset_850"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2557]["SampleDuration_851"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2558]["SampleSize_851"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2559]["SampleCompositionTimeOffset_851"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2560]["SampleDuration_852"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2561]["SampleSize_852"] == 911:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2562]["SampleCompositionTimeOffset_852"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2563]["SampleDuration_853"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2564]["SampleSize_853"] == 858:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2565]["SampleCompositionTimeOffset_853"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2566]["SampleDuration_854"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2567]["SampleSize_854"] == 850:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2568]["SampleCompositionTimeOffset_854"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2569]["SampleDuration_855"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2570]["SampleSize_855"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2571]["SampleCompositionTimeOffset_855"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2572]["SampleDuration_856"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2573]["SampleSize_856"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2574]["SampleCompositionTimeOffset_856"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2575]["SampleDuration_857"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2576]["SampleSize_857"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2577]["SampleCompositionTimeOffset_857"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2578]["SampleDuration_858"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2579]["SampleSize_858"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2580]["SampleCompositionTimeOffset_858"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2581]["SampleDuration_859"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2582]["SampleSize_859"] == 956:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2583]["SampleCompositionTimeOffset_859"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2584]["SampleDuration_860"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2585]["SampleSize_860"] == 911:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2586]["SampleCompositionTimeOffset_860"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2587]["SampleDuration_861"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2588]["SampleSize_861"] == 929:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2589]["SampleCompositionTimeOffset_861"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2590]["SampleDuration_862"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2591]["SampleSize_862"] == 875:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2592]["SampleCompositionTimeOffset_862"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2593]["SampleDuration_863"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2594]["SampleSize_863"] == 837:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2595]["SampleCompositionTimeOffset_863"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2596]["SampleDuration_864"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2597]["SampleSize_864"] == 837:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2598]["SampleCompositionTimeOffset_864"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2599]["SampleDuration_865"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2600]["SampleSize_865"] == 1022:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2601]["SampleCompositionTimeOffset_865"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2602]["SampleDuration_866"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2603]["SampleSize_866"] == 1009:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2604]["SampleCompositionTimeOffset_866"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2605]["SampleDuration_867"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2606]["SampleSize_867"] == 844:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2607]["SampleCompositionTimeOffset_867"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2608]["SampleDuration_868"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2609]["SampleSize_868"] == 885:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2610]["SampleCompositionTimeOffset_868"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2611]["SampleDuration_869"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2612]["SampleSize_869"] == 907:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2613]["SampleCompositionTimeOffset_869"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2614]["SampleDuration_870"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2615]["SampleSize_870"] == 916:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2616]["SampleCompositionTimeOffset_870"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2617]["SampleDuration_871"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2618]["SampleSize_871"] == 909:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2619]["SampleCompositionTimeOffset_871"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2620]["SampleDuration_872"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2621]["SampleSize_872"] == 918:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2622]["SampleCompositionTimeOffset_872"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2623]["SampleDuration_873"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2624]["SampleSize_873"] == 919:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2625]["SampleCompositionTimeOffset_873"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2626]["SampleDuration_874"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2627]["SampleSize_874"] == 902:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2628]["SampleCompositionTimeOffset_874"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2629]["SampleDuration_875"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2630]["SampleSize_875"] == 897:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2631]["SampleCompositionTimeOffset_875"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2632]["SampleDuration_876"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2633]["SampleSize_876"] == 900:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2634]["SampleCompositionTimeOffset_876"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2635]["SampleDuration_877"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2636]["SampleSize_877"] == 887:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2637]["SampleCompositionTimeOffset_877"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2638]["SampleDuration_878"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2639]["SampleSize_878"] == 902:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2640]["SampleCompositionTimeOffset_878"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2641]["SampleDuration_879"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2642]["SampleSize_879"] == 887:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2643]["SampleCompositionTimeOffset_879"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2644]["SampleDuration_880"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2645]["SampleSize_880"] == 893:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2646]["SampleCompositionTimeOffset_880"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2647]["SampleDuration_881"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2648]["SampleSize_881"] == 886:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2649]["SampleCompositionTimeOffset_881"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2650]["SampleDuration_882"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2651]["SampleSize_882"] == 871:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2652]["SampleCompositionTimeOffset_882"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2653]["SampleDuration_883"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2654]["SampleSize_883"] == 875:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2655]["SampleCompositionTimeOffset_883"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2656]["SampleDuration_884"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2657]["SampleSize_884"] == 837:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2658]["SampleCompositionTimeOffset_884"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2659]["SampleDuration_885"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2660]["SampleSize_885"] == 996:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2661]["SampleCompositionTimeOffset_885"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2662]["SampleDuration_886"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2663]["SampleSize_886"] == 883:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2664]["SampleCompositionTimeOffset_886"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2665]["SampleDuration_887"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2666]["SampleSize_887"] == 808:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2667]["SampleCompositionTimeOffset_887"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2668]["SampleDuration_888"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2669]["SampleSize_888"] == 778:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2670]["SampleCompositionTimeOffset_888"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2671]["SampleDuration_889"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2672]["SampleSize_889"] == 784:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2673]["SampleCompositionTimeOffset_889"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2674]["SampleDuration_890"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2675]["SampleSize_890"] == 802:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2676]["SampleCompositionTimeOffset_890"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2677]["SampleDuration_891"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2678]["SampleSize_891"] == 1186:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2679]["SampleCompositionTimeOffset_891"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2680]["SampleDuration_892"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2681]["SampleSize_892"] == 874:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2682]["SampleCompositionTimeOffset_892"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2683]["SampleDuration_893"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2684]["SampleSize_893"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2685]["SampleCompositionTimeOffset_893"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2686]["SampleDuration_894"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2687]["SampleSize_894"] == 856:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2688]["SampleCompositionTimeOffset_894"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2689]["SampleDuration_895"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2690]["SampleSize_895"] == 857:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2691]["SampleCompositionTimeOffset_895"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2692]["SampleDuration_896"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2693]["SampleSize_896"] == 870:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2694]["SampleCompositionTimeOffset_896"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2695]["SampleDuration_897"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2696]["SampleSize_897"] == 883:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2697]["SampleCompositionTimeOffset_897"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2698]["SampleDuration_898"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2699]["SampleSize_898"] == 884:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2700]["SampleCompositionTimeOffset_898"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2701]["SampleDuration_899"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2702]["SampleSize_899"] == 880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2703]["SampleCompositionTimeOffset_899"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2704]["SampleDuration_900"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2705]["SampleSize_900"] == 870:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2706]["SampleCompositionTimeOffset_900"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2707]["SampleDuration_901"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2708]["SampleSize_901"] == 867:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2709]["SampleCompositionTimeOffset_901"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2710]["SampleDuration_902"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2711]["SampleSize_902"] == 869:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2712]["SampleCompositionTimeOffset_902"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2713]["SampleDuration_903"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2714]["SampleSize_903"] == 861:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2715]["SampleCompositionTimeOffset_903"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2716]["SampleDuration_904"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2717]["SampleSize_904"] == 894:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2718]["SampleCompositionTimeOffset_904"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2719]["SampleDuration_905"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2720]["SampleSize_905"] == 860:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2721]["SampleCompositionTimeOffset_905"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2722]["SampleDuration_906"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2723]["SampleSize_906"] == 853:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2724]["SampleCompositionTimeOffset_906"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2725]["SampleDuration_907"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2726]["SampleSize_907"] == 859:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2727]["SampleCompositionTimeOffset_907"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2728]["SampleDuration_908"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2729]["SampleSize_908"] == 855:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2730]["SampleCompositionTimeOffset_908"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2731]["SampleDuration_909"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2732]["SampleSize_909"] == 867:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2733]["SampleCompositionTimeOffset_909"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2734]["SampleDuration_910"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2735]["SampleSize_910"] == 849:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2736]["SampleCompositionTimeOffset_910"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2737]["SampleDuration_911"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2738]["SampleSize_911"] == 936:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2739]["SampleCompositionTimeOffset_911"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2740]["SampleDuration_912"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2741]["SampleSize_912"] == 924:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2742]["SampleCompositionTimeOffset_912"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2743]["SampleDuration_913"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2744]["SampleSize_913"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2745]["SampleCompositionTimeOffset_913"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2746]["SampleDuration_914"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2747]["SampleSize_914"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2748]["SampleCompositionTimeOffset_914"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2749]["SampleDuration_915"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2750]["SampleSize_915"] == 870:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2751]["SampleCompositionTimeOffset_915"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2752]["SampleDuration_916"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2753]["SampleSize_916"] == 871:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2754]["SampleCompositionTimeOffset_916"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2755]["SampleDuration_917"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2756]["SampleSize_917"] == 875:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2757]["SampleCompositionTimeOffset_917"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2758]["SampleDuration_918"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2759]["SampleSize_918"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2760]["SampleCompositionTimeOffset_918"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2761]["SampleDuration_919"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2762]["SampleSize_919"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2763]["SampleCompositionTimeOffset_919"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2764]["SampleDuration_920"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2765]["SampleSize_920"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2766]["SampleCompositionTimeOffset_920"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2767]["SampleDuration_921"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2768]["SampleSize_921"] == 857:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2769]["SampleCompositionTimeOffset_921"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2770]["SampleDuration_922"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2771]["SampleSize_922"] == 887:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2772]["SampleCompositionTimeOffset_922"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2773]["SampleDuration_923"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2774]["SampleSize_923"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2775]["SampleCompositionTimeOffset_923"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2776]["SampleDuration_924"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2777]["SampleSize_924"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2778]["SampleCompositionTimeOffset_924"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2779]["SampleDuration_925"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2780]["SampleSize_925"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2781]["SampleCompositionTimeOffset_925"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2782]["SampleDuration_926"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2783]["SampleSize_926"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2784]["SampleCompositionTimeOffset_926"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2785]["SampleDuration_927"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2786]["SampleSize_927"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2787]["SampleCompositionTimeOffset_927"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2788]["SampleDuration_928"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2789]["SampleSize_928"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2790]["SampleCompositionTimeOffset_928"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2791]["SampleDuration_929"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2792]["SampleSize_929"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2793]["SampleCompositionTimeOffset_929"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2794]["SampleDuration_930"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2795]["SampleSize_930"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2796]["SampleCompositionTimeOffset_930"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2797]["SampleDuration_931"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2798]["SampleSize_931"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2799]["SampleCompositionTimeOffset_931"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2800]["SampleDuration_932"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2801]["SampleSize_932"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2802]["SampleCompositionTimeOffset_932"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2803]["SampleDuration_933"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2804]["SampleSize_933"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2805]["SampleCompositionTimeOffset_933"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2806]["SampleDuration_934"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2807]["SampleSize_934"] == 871:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2808]["SampleCompositionTimeOffset_934"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2809]["SampleDuration_935"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2810]["SampleSize_935"] == 869:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2811]["SampleCompositionTimeOffset_935"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2812]["SampleDuration_936"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2813]["SampleSize_936"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2814]["SampleCompositionTimeOffset_936"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2815]["SampleDuration_937"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2816]["SampleSize_937"] == 871:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2817]["SampleCompositionTimeOffset_937"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2818]["SampleDuration_938"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2819]["SampleSize_938"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2820]["SampleCompositionTimeOffset_938"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2821]["SampleDuration_939"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2822]["SampleSize_939"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2823]["SampleCompositionTimeOffset_939"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2824]["SampleDuration_940"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2825]["SampleSize_940"] == 877:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2826]["SampleCompositionTimeOffset_940"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2827]["SampleDuration_941"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2828]["SampleSize_941"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2829]["SampleCompositionTimeOffset_941"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2830]["SampleDuration_942"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2831]["SampleSize_942"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2832]["SampleCompositionTimeOffset_942"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2833]["SampleDuration_943"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2834]["SampleSize_943"] == 867:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2835]["SampleCompositionTimeOffset_943"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2836]["SampleDuration_944"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2837]["SampleSize_944"] == 829:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2838]["SampleCompositionTimeOffset_944"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2839]["SampleDuration_945"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2840]["SampleSize_945"] == 823:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2841]["SampleCompositionTimeOffset_945"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2842]["SampleDuration_946"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2843]["SampleSize_946"] == 819:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2844]["SampleCompositionTimeOffset_946"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2845]["SampleDuration_947"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2846]["SampleSize_947"] == 827:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2847]["SampleCompositionTimeOffset_947"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2848]["SampleDuration_948"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2849]["SampleSize_948"] == 884:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2850]["SampleCompositionTimeOffset_948"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2851]["SampleDuration_949"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2852]["SampleSize_949"] == 857:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2853]["SampleCompositionTimeOffset_949"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2854]["SampleDuration_950"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2855]["SampleSize_950"] == 866:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2856]["SampleCompositionTimeOffset_950"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2857]["SampleDuration_951"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2858]["SampleSize_951"] == 868:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2859]["SampleCompositionTimeOffset_951"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2860]["SampleDuration_952"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2861]["SampleSize_952"] == 882:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2862]["SampleCompositionTimeOffset_952"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2863]["SampleDuration_953"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2864]["SampleSize_953"] == 897:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2865]["SampleCompositionTimeOffset_953"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2866]["SampleDuration_954"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2867]["SampleSize_954"] == 878:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2868]["SampleCompositionTimeOffset_954"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2869]["SampleDuration_955"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2870]["SampleSize_955"] == 879:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2871]["SampleCompositionTimeOffset_955"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2872]["SampleDuration_956"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2873]["SampleSize_956"] == 857:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2874]["SampleCompositionTimeOffset_956"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2875]["SampleDuration_957"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2876]["SampleSize_957"] == 854:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2877]["SampleCompositionTimeOffset_957"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2878]["SampleDuration_958"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2879]["SampleSize_958"] == 839:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2880]["SampleCompositionTimeOffset_958"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2881]["SampleDuration_959"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2882]["SampleSize_959"] == 845:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2883]["SampleCompositionTimeOffset_959"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2884]["SampleDuration_960"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2885]["SampleSize_960"] == 846:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2886]["SampleCompositionTimeOffset_960"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2887]["SampleDuration_961"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2888]["SampleSize_961"] == 838:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2889]["SampleCompositionTimeOffset_961"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2890]["SampleDuration_962"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2891]["SampleSize_962"] == 833:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2892]["SampleCompositionTimeOffset_962"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2893]["SampleDuration_963"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2894]["SampleSize_963"] == 827:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2895]["SampleCompositionTimeOffset_963"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2896]["SampleDuration_964"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2897]["SampleSize_964"] == 1223:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2898]["SampleCompositionTimeOffset_964"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2899]["SampleDuration_965"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2900]["SampleSize_965"] == 932:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2901]["SampleCompositionTimeOffset_965"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2902]["SampleDuration_966"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2903]["SampleSize_966"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2904]["SampleCompositionTimeOffset_966"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2905]["SampleDuration_967"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2906]["SampleSize_967"] == 868:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2907]["SampleCompositionTimeOffset_967"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2908]["SampleDuration_968"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2909]["SampleSize_968"] == 876:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2910]["SampleCompositionTimeOffset_968"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2911]["SampleDuration_969"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2912]["SampleSize_969"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2913]["SampleCompositionTimeOffset_969"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2914]["SampleDuration_970"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2915]["SampleSize_970"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2916]["SampleCompositionTimeOffset_970"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2917]["SampleDuration_971"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2918]["SampleSize_971"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2919]["SampleCompositionTimeOffset_971"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2920]["SampleDuration_972"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2921]["SampleSize_972"] == 871:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2922]["SampleCompositionTimeOffset_972"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2923]["SampleDuration_973"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2924]["SampleSize_973"] == 869:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2925]["SampleCompositionTimeOffset_973"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2926]["SampleDuration_974"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2927]["SampleSize_974"] == 867:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2928]["SampleCompositionTimeOffset_974"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2929]["SampleDuration_975"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2930]["SampleSize_975"] == 827:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2931]["SampleCompositionTimeOffset_975"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2932]["SampleDuration_976"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2933]["SampleSize_976"] == 802:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2934]["SampleCompositionTimeOffset_976"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2935]["SampleDuration_977"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2936]["SampleSize_977"] == 793:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2937]["SampleCompositionTimeOffset_977"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2938]["SampleDuration_978"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2939]["SampleSize_978"] == 759:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2940]["SampleCompositionTimeOffset_978"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2941]["SampleDuration_979"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2942]["SampleSize_979"] == 742:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2943]["SampleCompositionTimeOffset_979"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2944]["SampleDuration_980"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2945]["SampleSize_980"] == 771:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2946]["SampleCompositionTimeOffset_980"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2947]["SampleDuration_981"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2948]["SampleSize_981"] == 759:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2949]["SampleCompositionTimeOffset_981"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2950]["SampleDuration_982"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2951]["SampleSize_982"] == 882:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2952]["SampleCompositionTimeOffset_982"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2953]["SampleDuration_983"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2954]["SampleSize_983"] == 785:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2955]["SampleCompositionTimeOffset_983"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2956]["SampleDuration_984"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2957]["SampleSize_984"] == 786:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2958]["SampleCompositionTimeOffset_984"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2959]["SampleDuration_985"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2960]["SampleSize_985"] == 859:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2961]["SampleCompositionTimeOffset_985"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2962]["SampleDuration_986"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2963]["SampleSize_986"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2964]["SampleCompositionTimeOffset_986"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2965]["SampleDuration_987"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2966]["SampleSize_987"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2967]["SampleCompositionTimeOffset_987"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2968]["SampleDuration_988"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2969]["SampleSize_988"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2970]["SampleCompositionTimeOffset_988"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2971]["SampleDuration_989"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2972]["SampleSize_989"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2973]["SampleCompositionTimeOffset_989"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2974]["SampleDuration_990"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2975]["SampleSize_990"] == 1081:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2976]["SampleCompositionTimeOffset_990"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2977]["SampleDuration_991"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2978]["SampleSize_991"] == 824:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2979]["SampleCompositionTimeOffset_991"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2980]["SampleDuration_992"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2981]["SampleSize_992"] == 813:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2982]["SampleCompositionTimeOffset_992"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2983]["SampleDuration_993"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2984]["SampleSize_993"] == 811:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2985]["SampleCompositionTimeOffset_993"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2986]["SampleDuration_994"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2987]["SampleSize_994"] == 837:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2988]["SampleCompositionTimeOffset_994"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2989]["SampleDuration_995"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2990]["SampleSize_995"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2991]["SampleCompositionTimeOffset_995"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2992]["SampleDuration_996"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2993]["SampleSize_996"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2994]["SampleCompositionTimeOffset_996"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2995]["SampleDuration_997"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2996]["SampleSize_997"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2997]["SampleCompositionTimeOffset_997"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2998]["SampleDuration_998"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2999]["SampleSize_998"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3000]["SampleCompositionTimeOffset_998"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3001]["SampleDuration_999"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3002]["SampleSize_999"] == 1005:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3003]["SampleCompositionTimeOffset_999"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3004]["SampleDuration_1000"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3005]["SampleSize_1000"] == 1075:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3006]["SampleCompositionTimeOffset_1000"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3007]["SampleDuration_1001"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3008]["SampleSize_1001"] == 836:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3009]["SampleCompositionTimeOffset_1001"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3010]["SampleDuration_1002"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3011]["SampleSize_1002"] == 844:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3012]["SampleCompositionTimeOffset_1002"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3013]["SampleDuration_1003"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3014]["SampleSize_1003"] == 908:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3015]["SampleCompositionTimeOffset_1003"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3016]["SampleDuration_1004"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3017]["SampleSize_1004"] == 941:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3018]["SampleCompositionTimeOffset_1004"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3019]["SampleDuration_1005"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3020]["SampleSize_1005"] == 943:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3021]["SampleCompositionTimeOffset_1005"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3022]["SampleDuration_1006"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3023]["SampleSize_1006"] == 928:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3024]["SampleCompositionTimeOffset_1006"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3025]["SampleDuration_1007"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3026]["SampleSize_1007"] == 913:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3027]["SampleCompositionTimeOffset_1007"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3028]["SampleDuration_1008"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3029]["SampleSize_1008"] == 907:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3030]["SampleCompositionTimeOffset_1008"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3031]["SampleDuration_1009"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3032]["SampleSize_1009"] == 898:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3033]["SampleCompositionTimeOffset_1009"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3034]["SampleDuration_1010"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3035]["SampleSize_1010"] == 901:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3036]["SampleCompositionTimeOffset_1010"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3037]["SampleDuration_1011"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3038]["SampleSize_1011"] == 897:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3039]["SampleCompositionTimeOffset_1011"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3040]["SampleDuration_1012"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3041]["SampleSize_1012"] == 901:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3042]["SampleCompositionTimeOffset_1012"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3043]["SampleDuration_1013"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3044]["SampleSize_1013"] == 894:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3045]["SampleCompositionTimeOffset_1013"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3046]["SampleDuration_1014"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3047]["SampleSize_1014"] == 886:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3048]["SampleCompositionTimeOffset_1014"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3049]["SampleDuration_1015"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3050]["SampleSize_1015"] == 882:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3051]["SampleCompositionTimeOffset_1015"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3052]["SampleDuration_1016"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3053]["SampleSize_1016"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3054]["SampleCompositionTimeOffset_1016"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3055]["SampleDuration_1017"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3056]["SampleSize_1017"] == 859:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3057]["SampleCompositionTimeOffset_1017"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3058]["SampleDuration_1018"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3059]["SampleSize_1018"] == 843:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3060]["SampleCompositionTimeOffset_1018"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3061]["SampleDuration_1019"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3062]["SampleSize_1019"] == 832:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3063]["SampleCompositionTimeOffset_1019"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3064]["SampleDuration_1020"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3065]["SampleSize_1020"] == 814:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3066]["SampleCompositionTimeOffset_1020"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3067]["SampleDuration_1021"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3068]["SampleSize_1021"] == 793:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3069]["SampleCompositionTimeOffset_1021"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3070]["SampleDuration_1022"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3071]["SampleSize_1022"] == 784:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3072]["SampleCompositionTimeOffset_1022"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3073]["SampleDuration_1023"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3074]["SampleSize_1023"] == 733:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3075]["SampleCompositionTimeOffset_1023"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3076]["SampleDuration_1024"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3077]["SampleSize_1024"] == 726:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3078]["SampleCompositionTimeOffset_1024"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3079]["SampleDuration_1025"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3080]["SampleSize_1025"] == 789:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3081]["SampleCompositionTimeOffset_1025"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3082]["SampleDuration_1026"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3083]["SampleSize_1026"] == 845:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3084]["SampleCompositionTimeOffset_1026"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3085]["SampleDuration_1027"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3086]["SampleSize_1027"] == 1116:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3087]["SampleCompositionTimeOffset_1027"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3088]["SampleDuration_1028"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3089]["SampleSize_1028"] == 832:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3090]["SampleCompositionTimeOffset_1028"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3091]["SampleDuration_1029"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3092]["SampleSize_1029"] == 881:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3093]["SampleCompositionTimeOffset_1029"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3094]["SampleDuration_1030"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3095]["SampleSize_1030"] == 781:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3096]["SampleCompositionTimeOffset_1030"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3097]["SampleDuration_1031"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3098]["SampleSize_1031"] == 795:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3099]["SampleCompositionTimeOffset_1031"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3100]["SampleDuration_1032"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3101]["SampleSize_1032"] == 837:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3102]["SampleCompositionTimeOffset_1032"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3103]["SampleDuration_1033"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3104]["SampleSize_1033"] == 887:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3105]["SampleCompositionTimeOffset_1033"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3106]["SampleDuration_1034"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3107]["SampleSize_1034"] == 864:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3108]["SampleCompositionTimeOffset_1034"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3109]["SampleDuration_1035"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3110]["SampleSize_1035"] == 1124:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3111]["SampleCompositionTimeOffset_1035"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3112]["SampleDuration_1036"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3113]["SampleSize_1036"] == 854:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3114]["SampleCompositionTimeOffset_1036"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3115]["SampleDuration_1037"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3116]["SampleSize_1037"] == 938:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3117]["SampleCompositionTimeOffset_1037"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3118]["SampleDuration_1038"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3119]["SampleSize_1038"] == 892:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3120]["SampleCompositionTimeOffset_1038"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3121]["SampleDuration_1039"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3122]["SampleSize_1039"] == 912:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3123]["SampleCompositionTimeOffset_1039"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3124]["SampleDuration_1040"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3125]["SampleSize_1040"] == 958:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3126]["SampleCompositionTimeOffset_1040"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3127]["SampleDuration_1041"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3128]["SampleSize_1041"] == 1033:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3129]["SampleCompositionTimeOffset_1041"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3130]["SampleDuration_1042"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3131]["SampleSize_1042"] == 988:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3132]["SampleCompositionTimeOffset_1042"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3133]["SampleDuration_1043"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3134]["SampleSize_1043"] == 984:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3135]["SampleCompositionTimeOffset_1043"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3136]["SampleDuration_1044"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3137]["SampleSize_1044"] == 905:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3138]["SampleCompositionTimeOffset_1044"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3139]["SampleDuration_1045"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3140]["SampleSize_1045"] == 876:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3141]["SampleCompositionTimeOffset_1045"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3142]["SampleDuration_1046"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3143]["SampleSize_1046"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3144]["SampleCompositionTimeOffset_1046"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3145]["SampleDuration_1047"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3146]["SampleSize_1047"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3147]["SampleCompositionTimeOffset_1047"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3148]["SampleDuration_1048"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3149]["SampleSize_1048"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3150]["SampleCompositionTimeOffset_1048"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3151]["SampleDuration_1049"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3152]["SampleSize_1049"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3153]["SampleCompositionTimeOffset_1049"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3154]["SampleDuration_1050"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3155]["SampleSize_1050"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3156]["SampleCompositionTimeOffset_1050"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3157]["SampleDuration_1051"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3158]["SampleSize_1051"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3159]["SampleCompositionTimeOffset_1051"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3160]["SampleDuration_1052"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3161]["SampleSize_1052"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3162]["SampleCompositionTimeOffset_1052"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3163]["SampleDuration_1053"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3164]["SampleSize_1053"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3165]["SampleCompositionTimeOffset_1053"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3166]["SampleDuration_1054"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3167]["SampleSize_1054"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3168]["SampleCompositionTimeOffset_1054"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3169]["SampleDuration_1055"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3170]["SampleSize_1055"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3171]["SampleCompositionTimeOffset_1055"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3172]["SampleDuration_1056"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3173]["SampleSize_1056"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3174]["SampleCompositionTimeOffset_1056"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3175]["SampleDuration_1057"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3176]["SampleSize_1057"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3177]["SampleCompositionTimeOffset_1057"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3178]["SampleDuration_1058"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3179]["SampleSize_1058"] == 867:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3180]["SampleCompositionTimeOffset_1058"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3181]["SampleDuration_1059"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3182]["SampleSize_1059"] == 865:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3183]["SampleCompositionTimeOffset_1059"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3184]["SampleDuration_1060"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3185]["SampleSize_1060"] == 863:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3186]["SampleCompositionTimeOffset_1060"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3187]["SampleDuration_1061"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3188]["SampleSize_1061"] == 852:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3189]["SampleCompositionTimeOffset_1061"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3190]["SampleDuration_1062"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3191]["SampleSize_1062"] == 836:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3192]["SampleCompositionTimeOffset_1062"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3193]["SampleDuration_1063"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3194]["SampleSize_1063"] == 909:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3195]["SampleCompositionTimeOffset_1063"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3196]["SampleDuration_1064"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3197]["SampleSize_1064"] == 889:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3198]["SampleCompositionTimeOffset_1064"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3199]["SampleDuration_1065"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3200]["SampleSize_1065"] == 899:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3201]["SampleCompositionTimeOffset_1065"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3202]["SampleDuration_1066"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3203]["SampleSize_1066"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3204]["SampleCompositionTimeOffset_1066"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3205]["SampleDuration_1067"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3206]["SampleSize_1067"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3207]["SampleCompositionTimeOffset_1067"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3208]["SampleDuration_1068"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3209]["SampleSize_1068"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3210]["SampleCompositionTimeOffset_1068"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3211]["SampleDuration_1069"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3212]["SampleSize_1069"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3213]["SampleCompositionTimeOffset_1069"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3214]["SampleDuration_1070"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3215]["SampleSize_1070"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3216]["SampleCompositionTimeOffset_1070"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3217]["SampleDuration_1071"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3218]["SampleSize_1071"] == 871:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3219]["SampleCompositionTimeOffset_1071"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3220]["SampleDuration_1072"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3221]["SampleSize_1072"] == 873:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3222]["SampleCompositionTimeOffset_1072"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3223]["SampleDuration_1073"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3224]["SampleSize_1073"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3225]["SampleCompositionTimeOffset_1073"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3226]["SampleDuration_1074"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3227]["SampleSize_1074"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3228]["SampleCompositionTimeOffset_1074"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3229]["SampleDuration_1075"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3230]["SampleSize_1075"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3231]["SampleCompositionTimeOffset_1075"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3232]["SampleDuration_1076"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3233]["SampleSize_1076"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3234]["SampleCompositionTimeOffset_1076"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3235]["SampleDuration_1077"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3236]["SampleSize_1077"] == 871:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3237]["SampleCompositionTimeOffset_1077"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3238]["SampleDuration_1078"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3239]["SampleSize_1078"] == 871:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3240]["SampleCompositionTimeOffset_1078"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3241]["SampleDuration_1079"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3242]["SampleSize_1079"] == 868:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3243]["SampleCompositionTimeOffset_1079"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3244]["SampleDuration_1080"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3245]["SampleSize_1080"] == 868:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3246]["SampleCompositionTimeOffset_1080"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3247]["SampleDuration_1081"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3248]["SampleSize_1081"] == 883:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3249]["SampleCompositionTimeOffset_1081"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3250]["SampleDuration_1082"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3251]["SampleSize_1082"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3252]["SampleCompositionTimeOffset_1082"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3253]["SampleDuration_1083"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3254]["SampleSize_1083"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3255]["SampleCompositionTimeOffset_1083"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3256]["SampleDuration_1084"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3257]["SampleSize_1084"] == 857:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3258]["SampleCompositionTimeOffset_1084"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3259]["SampleDuration_1085"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3260]["SampleSize_1085"] == 860:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3261]["SampleCompositionTimeOffset_1085"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3262]["SampleDuration_1086"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3263]["SampleSize_1086"] == 865:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3264]["SampleCompositionTimeOffset_1086"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3265]["SampleDuration_1087"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3266]["SampleSize_1087"] == 857:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3267]["SampleCompositionTimeOffset_1087"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3268]["SampleDuration_1088"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3269]["SampleSize_1088"] == 859:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3270]["SampleCompositionTimeOffset_1088"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3271]["SampleDuration_1089"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3272]["SampleSize_1089"] == 938:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3273]["SampleCompositionTimeOffset_1089"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3274]["SampleDuration_1090"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3275]["SampleSize_1090"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3276]["SampleCompositionTimeOffset_1090"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3277]["SampleDuration_1091"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3278]["SampleSize_1091"] == 859:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3279]["SampleCompositionTimeOffset_1091"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3280]["SampleDuration_1092"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3281]["SampleSize_1092"] == 874:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3282]["SampleCompositionTimeOffset_1092"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3283]["SampleDuration_1093"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3284]["SampleSize_1093"] == 880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3285]["SampleCompositionTimeOffset_1093"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3286]["SampleDuration_1094"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3287]["SampleSize_1094"] == 874:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3288]["SampleCompositionTimeOffset_1094"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3289]["SampleDuration_1095"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3290]["SampleSize_1095"] == 873:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3291]["SampleCompositionTimeOffset_1095"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3292]["SampleDuration_1096"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3293]["SampleSize_1096"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3294]["SampleCompositionTimeOffset_1096"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3295]["SampleDuration_1097"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3296]["SampleSize_1097"] == 867:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3297]["SampleCompositionTimeOffset_1097"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3298]["SampleDuration_1098"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3299]["SampleSize_1098"] == 873:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3300]["SampleCompositionTimeOffset_1098"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3301]["SampleDuration_1099"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3302]["SampleSize_1099"] == 864:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3303]["SampleCompositionTimeOffset_1099"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3304]["SampleDuration_1100"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3305]["SampleSize_1100"] == 861:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3306]["SampleCompositionTimeOffset_1100"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3307]["SampleDuration_1101"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3308]["SampleSize_1101"] == 857:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3309]["SampleCompositionTimeOffset_1101"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3310]["SampleDuration_1102"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3311]["SampleSize_1102"] == 856:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3312]["SampleCompositionTimeOffset_1102"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3313]["SampleDuration_1103"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3314]["SampleSize_1103"] == 846:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3315]["SampleCompositionTimeOffset_1103"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3316]["SampleDuration_1104"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3317]["SampleSize_1104"] == 846:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3318]["SampleCompositionTimeOffset_1104"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3319]["SampleDuration_1105"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3320]["SampleSize_1105"] == 849:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3321]["SampleCompositionTimeOffset_1105"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3322]["SampleDuration_1106"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3323]["SampleSize_1106"] == 1005:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3324]["SampleCompositionTimeOffset_1106"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3325]["SampleDuration_1107"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3326]["SampleSize_1107"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3327]["SampleCompositionTimeOffset_1107"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3328]["SampleDuration_1108"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3329]["SampleSize_1108"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3330]["SampleCompositionTimeOffset_1108"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3331]["SampleDuration_1109"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3332]["SampleSize_1109"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3333]["SampleCompositionTimeOffset_1109"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3334]["SampleDuration_1110"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3335]["SampleSize_1110"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3336]["SampleCompositionTimeOffset_1110"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3337]["SampleDuration_1111"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3338]["SampleSize_1111"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3339]["SampleCompositionTimeOffset_1111"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3340]["SampleDuration_1112"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3341]["SampleSize_1112"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3342]["SampleCompositionTimeOffset_1112"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3343]["SampleDuration_1113"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3344]["SampleSize_1113"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3345]["SampleCompositionTimeOffset_1113"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3346]["SampleDuration_1114"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3347]["SampleSize_1114"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3348]["SampleCompositionTimeOffset_1114"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3349]["SampleDuration_1115"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3350]["SampleSize_1115"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3351]["SampleCompositionTimeOffset_1115"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3352]["SampleDuration_1116"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3353]["SampleSize_1116"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3354]["SampleCompositionTimeOffset_1116"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3355]["SampleDuration_1117"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3356]["SampleSize_1117"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3357]["SampleCompositionTimeOffset_1117"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3358]["SampleDuration_1118"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3359]["SampleSize_1118"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3360]["SampleCompositionTimeOffset_1118"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3361]["SampleDuration_1119"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3362]["SampleSize_1119"] == 845:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3363]["SampleCompositionTimeOffset_1119"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3364]["SampleDuration_1120"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3365]["SampleSize_1120"] == 775:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3366]["SampleCompositionTimeOffset_1120"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3367]["SampleDuration_1121"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3368]["SampleSize_1121"] == 742:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3369]["SampleCompositionTimeOffset_1121"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3370]["SampleDuration_1122"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3371]["SampleSize_1122"] == 730:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3372]["SampleCompositionTimeOffset_1122"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3373]["SampleDuration_1123"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3374]["SampleSize_1123"] == 718:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3375]["SampleCompositionTimeOffset_1123"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3376]["SampleDuration_1124"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3377]["SampleSize_1124"] == 706:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3378]["SampleCompositionTimeOffset_1124"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3379]["SampleDuration_1125"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3380]["SampleSize_1125"] == 767:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3381]["SampleCompositionTimeOffset_1125"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3382]["SampleDuration_1126"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3383]["SampleSize_1126"] == 853:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3384]["SampleCompositionTimeOffset_1126"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3385]["SampleDuration_1127"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3386]["SampleSize_1127"] == 880:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3387]["SampleCompositionTimeOffset_1127"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3388]["SampleDuration_1128"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3389]["SampleSize_1128"] == 865:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3390]["SampleCompositionTimeOffset_1128"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3391]["SampleDuration_1129"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3392]["SampleSize_1129"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3393]["SampleCompositionTimeOffset_1129"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3394]["SampleDuration_1130"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3395]["SampleSize_1130"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3396]["SampleCompositionTimeOffset_1130"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3397]["SampleDuration_1131"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3398]["SampleSize_1131"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3399]["SampleCompositionTimeOffset_1131"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3400]["SampleDuration_1132"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3401]["SampleSize_1132"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3402]["SampleCompositionTimeOffset_1132"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3403]["SampleDuration_1133"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3404]["SampleSize_1133"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3405]["SampleCompositionTimeOffset_1133"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3406]["SampleDuration_1134"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3407]["SampleSize_1134"] == 872:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3408]["SampleCompositionTimeOffset_1134"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3409]["SampleDuration_1135"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3410]["SampleSize_1135"] == 962:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3411]["SampleCompositionTimeOffset_1135"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3412]["SampleDuration_1136"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3413]["SampleSize_1136"] == 849:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3414]["SampleCompositionTimeOffset_1136"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3415]["SampleDuration_1137"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3416]["SampleSize_1137"] == 944:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3417]["SampleCompositionTimeOffset_1137"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3418]["SampleDuration_1138"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3419]["SampleSize_1138"] == 1056:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3420]["SampleCompositionTimeOffset_1138"] == 312:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3421]["SampleDuration_1139"] == 34:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3422]["SampleSize_1139"] == 996:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3423]["SampleCompositionTimeOffset_1139"] == 312:
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
if "MagicCodeOBU_0" in obu_list[0]:
	pass_count += 1
	obu = obu_list[0].get("MagicCodeOBU_0")[0]
	no_of_check_items += 1
	if obu.get("ia_code") == 1767992678:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if obu.get("version") == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if obu.get("profile_version") == 0:
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
		if obu["codec_config"].get("num_samples_per_frame") == 960:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if obu["codec_config"].get("roll_distance") == -4:
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
	if obu.get("num_substreams") == 7:
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
		no_of_check_items += 1
		if audio_substream_ids[4] == 4:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if audio_substream_ids[5] == 5:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if audio_substream_ids[6] == 6:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if obu.get("num_parameters") == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if obu.get("scalable_channel_layout_config") is not None:
		pass_count += 1
		no_of_check_items += 1
		if obu["scalable_channel_layout_config"].get("num_layers") == 4:
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
			if channel_audio_layer_configs[1].get("loudspeaker_layout") == 8:
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
			if channel_audio_layer_configs[1].get("recon_gain_is_present_flag") == 0:
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
			no_of_check_items += 1
			if channel_audio_layer_configs[2].get("loudspeaker_layout") == 6:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if channel_audio_layer_configs[2].get("output_gain_is_present_flag") == 0:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if channel_audio_layer_configs[2].get("recon_gain_is_present_flag") == 0:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if channel_audio_layer_configs[2].get("substream_count") == 2:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if channel_audio_layer_configs[2].get("coupled_substream_count") == 2:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if channel_audio_layer_configs[3].get("loudspeaker_layout") == 7:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if channel_audio_layer_configs[3].get("output_gain_is_present_flag") == 0:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if channel_audio_layer_configs[3].get("recon_gain_is_present_flag") == 0:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if channel_audio_layer_configs[3].get("substream_count") == 1:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if channel_audio_layer_configs[3].get("coupled_substream_count") == 1:
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
	if obu.get("mix_presentation_annotations") is not None:
		pass_count += 1
		no_of_check_items += 1
		if obu["mix_presentation_annotations"].get("mix_presentation_friendly_label") == "test_mix_pres":
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
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
		if sub_mixes[0].get("num_layouts") == 4:
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
				if layouts[0]["loudness"].get("integrated_loudness") == -8334:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if layouts[0]["loudness"].get("digital_peak") == -3905:
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
					if layouts[1]["loudness_layout"]["ss_layout"].get("sound_system") == 11: # SOUND_SYSTEM_11_2_3_0
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
				if layouts[1]["loudness"].get("integrated_loudness") == -6462:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if layouts[1]["loudness"].get("digital_peak") == -2806:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if layouts[2].get("loudness_layout") is not None:
				pass_count += 1
				no_of_check_items += 1
				if layouts[2]["loudness_layout"].get("layout_type") == 2: # LAYOUT_TYPE_LOUDSPEAKERS_SS_CONVENTION
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if layouts[2]["loudness_layout"].get("ss_layout") is not None:
					pass_count += 1
					no_of_check_items += 1
					if layouts[2]["loudness_layout"]["ss_layout"].get("sound_system") == 10: # SOUND_SYSTEM_10_2_7_0
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
			if layouts[2].get("loudness") is not None:
				pass_count += 1
				no_of_check_items += 1
				if layouts[2]["loudness"].get("info_type") == 0:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if layouts[2]["loudness"].get("integrated_loudness") == -6462:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if layouts[2]["loudness"].get("digital_peak") == -2806:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if layouts[3].get("loudness_layout") is not None:
				pass_count += 1
				no_of_check_items += 1
				if layouts[3]["loudness_layout"].get("layout_type") == 2: # LAYOUT_TYPE_LOUDSPEAKERS_SS_CONVENTION
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if layouts[3]["loudness_layout"].get("ss_layout") is not None:
					pass_count += 1
					no_of_check_items += 1
					if layouts[3]["loudness_layout"]["ss_layout"].get("sound_system") == 9: # SOUND_SYSTEM_J_4_7_0
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
			if layouts[3].get("loudness") is not None:
				pass_count += 1
				no_of_check_items += 1
				if layouts[3]["loudness"].get("info_type") == 0:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if layouts[3]["loudness"].get("integrated_loudness") == -6462:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if layouts[3]["loudness"].get("digital_peak") == -2806:
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
no_of_check_items += 1
if "SyncOBU_4" in obu_list[4]:
	pass_count += 1
	obu = obu_list[4].get("SyncOBU_4")[0]
	no_of_check_items += 1
	if obu.get("global_offset") == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if obu.get("num_obu_ids") == 8:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if obu.get("sync_array") is not None:
		pass_count += 1
		sync_array = obu.get("sync_array")
		no_of_check_items += 1
		if sync_array[0].get("obu_id") == 0:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[0].get("obu_data_type") == 0: # OBU_DATA_TYPE_SUBSTREAM
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[0].get("reinitialize_decoder") == False:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[0].get("relative_offset") == 0:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[1].get("obu_id") == 1:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[1].get("obu_data_type") == 0: # OBU_DATA_TYPE_SUBSTREAM
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[1].get("reinitialize_decoder") == False:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[1].get("relative_offset") == 0:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[2].get("obu_id") == 2:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[2].get("obu_data_type") == 0: # OBU_DATA_TYPE_SUBSTREAM
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[2].get("reinitialize_decoder") == False:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[2].get("relative_offset") == 0:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[3].get("obu_id") == 3:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[3].get("obu_data_type") == 0: # OBU_DATA_TYPE_SUBSTREAM
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[3].get("reinitialize_decoder") == False:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[3].get("relative_offset") == 0:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[4].get("obu_id") == 4:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[4].get("obu_data_type") == 0: # OBU_DATA_TYPE_SUBSTREAM
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[4].get("reinitialize_decoder") == False:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[4].get("relative_offset") == 0:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[5].get("obu_id") == 5:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[5].get("obu_data_type") == 0: # OBU_DATA_TYPE_SUBSTREAM
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[5].get("reinitialize_decoder") == False:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[5].get("relative_offset") == 0:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[6].get("obu_id") == 6:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[6].get("obu_data_type") == 0: # OBU_DATA_TYPE_SUBSTREAM
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[6].get("reinitialize_decoder") == False:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[6].get("relative_offset") == 0:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[7].get("obu_id") == 100:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[7].get("obu_data_type") == 1: # OBU_DATA_TYPE_PARAMETER
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[7].get("reinitialize_decoder") == False:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if sync_array[7].get("relative_offset") == 0:
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
		
		num_channels = ref_signal.shape[1]
		for i in range(num_channels):
			if mse[i]==0:
				print(f'ch#{i} PSNR: inf')
			else:
				print(f'ch#{i} PSNR: {10*math.log10(max_value**2/mse[i])} dB')
				
		return
		
	# Compare two signals
	def bitwise_compare(ref_signal, signal):
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
				
		print("PSNR evaluation:")
		
		try:
			ref_samplerate, ref_data = wavfile.read(ref_file)	
			cmp_samplerate, cmp_data = wavfile.read(cmp_file)
			
			# Check sampling rate
			if not (ref_samplerate == cmp_samplerate):
				raise Exception("Sampling rate of reference file and comparison file are different.")
			
			# Check number of channels
			if not (ref_data.shape[1] == cmp_data.shape[1]):
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
			if not (ref_data.shape[1] == cmp_data.shape[1]):
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
print("""A 4-layer IAMF stream encoded using Opus with the last layer
being 7.1.4.""")
print("is_valid: True")
print("primary_tested_spec_sections: ['3.7.2/channel_audio_layer_config', '3.10', '3.13.1', '6']")
print("*"*40)

