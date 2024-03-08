import yaml
import inspect
import argparse

parser = argparse.ArgumentParser(description="test_000214_s verification script")
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
with open(args.log,"r",encoding="utf-8-sig") as log_data:
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
if "moov_000000000002aa30" in atom_list[1]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "mvhd_000000000002aa38" in atom_list[2]:
	pass_count += 1
	atom = atom_list[2]["mvhd_000000000002aa38"]
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
if "trak_000000000002aaa4" in atom_list[3]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "tkhd_000000000002aaac" in atom_list[4]:
	pass_count += 1
	atom = atom_list[4]["tkhd_000000000002aaac"]
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
if "edts_000000000002ab08" in atom_list[5]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "elst_000000000002ab10" in atom_list[6]:
	pass_count += 1
	atom = atom_list[6]["elst_000000000002ab10"]
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
	if atom[3]["SegmentDuration_0"] == 240000:
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
if "mdhd_000000000002ab34" in atom_list[7]:
	pass_count += 1
	atom = atom_list[7]["mdhd_000000000002ab34"]
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
if "hdlr_000000000002ab54" in atom_list[8]:
	pass_count += 1
	atom = atom_list[8]["hdlr_000000000002ab54"]
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
if "stbl_000000000002abdf" in atom_list[9]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "stsd_000000000002abe7" in atom_list[10]:
	pass_count += 1
	atom = atom_list[10]["stsd_000000000002abe7"]
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
if "iamf_000000000002abf7" in atom_list[11]:
	pass_count += 1
	atom = atom_list[11]["iamf_000000000002abf7"]
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
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "iacb_000000000002ac1b" in atom_list[12]:
	pass_count += 1
	atom = atom_list[12]["iacb_000000000002ac1b"]
	no_of_check_items += 1
	if atom[0]["configurationVersion"] == 1:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[1]["configOBUs_size"] == 138:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[2]["codec_config_id"] == 200:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[3]["codec_id"] == "Opus":
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[4]["num_samples_per_frame"] == 960:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	no_of_check_items += 1
	if atom[5]["audio_roll_distance"] == -4:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "stts_000000000002acb0" in atom_list[13]:
	pass_count += 1
	atom = atom_list[13]["stts_000000000002acb0"]
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
		if atom[3]["SampleCount_0"] == 250:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		stts_SampleCountSum += SampleCount
		SampleDelta = atom[4]["SampleDelta_0"]
		no_of_check_items += 1
		if atom[4]["SampleDelta_0"] == 960:
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
		if atom[6]["SampleDelta_1"] == 312:
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
		if (mdhd_Duration + elst_MediaTime)%960 == (SampleDelta%960):
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		number_of_stts_sample_count = int((mdhd_Duration + elst_MediaTime + 960 - 1)) // 960
		if stts_SampleCountSum == number_of_stts_sample_count:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		stts_end_trimming = (960 - (stts_SampleDeltaSum)%960)%960
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "stsc_000000000002acd0" in atom_list[14]:
	pass_count += 1
	atom = atom_list[14]["stsc_000000000002acd0"]
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
		if atom[4]["SamplePerChunk_0"] == 25:
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
		if atom[7]["SamplePerChunk_1"] == 1:
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
if "stco_000000000002acf8" in atom_list[15]:
	pass_count += 1
	atom = atom_list[15]["stco_000000000002acf8"]
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
		if atom[4]["ChunkOffset_1"] == 17439:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[5]["ChunkOffset_2"] == 33909:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[6]["ChunkOffset_3"] == 51137:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[7]["ChunkOffset_4"] == 68236:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[8]["ChunkOffset_5"] == 85745:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[9]["ChunkOffset_6"] == 103153:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[10]["ChunkOffset_7"] == 120812:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[11]["ChunkOffset_8"] == 138583:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[12]["ChunkOffset_9"] == 156068:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[13]["ChunkOffset_10"] == 173604:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "stsz_000000000002ad34" in atom_list[16]:
	pass_count += 1
	atom = atom_list[16]["stsz_000000000002ad34"]
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
	if atom[3]["SampleCount"] == 251:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[4]["EntrySize_0"] == 942:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[5]["EntrySize_1"] == 655:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[6]["EntrySize_2"] == 744:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[7]["EntrySize_3"] == 633:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[8]["EntrySize_4"] == 662:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[9]["EntrySize_5"] == 679:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[10]["EntrySize_6"] == 640:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[11]["EntrySize_7"] == 643:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[12]["EntrySize_8"] == 649:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[13]["EntrySize_9"] == 650:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[14]["EntrySize_10"] == 655:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[15]["EntrySize_11"] == 665:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[16]["EntrySize_12"] == 667:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[17]["EntrySize_13"] == 664:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[18]["EntrySize_14"] == 746:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[19]["EntrySize_15"] == 817:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[20]["EntrySize_16"] == 612:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[21]["EntrySize_17"] == 801:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[22]["EntrySize_18"] == 629:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[23]["EntrySize_19"] == 618:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[24]["EntrySize_20"] == 612:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[25]["EntrySize_21"] == 794:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[26]["EntrySize_22"] == 851:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[27]["EntrySize_23"] == 713:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[28]["EntrySize_24"] == 658:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[29]["EntrySize_25"] == 629:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[30]["EntrySize_26"] == 597:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[31]["EntrySize_27"] == 611:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[32]["EntrySize_28"] == 590:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[33]["EntrySize_29"] == 631:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[34]["EntrySize_30"] == 642:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[35]["EntrySize_31"] == 643:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[36]["EntrySize_32"] == 816:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[37]["EntrySize_33"] == 677:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[38]["EntrySize_34"] == 744:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[39]["EntrySize_35"] == 682:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[40]["EntrySize_36"] == 813:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[41]["EntrySize_37"] == 699:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[42]["EntrySize_38"] == 631:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[43]["EntrySize_39"] == 614:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[44]["EntrySize_40"] == 613:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[45]["EntrySize_41"] == 615:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[46]["EntrySize_42"] == 620:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[47]["EntrySize_43"] == 618:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[48]["EntrySize_44"] == 623:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[49]["EntrySize_45"] == 644:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[50]["EntrySize_46"] == 681:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[51]["EntrySize_47"] == 673:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[52]["EntrySize_48"] == 679:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[53]["EntrySize_49"] == 685:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[54]["EntrySize_50"] == 681:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[55]["EntrySize_51"] == 703:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[56]["EntrySize_52"] == 740:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[57]["EntrySize_53"] == 653:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[58]["EntrySize_54"] == 646:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[59]["EntrySize_55"] == 665:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[60]["EntrySize_56"] == 643:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[61]["EntrySize_57"] == 682:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[62]["EntrySize_58"] == 692:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[63]["EntrySize_59"] == 711:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[64]["EntrySize_60"] == 699:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[65]["EntrySize_61"] == 689:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[66]["EntrySize_62"] == 688:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[67]["EntrySize_63"] == 706:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[68]["EntrySize_64"] == 679:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[69]["EntrySize_65"] == 713:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[70]["EntrySize_66"] == 730:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[71]["EntrySize_67"] == 696:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[72]["EntrySize_68"] == 714:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[73]["EntrySize_69"] == 659:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[74]["EntrySize_70"] == 718:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[75]["EntrySize_71"] == 711:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[76]["EntrySize_72"] == 660:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[77]["EntrySize_73"] == 658:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[78]["EntrySize_74"] == 692:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[79]["EntrySize_75"] == 715:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[80]["EntrySize_76"] == 702:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[81]["EntrySize_77"] == 654:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[82]["EntrySize_78"] == 651:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[83]["EntrySize_79"] == 647:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[84]["EntrySize_80"] == 652:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[85]["EntrySize_81"] == 735:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[86]["EntrySize_82"] == 778:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[87]["EntrySize_83"] == 675:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[88]["EntrySize_84"] == 640:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[89]["EntrySize_85"] == 670:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[90]["EntrySize_86"] == 710:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[91]["EntrySize_87"] == 747:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[92]["EntrySize_88"] == 659:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[93]["EntrySize_89"] == 617:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[94]["EntrySize_90"] == 853:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[95]["EntrySize_91"] == 699:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[96]["EntrySize_92"] == 670:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[97]["EntrySize_93"] == 641:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[98]["EntrySize_94"] == 651:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[99]["EntrySize_95"] == 655:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[100]["EntrySize_96"] == 648:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[101]["EntrySize_97"] == 688:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[102]["EntrySize_98"] == 678:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[103]["EntrySize_99"] == 664:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[104]["EntrySize_100"] == 654:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[105]["EntrySize_101"] == 667:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[106]["EntrySize_102"] == 695:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[107]["EntrySize_103"] == 661:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[108]["EntrySize_104"] == 661:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[109]["EntrySize_105"] == 654:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[110]["EntrySize_106"] == 773:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[111]["EntrySize_107"] == 651:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[112]["EntrySize_108"] == 826:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[113]["EntrySize_109"] == 625:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[114]["EntrySize_110"] == 655:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[115]["EntrySize_111"] == 673:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[116]["EntrySize_112"] == 672:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[117]["EntrySize_113"] == 685:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[118]["EntrySize_114"] == 707:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[119]["EntrySize_115"] == 716:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[120]["EntrySize_116"] == 711:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[121]["EntrySize_117"] == 707:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[122]["EntrySize_118"] == 735:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[123]["EntrySize_119"] == 790:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[124]["EntrySize_120"] == 759:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[125]["EntrySize_121"] == 755:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[126]["EntrySize_122"] == 711:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[127]["EntrySize_123"] == 674:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[128]["EntrySize_124"] == 692:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[129]["EntrySize_125"] == 681:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[130]["EntrySize_126"] == 679:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[131]["EntrySize_127"] == 756:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[132]["EntrySize_128"] == 684:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[133]["EntrySize_129"] == 664:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[134]["EntrySize_130"] == 730:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[135]["EntrySize_131"] == 811:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[136]["EntrySize_132"] == 739:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[137]["EntrySize_133"] == 680:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[138]["EntrySize_134"] == 665:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[139]["EntrySize_135"] == 673:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[140]["EntrySize_136"] == 656:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[141]["EntrySize_137"] == 676:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[142]["EntrySize_138"] == 691:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[143]["EntrySize_139"] == 679:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[144]["EntrySize_140"] == 671:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[145]["EntrySize_141"] == 675:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[146]["EntrySize_142"] == 686:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[147]["EntrySize_143"] == 686:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[148]["EntrySize_144"] == 703:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[149]["EntrySize_145"] == 729:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[150]["EntrySize_146"] == 684:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[151]["EntrySize_147"] == 699:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[152]["EntrySize_148"] == 704:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[153]["EntrySize_149"] == 707:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[154]["EntrySize_150"] == 704:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[155]["EntrySize_151"] == 705:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[156]["EntrySize_152"] == 696:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[157]["EntrySize_153"] == 703:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[158]["EntrySize_154"] == 714:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[159]["EntrySize_155"] == 701:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[160]["EntrySize_156"] == 707:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[161]["EntrySize_157"] == 708:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[162]["EntrySize_158"] == 713:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[163]["EntrySize_159"] == 730:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[164]["EntrySize_160"] == 707:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[165]["EntrySize_161"] == 695:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[166]["EntrySize_162"] == 712:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[167]["EntrySize_163"] == 704:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[168]["EntrySize_164"] == 737:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[169]["EntrySize_165"] == 729:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[170]["EntrySize_166"] == 701:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[171]["EntrySize_167"] == 699:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[172]["EntrySize_168"] == 702:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[173]["EntrySize_169"] == 709:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[174]["EntrySize_170"] == 707:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[175]["EntrySize_171"] == 700:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[176]["EntrySize_172"] == 692:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[177]["EntrySize_173"] == 686:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[178]["EntrySize_174"] == 698:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[179]["EntrySize_175"] == 738:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[180]["EntrySize_176"] == 704:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[181]["EntrySize_177"] == 727:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[182]["EntrySize_178"] == 695:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[183]["EntrySize_179"] == 688:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[184]["EntrySize_180"] == 702:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[185]["EntrySize_181"] == 720:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[186]["EntrySize_182"] == 940:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[187]["EntrySize_183"] == 684:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[188]["EntrySize_184"] == 719:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[189]["EntrySize_185"] == 712:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[190]["EntrySize_186"] == 649:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[191]["EntrySize_187"] == 688:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[192]["EntrySize_188"] == 701:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[193]["EntrySize_189"] == 687:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[194]["EntrySize_190"] == 662:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[195]["EntrySize_191"] == 681:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[196]["EntrySize_192"] == 718:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[197]["EntrySize_193"] == 696:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[198]["EntrySize_194"] == 706:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[199]["EntrySize_195"] == 705:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[200]["EntrySize_196"] == 698:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[201]["EntrySize_197"] == 715:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[202]["EntrySize_198"] == 687:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[203]["EntrySize_199"] == 749:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[204]["EntrySize_200"] == 687:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[205]["EntrySize_201"] == 682:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[206]["EntrySize_202"] == 756:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[207]["EntrySize_203"] == 679:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[208]["EntrySize_204"] == 678:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[209]["EntrySize_205"] == 831:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[210]["EntrySize_206"] == 666:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[211]["EntrySize_207"] == 663:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[212]["EntrySize_208"] == 659:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[213]["EntrySize_209"] == 674:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[214]["EntrySize_210"] == 681:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[215]["EntrySize_211"] == 691:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[216]["EntrySize_212"] == 692:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[217]["EntrySize_213"] == 754:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[218]["EntrySize_214"] == 687:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[219]["EntrySize_215"] == 671:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[220]["EntrySize_216"] == 694:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[221]["EntrySize_217"] == 708:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[222]["EntrySize_218"] == 693:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[223]["EntrySize_219"] == 697:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[224]["EntrySize_220"] == 712:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[225]["EntrySize_221"] == 713:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[226]["EntrySize_222"] == 704:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[227]["EntrySize_223"] == 687:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[228]["EntrySize_224"] == 726:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[229]["EntrySize_225"] == 690:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[230]["EntrySize_226"] == 707:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[231]["EntrySize_227"] == 701:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[232]["EntrySize_228"] == 701:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[233]["EntrySize_229"] == 706:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[234]["EntrySize_230"] == 696:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[235]["EntrySize_231"] == 698:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[236]["EntrySize_232"] == 682:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[237]["EntrySize_233"] == 692:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[238]["EntrySize_234"] == 723:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[239]["EntrySize_235"] == 706:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[240]["EntrySize_236"] == 705:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[241]["EntrySize_237"] == 710:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[242]["EntrySize_238"] == 721:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[243]["EntrySize_239"] == 724:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[244]["EntrySize_240"] == 700:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[245]["EntrySize_241"] == 740:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[246]["EntrySize_242"] == 728:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[247]["EntrySize_243"] == 701:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[248]["EntrySize_244"] == 708:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[249]["EntrySize_245"] == 687:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[250]["EntrySize_246"] == 667:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[251]["EntrySize_247"] == 669:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[252]["EntrySize_248"] == 671:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[253]["EntrySize_249"] == 703:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		no_of_check_items += 1
		if atom[254]["EntrySize_250"] == 1036:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items += 1
if "sgpd_000000000002b134" in atom_list[17]:
	pass_count += 1
	atom = atom_list[17]["sgpd_000000000002b134"]
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
		if atom[5]["GroupingEntryVal_0"] == -4:
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
		if obu["codec_config"].get("num_samples_per_frame") == 960:
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
		if obu["codec_config"].get("audio_roll_distance") == -4:
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
			if channel_audio_layer_configs[0].get("loudspeaker_layout") == 8:
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
			if channel_audio_layer_configs[0].get("substream_count") == 4:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			no_of_check_items += 1
			if channel_audio_layer_configs[0].get("coupled_substream_count") == 2:
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
				if layouts[0]["loudness"].get("integrated_loudness") == -4710:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if layouts[0]["loudness"].get("digital_peak") == -687:
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
				if layouts[1]["loudness"].get("integrated_loudness") == -4717:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				no_of_check_items += 1
				if layouts[1]["loudness"].get("digital_peak") == -998:
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
print("""A simple example of an Opus 3.1.2 IAMF stream and no
parameter blocks.""")
print("is_valid: True")
print("primary_tested_spec_sections: ['3.2/num_samples_to_trim_at_end', '3.2/num_samples_to_trim_at_start', '3.6.2/loudspeaker_layout == 3.1.2', '3.11.1/OPUS Specific', '3.11.1/pre_skip']")
print("*"*40)

