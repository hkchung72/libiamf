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
	if atom[0]["MajorBrands"] == "mp42":
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
if "moov_00000000001d62ec" in atom_list[1]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "mvhd_00000000001d62f4" in atom_list[2]:
	pass_count += 1
	atom = atom_list[2]["mvhd_00000000001d62f4"]
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
	if atom[2]["CreationTime"] == "2023-04-19 00:00:00 UTC":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3]["ModificationTime"] == "2023-04-19 00:00:00 UTC":
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
	if atom[5]["Duration"] == 240000:
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
if "trak_00000000001d6360" in atom_list[3]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "tkhd_00000000001d6368" in atom_list[4]:
	pass_count += 1
	atom = atom_list[4]["tkhd_00000000001d6368"]
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
	if atom[2]["CreationTime"] == "2023-04-19 00:00:00 UTC":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3]["ModificationTime"] == "2023-04-19 00:00:00 UTC":
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
	if atom[6]["Duration"] == 240000:
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
if "mdhd_00000000001d63cc" in atom_list[5]:
	pass_count += 1
	atom = atom_list[5]["mdhd_00000000001d63cc"]
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
	if atom[2]["CreationTime"] == "2023-04-19 00:00:00 UTC":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3]["ModificationTime"] == "2023-04-19 00:00:00 UTC":
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
	if atom[5]["Duration"] == 240000:
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
if "hdlr_00000000001d63ec" in atom_list[6]:
	pass_count += 1
	atom = atom_list[6]["hdlr_00000000001d63ec"]
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
	if atom[7]["Name"] == "ISO Media file produced by Google Inc. Created on: 04/19/2023.":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "stbl_00000000001d6477" in atom_list[7]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "stsd_00000000001d647f" in atom_list[8]:
	pass_count += 1
	atom = atom_list[8]["stsd_00000000001d647f"]
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
if "iamf_00000000001d648f" in atom_list[9]:
	pass_count += 1
	atom = atom_list[9]["iamf_00000000001d648f"]
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
	if atom[5]["ChannelCount"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	iamf_SampleSize = atom[6]["SampleSize"]
	no_of_check_items += 1
	if atom[6]["SampleSize"] == 32:
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
	if atom[9]["SampleRate"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[11]["codec_id"] == "ipcm":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[12]["num_samples_per_frame"] == 1024:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[13]["audio_roll_distance"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "stts_00000000001d652f" in atom_list[10]:
	pass_count += 1
	atom = atom_list[10]["stts_00000000001d652f"]
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
	if atom[2]["EntryCount"] == 2:
		pass_count += 1
		stts_SampleCountSum = 0
		stts_SampleDeltaSum = 0
		SampleCount = atom[3]["SampleCount_0"]
		no_of_check_items += 1
		if atom[3]["SampleCount_0"] == 234:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		stts_SampleCountSum += SampleCount
		SampleDelta = atom[4]["SampleDelta_0"]
		no_of_check_items += 1
		if atom[4]["SampleDelta_0"] == 1024:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		stts_SampleDeltaSum += SampleCount * SampleDelta
		SampleCount = atom[5]["SampleCount_1"]
		no_of_check_items += 1
		if atom[5]["SampleCount_1"] == 1:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		stts_SampleCountSum += SampleCount
		SampleDelta = atom[6]["SampleDelta_1"]
		no_of_check_items += 1
		if atom[6]["SampleDelta_1"] == 384:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		stts_SampleDeltaSum += SampleCount * SampleDelta
		no_of_check_items += 1
		if stts_SampleDeltaSum == mdhd_Duration + elst_MediaTime:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if (mdhd_Duration + elst_MediaTime)%1024 == (SampleDelta%1024):
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		number_of_stts_sample_count = int((mdhd_Duration + elst_MediaTime + 1024 - 1)) // 1024
		if stts_SampleCountSum == number_of_stts_sample_count:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		stts_end_trimming = (1024 - (stts_SampleDeltaSum)%1024)%1024
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "stsc_00000000001d654f" in atom_list[11]:
	pass_count += 1
	atom = atom_list[11]["stsc_00000000001d654f"]
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
	if atom[2]["EntryCount"] == 2:
		pass_count += 1
		no_of_check_items += 1
		if atom[3]["FirstChunk_0"] == 1:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[4]["SamplePerChunk_0"] == 23:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[5]["SampleDescriptionIndex_0"] == 1:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[6]["FirstChunk_1"] == 11:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[7]["SamplePerChunk_1"] == 5:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[8]["SampleDescriptionIndex_1"] == 1:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "stco_00000000001d6577" in atom_list[12]:
	pass_count += 1
	atom = atom_list[12]["stco_00000000001d6577"]
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
	if atom[2]["EntryCount"] == 11:
		pass_count += 1
		no_of_check_items += 1
		if atom[3]["ChunkOffset_0"] == 40:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[4]["ChunkOffset_1"] == 188525:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[5]["ChunkOffset_2"] == 377010:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[6]["ChunkOffset_3"] == 565495:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[7]["ChunkOffset_4"] == 753980:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[8]["ChunkOffset_5"] == 942465:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[9]["ChunkOffset_6"] == 1130950:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[10]["ChunkOffset_7"] == 1319435:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[11]["ChunkOffset_8"] == 1507920:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[12]["ChunkOffset_9"] == 1696405:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[13]["ChunkOffset_10"] == 1884890:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "stsz_00000000001d65b3" in atom_list[13]:
	pass_count += 1
	atom = atom_list[13]["stsz_00000000001d65b3"]
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
	if atom[3]["SampleCount"] == 235:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[4]["EntrySize_0"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[5]["EntrySize_1"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[6]["EntrySize_2"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[7]["EntrySize_3"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[8]["EntrySize_4"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[9]["EntrySize_5"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[10]["EntrySize_6"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[11]["EntrySize_7"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[12]["EntrySize_8"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[13]["EntrySize_9"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[14]["EntrySize_10"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[15]["EntrySize_11"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[16]["EntrySize_12"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[17]["EntrySize_13"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[18]["EntrySize_14"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[19]["EntrySize_15"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[20]["EntrySize_16"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[21]["EntrySize_17"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[22]["EntrySize_18"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[23]["EntrySize_19"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[24]["EntrySize_20"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[25]["EntrySize_21"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[26]["EntrySize_22"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[27]["EntrySize_23"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[28]["EntrySize_24"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[29]["EntrySize_25"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[30]["EntrySize_26"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[31]["EntrySize_27"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[32]["EntrySize_28"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[33]["EntrySize_29"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[34]["EntrySize_30"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[35]["EntrySize_31"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[36]["EntrySize_32"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[37]["EntrySize_33"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[38]["EntrySize_34"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[39]["EntrySize_35"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[40]["EntrySize_36"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[41]["EntrySize_37"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[42]["EntrySize_38"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[43]["EntrySize_39"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[44]["EntrySize_40"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[45]["EntrySize_41"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[46]["EntrySize_42"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[47]["EntrySize_43"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[48]["EntrySize_44"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[49]["EntrySize_45"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[50]["EntrySize_46"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[51]["EntrySize_47"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[52]["EntrySize_48"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[53]["EntrySize_49"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[54]["EntrySize_50"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[55]["EntrySize_51"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[56]["EntrySize_52"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[57]["EntrySize_53"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[58]["EntrySize_54"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[59]["EntrySize_55"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[60]["EntrySize_56"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[61]["EntrySize_57"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[62]["EntrySize_58"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[63]["EntrySize_59"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[64]["EntrySize_60"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[65]["EntrySize_61"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[66]["EntrySize_62"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[67]["EntrySize_63"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[68]["EntrySize_64"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[69]["EntrySize_65"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[70]["EntrySize_66"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[71]["EntrySize_67"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[72]["EntrySize_68"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[73]["EntrySize_69"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[74]["EntrySize_70"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[75]["EntrySize_71"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[76]["EntrySize_72"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[77]["EntrySize_73"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[78]["EntrySize_74"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[79]["EntrySize_75"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[80]["EntrySize_76"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[81]["EntrySize_77"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[82]["EntrySize_78"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[83]["EntrySize_79"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[84]["EntrySize_80"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[85]["EntrySize_81"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[86]["EntrySize_82"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[87]["EntrySize_83"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[88]["EntrySize_84"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[89]["EntrySize_85"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[90]["EntrySize_86"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[91]["EntrySize_87"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[92]["EntrySize_88"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[93]["EntrySize_89"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[94]["EntrySize_90"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[95]["EntrySize_91"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[96]["EntrySize_92"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[97]["EntrySize_93"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[98]["EntrySize_94"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[99]["EntrySize_95"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[100]["EntrySize_96"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[101]["EntrySize_97"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[102]["EntrySize_98"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[103]["EntrySize_99"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[104]["EntrySize_100"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[105]["EntrySize_101"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[106]["EntrySize_102"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[107]["EntrySize_103"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[108]["EntrySize_104"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[109]["EntrySize_105"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[110]["EntrySize_106"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[111]["EntrySize_107"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[112]["EntrySize_108"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[113]["EntrySize_109"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[114]["EntrySize_110"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[115]["EntrySize_111"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[116]["EntrySize_112"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[117]["EntrySize_113"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[118]["EntrySize_114"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[119]["EntrySize_115"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[120]["EntrySize_116"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[121]["EntrySize_117"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[122]["EntrySize_118"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[123]["EntrySize_119"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[124]["EntrySize_120"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[125]["EntrySize_121"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[126]["EntrySize_122"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[127]["EntrySize_123"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[128]["EntrySize_124"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[129]["EntrySize_125"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[130]["EntrySize_126"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[131]["EntrySize_127"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[132]["EntrySize_128"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[133]["EntrySize_129"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[134]["EntrySize_130"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[135]["EntrySize_131"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[136]["EntrySize_132"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[137]["EntrySize_133"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[138]["EntrySize_134"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[139]["EntrySize_135"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[140]["EntrySize_136"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[141]["EntrySize_137"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[142]["EntrySize_138"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[143]["EntrySize_139"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[144]["EntrySize_140"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[145]["EntrySize_141"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[146]["EntrySize_142"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[147]["EntrySize_143"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[148]["EntrySize_144"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[149]["EntrySize_145"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[150]["EntrySize_146"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[151]["EntrySize_147"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[152]["EntrySize_148"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[153]["EntrySize_149"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[154]["EntrySize_150"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[155]["EntrySize_151"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[156]["EntrySize_152"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[157]["EntrySize_153"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[158]["EntrySize_154"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[159]["EntrySize_155"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[160]["EntrySize_156"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[161]["EntrySize_157"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[162]["EntrySize_158"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[163]["EntrySize_159"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[164]["EntrySize_160"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[165]["EntrySize_161"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[166]["EntrySize_162"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[167]["EntrySize_163"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[168]["EntrySize_164"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[169]["EntrySize_165"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[170]["EntrySize_166"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[171]["EntrySize_167"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[172]["EntrySize_168"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[173]["EntrySize_169"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[174]["EntrySize_170"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[175]["EntrySize_171"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[176]["EntrySize_172"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[177]["EntrySize_173"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[178]["EntrySize_174"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[179]["EntrySize_175"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[180]["EntrySize_176"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[181]["EntrySize_177"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[182]["EntrySize_178"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[183]["EntrySize_179"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[184]["EntrySize_180"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[185]["EntrySize_181"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[186]["EntrySize_182"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[187]["EntrySize_183"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[188]["EntrySize_184"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[189]["EntrySize_185"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[190]["EntrySize_186"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[191]["EntrySize_187"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[192]["EntrySize_188"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[193]["EntrySize_189"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[194]["EntrySize_190"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[195]["EntrySize_191"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[196]["EntrySize_192"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[197]["EntrySize_193"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[198]["EntrySize_194"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[199]["EntrySize_195"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[200]["EntrySize_196"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[201]["EntrySize_197"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[202]["EntrySize_198"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[203]["EntrySize_199"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[204]["EntrySize_200"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[205]["EntrySize_201"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[206]["EntrySize_202"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[207]["EntrySize_203"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[208]["EntrySize_204"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[209]["EntrySize_205"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[210]["EntrySize_206"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[211]["EntrySize_207"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[212]["EntrySize_208"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[213]["EntrySize_209"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[214]["EntrySize_210"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[215]["EntrySize_211"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[216]["EntrySize_212"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[217]["EntrySize_213"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[218]["EntrySize_214"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[219]["EntrySize_215"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[220]["EntrySize_216"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[221]["EntrySize_217"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[222]["EntrySize_218"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[223]["EntrySize_219"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[224]["EntrySize_220"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[225]["EntrySize_221"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[226]["EntrySize_222"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[227]["EntrySize_223"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[228]["EntrySize_224"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[229]["EntrySize_225"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[230]["EntrySize_226"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[231]["EntrySize_227"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[232]["EntrySize_228"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[233]["EntrySize_229"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[234]["EntrySize_230"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[235]["EntrySize_231"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[236]["EntrySize_232"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[237]["EntrySize_233"] == 8195:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[238]["EntrySize_234"] == 8198:
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
	if obu.get("primary_profile") == 0: # PROFILE_VERSION_SIMPLE
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if obu.get("additional_profile") == 0: # PROFILE_VERSION_SIMPLE
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
		if obu["codec_config"].get("codec_id") == 1768973165:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if obu["codec_config"].get("num_samples_per_frame") == 1024:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if obu["codec_config"].get("decoder_config_lpcm") is not None:
			pass_count += 1
			no_of_check_items += 1
			if obu["codec_config"]["decoder_config_lpcm"].get("sample_format_flags") == 0: # LPCM_BIG_ENDIAN
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if obu["codec_config"]["decoder_config_lpcm"].get("sample_size") == 32:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if obu["codec_config"]["decoder_config_lpcm"].get("sample_rate") == 48000:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if obu["codec_config"].get("audio_roll_distance") == 0:
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
	if obu.get("num_substreams") == 1:
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
		if obu["scalable_channel_layout_config"].get("num_layers") == 1:
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
			if audio_elements[0].get("element_mix_config") is not None:
				pass_count += 1
				no_of_check_items += 1
				if audio_elements[0]["element_mix_config"].get("mix_gain") is not None:
					pass_count += 1
					no_of_check_items += 1
					if audio_elements[0]["element_mix_config"]["mix_gain"].get("param_definition") is not None:
						pass_count += 1
						no_of_check_items += 1
						if audio_elements[0]["element_mix_config"]["mix_gain"]["param_definition"].get("parameter_id") == 999:
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
			no_of_check_items += 1
			if audio_elements[0].get("mix_presentation_element_annotations_array") is not None:
				pass_count += 1
				mix_presentation_element_annotations_array = audio_elements[0].get("mix_presentation_element_annotations_array")
				no_of_check_items += 1
				if mix_presentation_element_annotations_array[0].get("audio_element_friendly_label") == "test_sub_mix_0_audio_element_0":
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if audio_elements[0].get("rendering_config") is not None:
				pass_count += 1
				no_of_check_items += 1
				if audio_elements[0]["rendering_config"].get("headphones_rendering_mode") == 0: # HEADPHONES_RENDERING_MODE_STEREO
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
		if sub_mixes[0].get("output_mix_config") is not None:
			pass_count += 1
			no_of_check_items += 1
			if sub_mixes[0]["output_mix_config"].get("output_mix_gain") is not None:
				pass_count += 1
				no_of_check_items += 1
				if sub_mixes[0]["output_mix_config"]["output_mix_gain"].get("param_definition") is not None:
					pass_count += 1
					no_of_check_items += 1
					if sub_mixes[0]["output_mix_config"]["output_mix_gain"]["param_definition"].get("parameter_id") == 998:
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
		if sub_mixes[0].get("num_layouts") == 1:
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
				if layouts[0]["loudness"].get("integrated_loudness") == -5129:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if layouts[0]["loudness"].get("digital_peak") == -1009:
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
		
		psnr_list = list()
		
		# To support mono signal
		num_channels = 1 if ref_signal.shape[1:] == () else ref_signal.shape[1]
		for i in range(num_channels):
			mse_value = mse[i] if num_channels > 1 else mse
			if mse_value==0:
				print(f'ch#{i} PSNR: inf')
			else:
				psnr_value = 10*math.log10(max_value**2/mse_value)
				psnr_list.append(psnr_value)
				print(f'ch#{i} PSNR: {psnr_value} dB')
				
		return -1 if len(psnr_list)==0 else sum(psnr_list)/len(psnr_list)
		
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
		import os
		import scipy.io.wavfile as wavfile
		ref_folder, ref_files = args.psnr.rsplit('/',1)
		cmp_folder, cmp_files = args.wav.rsplit('/',1)
		
		for idx, (ref_file, cmp_file) in enumerate(zip(ref_files.split('::'), cmp_files.split('::'))):
			print("[%d] PSNR evaluation:" %(idx+1))		
		
			try:
				ref_samplerate, ref_data = wavfile.read(os.path.join(ref_folder,ref_file))	
				cmp_samplerate, cmp_data = wavfile.read(os.path.join(cmp_folder,cmp_file))
				
				# Check sampling rate
				if not (ref_samplerate == cmp_samplerate):
					raise Exception("Sampling rate of reference file and comparison file are different.")
				
				# Check number of channels
				if not (ref_data.shape[1:] == cmp_data.shape[1:]):
					raise Exception("Number of channels of reference file and comparison file are different.")
				
				# Check number of samples
				if not (ref_data.shape[0] == cmp_data.shape[0]):
					raise Exception("Number of samples of reference file and comparison file are different.")
				
				average_psnr = calc_psnr(ref_data, cmp_data)
				if average_psnr != -1:
					print("average PSNR: %.15f" %(average_psnr))
				
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
	
	cmp_folder, cmp_files = args.wav.rsplit('/',1)
	for idx, cmp_file in enumerate(cmp_files.split('::')):
		print("* [%d] wav output file: %s"%(idx+1, cmp_file))
	
	if args.psnr is not None:
		ref_folder, ref_files = args.psnr.rsplit('/',1)
		for idx, ref_file in enumerate(ref_files.split('::')):
			print("* [%d] reference wav file: %s"%(idx+1, ref_file))
	
	print("*"*40)

print("*"*40)
print("description:")
print("""A simple example of a 32bit stereo IAMF stream and no
parameter blocks.""")
print("is_valid: True")
print("primary_tested_spec_sections: ['3.11.4/sample_size']")
print("*"*40)

