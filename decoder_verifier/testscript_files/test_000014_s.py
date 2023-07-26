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
if "moov_000000000000514e" in atom_list[1]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "mvhd_0000000000005156" in atom_list[2]:
	pass_count += 1
	atom = atom_list[2]["mvhd_0000000000005156"]
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
	if atom[5]["Duration"] == 96000:
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
if "trak_00000000000051c2" in atom_list[3]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "tkhd_00000000000051ca" in atom_list[4]:
	pass_count += 1
	atom = atom_list[4]["tkhd_00000000000051ca"]
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
	if atom[6]["Duration"] == 96000:
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
if "mdhd_000000000000522e" in atom_list[5]:
	pass_count += 1
	atom = atom_list[5]["mdhd_000000000000522e"]
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
	if atom[5]["Duration"] == 96000:
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
if "hdlr_000000000000524e" in atom_list[6]:
	pass_count += 1
	atom = atom_list[6]["hdlr_000000000000524e"]
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
	if atom[7]["Name"] == "ISO Media file produced by Google Inc. Created on: 04/18/2023.":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "stbl_00000000000052d9" in atom_list[7]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "stsd_00000000000052e1" in atom_list[8]:
	pass_count += 1
	atom = atom_list[8]["stsd_00000000000052e1"]
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
if "iamf_00000000000052f1" in atom_list[9]:
	pass_count += 1
	atom = atom_list[9]["iamf_00000000000052f1"]
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
	if atom[9]["SampleRate"] == 0:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[11]["codec_id"] == "Opus":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[12]["num_samples_per_frame"] == 120:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[13]["audio_roll_distance"] == -32:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "stts_0000000000005393" in atom_list[10]:
	pass_count += 1
	atom = atom_list[10]["stts_0000000000005393"]
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
	if atom[2]["EntryCount"] == 1:
		pass_count += 1
		stts_SampleCountSum = 0
		stts_SampleDeltaSum = 0
		SampleCount = atom[3]["SampleCount_0"]
		no_of_check_items += 1
		if atom[3]["SampleCount_0"] == 800:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		stts_SampleCountSum += SampleCount
		SampleDelta = atom[4]["SampleDelta_0"]
		no_of_check_items += 1
		if atom[4]["SampleDelta_0"] == 120:
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
		if (mdhd_Duration + elst_MediaTime)%120 == (SampleDelta%120):
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		number_of_stts_sample_count = int((mdhd_Duration + elst_MediaTime + 120 - 1)) // 120
		if stts_SampleCountSum == number_of_stts_sample_count:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		stts_end_trimming = (120 - (stts_SampleDeltaSum)%120)%120
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "stsc_00000000000053ab" in atom_list[11]:
	pass_count += 1
	atom = atom_list[11]["stsc_00000000000053ab"]
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
		no_of_check_items += 1
		if atom[3]["FirstChunk_0"] == 1:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[4]["SamplePerChunk_0"] == 200:
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
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "stco_00000000000053c7" in atom_list[12]:
	pass_count += 1
	atom = atom_list[12]["stco_00000000000053c7"]
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
	if atom[2]["EntryCount"] == 4:
		pass_count += 1
		no_of_check_items += 1
		if atom[3]["ChunkOffset_0"] == 40:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[4]["ChunkOffset_1"] == 5214:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[5]["ChunkOffset_2"] == 10429:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[6]["ChunkOffset_3"] == 15616:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "stsz_00000000000053e7" in atom_list[13]:
	pass_count += 1
	atom = atom_list[13]["stsz_00000000000053e7"]
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
	if atom[3]["SampleCount"] == 800:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[4]["EntrySize_0"] == 13:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[5]["EntrySize_1"] == 13:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[6]["EntrySize_2"] == 29:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[7]["EntrySize_3"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[8]["EntrySize_4"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[9]["EntrySize_5"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[10]["EntrySize_6"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[11]["EntrySize_7"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[12]["EntrySize_8"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[13]["EntrySize_9"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[14]["EntrySize_10"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[15]["EntrySize_11"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[16]["EntrySize_12"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[17]["EntrySize_13"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[18]["EntrySize_14"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[19]["EntrySize_15"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[20]["EntrySize_16"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[21]["EntrySize_17"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[22]["EntrySize_18"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[23]["EntrySize_19"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[24]["EntrySize_20"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[25]["EntrySize_21"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[26]["EntrySize_22"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[27]["EntrySize_23"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[28]["EntrySize_24"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[29]["EntrySize_25"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[30]["EntrySize_26"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[31]["EntrySize_27"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[32]["EntrySize_28"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[33]["EntrySize_29"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[34]["EntrySize_30"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[35]["EntrySize_31"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[36]["EntrySize_32"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[37]["EntrySize_33"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[38]["EntrySize_34"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[39]["EntrySize_35"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[40]["EntrySize_36"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[41]["EntrySize_37"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[42]["EntrySize_38"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[43]["EntrySize_39"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[44]["EntrySize_40"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[45]["EntrySize_41"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[46]["EntrySize_42"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[47]["EntrySize_43"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[48]["EntrySize_44"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[49]["EntrySize_45"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[50]["EntrySize_46"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[51]["EntrySize_47"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[52]["EntrySize_48"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[53]["EntrySize_49"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[54]["EntrySize_50"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[55]["EntrySize_51"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[56]["EntrySize_52"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[57]["EntrySize_53"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[58]["EntrySize_54"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[59]["EntrySize_55"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[60]["EntrySize_56"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[61]["EntrySize_57"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[62]["EntrySize_58"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[63]["EntrySize_59"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[64]["EntrySize_60"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[65]["EntrySize_61"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[66]["EntrySize_62"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[67]["EntrySize_63"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[68]["EntrySize_64"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[69]["EntrySize_65"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[70]["EntrySize_66"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[71]["EntrySize_67"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[72]["EntrySize_68"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[73]["EntrySize_69"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[74]["EntrySize_70"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[75]["EntrySize_71"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[76]["EntrySize_72"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[77]["EntrySize_73"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[78]["EntrySize_74"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[79]["EntrySize_75"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[80]["EntrySize_76"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[81]["EntrySize_77"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[82]["EntrySize_78"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[83]["EntrySize_79"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[84]["EntrySize_80"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[85]["EntrySize_81"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[86]["EntrySize_82"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[87]["EntrySize_83"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[88]["EntrySize_84"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[89]["EntrySize_85"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[90]["EntrySize_86"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[91]["EntrySize_87"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[92]["EntrySize_88"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[93]["EntrySize_89"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[94]["EntrySize_90"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[95]["EntrySize_91"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[96]["EntrySize_92"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[97]["EntrySize_93"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[98]["EntrySize_94"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[99]["EntrySize_95"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[100]["EntrySize_96"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[101]["EntrySize_97"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[102]["EntrySize_98"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[103]["EntrySize_99"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[104]["EntrySize_100"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[105]["EntrySize_101"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[106]["EntrySize_102"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[107]["EntrySize_103"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[108]["EntrySize_104"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[109]["EntrySize_105"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[110]["EntrySize_106"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[111]["EntrySize_107"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[112]["EntrySize_108"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[113]["EntrySize_109"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[114]["EntrySize_110"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[115]["EntrySize_111"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[116]["EntrySize_112"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[117]["EntrySize_113"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[118]["EntrySize_114"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[119]["EntrySize_115"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[120]["EntrySize_116"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[121]["EntrySize_117"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[122]["EntrySize_118"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[123]["EntrySize_119"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[124]["EntrySize_120"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[125]["EntrySize_121"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[126]["EntrySize_122"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[127]["EntrySize_123"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[128]["EntrySize_124"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[129]["EntrySize_125"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[130]["EntrySize_126"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[131]["EntrySize_127"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[132]["EntrySize_128"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[133]["EntrySize_129"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[134]["EntrySize_130"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[135]["EntrySize_131"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[136]["EntrySize_132"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[137]["EntrySize_133"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[138]["EntrySize_134"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[139]["EntrySize_135"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[140]["EntrySize_136"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[141]["EntrySize_137"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[142]["EntrySize_138"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[143]["EntrySize_139"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[144]["EntrySize_140"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[145]["EntrySize_141"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[146]["EntrySize_142"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[147]["EntrySize_143"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[148]["EntrySize_144"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[149]["EntrySize_145"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[150]["EntrySize_146"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[151]["EntrySize_147"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[152]["EntrySize_148"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[153]["EntrySize_149"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[154]["EntrySize_150"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[155]["EntrySize_151"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[156]["EntrySize_152"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[157]["EntrySize_153"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[158]["EntrySize_154"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[159]["EntrySize_155"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[160]["EntrySize_156"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[161]["EntrySize_157"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[162]["EntrySize_158"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[163]["EntrySize_159"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[164]["EntrySize_160"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[165]["EntrySize_161"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[166]["EntrySize_162"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[167]["EntrySize_163"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[168]["EntrySize_164"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[169]["EntrySize_165"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[170]["EntrySize_166"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[171]["EntrySize_167"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[172]["EntrySize_168"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[173]["EntrySize_169"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[174]["EntrySize_170"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[175]["EntrySize_171"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[176]["EntrySize_172"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[177]["EntrySize_173"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[178]["EntrySize_174"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[179]["EntrySize_175"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[180]["EntrySize_176"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[181]["EntrySize_177"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[182]["EntrySize_178"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[183]["EntrySize_179"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[184]["EntrySize_180"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[185]["EntrySize_181"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[186]["EntrySize_182"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[187]["EntrySize_183"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[188]["EntrySize_184"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[189]["EntrySize_185"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[190]["EntrySize_186"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[191]["EntrySize_187"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[192]["EntrySize_188"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[193]["EntrySize_189"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[194]["EntrySize_190"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[195]["EntrySize_191"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[196]["EntrySize_192"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[197]["EntrySize_193"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[198]["EntrySize_194"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[199]["EntrySize_195"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[200]["EntrySize_196"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[201]["EntrySize_197"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[202]["EntrySize_198"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[203]["EntrySize_199"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[204]["EntrySize_200"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[205]["EntrySize_201"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[206]["EntrySize_202"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[207]["EntrySize_203"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[208]["EntrySize_204"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[209]["EntrySize_205"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[210]["EntrySize_206"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[211]["EntrySize_207"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[212]["EntrySize_208"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[213]["EntrySize_209"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[214]["EntrySize_210"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[215]["EntrySize_211"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[216]["EntrySize_212"] == 28:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[217]["EntrySize_213"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[218]["EntrySize_214"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[219]["EntrySize_215"] == 28:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[220]["EntrySize_216"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[221]["EntrySize_217"] == 28:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[222]["EntrySize_218"] == 28:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[223]["EntrySize_219"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[224]["EntrySize_220"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[225]["EntrySize_221"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[226]["EntrySize_222"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[227]["EntrySize_223"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[228]["EntrySize_224"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[229]["EntrySize_225"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[230]["EntrySize_226"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[231]["EntrySize_227"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[232]["EntrySize_228"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[233]["EntrySize_229"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[234]["EntrySize_230"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[235]["EntrySize_231"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[236]["EntrySize_232"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[237]["EntrySize_233"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[238]["EntrySize_234"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[239]["EntrySize_235"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[240]["EntrySize_236"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[241]["EntrySize_237"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[242]["EntrySize_238"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[243]["EntrySize_239"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[244]["EntrySize_240"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[245]["EntrySize_241"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[246]["EntrySize_242"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[247]["EntrySize_243"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[248]["EntrySize_244"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[249]["EntrySize_245"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[250]["EntrySize_246"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[251]["EntrySize_247"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[252]["EntrySize_248"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[253]["EntrySize_249"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[254]["EntrySize_250"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[255]["EntrySize_251"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[256]["EntrySize_252"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[257]["EntrySize_253"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[258]["EntrySize_254"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[259]["EntrySize_255"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[260]["EntrySize_256"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[261]["EntrySize_257"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[262]["EntrySize_258"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[263]["EntrySize_259"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[264]["EntrySize_260"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[265]["EntrySize_261"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[266]["EntrySize_262"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[267]["EntrySize_263"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[268]["EntrySize_264"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[269]["EntrySize_265"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[270]["EntrySize_266"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[271]["EntrySize_267"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[272]["EntrySize_268"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[273]["EntrySize_269"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[274]["EntrySize_270"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[275]["EntrySize_271"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[276]["EntrySize_272"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[277]["EntrySize_273"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[278]["EntrySize_274"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[279]["EntrySize_275"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[280]["EntrySize_276"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[281]["EntrySize_277"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[282]["EntrySize_278"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[283]["EntrySize_279"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[284]["EntrySize_280"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[285]["EntrySize_281"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[286]["EntrySize_282"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[287]["EntrySize_283"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[288]["EntrySize_284"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[289]["EntrySize_285"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[290]["EntrySize_286"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[291]["EntrySize_287"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[292]["EntrySize_288"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[293]["EntrySize_289"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[294]["EntrySize_290"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[295]["EntrySize_291"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[296]["EntrySize_292"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[297]["EntrySize_293"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[298]["EntrySize_294"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[299]["EntrySize_295"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[300]["EntrySize_296"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[301]["EntrySize_297"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[302]["EntrySize_298"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[303]["EntrySize_299"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[304]["EntrySize_300"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[305]["EntrySize_301"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[306]["EntrySize_302"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[307]["EntrySize_303"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[308]["EntrySize_304"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[309]["EntrySize_305"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[310]["EntrySize_306"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[311]["EntrySize_307"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[312]["EntrySize_308"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[313]["EntrySize_309"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[314]["EntrySize_310"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[315]["EntrySize_311"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[316]["EntrySize_312"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[317]["EntrySize_313"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[318]["EntrySize_314"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[319]["EntrySize_315"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[320]["EntrySize_316"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[321]["EntrySize_317"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[322]["EntrySize_318"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[323]["EntrySize_319"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[324]["EntrySize_320"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[325]["EntrySize_321"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[326]["EntrySize_322"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[327]["EntrySize_323"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[328]["EntrySize_324"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[329]["EntrySize_325"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[330]["EntrySize_326"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[331]["EntrySize_327"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[332]["EntrySize_328"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[333]["EntrySize_329"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[334]["EntrySize_330"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[335]["EntrySize_331"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[336]["EntrySize_332"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[337]["EntrySize_333"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[338]["EntrySize_334"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[339]["EntrySize_335"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[340]["EntrySize_336"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[341]["EntrySize_337"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[342]["EntrySize_338"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[343]["EntrySize_339"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[344]["EntrySize_340"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[345]["EntrySize_341"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[346]["EntrySize_342"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[347]["EntrySize_343"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[348]["EntrySize_344"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[349]["EntrySize_345"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[350]["EntrySize_346"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[351]["EntrySize_347"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[352]["EntrySize_348"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[353]["EntrySize_349"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[354]["EntrySize_350"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[355]["EntrySize_351"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[356]["EntrySize_352"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[357]["EntrySize_353"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[358]["EntrySize_354"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[359]["EntrySize_355"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[360]["EntrySize_356"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[361]["EntrySize_357"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[362]["EntrySize_358"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[363]["EntrySize_359"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[364]["EntrySize_360"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[365]["EntrySize_361"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[366]["EntrySize_362"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[367]["EntrySize_363"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[368]["EntrySize_364"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[369]["EntrySize_365"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[370]["EntrySize_366"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[371]["EntrySize_367"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[372]["EntrySize_368"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[373]["EntrySize_369"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[374]["EntrySize_370"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[375]["EntrySize_371"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[376]["EntrySize_372"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[377]["EntrySize_373"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[378]["EntrySize_374"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[379]["EntrySize_375"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[380]["EntrySize_376"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[381]["EntrySize_377"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[382]["EntrySize_378"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[383]["EntrySize_379"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[384]["EntrySize_380"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[385]["EntrySize_381"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[386]["EntrySize_382"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[387]["EntrySize_383"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[388]["EntrySize_384"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[389]["EntrySize_385"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[390]["EntrySize_386"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[391]["EntrySize_387"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[392]["EntrySize_388"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[393]["EntrySize_389"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[394]["EntrySize_390"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[395]["EntrySize_391"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[396]["EntrySize_392"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[397]["EntrySize_393"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[398]["EntrySize_394"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[399]["EntrySize_395"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[400]["EntrySize_396"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[401]["EntrySize_397"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[402]["EntrySize_398"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[403]["EntrySize_399"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[404]["EntrySize_400"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[405]["EntrySize_401"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[406]["EntrySize_402"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[407]["EntrySize_403"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[408]["EntrySize_404"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[409]["EntrySize_405"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[410]["EntrySize_406"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[411]["EntrySize_407"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[412]["EntrySize_408"] == 28:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[413]["EntrySize_409"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[414]["EntrySize_410"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[415]["EntrySize_411"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[416]["EntrySize_412"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[417]["EntrySize_413"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[418]["EntrySize_414"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[419]["EntrySize_415"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[420]["EntrySize_416"] == 23:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[421]["EntrySize_417"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[422]["EntrySize_418"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[423]["EntrySize_419"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[424]["EntrySize_420"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[425]["EntrySize_421"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[426]["EntrySize_422"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[427]["EntrySize_423"] == 23:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[428]["EntrySize_424"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[429]["EntrySize_425"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[430]["EntrySize_426"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[431]["EntrySize_427"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[432]["EntrySize_428"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[433]["EntrySize_429"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[434]["EntrySize_430"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[435]["EntrySize_431"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[436]["EntrySize_432"] == 29:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[437]["EntrySize_433"] == 28:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[438]["EntrySize_434"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[439]["EntrySize_435"] == 23:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[440]["EntrySize_436"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[441]["EntrySize_437"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[442]["EntrySize_438"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[443]["EntrySize_439"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[444]["EntrySize_440"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[445]["EntrySize_441"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[446]["EntrySize_442"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[447]["EntrySize_443"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[448]["EntrySize_444"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[449]["EntrySize_445"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[450]["EntrySize_446"] == 30:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[451]["EntrySize_447"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[452]["EntrySize_448"] == 30:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[453]["EntrySize_449"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[454]["EntrySize_450"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[455]["EntrySize_451"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[456]["EntrySize_452"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[457]["EntrySize_453"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[458]["EntrySize_454"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[459]["EntrySize_455"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[460]["EntrySize_456"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[461]["EntrySize_457"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[462]["EntrySize_458"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[463]["EntrySize_459"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[464]["EntrySize_460"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[465]["EntrySize_461"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[466]["EntrySize_462"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[467]["EntrySize_463"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[468]["EntrySize_464"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[469]["EntrySize_465"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[470]["EntrySize_466"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[471]["EntrySize_467"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[472]["EntrySize_468"] == 28:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[473]["EntrySize_469"] == 28:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[474]["EntrySize_470"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[475]["EntrySize_471"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[476]["EntrySize_472"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[477]["EntrySize_473"] == 29:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[478]["EntrySize_474"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[479]["EntrySize_475"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[480]["EntrySize_476"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[481]["EntrySize_477"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[482]["EntrySize_478"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[483]["EntrySize_479"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[484]["EntrySize_480"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[485]["EntrySize_481"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[486]["EntrySize_482"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[487]["EntrySize_483"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[488]["EntrySize_484"] == 29:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[489]["EntrySize_485"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[490]["EntrySize_486"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[491]["EntrySize_487"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[492]["EntrySize_488"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[493]["EntrySize_489"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[494]["EntrySize_490"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[495]["EntrySize_491"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[496]["EntrySize_492"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[497]["EntrySize_493"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[498]["EntrySize_494"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[499]["EntrySize_495"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[500]["EntrySize_496"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[501]["EntrySize_497"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[502]["EntrySize_498"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[503]["EntrySize_499"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[504]["EntrySize_500"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[505]["EntrySize_501"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[506]["EntrySize_502"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[507]["EntrySize_503"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[508]["EntrySize_504"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[509]["EntrySize_505"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[510]["EntrySize_506"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[511]["EntrySize_507"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[512]["EntrySize_508"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[513]["EntrySize_509"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[514]["EntrySize_510"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[515]["EntrySize_511"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[516]["EntrySize_512"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[517]["EntrySize_513"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[518]["EntrySize_514"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[519]["EntrySize_515"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[520]["EntrySize_516"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[521]["EntrySize_517"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[522]["EntrySize_518"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[523]["EntrySize_519"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[524]["EntrySize_520"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[525]["EntrySize_521"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[526]["EntrySize_522"] == 28:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[527]["EntrySize_523"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[528]["EntrySize_524"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[529]["EntrySize_525"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[530]["EntrySize_526"] == 28:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[531]["EntrySize_527"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[532]["EntrySize_528"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[533]["EntrySize_529"] == 28:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[534]["EntrySize_530"] == 28:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[535]["EntrySize_531"] == 28:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[536]["EntrySize_532"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[537]["EntrySize_533"] == 29:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[538]["EntrySize_534"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[539]["EntrySize_535"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[540]["EntrySize_536"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[541]["EntrySize_537"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[542]["EntrySize_538"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[543]["EntrySize_539"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[544]["EntrySize_540"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[545]["EntrySize_541"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[546]["EntrySize_542"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[547]["EntrySize_543"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[548]["EntrySize_544"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[549]["EntrySize_545"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[550]["EntrySize_546"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[551]["EntrySize_547"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[552]["EntrySize_548"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[553]["EntrySize_549"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[554]["EntrySize_550"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[555]["EntrySize_551"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[556]["EntrySize_552"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[557]["EntrySize_553"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[558]["EntrySize_554"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[559]["EntrySize_555"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[560]["EntrySize_556"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[561]["EntrySize_557"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[562]["EntrySize_558"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[563]["EntrySize_559"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[564]["EntrySize_560"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[565]["EntrySize_561"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[566]["EntrySize_562"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[567]["EntrySize_563"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[568]["EntrySize_564"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[569]["EntrySize_565"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[570]["EntrySize_566"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[571]["EntrySize_567"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[572]["EntrySize_568"] == 28:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[573]["EntrySize_569"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[574]["EntrySize_570"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[575]["EntrySize_571"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[576]["EntrySize_572"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[577]["EntrySize_573"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[578]["EntrySize_574"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[579]["EntrySize_575"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[580]["EntrySize_576"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[581]["EntrySize_577"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[582]["EntrySize_578"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[583]["EntrySize_579"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[584]["EntrySize_580"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[585]["EntrySize_581"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[586]["EntrySize_582"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[587]["EntrySize_583"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[588]["EntrySize_584"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[589]["EntrySize_585"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[590]["EntrySize_586"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[591]["EntrySize_587"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[592]["EntrySize_588"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[593]["EntrySize_589"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[594]["EntrySize_590"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[595]["EntrySize_591"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[596]["EntrySize_592"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[597]["EntrySize_593"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[598]["EntrySize_594"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[599]["EntrySize_595"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[600]["EntrySize_596"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[601]["EntrySize_597"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[602]["EntrySize_598"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[603]["EntrySize_599"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[604]["EntrySize_600"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[605]["EntrySize_601"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[606]["EntrySize_602"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[607]["EntrySize_603"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[608]["EntrySize_604"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[609]["EntrySize_605"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[610]["EntrySize_606"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[611]["EntrySize_607"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[612]["EntrySize_608"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[613]["EntrySize_609"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[614]["EntrySize_610"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[615]["EntrySize_611"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[616]["EntrySize_612"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[617]["EntrySize_613"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[618]["EntrySize_614"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[619]["EntrySize_615"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[620]["EntrySize_616"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[621]["EntrySize_617"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[622]["EntrySize_618"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[623]["EntrySize_619"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[624]["EntrySize_620"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[625]["EntrySize_621"] == 30:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[626]["EntrySize_622"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[627]["EntrySize_623"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[628]["EntrySize_624"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[629]["EntrySize_625"] == 28:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[630]["EntrySize_626"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[631]["EntrySize_627"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[632]["EntrySize_628"] == 30:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[633]["EntrySize_629"] == 30:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[634]["EntrySize_630"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[635]["EntrySize_631"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[636]["EntrySize_632"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[637]["EntrySize_633"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[638]["EntrySize_634"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[639]["EntrySize_635"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[640]["EntrySize_636"] == 28:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[641]["EntrySize_637"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[642]["EntrySize_638"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[643]["EntrySize_639"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[644]["EntrySize_640"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[645]["EntrySize_641"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[646]["EntrySize_642"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[647]["EntrySize_643"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[648]["EntrySize_644"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[649]["EntrySize_645"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[650]["EntrySize_646"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[651]["EntrySize_647"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[652]["EntrySize_648"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[653]["EntrySize_649"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[654]["EntrySize_650"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[655]["EntrySize_651"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[656]["EntrySize_652"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[657]["EntrySize_653"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[658]["EntrySize_654"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[659]["EntrySize_655"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[660]["EntrySize_656"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[661]["EntrySize_657"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[662]["EntrySize_658"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[663]["EntrySize_659"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[664]["EntrySize_660"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[665]["EntrySize_661"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[666]["EntrySize_662"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[667]["EntrySize_663"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[668]["EntrySize_664"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[669]["EntrySize_665"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[670]["EntrySize_666"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[671]["EntrySize_667"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[672]["EntrySize_668"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[673]["EntrySize_669"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[674]["EntrySize_670"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[675]["EntrySize_671"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[676]["EntrySize_672"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[677]["EntrySize_673"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[678]["EntrySize_674"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[679]["EntrySize_675"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[680]["EntrySize_676"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[681]["EntrySize_677"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[682]["EntrySize_678"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[683]["EntrySize_679"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[684]["EntrySize_680"] == 28:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[685]["EntrySize_681"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[686]["EntrySize_682"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[687]["EntrySize_683"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[688]["EntrySize_684"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[689]["EntrySize_685"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[690]["EntrySize_686"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[691]["EntrySize_687"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[692]["EntrySize_688"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[693]["EntrySize_689"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[694]["EntrySize_690"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[695]["EntrySize_691"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[696]["EntrySize_692"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[697]["EntrySize_693"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[698]["EntrySize_694"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[699]["EntrySize_695"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[700]["EntrySize_696"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[701]["EntrySize_697"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[702]["EntrySize_698"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[703]["EntrySize_699"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[704]["EntrySize_700"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[705]["EntrySize_701"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[706]["EntrySize_702"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[707]["EntrySize_703"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[708]["EntrySize_704"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[709]["EntrySize_705"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[710]["EntrySize_706"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[711]["EntrySize_707"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[712]["EntrySize_708"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[713]["EntrySize_709"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[714]["EntrySize_710"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[715]["EntrySize_711"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[716]["EntrySize_712"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[717]["EntrySize_713"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[718]["EntrySize_714"] == 29:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[719]["EntrySize_715"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[720]["EntrySize_716"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[721]["EntrySize_717"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[722]["EntrySize_718"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[723]["EntrySize_719"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[724]["EntrySize_720"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[725]["EntrySize_721"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[726]["EntrySize_722"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[727]["EntrySize_723"] == 28:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[728]["EntrySize_724"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[729]["EntrySize_725"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[730]["EntrySize_726"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[731]["EntrySize_727"] == 30:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[732]["EntrySize_728"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[733]["EntrySize_729"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[734]["EntrySize_730"] == 28:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[735]["EntrySize_731"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[736]["EntrySize_732"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[737]["EntrySize_733"] == 28:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[738]["EntrySize_734"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[739]["EntrySize_735"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[740]["EntrySize_736"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[741]["EntrySize_737"] == 31:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[742]["EntrySize_738"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[743]["EntrySize_739"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[744]["EntrySize_740"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[745]["EntrySize_741"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[746]["EntrySize_742"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[747]["EntrySize_743"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[748]["EntrySize_744"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[749]["EntrySize_745"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[750]["EntrySize_746"] == 23:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[751]["EntrySize_747"] == 28:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[752]["EntrySize_748"] == 28:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[753]["EntrySize_749"] == 28:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[754]["EntrySize_750"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[755]["EntrySize_751"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[756]["EntrySize_752"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[757]["EntrySize_753"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[758]["EntrySize_754"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[759]["EntrySize_755"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[760]["EntrySize_756"] == 28:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[761]["EntrySize_757"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[762]["EntrySize_758"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[763]["EntrySize_759"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[764]["EntrySize_760"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[765]["EntrySize_761"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[766]["EntrySize_762"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[767]["EntrySize_763"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[768]["EntrySize_764"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[769]["EntrySize_765"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[770]["EntrySize_766"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[771]["EntrySize_767"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[772]["EntrySize_768"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[773]["EntrySize_769"] == 29:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[774]["EntrySize_770"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[775]["EntrySize_771"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[776]["EntrySize_772"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[777]["EntrySize_773"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[778]["EntrySize_774"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[779]["EntrySize_775"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[780]["EntrySize_776"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[781]["EntrySize_777"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[782]["EntrySize_778"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[783]["EntrySize_779"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[784]["EntrySize_780"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[785]["EntrySize_781"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[786]["EntrySize_782"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[787]["EntrySize_783"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[788]["EntrySize_784"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[789]["EntrySize_785"] == 24:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[790]["EntrySize_786"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[791]["EntrySize_787"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[792]["EntrySize_788"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[793]["EntrySize_789"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[794]["EntrySize_790"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[795]["EntrySize_791"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[796]["EntrySize_792"] == 25:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[797]["EntrySize_793"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[798]["EntrySize_794"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[799]["EntrySize_795"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[800]["EntrySize_796"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[801]["EntrySize_797"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[802]["EntrySize_798"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[803]["EntrySize_799"] == 26:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "sgpd_000000000000607b" in atom_list[14]:
	pass_count += 1
	atom = atom_list[14]["sgpd_000000000000607b"]
	no_of_check_items += 1
	if atom[0]["Version"] == 1:
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
	if atom[2]["GroupingType"] == 1919904876:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3]["DefaultLength"] == 2:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[4]["EntryCount"] == 1:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[5]["GroupingEntryVal_0"] == -32:
			pass_count += 1
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
		if obu["codec_config"].get("codec_id") == 1332770163:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if obu["codec_config"].get("num_samples_per_frame") == 120:
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
			if obu["codec_config"]["decoder_config_opus"].get("pre_skip") == 0:
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
		if obu["codec_config"].get("audio_roll_distance") == -32:
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
				if layouts[0]["loudness"].get("integrated_loudness") == -3954:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if layouts[0]["loudness"].get("digital_peak") == -840:
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
print("""A stereo IAMF stream with no trimming encoded using Opus. It
is invalid because `pre_skip` is incorrectly set to 0.""")
print("is_valid: False")
print("primary_tested_spec_sections: ['3.9/Audio Frame OBU Syntax and Semantics', '3.11.1/pre_skip']")
print("*"*40)

