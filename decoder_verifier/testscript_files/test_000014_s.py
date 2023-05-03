import yaml
import inspect
import argparse

parser = argparse.ArgumentParser(description="test_000014 verification script")
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
	if atom[0]["MajorBrands"] == "mp42":
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

if "moov_0000000000001526" in atom_list[1]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

if "mvhd_000000000000152e" in atom_list[2]:
	pass_count += 1
	atom = atom_list[2]["mvhd_000000000000152e"]
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
	if atom[4]["TimeScale"] == 1000:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
	if atom[5]["Duration"] == 1500:
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

if "trak_000000000000159a" in atom_list[3]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

if "tkhd_00000000000015a2" in atom_list[4]:
	pass_count += 1
	atom = atom_list[4]["tkhd_00000000000015a2"]
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
	if atom[6]["Duration"] == 1500:
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

if "mdhd_0000000000001606" in atom_list[5]:
	pass_count += 1
	atom = atom_list[5]["mdhd_0000000000001606"]
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
	if atom[5]["Duration"] == 24000:
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

if "hdlr_0000000000001626" in atom_list[6]:
	pass_count += 1
	atom = atom_list[6]["hdlr_0000000000001626"]
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

if "stbl_00000000000016b1" in atom_list[7]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

if "stsd_00000000000016b9" in atom_list[8]:
	pass_count += 1
	atom = atom_list[8]["stsd_00000000000016b9"]
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

if "iamf_00000000000016c9" in atom_list[9]:
	pass_count += 1
	atom = atom_list[9]["iamf_00000000000016c9"]
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

if "iamd_00000000000016ed" in atom_list[10]:
	pass_count += 1
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

if "stts_0000000000001770" in atom_list[11]:
	pass_count += 1
	atom = atom_list[11]["stts_0000000000001770"]
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
		if atom[3]["SampleCount_0"] == 200:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[4]["SampleDelta_0"] == 120:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

if "stsc_0000000000001788" in atom_list[12]:
	pass_count += 1
	atom = atom_list[12]["stsc_0000000000001788"]
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
	if atom[2]["EntryCount"] == 2:
		pass_count += 1
		if atom[3]["FirstChunk_0"] == 1:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[4]["SamplePerChunk_0"] == 66:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[5]["SampleDescriptionIndex_0"] == 1:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[6]["FirstChunk_1"] == 4:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[7]["SamplePerChunk_1"] == 2:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[8]["SampleDescriptionIndex_1"] == 1:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

if "stsz_00000000000017d0" in atom_list[13]:
	pass_count += 1
	atom = atom_list[13]["stsz_00000000000017d0"]
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
	if atom[3]["SampleCount"] == 200:
		pass_count += 1
	else:
		frame = inspect.currentframe()
		print("failure line is #%d."%(frame.f_lineno))
		if atom[4]["EntrySize_0"] == 14:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[5]["EntrySize_1"] == 14:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[6]["EntrySize_2"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[7]["EntrySize_3"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[8]["EntrySize_4"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[9]["EntrySize_5"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[10]["EntrySize_6"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[11]["EntrySize_7"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[12]["EntrySize_8"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[13]["EntrySize_9"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[14]["EntrySize_10"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[15]["EntrySize_11"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[16]["EntrySize_12"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[17]["EntrySize_13"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[18]["EntrySize_14"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[19]["EntrySize_15"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[20]["EntrySize_16"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[21]["EntrySize_17"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[22]["EntrySize_18"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[23]["EntrySize_19"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[24]["EntrySize_20"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[25]["EntrySize_21"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[26]["EntrySize_22"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[27]["EntrySize_23"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[28]["EntrySize_24"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[29]["EntrySize_25"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[30]["EntrySize_26"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[31]["EntrySize_27"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[32]["EntrySize_28"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[33]["EntrySize_29"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[34]["EntrySize_30"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[35]["EntrySize_31"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[36]["EntrySize_32"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[37]["EntrySize_33"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[38]["EntrySize_34"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[39]["EntrySize_35"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[40]["EntrySize_36"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[41]["EntrySize_37"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[42]["EntrySize_38"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[43]["EntrySize_39"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[44]["EntrySize_40"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[45]["EntrySize_41"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[46]["EntrySize_42"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[47]["EntrySize_43"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[48]["EntrySize_44"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[49]["EntrySize_45"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[50]["EntrySize_46"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[51]["EntrySize_47"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[52]["EntrySize_48"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[53]["EntrySize_49"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[54]["EntrySize_50"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[55]["EntrySize_51"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[56]["EntrySize_52"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[57]["EntrySize_53"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[58]["EntrySize_54"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[59]["EntrySize_55"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[60]["EntrySize_56"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[61]["EntrySize_57"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[62]["EntrySize_58"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[63]["EntrySize_59"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[64]["EntrySize_60"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[65]["EntrySize_61"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[66]["EntrySize_62"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[67]["EntrySize_63"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[68]["EntrySize_64"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[69]["EntrySize_65"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[70]["EntrySize_66"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[71]["EntrySize_67"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[72]["EntrySize_68"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[73]["EntrySize_69"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[74]["EntrySize_70"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[75]["EntrySize_71"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[76]["EntrySize_72"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[77]["EntrySize_73"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[78]["EntrySize_74"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[79]["EntrySize_75"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[80]["EntrySize_76"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[81]["EntrySize_77"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[82]["EntrySize_78"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[83]["EntrySize_79"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[84]["EntrySize_80"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[85]["EntrySize_81"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[86]["EntrySize_82"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[87]["EntrySize_83"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[88]["EntrySize_84"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[89]["EntrySize_85"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[90]["EntrySize_86"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[91]["EntrySize_87"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[92]["EntrySize_88"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[93]["EntrySize_89"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[94]["EntrySize_90"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[95]["EntrySize_91"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[96]["EntrySize_92"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[97]["EntrySize_93"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[98]["EntrySize_94"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[99]["EntrySize_95"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[100]["EntrySize_96"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[101]["EntrySize_97"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[102]["EntrySize_98"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[103]["EntrySize_99"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[104]["EntrySize_100"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[105]["EntrySize_101"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[106]["EntrySize_102"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[107]["EntrySize_103"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[108]["EntrySize_104"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[109]["EntrySize_105"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[110]["EntrySize_106"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[111]["EntrySize_107"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[112]["EntrySize_108"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[113]["EntrySize_109"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[114]["EntrySize_110"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[115]["EntrySize_111"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[116]["EntrySize_112"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[117]["EntrySize_113"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[118]["EntrySize_114"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[119]["EntrySize_115"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[120]["EntrySize_116"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[121]["EntrySize_117"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[122]["EntrySize_118"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[123]["EntrySize_119"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[124]["EntrySize_120"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[125]["EntrySize_121"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[126]["EntrySize_122"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[127]["EntrySize_123"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[128]["EntrySize_124"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[129]["EntrySize_125"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[130]["EntrySize_126"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[131]["EntrySize_127"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[132]["EntrySize_128"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[133]["EntrySize_129"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[134]["EntrySize_130"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[135]["EntrySize_131"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[136]["EntrySize_132"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[137]["EntrySize_133"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[138]["EntrySize_134"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[139]["EntrySize_135"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[140]["EntrySize_136"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[141]["EntrySize_137"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[142]["EntrySize_138"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[143]["EntrySize_139"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[144]["EntrySize_140"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[145]["EntrySize_141"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[146]["EntrySize_142"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[147]["EntrySize_143"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[148]["EntrySize_144"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[149]["EntrySize_145"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[150]["EntrySize_146"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[151]["EntrySize_147"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[152]["EntrySize_148"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[153]["EntrySize_149"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[154]["EntrySize_150"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[155]["EntrySize_151"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[156]["EntrySize_152"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[157]["EntrySize_153"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[158]["EntrySize_154"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[159]["EntrySize_155"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[160]["EntrySize_156"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[161]["EntrySize_157"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[162]["EntrySize_158"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[163]["EntrySize_159"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[164]["EntrySize_160"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[165]["EntrySize_161"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[166]["EntrySize_162"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[167]["EntrySize_163"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[168]["EntrySize_164"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[169]["EntrySize_165"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[170]["EntrySize_166"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[171]["EntrySize_167"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[172]["EntrySize_168"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[173]["EntrySize_169"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[174]["EntrySize_170"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[175]["EntrySize_171"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[176]["EntrySize_172"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[177]["EntrySize_173"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[178]["EntrySize_174"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[179]["EntrySize_175"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[180]["EntrySize_176"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[181]["EntrySize_177"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[182]["EntrySize_178"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[183]["EntrySize_179"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[184]["EntrySize_180"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[185]["EntrySize_181"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[186]["EntrySize_182"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[187]["EntrySize_183"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[188]["EntrySize_184"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[189]["EntrySize_185"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[190]["EntrySize_186"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[191]["EntrySize_187"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[192]["EntrySize_188"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[193]["EntrySize_189"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[194]["EntrySize_190"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[195]["EntrySize_191"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[196]["EntrySize_192"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[197]["EntrySize_193"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[198]["EntrySize_194"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[199]["EntrySize_195"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[200]["EntrySize_196"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[201]["EntrySize_197"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[202]["EntrySize_198"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[203]["EntrySize_199"] == 27:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

if "stco_00000000000017b0" in atom_list[14]:
	pass_count += 1
	atom = atom_list[14]["stco_00000000000017b0"]
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
	if atom[2]["EntryCount"] == 4:
		pass_count += 1
		if atom[3]["ChunkOffset_0"] == 40:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[4]["ChunkOffset_1"] == 1796:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[5]["ChunkOffset_2"] == 3578:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if atom[6]["ChunkOffset_3"] == 5360:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
else:
	frame = inspect.currentframe()
	print("failure line is #%d."%(frame.f_lineno))

no_of_check_items = 104
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
		if obu["codec_config"].get("codec_id") == 1332770163:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if obu["codec_config"].get("num_samples_per_frame") == 120:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if obu["codec_config"].get("roll_distance") == -32:
			pass_count += 1
		else:
			frame = inspect.currentframe()
			print("failure line is #%d."%(frame.f_lineno))
		if obu["codec_config"].get("decoder_config_opus") is not None:
			pass_count += 1
			if obu["codec_config"]["decoder_config_opus"].get("version") == 1:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			if obu["codec_config"]["decoder_config_opus"].get("output_channel_count") == 2:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			if obu["codec_config"]["decoder_config_opus"].get("pre_skip") == 0:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			if obu["codec_config"]["decoder_config_opus"].get("input_sample_rate") == 48000:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
			if obu["codec_config"]["decoder_config_opus"].get("output_gain") == 0:
				pass_count += 1
			else:
				frame = inspect.currentframe()
				print("failure line is #%d."%(frame.f_lineno))
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
						if audio_elements[0]["element_mix_config"]["mix_gain"]["param_definition"].get("parameter_rate") == 48000:
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
					if sub_mixes[0]["output_mix_config"]["output_mix_gain"]["param_definition"].get("parameter_rate") == 48000:
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
				if layouts[0]["loudness"].get("integrated_loudness") == -3485:
					pass_count += 1
				else:
					frame = inspect.currentframe()
					print("failure line is #%d."%(frame.f_lineno))
				if layouts[0]["loudness"].get("digital_peak") == -2639:
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
		if sync_array[1].get("obu_id") == 0:
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

no_of_check_items = 86
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
	