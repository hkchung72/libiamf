from typing import List, Dict, Union, Optional
from pydantic import BaseModel, validator, root_validator
from enum import IntEnum
from collections import defaultdict
import math

def four_cc(string:str):
    ret = 0
    for i in [ord(s) for s in string]:
        ret = (ret<<8) + i
    return ret

""" IA Sequence Header OBU Validation """
class IaSequenceHeaderOBU(BaseModel):
    ia_code: int
    primary_profile: int
    additional_profile: int
    
    @validator('ia_code')
    def check_ia_code(cls, value):
        if not (value == four_cc('iamf')):
            raise ValueError("'ia_code' must be 'iamf'")
        return value
    
    @validator('primary_profile')
    def check_primary_profile(cls, value):
        if not (value == 0 or 
                value == 1):
            raise ValueError("'primary_profile' must be set to 0 or 1 in this version")
        return value    
    
    
""" Codec Config OBU Validation """
class LpcmFormatFlags(IntEnum):
    LPCM_BIG_ENDIAN = 0
    LCPM_LITTLE_ENDIAN = 1
    
class DecoderConfigLpcm(BaseModel):
    sample_format_flags: LpcmFormatFlags
    sample_size: int
    sample_rate: int
    
    @validator('sample_size')
    def check_sample_size(cls, value):
        if not (value == 16 or 
                value == 24 or 
                value == 32):
            raise ValueError("'sample_size' SHALL take a value from the set 16, 24 or 32")    
        return value
    
    @validator('sample_rate')
    def check_sample_rate(cls, value):
        if not (value == 44100 or
                value == 16000 or
                value == 32000 or
                value == 48000 or
                value == 96000):
            raise ValueError("'sample_rate' SHALL take a value from the set 44.1k, 16k, 32k, 48k, 96k")
        return value
    
class DecoderConfigOpus(BaseModel):
    version: int
    output_channel_count:int
    pre_skip: int
    input_sample_rate:int
    output_gain: int
    mapping_family: int
    
    # [RFC7845] Ogg Encapsulation for the Opus Audio Codec
    # https://www.rfc-editor.org/rfc/rfc7845
    @validator('version')
    def check_version(cls, value):
        if not (value == 1):
            raise ValueError("'version' must be set to 1")    
        return value
    
    @validator('output_channel_count')
    def check_output_channel_count(cls, value):
        if not (value == 2):
            raise ValueError("'output_channel_count' SHALL be set to 2")
        return value

    @validator('output_gain')
    def check_output_gain(cls, value):
        if not (value == 0):
            raise ValueError("'output_gain' SHALL be set to 0dB")
        return value
    
    @validator('mapping_family')
    def check_mapping_family(cls, value):
        if not (value == 0 or value == 1 or value == 2):
            raise ValueError("'mapping_family' must take a value from the set 0, 1 or 2")
        return value
    
class AacSampleFrequencyIndex(IntEnum):
  AAC_SAMPLE_FREQUENCY_INDEX_INVALID = 0
  AAC_SAMPLE_FREQUENCY_INDEX_96000 = 1
  AAC_SAMPLE_FREQUENCY_INDEX_88200 = 2
  AAC_SAMPLE_FREQUENCY_INDEX_64000 = 3
  AAC_SAMPLE_FREQUENCY_INDEX_48000 = 4
  AAC_SAMPLE_FREQUENCY_INDEX_44100 = 5
  AAC_SAMPLE_FREQUENCY_INDEX_32000 = 6
  AAC_SAMPLE_FREQUENCY_INDEX_23000 = 7
  AAC_SAMPLE_FREQUENCY_INDEX_22050 = 8
  AAC_SAMPLE_FREQUENCY_INDEX_16000 = 9
  AAC_SAMPLE_FREQUENCY_INDEX_12000 = 10
  AAC_SAMPLE_FREQUENCY_INDEX_11025 = 11
  AAC_SAMPLE_FREQUENCY_INDEX_8000 = 12
  AAC_SAMPLE_FREQUENCY_INDEX_7350 = 13
  AAC_SAMPLE_FREQUENCY_INDEX_RESERVED_A = 14
  AAC_SAMPLE_FREQUENCY_INDEX_RESERVED_B = 15
  AAC_SAMPLE_FREQUENCY_INDEX_ESCAPE_VALUE = 16


class AacDecoderSpecificInfo(BaseModel):
    decoder_specific_info_descriptor_tag: int
    audio_object_type: int
    sample_frequency_index: Optional[AacSampleFrequencyIndex] = None
    sampling_frequency: Optional[int] = None
    channel_configuration: int

    @validator('decoder_specific_info_descriptor_tag')
    def check_decoder_specific_info_descriptor_tag(cls, value):
        if not (value == 5):
            raise ValueError("'decoder_specific_info_descriptor_tag' must be 4")
        return value
    
    @validator('audio_object_type')
    def check_audio_object_type(cls, value):
        if not(value == 2):
            raise ValueError("'audio_object_type' must be 0x40")
        return value
    
    @validator('channel_configuration')
    def check_channel_configuration(cls, value):
        if not (value == 2):
            raise ValueError("'channel_configuration' must be 2")
        return value

class AacGaSpecificConfig(BaseModel):
    frame_length_flag: int
    depends_on_core_coder: int
    extension_flag: int

    @validator('frame_length_flag')
    def check_frame_length_flag(cls, value):
        if not (value == 0):
            raise ValueError("'frame_length_flag' must be 0")
        return value
    
    @validator('depends_on_core_coder')
    def check_depends_on_core_coder(cls, value):
        if not (value == 0):
            raise ValueError("'depends_on_core_coder' must be 0")
        return value
    
    @validator('extension_flag')
    def check_extension_flag(cls, value):
        if not (value == 0):
            raise ValueError("'extension_flag' must be 0")
        return value


class DecoderConfigAac(BaseModel):
    decoder_config_descriptor_tag: int
    object_type_indication: int
    stream_type: int
    buffer_size_db: Optional[int] = None
    max_bitrate: Optional[int] = None
    average_bit_rate: Optional[int] = None
    
    decoder_specific_info: AacDecoderSpecificInfo
    ga_specific_config: AacGaSpecificConfig
    
    @validator('decoder_config_descriptor_tag')
    def check_decoder_config_descriptor_tag(cls, value):
        if not (value == 4):
            raise ValueError("'decoder_config_descriptor_tag' must be 4")
        return value
    
    @validator('object_type_indication')
    def check_object_type_indication(cls, value):
        if not (value == 0x40):
            raise ValueError("'object_type_indication' must be 0x40")
        return value
    
    @validator('stream_type')
    def check_stream_type(cls, value):
        if not (value == 0x05):
            raise ValueError("'stream_type' must be 0x05")
        return value
        
class FlacBlockType(IntEnum):
    FLAC_BLOCK_TYPE_INVALID = 0
    FLAC_BLOCK_TYPE_STREAMINFO = 1
    FLAC_BLOCK_TYPE_PADDING = 2
    FLAC_BLOCK_TYPE_APPLICATION = 3
    FLAC_BLOCK_TYPE_SEEKTABLE = 4
    FLAC_BLOCK_TYPE_VORBIS_COMMENT = 5
    FLAC_BLOCK_TYPE_CUESHEET = 6
    FLAC_BLOCK_TYPE_PICTURE = 7
    
class FlacMetaBlockHeader(BaseModel):
    last_metadata_block_flag: int
    block_type: FlacBlockType
    metadata_data_block_length: int
    
    
class FlacMetaBlockStreamInfo(BaseModel):
    minimum_block_size: int
    maximum_block_size: int
    minimum_frame_size: int
    maximum_frame_size: int
    sample_rate: int
    number_of_channels: int
    bits_per_sample: int
    total_samples_in_stream: int
    md5_signature: str | int
    
    @validator('minimum_frame_size')
    def check_minimum_frame_size(cls, value):
        if not (value==0):
            raise ValueError("'minimum_frame_size' must be 0")
        return value
    
    @validator('maximum_frame_size')
    def check_maximum_frame_size(cls, value):
        if not (value==0):
            raise ValueError("'maximum_frame_size' must be 0")
        return value
    
    @validator('number_of_channels')
    def check_number_of_channels(cls, value):
        if not (value == 1):
            raise ValueError("'number_of_channels' must be 1")
        return value    
    
class FlacMetaBlock(BaseModel):
    header: FlacMetaBlockHeader    
    stream_info: Optional[FlacMetaBlockStreamInfo] = None
    generic_block: Optional[str] = None
    
class DecoderConfigFlac(BaseModel):
    metadata_blocks: List[FlacMetaBlock]


class CodecConfig(BaseModel):
    codec_id: int
    num_samples_per_frame: int
    audio_roll_distance: int
    
    # oneof decoder_config: Union[DecoderConfigLpcm, DecoderConfigOpus, DecoderConfigAac, DecoderConfigFlac]
    decoder_config_lpcm: Optional[DecoderConfigLpcm] = None
    decoder_config_opus: Optional[DecoderConfigOpus] = None
    decoder_config_aac: Optional[DecoderConfigAac] = None
    decoder_config_flac: Optional[DecoderConfigFlac] = None
        
    @validator('codec_id')
    def check_codec_id(cls, value):
        if not (value == four_cc('Opus') or
                value == four_cc('mp4a') or
                value == four_cc('fLaC') or
                value == four_cc('ipcm')):
            raise ValueError("'codec_id' SHALL be set to one of four codec_id values (Opus, mp4a, fLaC or ipcm)")
        return value
    
    @validator('num_samples_per_frame')
    def check_num_sample_per_frame(cls, value):
        if (value == 0):
            raise ValueError("'num_sample_per_frame' SHALL NOT be set to 0")
        return value
    
    @validator('audio_roll_distance')
    def check_audio_roll_instance(cls, value, values):
        codec_id = values.get('codec_id')
        if codec_id == four_cc('fLaC') or codec_id == four_cc('ipcm'):
            if not (value == 0):
                raise ValueError("'audio_roll_distance' SHALL be set to 0 when 'codec_id' is set to 'fLac' or 'ipcm'")
        elif codec_id == four_cc('mp4a'):
            if not (value == -1):
                raise ValueError("'audio_roll_distance' SHALL be set to -1 when 'codec_id' is set to 'mp4a'")
        elif codec_id == four_cc('Opus'):
            R_value = math.ceil(3840/values.get('num_samples_per_frame'))
            if not (abs(value) == R_value):
                raise ValueError("'audio_roll_distance' SHALL be set to -R when 'codec_id' is set to 'Opus'. Where, R is the smallest integer greater than or equal to floor(3840/num_samples_per_frame)")
        
        return value
    
class CodecConfigOBU(BaseModel):
    codec_config_id: int
    codec_config: CodecConfig

   
""" Parameter Block OBU Validation """
class AnimationType(IntEnum):
    ANIMATE_STEP = 0
    ANIMATE_LINEAR = 1
    ANIMATE_BEZIER = 2
    
class AnimationStepInt(BaseModel):
    start_point_value: int

class AnimationLinearInt(BaseModel):
    start_point_value: int
    end_point_value: int
    
class AnimationBezierInt(BaseModel):
    start_point_value: int
    end_point_value: int
    control_point_value: int
    control_point_relative_time: int
    
class AnimatedParameterDataInt(BaseModel):
    # oneof parameter_data: Union[AnimationStepInt,AnimationLinearInt,AnimationBezierInt]
    step: Optional[AnimationStepInt] = None
    linear: Optional[AnimationLinearInt] = None
    bezier: Optional[AnimationBezierInt] = None 
    
class MixGainParameterData(BaseModel):
    animation_type: AnimationType
    param_data: AnimatedParameterDataInt
    
class DMixPMode(IntEnum):
  #                       (alpha, beta,  gamma, delta, w_idx_offset)
  DMIXP_MODE_1 = 0  #    (    1,     1, 0.707, 0.707,           -1)
  DMIXP_MODE_2 = 1  #    (0.707, 0.707, 0.707, 0.707,           -1)
  DMIXP_MODE_3 = 2  #    (    1, 0.866, 0.866, 0.866,           -1)
  # reserved = 3
  DMIXP_MODE_1_N = 4  #  (    1,     1, 0.707, 0.707,            1)
  DMIXP_MODE_2_N = 5  #  (0.707, 0.707, 0.707, 0.707,            1)
  DMIXP_MODE_3_N = 6  #  (    1, 0.866, 0.866, 0.866,            1)
  # reserved = 7
  
class DemixingInfoParameterData(BaseModel):
    dmixp_mode: DMixPMode
    # reserved: 5 bits
    
class ReconGainParameterData(BaseModel):
    # TODO: ReconGainParamDefinition
    pass

class ParameterSubblock(BaseModel):
    subblock_duration: Optional[int] = None
    
    # oneof parameter_data: Union[MixGainParameterData,DemixingInfoParameterData,ReconGainParameterData]    
    mix_gain_parameter_data: Optional[MixGainParameterData] = None
    demixing_info_parameter_data: Optional[DemixingInfoParameterData] = None
    recon_gain_parameter_data: Optional[ReconGainParameterData] = None
    
class ParameterBlockOBU(BaseModel):
    parameter_id: int
    duration: Optional[int] = None
    num_subblocks: Optional[int] = None
    constant_subblock_duration: Optional[int] = None
    subblocks: Optional[List[ParameterSubblock]] = None
    # start_timestamp in Sync??
    
    def __hash__(self):
        return self.parameter_id
    
""" Param Definition Validation """
class ParamDefinition(BaseModel):
    parameter_id: int
    parameter_rate: int
    param_definition_mode: int
    # reserved: 7 bits
    duration: Optional[int] = None
    constant_subblock_duration: Optional[int] = None
    num_subblocks: Optional[int] = None
    subblock_durations: Optional[List[int]] = None
    
    @validator('parameter_rate')
    def check_parameter_rate(cls, value):
        if (value == 0):
            raise ValueError("'parameter_rate' SHALL be non-zero integer")
        return value
    
    @root_validator(pre=True)
    def check_param_definition_mode(cls, values):
        if values.get('param_definition_mode') == 0:
            if (values.get('duration') is None and
                values.get('num_subblocks') is None and
                values.get('constant_subblock_duration') is None and
                values.get('subblock_durations') is None):
                raise ValueError("When 'param_definition_mode' is set to 0, all of 'duration', 'num_subblocks', 'constant_subblock_dratuion' and 'subblock_duration' fields SHALL be specified in this parameter definition")
        elif values.get('param_definition_mode') == 1:
            if not (values.get('duration') is None and
                values.get('num_subblocks') is None and
                values.get('constant_subblock_duration') is None and
                values.get('subblock_durations') is None):
                raise ValueError("When 'param_definition_mode' is set to 1, none of 'duration', 'num_subblocks', 'constant_subblock_dratuion' and 'subblock_duration' fields SHALL be specified in this parameter definition")
        return values
    
    @validator('duration')
    def check_duration(cls, value):
        if value is not None:
            if (value == 0):
                raise ValueError("'duration' SHALL NOT be set to 0")
        return value
    
    @validator('subblock_durations')
    def check_subblock_durations(cls, value):
        if value is not None:
            for duration in value:
                if (duration == 0):
                    raise ValueError("'subblock_durations' SHALL NOT be set to 0")
        return value
    
    # root_validator
    @root_validator(pre=True)
    def check_duration_values(cls, values):        
        D = values.get('duration')
        NS = values.get('num_subblocks')
        CSD = values.get('constant_subblock_duration')
        SD = values.get('subblock_durations')
        
        if not (D is None or NS is None or CSD is None or SD is None):
            
            if CSD == 0:
                if not (sum(SD) == D):
                    raise ValueError("When CSD=0, the summation of all SDs in this parameter block SHALL be equal to the value of 'duration'")
            else:
                num_subblocks = math.ceil(D/CSD)
                if (num_subblocks * CSD > D):
                    if not ((D-(NS-1)*CSD) == SD[-1]): # SD[-1]: duration of last subblock
                        raise ValueError("When CSD!=0, if NS x CSD > D, the actual duration of the last subblock SHALL be D - (NS - 1) x CSD")
               
        return values
    
    
    
class MixGainParamDefinition(BaseModel):
    param_definition: ParamDefinition
    default_mix_gain: int
    
class DemixingParamDefinition(BaseModel):
    param_definition: ParamDefinition
    default_demixing_info_parameter_data: DemixingInfoParameterData
    default_w: int
    # reserved: 5 bits
    
    @validator('param_definition')
    def check_param_definition(cls, value):
        if not (value.param_definition_mode == 0):
            raise ValueError("In this parameter definition, 'param_definition_mode' SHALL be set to 0")
        
        if not (value.num_subblocks == 1):
            raise ValueError("In this parameter definition, 'num_subblocks' SHALL be set to 1")
        
        if not (value.constant_subblock_duration == value.duration):
            raise ValueError("In this parameter definition, 'constant_subblock_duration' SHALL be same as 'duration'")
        
        return value
            
    
class ReconGainParamDefinition(BaseModel):
    param_definition: ParamDefinition
    
    @validator('param_definition')
    def check_param_definition(cls, value):
        if not (value.param_definition_mode == 0):
            raise ValueError("In this parameter definition, 'param_definition_mode' SHALL be set to 0")
        
        if not (value.num_subblocks == 1):
            raise ValueError("In this parameter definition, 'num_subblocks' SHALL be set to 1")
        
        if not (value.constant_subblock_duration == value.duration):
            raise ValueError("In this parameter definition, 'constant_subblock_duration' SHALL be same as 'duration'")
        
        return value

""" Audio Element OBU Validation """
class AudioElementType(IntEnum):
    AUDIO_ELEMENT_CHANNEL_BASED = 0
    AUDIO_ELEMENT_SCENE_BASED = 1
    
class AudioElementParam(BaseModel):
    param_definition_type: int
        
    # oneof param_definition: Union[DemixingParamDefinition,ReconGainParamDefinition]
    demixing_param: Optional[DemixingParamDefinition] = None
    recon_gain_param: Optional[ReconGainParamDefinition] = None
        
    @validator('param_definition_type')
    def check_param_definition_type(cls, value):
        # 0: MixGain
        # 1: Demixing
        # 2: ReconGain
        if value == 0:
            raise ValueError("'parameter_definition_mix_gain' SHALL NOT be present in AudioElementOBU")
        return value
    
class ChannelAudioLayerConfig(BaseModel):
    loudspeaker_layout: int
    output_gain_is_present_flag: int
    recon_gain_is_present_flag: int
    # reserved: 2 bits
    substream_count: int
    coupled_substream_count: int
    output_gain_flag: Optional[int] = None
    # reserved: 2 bits
    output_gain: Optional[int]=None
    
    @validator('loudspeaker_layout')
    def check_loudspeaker_layout(cls, value):
        if not (0 <= value <=9):
            raise ValueError('loudspeaker_layout must be 0-9')    
        return value
    
    @validator('substream_count')
    def check_substream_count(cls, value):
        if (value == 0):
            raise ValueError("'substream_count' SHALL NOT be set to 0")
        return value
    
    @validator('output_gain_flag')
    def check_output_gain_flag(cls, value):
        if value is not None:
           if not (0 <= value <64):
               raise ValueError('output_gain_flag must be 0-64')
        return value                    
    
class ScalableChannelLayoutConfig(BaseModel):
    num_layers: int
    # reserved: 5 bits
    channel_audio_layer_configs: List[ChannelAudioLayerConfig]
    
    @validator('num_layers')
    def check_num_layers(cls, value):
        if (value == 0):
            raise ValueError("'num_layers' SHALL NOT be set to 0")
        if (value > 6):
            raise ValueError("maximum number of 'num_layers' SHALL be limited to 6")
        return value
    
    @validator('channel_audio_layer_configs')
    def check_count_match(cls, v,values):
        if not( len(v) == values.get('num_layers') ):
            raise ValueError('length of channel_audio_layer_configs must be equal to num_layers')
        return v
    
    @validator('channel_audio_layer_configs')
    def check_channel_audio_layer_configs(cls, value):
        # substream_count and coupled_substream_count must have a specific value by channel_layout
        ref_dict = {0:(1,0), # Mono
                    1:(1,1), # Stereo
                    2:(4,2), # 5.1 ch
                    3:(5,3), # 5.1.2 ch
                    4:(6,4), # 5.1.4 ch
                    5:(5,3), # 7.1 ch
                    6:(6,4), # 7.1.2 ch
                    7:(7,5), # 7.1.4 ch
                    8:(4,2)} # 3.1.2 ch

        ref_dict_with_mono = {0:(1,0), # Mono
                              1:(2,0), # Stereo
                              2:(5,1), # 5.1 ch
                              3:(6,2), # 5.1.2 ch
                              4:(7,3), # 5.1.4 ch
                              5:(6,2), # 7.1 ch
                              6:(7,3), # 7.1.2 ch
                              7:(8,4), # 7.1.4 ch
                              8:(5,1)} # 3.1.2 ch

        sum_of_substream_count = 0
        sum_of_coupled_substream_count = 0
        
        for layer_info in value:
            if layer_info.loudspeaker_layout == 0: # Mono
                ref_dict = ref_dict_with_mono
                break
                        
        for layer_info in value:
            cur_layout = layer_info.loudspeaker_layout
            sum_of_substream_count += layer_info.substream_count
            sum_of_coupled_substream_count += layer_info.coupled_substream_count
            
            if not (ref_dict[cur_layout][0] == sum_of_substream_count and
                    ref_dict[cur_layout][1] == sum_of_coupled_substream_count ):
                raise ValueError("'substream_count' and 'coupled_substream_count' must have a specific value by channel layout")
        
        return value
        
    
    
class AmbisonicsMode(IntEnum):
    AMBISONICS_MODE_MONO = 0
    AMBISONICS_MODE_PROJECTION = 1
    
class AmbisonicsMonoConfig(BaseModel):
    output_channel_count: int
    substream_count: int
    channel_mapping: List[int]
    
    @validator('output_channel_count')
    def check_output_channel_count(cls, value):
        ambisonic_order = [0,1,2,3]
        allowed_channel_count = [(n+1)**2 for n in ambisonic_order]
        
        if not (value in allowed_channel_count):
            raise ValueError(f"'output_channel_count' must be one of the following: {allowed_channel_count}")
        return value
    
class AmbisonicsProjectionConfig(BaseModel):
    output_channel_count: int
    substream_count: int
    coupled_substream_count: int
    demixing_matrix: List[int]
    
    @validator('output_channel_count')
    def check_output_channel_count(cls, value):
        ambisonic_order = [0,1,2,3]
        allowed_channel_count = [(n+1)**2 for n in ambisonic_order]
        
        if not (value in allowed_channel_count):
            raise ValueError(f"'output_channel_count' must be one of the following: {allowed_channel_count}")
        return value
    
    @validator('coupled_substream_count')
    def check_coupled_substream_count(cls, v, values):
        if not (v <= values.get('substream_count')):
            raise ValueError("'coupled_substream_count' must be less than or equal to 'substream_count'")
        return v
    
class AmbisonicsConfig(BaseModel):
    ambisonics_mode: AmbisonicsMode    
    
    # oneof config Union[AmbisonicsMonoConfig,AmbisonicsProjectionConfig]
    ambisonics_mono_config: Optional[AmbisonicsMonoConfig] = None
    ambisonics_projection_config: Optional[AmbisonicsProjectionConfig] = None
    
class AudioElementOBU(BaseModel):
    audio_element_id: int
    audio_element_type: AudioElementType
    # reserved: 5 bits
    codec_config_id: int
    num_substreams: int
    audio_substream_ids: List[int]
    num_parameters: int
    audio_element_params: Optional[List[AudioElementParam]] = None
    
    # oneof config: Union[ScalableChannelLayoutConfig,AmbisonicsConfig]
    scalable_channel_layout_config: Optional[ScalableChannelLayoutConfig] = None
    ambisonics_config: Optional[AmbisonicsConfig] = None
        
        
    @validator('num_substreams')
    def check_num_substreams(cls, value):
        if value == 0:
            raise ValueError("'num_substreams' SHALL NOT be set to 0")
        return value
    
    @validator('audio_substream_ids')
    def check_substream_count(cls, v, values):
        if 'num_substreams' in values and len(v) != values['num_substreams']:
            raise ValueError("'num_substreams' must be equal to the length of 'audio_substream_ids'")
        return v
    
    @validator('num_parameters')
    def check_num_parameters(cls, v, values):
        if 'audio_element_type' in values:
            if values['audio_element_type'] == AudioElementType.AUDIO_ELEMENT_CHANNEL_BASED:
                if not (v == 0 or v==1 or v==2):
                    raise ValueError("When audio_element_type = 0, 'num_parameters' SHALL be set to 0, 1 or 2 for this version of the specification")
            elif values['audio_element_type'] == AudioElementType.AUDIO_ELEMENT_SCENE_BASED:
                if not (v == 0):
                    raise ValueError("When audio_element_type = 1, 'num_parameters' SHALL be set to 0 for this version of the specification")
        return v
    
    @root_validator(pre=True)
    def check_parameter_definition(cls, values):
        num_parameters = values.get('num_parameters')
        audio_element_params = values.get('audio_element_params')
        if audio_element_params is not None:
            if len(audio_element_params) != num_parameters:
                raise ValueError("'num_parameters' must be equal to the length of audio_element_params")
            
            param_definition_type_set = set()
            for parameter_info in (audio_element_params or []):
                if parameter_info.get('param_definition_type') not in param_definition_type_set:
                    param_definition_type_set.add(parameter_info.get('param_definition_type'))
                else:
                    raise ValueError("'param_definition_type' SHALL NOT be duplicated in one AudioElementOBU")
        return values
    



""" Mix Presentation OBU Validation """
class MixPresentationAnnotations(BaseModel):
    mix_presentation_friendly_label: str
    
class MixPresentationElementAnnotations(BaseModel):
    audio_element_friendly_label: str
    
class ElementMixConfig(BaseModel):
    mix_gain: MixGainParamDefinition
    
class SubMixAudioElement(BaseModel):
    audio_element_id: int
    mix_presentation_element_annotations_array: List[MixPresentationElementAnnotations]
    # TODO: rendering_config
    element_mix_config: ElementMixConfig

class LoudspeakerSPLabelLayout(BaseModel):
    num_loudspeakers: int
    sp_label: List[int]
    
    @validator('num_loudspeakers')
    def check_num_loudspeakers(cls, value):
        if (value == 0):
            raise ValueError("'num_loudspeakers' SHALL NOT be set to 0")
        return value
    
    @root_validator(pre=True)
    def check_loudspeaker_count(cls, values):
        loudspeaker_count = values.get('num_loudspeakers')
        loudspeaker_list = values.get('sp_label')
        
        if not (loudspeaker_count == len(loudspeaker_list)):
            raise ValueError("'num_loudspeakers' must be equal to the length of 'sp_label'")
        return values
    
    @validator('sp_label', each_item=True)
    def check_sp_label(cls, value):
        # 0~53: Used
        # 54~256: Reserved
        if not (0 <= value <= 53):
            raise ValueError('sp_label must be 0-53')
        return value
    
class OutputMixConfig(BaseModel):
    output_mix_gain: MixGainParamDefinition
    
class SoundSystem(IntEnum):
    SOUND_SYSTEM_INVALID = 0
    SOUND_SYSTEM_A_0_2_0 = 1
    SOUND_SYSTEM_B_0_5_0 = 2
    SOUND_SYSTEM_C_2_5_0 = 3
    SOUND_SYSTEM_D_4_5_0 = 4
    SOUND_SYSTEM_E_4_5_1 = 5
    SOUND_SYSTEM_F_3_7_0 = 6
    SOUND_SYSTEM_G_4_9_0 = 7
    SOUND_SYSTEM_H_9_10_3 = 8
    SOUND_SYSTEM_I_0_7_0 = 9
    SOUND_SYSTEM_J_4_7_0 = 10
    SOUND_SYSTEM_10_2_7_0 = 11
    SOUND_SYSTEM_11_2_3_0 = 12
    
class LoudspeakersSsConventionLayout(BaseModel):
    sound_system: SoundSystem
    # reserved: 2 bits
    
class LoudspeakersNotDefOrBinauralLayout(BaseModel):
    pass
    # reserved: 6 bits
    
class LayoutType(IntEnum):
    LAYOUT_TYPE_NOT_DEFINED = 0
    LAYOUT_TYPE_LOUDSPEAKERS_SP_LABEL = 1
    LAYOUT_TYPE_LOUDSPEAKERS_SS_CONVENTION = 2
    LAYOUT_TYPE_BINAURAL = 3
    
class Layout(BaseModel):
    layout_type: LayoutType
    
    # oneof specific_layout: Union[LoudspeakerSPLabelLayout,LoudspeakersSsConventionLayout,LoudspeakersNotDefOrBinauralLayout]
    sp_layout: Optional[LoudspeakerSPLabelLayout] = None
    ss_layout: Optional[LoudspeakersSsConventionLayout] = None
    notdef_or_binaural_layout: Optional[LoudspeakersNotDefOrBinauralLayout] = None
    
    
class AnchorType(IntEnum):
    ANCHOR_TYPE_NOT_DEFINED=0
    ANCHOR_TYPE_UNKNOWN=1
    ANCHOR_TYPE_DIALOGUE=2
    ANCHOR_TYPE_ALBUM=3
    
class AnchorElement(BaseModel):
    anchor_element: AnchorType
    anchored_loudness: int

class AnchoredLoudness(BaseModel):
    num_anchored_loudness: int
    anchor_elements: Optional[List[AnchorElement]] = None
    
    @validator('anchor_elements')
    def check_anchor_elements(cls, value):
        anchor_type_set = set()
        for anchor_element in (value or []):
            if anchor_element.anchor_element not in anchor_type_set:
                anchor_type_set.add(anchor_element.anchor_element)
            else:
                raise ValueError("'anchor_element' SHALL NOT be duplicated in one AnchoredLoudness")
                        
        return value
        

class LoudnessInfo(BaseModel):
    info_type: int
    integrated_loudness: int
    digital_peak: int
    true_peak: Optional[int] = None
    anchored_loudness: Optional[AnchoredLoudness] = None
    
    @validator('info_type')
    def check_info_type(cls, value):
        if not (value <4):
            raise ValueError('info_type value must be less than 4')
        return value
    
class MixPresentationLayout(BaseModel):
    loudness_layout: Layout
    loudness: LoudnessInfo    
    
class MixPresentationSubMix(BaseModel):
    num_audio_elements: int
    audio_elements: List[SubMixAudioElement]
    output_mix_config: OutputMixConfig
    num_layouts: int
    layouts: List[MixPresentationLayout]
    
    # TODO: each sub-mix shall include loudness_info() for Stereo
    
    @validator('num_audio_elements')
    def check_num_audio_elements(cls, value):
        if (value == 0):
            raise ValueError("'num_audio_elements' SHALL NOT be set to 0")
        return value
    
    @validator('audio_elements')
    def check_element_count(cls, v, values):
        if 'num_audio_elements' in values and len(v) != values['num_audio_elements']:
            raise ValueError("'num_audio_elements' must be equal to the length of audio_elements")
        return v
    
    @validator('layouts')
    def check_layout_count(cls, v, values):
        if 'num_layouts' in values and len(v) != values['num_layouts']:
            raise ValueError("'num_layouts' must be equal to the length of 'layouts'")
        return v
    
class MixPresentationOBU(BaseModel):
    mix_presentation_id: int
    count_label: int
    language_labels: List[str]    
    mix_presentation_annotations_array: List[MixPresentationAnnotations]
    num_sub_mixes: int
    sub_mixes: List[MixPresentationSubMix]
    
    @root_validator(pre=True)
    def check_label_count(cls, values):
        if not (values.get('count_label') == len(values.get('language_labels'))) or not (values.get('count_label') == len(values.get('mix_presentation_annotations_array'))):
            raise ValueError("'language_labels' and 'mix_presentation_annotations' must have the same length as 'count_label' value")
        return values
    
    @validator('language_labels')
    def check_language_labels(cls, value):
        language_label_set = set()
        for label in (value or []):
            if label not in language_label_set:
                language_label_set.add(label)
            else:
                raise ValueError("'language_labels' SHALL NOT be duplicated in one MixPresentationOBU")
        return value
    
    @validator('num_sub_mixes')
    def check_num_submixes(cls, value):
        if (value == 0):
            raise ValueError("'num_sub_mixes' SHALL NOT be set to 0")        
        return value
    
    @validator('sub_mixes')
    def check_submix_count(cls, v, values):
        if 'num_sub_mixes' in values and len(v) != values['num_sub_mixes']:
            raise ValueError("'num_sub_mixes' must be equal to the length of 'sub_mixes'")
        return v
    
    
""" Audio Frame OBU Validation """
class SubstreamMetadata(BaseModel):
    channel_ids: List[int]
    
class AudioFrameOBU(BaseModel):
    audio_substream_id: int
    
    num_samples_to_trim_at_end: int
    num_samples_to_trim_at_start: int
    
    size_of_audio_frame: int
    
    def __hash__(self):
        return self.audio_substream_id
    
    

    
    
    
""" Temporal Delimiter OBU Validation """
class TemporalDelimiterOBU(BaseModel):
    # No payload
    pass





""" IAMF Bitstream Validation """
class Descriptor(BaseModel):
    ia_sequence_header_obu: IaSequenceHeaderOBU
    codec_config_obu: CodecConfigOBU
    audio_element_obus: List[AudioElementOBU]
    mix_presentation_obus: List[MixPresentationOBU]
    
    
class Data(BaseModel):
    parameter_block_obus: List[ParameterBlockOBU]
    audio_frame_obus: List[AudioFrameOBU]
    temporal_delimiter_obus: Optional[List[TemporalDelimiterOBU]] = None
    
    
class IAMFBitstream(BaseModel):
    descriptor: Descriptor
    data: Data
            
    # pre-skip shall be same as the number of audio samples to be trimmed at the start of substreams.
    @root_validator(pre=True)
    def check_pre_skip_value(cls, values):
        codec_config_data = values.get('descriptor').codec_config_obu.codec_config
                
        if codec_config_data.codec_id == four_cc('Opus'):
            pre_skip = codec_config_data.decoder_config_opus.pre_skip
            audio_frame_dict = defaultdict(list)
            for audio_frame_obu in values.get('data').audio_frame_obus:
                audio_frame_dict[audio_frame_obu.audio_substream_id].append(audio_frame_obu)
                
            for _, audio_frame_obus in audio_frame_dict.items():
                num_samples_to_trim_at_start = 0
                for audio_frame_obu in audio_frame_obus:
                    num_samples_to_trim_at_start += audio_frame_obu.num_samples_to_trim_at_start
                if not (pre_skip > 0 and pre_skip == num_samples_to_trim_at_start):
                    raise ValueError("'pre_skip' must be same as the number of audio samples to be 'trimmed at the start'")
                
        return values
        
    # mapping_family shall be 0 for channel based, 2 for scene-based mono, 3 for scene-based projection
    @root_validator(pre=True)
    def check_mapping_family_value(cls, values):
        codec_config_data = values.get('descriptor').codec_config_obu.codec_config
        
        if codec_config_data.codec_id == four_cc('Opus') and codec_config_data.decoder_config_opus is not None:
            mapping_family_value = codec_config_data.decoder_config_opus.mapping_family
            
            for audio_element in (values.get('descriptor').audio_element_obus or []):
                if audio_element.audio_element_type == AudioElementType.AUDIO_ELEMENT_CHANNEL_BASED and not (mapping_family_value == 0):
                    raise ValueError("'mapping_family' shall be 0 for channel based")
                elif audio_element.audio_element_type == AudioElementType.AUDIO_ELEMENT_SCENE_BASED:
                    if audio_element.ambisonics_config == AmbisonicsMode.AMBISONICS_MODE_MONO and not (mapping_family_value == 2):
                        raise ValueError("'mapping_family' shall be 2 for scene-based mono config")
                    elif audio_element.ambisonics_config == AmbisonicsMode.AMBISONICS_MODE_PROJECTION and not (mapping_family_value == 3):
                        raise ValueError("'mapping_family' shall be 3 for scene-based projection config")
        return values
    
    @root_validator(pre=True)
    def check_trimming_value(cls, values):
        codec_config_data = num_samples_per_frame = values.get('descriptor').codec_config_obu.codec_config
        num_samples_per_frame = codec_config_data.num_samples_per_frame
        
        audio_frame_dict = defaultdict(list)
        for audio_frame_obu in values.get('data').audio_frame_obus:
            audio_frame_dict[audio_frame_obu.audio_substream_id].append(audio_frame_obu)
            
        for _, audio_frame_obus in audio_frame_dict.items():
            trim_finished_at_start = False
            for audio_frame_obu in audio_frame_obus:
                if not (audio_frame_obu.num_samples_to_trim_at_start == num_samples_per_frame):
                    trim_finished_at_start = True
                    continue
                
                if (audio_frame_obu.num_samples_to_trim_at_start > 0 ) and (trim_finished_at_start == True):
                    raise ValueError("When 'num_samples_to_trim_at_start' is non-zero, all audio_frame_obus preceding SHALL have their 'num_samples_to_trim_at_start' field equal to 'num_samples_per_frame'")
            
            trim_finished_at_end=False
            for audio_frame_obu in reversed(audio_frame_obus[:-1]):
                if audio_frame_obu.num_samples_to_trim_at_end > 0:
                    raise ValueError("When 'num_samples_to_trim_at_end' is non-zero, all audio_frame_obus following SHALL have no subsequent audio_frame_obus")        
        
            if (codec_config_data.codec_id == four_cc('ipcm')) and (not all(audio_frame.size_of_audio_frame == audio_frame_obus[0].size_of_audio_frame for audio_frame in audio_frame_obus)):
                raise ValueError('all audio_frame_obus shall have the same size_of_audio_frame')
        
        return values
    
    @root_validator(pre=True)
    def check_trim_samples_count(cls, values):
        codec_config_data = num_samples_per_frame = values.get('descriptor').codec_config_obu.codec_config
        num_samples_per_frame = codec_config_data.num_samples_per_frame
        
        for audio_frame_obu in values.get('data').audio_frame_obus:
            if not (audio_frame_obu.num_samples_to_trim_at_start + audio_frame_obu.num_samples_to_trim_at_end <= num_samples_per_frame):
                raise ValueError("the sum of 'num_samples_to_trim' SHALL be less or equal to the number of samples")
                    
        return values
    
    @root_validator(pre=True)
    def check_temporal_delimiter(cls, values):
        primary_profile = values.get('descriptor').ia_sequence_header_obu.primary_profile
        additional_profile = values.get('descriptor').ia_sequence_header_obu.additional_profile
        
        if primary_profile == 0: # Simple Profile  
            if len(values.get('data').temporal_delimiter_obus) > 0:
                raise ValueError("'temporal_delimiter_obus' must not exist in simple profile")
        return values

    @root_validator(pre=True)
    def check_parameter_values(cls, values):
        
        # get all parameter id
        parameter_id_set = set()
        
        # make (parameter_id, ParamDefinition) pair
        for audio_element_obu in values.get('descriptor').audio_element_obus:
            for audio_element_param in (audio_element_obu.audio_element_params or []): # check None type
                if audio_element_param.demixing_param is not None: # demixing_gain
                    parameter_id_set.add(audio_element_param.demixing_param.param_definition.parameter_id)                    
                elif audio_element_param.recon_gain_param is not None: # recon_gain
                    parameter_id_set.add(audio_element_param.recon_gain_param.param_definition.parameter_id)
                    
        # mix_presentation
        # element_mix_gain + output_mix_gain
        for mix_presentation_obu in values.get('descriptor').mix_presentation_obus:
            for submix in mix_presentation_obu.sub_mixes:
                for audio_element in submix.audio_elements:
                    mix_gain_param = audio_element.element_mix_config.mix_gain
                    parameter_id_set.add(mix_gain_param.param_definition.parameter_id)
                parameter_id_set.add(submix.output_mix_config.output_mix_gain.param_definition.parameter_id)                
                
                
        for parameter_block in values.get('data').parameter_block_obus:
            if not (parameter_block.parameter_id in parameter_id_set):
                raise ValueError('extra parameter_block is included in the bitstream')        
        
        return values
    
    
    
    @root_validator(pre=True)
    def check_parameter_coverage_and_duration(cls, values):
        codec_config = values.get('descriptor').codec_config_obu.codec_config
        
        audio_frame_obus = values.get('data').audio_frame_obus
        audio_frame_durations = defaultdict(int)
        
        for audio_frame_obu in audio_frame_obus:
            audio_frame_durations[audio_frame_obu.audio_substream_id] += codec_config.num_samples_per_frame
                
        total_audio_frame_duration = audio_frame_durations.get(next(iter(audio_frame_durations)))
        for k, v in audio_frame_durations.items():
            if not (v == total_audio_frame_duration):
                raise ValueError('audio_frame_durations must be equal in each substream')
                        
        # make (parameter_id, ParamDefinition) pair
        parameter_info_dict = dict()
        for audio_element_obu in values.get('descriptor').audio_element_obus:
            for audio_element_param in (audio_element_obu.audio_element_params or []): # check None type
                if audio_element_param.demixing_param is not None: # demixing_gain
                    id = audio_element_param.demixing_param.param_definition.parameter_id
                    if parameter_info_dict.get(id) is not None:
                        if not (parameter_info_dict[id].param_definition_mode == audio_element_param.param_definition_mode):
                            raise ValueError("'param_definition_mode' value shall be the same for same 'parameter_id'")
                    parameter_info_dict[id]=audio_element_param.demixing_param.param_definition
                elif audio_element_param.recon_gain_param is not None: # recon_gain
                    id = audio_element_param.recon_gain_param.param_definition.parameter_id
                    if parameter_info_dict.get(id) is not None:
                        if not (parameter_info_dict[id].param_definition_mode == audio_element_param.param_definition_mode):
                            raise ValueError("'param_definition_mode' value shall be the same for same 'parameter_id'")
                    parameter_info_dict[id]=audio_element_param.recon_gain_param.param_definition
        
        # mix_presentation
        # element_mix_gain + output_mix_gain
        for mix_presentation_obu in values.get('descriptor').mix_presentation_obus:
            for submix in mix_presentation_obu.sub_mixes:
                for audio_element in submix.audio_elements:
                    mix_gain_param = audio_element.element_mix_config.mix_gain
                    id = mix_gain_param.param_definition.parameter_id
                    if parameter_info_dict.get(id) is not None:
                        if not (parameter_info_dict[id].param_definition_mode == mix_gain_param.param_definition.param_definition_mode):
                            raise ValueError("'param_definition_mode' value shall be the same for same 'parameter_id'")
                    parameter_info_dict[id]=mix_gain_param.param_definition                                    
                param = submix.output_mix_config.output_mix_gain.param_definition
                if parameter_info_dict.get(param.parameter_id) is not None:
                    if not (parameter_info_dict[id].param_definition_mode == param.param_definition_mode):
                        raise ValueError("'param_definition_mode' value shall be the same for same 'parameter_id'")
                parameter_info_dict[param.parameter_id] = param
            
        total_param_duration = defaultdict(int)
        for parameter_block in values.get('data').parameter_block_obus:
            param_id = parameter_block.parameter_id
            
            parameter_info = parameter_info_dict.get(param_id)
            if parameter_info is not None:
                if parameter_info.param_definition_mode == 0:
                    total_param_duration[param_id] = total_param_duration[param_id] + parameter_info.duration
                else:
                    total_param_duration[param_id] = total_param_duration[param_id] + parameter_block.duration
        
        if not (len(total_param_duration) == 0):
            for param_id,param_duration in total_param_duration.items():
                if not (total_audio_frame_duration == param_duration):
                    raise ValueError('total_audio_frame_duration and total_parameter_duration must be equal')
        
        
        ### check_parameter_duration ###
        num_samples_per_frame = codec_config.num_samples_per_frame
        if codec_config.decoder_config_opus is not None:
            audio_frame_length = num_samples_per_frame/codec_config.decoder_config_opus.input_sample_rate
        elif codec_config.decoder_config_lpcm is not None:
            audio_frame_length = num_samples_per_frame/codec_config.decoder_config_lpcm.sample_rate
        else:
            audio_frame_length = 1024/48000
        
        for parameter_block in values.get('data').parameter_block_obus:
            parameter_info = parameter_info_dict.get(parameter_block.parameter_id)
            if parameter_info is not None:
                if parameter_info.param_definition_mode == 0:
                    parameter_length = parameter_info.duration/parameter_info.parameter_rate
                else:
                    parameter_length = parameter_block.duration/parameter_info.parameter_rate
                
                # Division of floating point value
                Q = parameter_length/audio_frame_length
                R = parameter_length - audio_frame_length*Q
                if not (R <= 1e-9):                    
                    raise ValueError('parameter duration must be same as audio frame duration')
        
        return values
        
    """
    @root_validator(pre=True)
    def check_parameter_duration(cls, values):    
        codec_config = values.get('descriptor').codec_config_obu.codec_config
        
        num_samples_per_frame = codec_config.num_samples_per_frame
        parameter_block_obus = values.get('data').parameter_block_obus
                
        if codec_config.decoder_config_opus is not None:
            audio_frame_length = num_samples_per_frame/codec_config.decoder_config_opus.input_sample_rate
        elif codec_config.decoder_config_lpcm is not None:
            audio_frame_length = num_samples_per_frame/codec_config.decoder_config_lpcm.sample_rate
        else:
            pass
                
        # make (parameter_id, ParamDefinition) pair
        parameter_rate_dict = dict()
        for audio_element_obu in values.get('descriptor').audio_element_obus:
            for audio_element_param in (audio_element_obu.audio_element_params or []): # check None type
                if audio_element_param.demixing_param is not None: # demixing_gain
                    id = audio_element_param.demixing_param.param_definition.parameter_id
                    parameter_rate_dict[id]=audio_element_param.demixing_param.param_definition
                elif audio_element_param.recon_gain_param is not None: # recon_gain
                    id = audio_element_param.recon_gain_param.param_definition.parameter_id
                    parameter_rate_dict[id]=audio_element_param.recon_gain_param.param_definition
        
        # mix_presentation
        # element_mix_gain + output_mix_gain
        for mix_presentation_obu in values.get('descriptor').mix_presentation_obus:
            for submix in mix_presentation_obu.sub_mixes:
                for audio_element in submix.audio_elements:
                    mix_gain_param = audio_element.element_mix_config.mix_gain
                    id = mix_gain_param.param_definition.parameter_id
                    parameter_rate_dict[id]=mix_gain_param.param_definition                    
                param = submix.output_mix_config.output_mix_gain.param_definition
                parameter_rate_dict[param.parameter_id] = param
        
        
        for parameter_block in parameter_block_obus:
            parameter_info = parameter_rate_dict.get(parameter_block.parameter_id)
            if parameter_info is not None:
                if parameter_info.param_definition_mode == 0:
                    parameter_length = parameter_info.duration/parameter_info.parameter_rate
                else:
                    parameter_length = parameter_block.duration/parameter_info.parameter_rate
                
                # Division of floating point value
                Q = parameter_length/audio_frame_length
                R = parameter_length - audio_frame_length*Q
                if not (R <= 1e-9):                    
                    raise ValueError('parameter duration must be same as audio frame duration')
                
        return values
    """
    
    
    
""" Bitstream Validator """
def is_valid_bitstream(obu_list: list):
    import re
    
    audio_element_obu_list = list()
    mix_presentation_obu_list = list()

    audio_frame_obu_list = list()
    parameter_block_obu_list = list()
    temporal_delimiter_obu_list = list()
    
    
    for obu in obu_list:
        for k, v in obu.items():
            
            # v is None
            if re.match(r'TemporalDelimiterOBU_\d+',k):
                try:
                    temporal_delimiter_obu = TemporalDelimiterOBU(**value)
                    temporal_delimiter_obu_list.append(temporal_delimiter_obu)
                except Exception as err:
                    return False, err
                continue
            
            value = v[0]            
            if re.match(r'IaSequenceHeaderOBU_\d+',k):
                try:
                    ia_sequence_header_obu = IaSequenceHeaderOBU(**value)
                except Exception as err:
                    return False, err
            elif re.match(r'CodecConfigOBU_\d+',k):
                try:
                    codec_config_obu = CodecConfigOBU(**value)
                except Exception as err:
                    return False, err
            elif re.match(r'AudioElementOBU_\d+',k):
                try:
                    audio_element_obu = AudioElementOBU(**value)
                    audio_element_obu_list.append(audio_element_obu)
                except Exception as err:
                    return False, err
            elif re.match(r'MixPresentationOBU_\d+',k):
                try:
                    mix_presentation_obu = MixPresentationOBU(**value)
                    mix_presentation_obu_list.append(mix_presentation_obu)
                except Exception as err:
                    return False, err
            elif re.match(r'AudioFrameOBU_\d+',k):
                try:
                    audio_frame_obu = AudioFrameOBU(**value)
                    audio_frame_obu_list.append(audio_frame_obu)
                except Exception as err:
                    return False, err
            elif re.match(r'ParameterBlockOBU_\d+',k):
                try:
                    parameter_block_obu = ParameterBlockOBU(**value)
                    parameter_block_obu_list.append(parameter_block_obu)
                except Exception as err:
                    return False, err
            

    try:
        iamf_descriptor = Descriptor(ia_sequence_header_obu=ia_sequence_header_obu,
                                    codec_config_obu=codec_config_obu,
                                    audio_element_obus = audio_element_obu_list,
                                    mix_presentation_obus=mix_presentation_obu_list)
    except Exception as err:
        return False, err

    try:
        iamf_data = Data(parameter_block_obus=parameter_block_obu_list,
                         audio_frame_obus=audio_frame_obu_list,                        
                        temporal_delimiter_obus=temporal_delimiter_obu_list)
    except Exception as err:
        return False, err
                    
    try:
        iamf_bitstream = IAMFBitstream(descriptor=iamf_descriptor,
                                        data=iamf_data)
    except Exception as err:
        return False, err
    
    return True, None
