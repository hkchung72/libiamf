from typing import List, Dict, Union, Optional
from pydantic import BaseModel, validator, root_validator
from enum import IntEnum
import math

def four_cc(string:str):
    ret = 0
    for i in [ord(s) for s in string]:
        ret = (ret<<8) + i
    return ret

""" Magic Code OBU Validation """
class MagicCodeOBU(BaseModel):
    ia_code: int
    version: int
    profile_version: int
    
    @validator('ia_code')
    def check_ia_code(cls, value):
        if not (value == four_cc('iamf')):
            raise ValueError('ia_code must be iamf')
        return value
    
    @validator('version')
    def check_version(cls, value):
        if not (value == 0):
            raise ValueError('version must be set to 0')
        return value
    
    @validator('profile_version')
    def check_profile_version(cls, value):
        if not (value == 0 or 
                value == 16):
            raise ValueError('profile_version must be set to 0 or 16')
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
            raise ValueError('sample_size must be 16, 24 or 32')    
        return value
    
    @validator('sample_rate')
    def check_sample_rate(cls, value):
        if not (value == 44100 or
                value == 16000 or
                value == 32000 or
                value == 48000 or
                value == 96000):
            raise ValueError('sample_rate is not supported')
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
            raise ValueError('version must be set to 1')    
        return value
    
    @validator('output_channel_count')
    def check_output_channel_count(cls, value):
        if not (value == 2):
            raise ValueError('output_channel_count must be 2')
        return value
        
    @validator('output_gain')
    def check_output_gain(cls, value):
        if not (value == 0):
            raise ValueError('output_gain must be 0')
        return value
    
    @validator('mapping_family')
    def check_mapping_family(cls, value):
        if not (value == 0):
            raise ValueError('mapping_family must be 0')
        return value
    
class DecoderConfigAac(BaseModel):
    pass

class DecoderConfigFlac(BaseModel):
    pass

class CodecConfig(BaseModel):
    codec_id: int
    num_samples_per_frame: int
    roll_distance: int
    
    # oneof decoder_config: Union[DecoderConfigLpcm, DecoderConfigOpus, DecoderConfigAac, DecoderConfigFlac]
    decoder_config_lpcm: Optional[DecoderConfigLpcm]
    decoder_config_opus: Optional[DecoderConfigOpus]
    decoder_config_aac: Optional[DecoderConfigAac]
    decoder_config_flac: Optional[DecoderConfigFlac]
        
    @validator('codec_id')
    def check_codec_id(cls, value):
        if not (value == four_cc('Opus') or
                value == four_cc('mp4a') or
                value == four_cc('fLaC') or
                value == four_cc('ipcm')):
            raise ValueError('codec_id must be Opus, mp4a, fLaC or ipcm')    
        return value
    
    @validator('num_samples_per_frame')
    def check_num_sample_per_frame(cls, value):
        if value == 0:
            raise ValueError('num_sample_per_frame must not be set to 0')
        return value
    
    @validator('roll_distance')
    def check_roll_instance(cls, value, values):
        if values.get('codec_id') == four_cc('mp4a'):
            if not (value == -1):
                raise ValueError('roll_instance must be -1 with AAC codec')                
        elif values.get('codec_id') == four_cc('Opus'):
            R_value = math.ceil(3840/values.get('num_samples_per_frame'))            
            if not (abs(value) == R_value):
                raise ValueError(f'value of roll_instance must be ceil(3840/num_samples_per_frame) = -{R_value}')
        return value           
    
class CodecConfigOBU(BaseModel):
    codec_config_id: int
    codec_config: CodecConfig
    
   

""" Param Definition Validation """
class ParamDefinition(BaseModel):
    parameter_id: int
    parameter_rate: int
    param_definition_mode: int
    # reserved: 7 bits
    duration: Optional[int] = None
    num_subblocks: Optional[int] = None
    constant_subblock_duration: Optional[int] = None
    subblock_durations: Optional[List[int]] = None
    
    @root_validator(pre=True)
    def check_param_definition_mode(cls, values):
        if values.get('param_definition_mode') == 0:
            if not (values.get('duration') is None and
                    values.get('num_subblocks') is None and
                    values.get('constant_subblock_duration') is None and
                    values.get('subblock_durations') is None):
                raise ValueError('duration, num_subblocks, constant_subblock_duration and subblock_durations exists according to the param_definition_mode value')
        return values
    
    # root_validator
    @root_validator(pre=True)
    def check_duration_values(cls, values):
        D = values.get('duration')
        NS = values.get('num_subblocks')
        CSI = values.get('constant_subblock_duration')
        SI = values.get('subblock_durations')
        
        if not (D is None or NS is None or CSI is None or SI is None):
            if CSI == 0:
                if not (sum(SI) == D):
                    raise ValueError('duration must be equal to sum of subblock_durations')
            else:
                if not (NS*CSI >= D):
                    raise ValueError('duration must be equal to or less than num_subblocks*constant_subblock_duration')
                else:
                    if NS*CSI > D:
                        if not (D - (NS-1)*CSI == SI[-1]): # SI[-1]: duration of last subblock 
                            raise ValueError('actual duration of the last subblock is not match to the valud of duration')
        return values
    
class MixGainParamDefinition(BaseModel):
    param_definition: ParamDefinition
    default_mix_gain: int
    
class DemixingParamDefinition(BaseModel):
    param_definition: ParamDefinition
    
class ReconGainParamDefinition(BaseModel):
    param_definition: ParamDefinition
    

""" Audio Element OBU Validation """
class AudioElementType(IntEnum):
    AUDIO_ELEMENT_CHANNEL_BASED = 0
    AUDIO_ELEMENT_SCENE_BASED = 1
    
class AudioElementParam(BaseModel):
    param_definition_type: int
    param_definition: Union[DemixingParamDefinition,ReconGainParamDefinition]
    
    @validator('param_definition_type')
    def check_param_definition_type(cls, value):
        # 0: MixGain
        # 1: Demixing
        # 2: ReconGain
        if not (0<=value<=2):
            raise ValueError('param_definition_type must be 0-2')
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
    
    @validator('output_gain_flag')
    def check_output_gain_flag(cls, value):
        if value is not None:
           if not (0 <= value <=31):
               raise ValueError('output_gain_flag must be 0-31')
        return value                    
    
class ScalableChannelLayoutConfig(BaseModel):
    num_layers: int
    # reserved: 5 bits
    channel_audio_layer_configs: List[ChannelAudioLayerConfig]
    
    @validator('num_layers')
    def check_num_layers(cls, value):
        if not (0 < value <= 6):
            raise ValueError('num_layers must be 1-6')
        return value
    
    @validator('channel_audio_layer_configs')
    def check_count_match(cls, v,values):
        if not( len(v) == values.get('num_layers') ):
            raise ValueError(f'length of channel_audio_layer_configs must be equal to num_layers')
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

        sum_of_substream_count = 0
        sum_of_coupled_substream_count = 0
        for layer_info in value:
            cur_layout = layer_info.loudspeaker_layout
            sum_of_substream_count += layer_info.substream_count
            sum_of_coupled_substream_count += layer_info.coupled_substream_count
            
            if not (ref_dict[cur_layout][0] == sum_of_substream_count and
                    ref_dict[cur_layout][1] == sum_of_coupled_substream_count ):
                raise ValueError('substream_count and coupled_substream_count must have a specific value by channel layout')
        
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
            raise ValueError(f'output_channel_count must be one of the following: {allowed_channel_count}')
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
            raise ValueError(f'output_channel_count must be one of the following: {allowed_channel_count}')
        return value
    
class AmbisonicsConfig(BaseModel):
    ambisonics_mode: AmbisonicsMode    
    
    # oneof config Union[AmbisonicsMonoConfig,AmbisonicsProjectionConfig]
    ambisonics_mono_config: Optional[AmbisonicsMonoConfig]
    ambisonics_projection_config: Optional[AmbisonicsProjectionConfig]    
    
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
    scalable_channel_layout_config: Optional[ScalableChannelLayoutConfig]
    ambisonics_config: Optional[AmbisonicsConfig]
        
    @validator('audio_substream_ids')
    def check_substream_count(cls, v, values):
        if 'num_substreams' in values and len(v) != values['num_substreams']:
            raise ValueError('num_substreams must be equal to the length of audio_substream_ids')
        return v
    
    @validator('audio_element_params')
    def check_parameter_count(cls, v, values):
        if 'num_parameters' in values and len(v) != values['num_parameters']:
            raise ValueError('num_parameters must be equal to the length of audio_element_params')
        return v
    



""" Mix Presentation OBU Validation """
class MixPresentationAnnotations(BaseModel):
    mix_presentation_friendly_label: str
    
class MixPresentationElementAnnotations(BaseModel):
    audio_element_friendly_label: str
    
class ElementMixConfig(BaseModel):
    mix_gain: MixGainParamDefinition
    
class SubMixAudioElement(BaseModel):
    audio_element_id: int
    mix_presentation_element_annotations: MixPresentationElementAnnotations
    # RenderingConfig has no payload
    element_mix_config: ElementMixConfig

class LoudspeakerSPLabelLayout(BaseModel):
    num_loudspeakers: int
    sp_label: List[int]
    
    @root_validator(pre=True)
    def check_loudspeaker_count(cls, values):
        loudspeaker_count = values.get('num_loudspeakers')
        loudspeaker_list = values.get('sp_label')
        
        if not (loudspeaker_count == len(loudspeaker_list)):
            raise ValueError('num_loudspeakers must be equal to the length of sp_label')
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
    sp_layout: Optional[LoudspeakerSPLabelLayout]
    ss_layout: Optional[LoudspeakersSsConventionLayout]
    notdef_or_binaural_layout: Optional[LoudspeakersNotDefOrBinauralLayout]
    
    
class LoudnessInfo(BaseModel):
    info_type: int
    integrated_loudness: int
    digital_peak: int
    true_peak: Optional[int]
    
    @validator('info_type')
    def check_info_type(cls, value):
        value_list = [0,1,2]
        if value not in value_list:
            raise ValueError(f'info_type value must be one of the following: {value_list}')
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
    
    @validator('audio_elements')
    def check_element_count(cls, v, values):
        if 'num_audio_elements' in values and len(v) != values['num_audio_elements']:
            raise ValueError('num_audio_elements must be equal to the length of audio_elements')
        return v
    
    @validator('layouts')
    def check_layout_count(cls, v, values):
        if 'num_layouts' in values and len(v) != values['num_layouts']:
            raise ValueError('num_layouts must be equal to the length of layouts')
        return v
    
class MixPresentationOBU(BaseModel):
    mix_presentation_id: int
    mix_presentation_annotations: MixPresentationAnnotations
    num_sub_mixes: int
    sub_mixes: List[MixPresentationSubMix]
    
    @validator('sub_mixes')
    def check_submix_count(cls, v, values):
        if 'num_sub_mixes' in values and len(v) != values['num_sub_mixes']:
            raise ValueError('num_sub_mixes must be equal to the length of sub_mixes')
        return v
    
    
    
    
    
""" Sync OBU Validation """
class SyncObuDataType(IntEnum):
    OBU_DATA_TYPE_SUBSTREAM = 0
    OBU_DATA_TYPE_PARAMETER = 1
    
class SyncElement(BaseModel):
    obu_id: int
    obu_data_type: SyncObuDataType
    reinitialize_decoder: bool
    # reserved: 6 bits
    relative_offset: int
    
    @validator('reinitialize_decoder')
    def check_reinitialize_decoder(cls, value):
        if not (value == False):
            raise ValueError('reinitialize_decoder must be False in this version')
        return value
    
    # TODO: relative_offset
    
class SyncOBU(BaseModel):
    global_offset: int
    num_obu_ids: int
    sync_array: List[SyncElement]
    
    @validator('global_offset')
    def check_global_offset(cls, value):
        if not (value == 0):
            raise ValueError('global_offset must be 0 in this version')
        return value
    
    @validator('sync_array')
    def check_sync_array_count(cls, v, values):
        if 'num_obu_ids' in values and len(v) != values['num_obu_ids']:
            raise ValueError('num_obu_ids must be equal to the length of sync_array')
        return values
    
    
    
""" Audio Frame OBU Validation """
class SubstreamMetadata(BaseModel):
    channel_ids: List[int]
    
class AudioFrameOBU(BaseModel):
    audio_substream_id: int
    
    num_samples_to_trim_at_end: int
    num_samples_to_trim_at_start: int
    
    def __hash__(self):
        return self.audio_substream_id
    
    



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
    step: Optional[AnimationStepInt]
    linear: Optional[AnimationLinearInt]
    bezier: Optional[AnimationBezierInt]        
    
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
    subblock_duration: Optional[int]
    
    # oneof parameter_data: Union[MixGainParameterData,DemixingInfoParameterData,ReconGainParameterData]    
    mix_gain_parameter_data: Optional[MixGainParameterData]
    demixing_info_parameter_data: Optional[DemixingInfoParameterData]
    recon_gain_parameter_data: Optional[ReconGainParameterData]
    
class ParameterBlockOBU(BaseModel):
    parameter_id: int
    duration: Optional[int]
    num_subblocks: Optional[int]
    constant_subblock_duration: Optional[int]
    subblocks: Optional[List[ParameterSubblock]]
    # start_timestamp in Sync??
    
    def __hash__(self):
        return self.parameter_id
    
    
    
""" Temporal Delimiter OBU Validation """
class TemporalDelimiterOBU(BaseModel):
    # No payload
    pass





""" IAMF Bitstream Validation """
class Descriptor(BaseModel):
    magic_code_obu: MagicCodeOBU
    codec_config_obu: CodecConfigOBU
    audio_element_obus: List[AudioElementOBU]
    mix_presentation_obus: List[MixPresentationOBU]
    
    
class Data(BaseModel):
    sync_obu: SyncOBU
    audio_frame_obus: List[AudioFrameOBU]
    parameter_block_obus: List[ParameterBlockOBU]
    temporal_delimiter_obus: Optional[List[TemporalDelimiterOBU]] = None
    
    
class IAMFBitstream(BaseModel):
    descriptor: Descriptor
    data: Data
            
    @validator('data')
    def check_sync_obu_num_obu_ids(cls, value):
        sync_data = value.sync_obu
        num_obu_ids = sync_data.num_obu_ids
        
        audio_frame_ids = set([audio_frame.audio_substream_id for audio_frame in set(value.audio_frame_obus)])
        parameter_ids = set([parameter.parameter_id for parameter in set(value.parameter_block_obus)])
        
        if not (num_obu_ids == 
                ( len(audio_frame_ids) + len(parameter_ids)) ): 
            raise ValueError('sync_obu must have all obu_ids in audio_frame_obus and parameter_block_obus')    
        return value
       
    # pre-skip shall be same as the number of audio samples to be trimmed at the start of substreams.
    @root_validator(pre=True)
    def check_pre_skip_value(cls, values):
        codec_config_data = values.get('descriptor').codec_config_obu.codec_config
                
        if codec_config_data.codec_id == four_cc('Opus'):
            pre_skip = codec_config_data.decoder_config_opus.pre_skip
            trim_at_start = values.get('data').audio_frame_obus[0].num_samples_to_trim_at_start
            if not (pre_skip > 0 and pre_skip == trim_at_start):
                raise ValueError('pre_skip must be same as the number of audio samples to be trimmed at the start')
        return values
        
    @root_validator(pre=True)
    def check_temporal_delimiter(cls, values):
        profile = values.get('descriptor').magic_code_obu.profile_version
        if profile == 0 and len(values.get('data').temporal_delimiter_obus) > 0:
            raise ValueError('temporal_delimiter_obus must not exist in simple profile')
        return values

    @root_validator(pre=True)
    def check_parameter_coverage(cls, values):
        sync_data = values.get('data').sync_obu.sync_array
        # TODO: relative_offset(P) - relative_offset(A)
        # TODO: audio_element / element_mix_gain / output_mix_gain
        # TODO: duration: num_samples_per_frame * len(audio_frame per substream_id)
                
        return values


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
            if re.match(r'MagicCodeOBU_\d+',k):
                try:
                    magic_code_obu = MagicCodeOBU(**value)
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
            elif re.match(r'SyncOBU_\d+',k):
                try:
                    sync_obu = SyncOBU(**value)
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
        iamf_descriptor = Descriptor(magic_code_obu=magic_code_obu,
                                    codec_config_obu=codec_config_obu,
                                    audio_element_obus = audio_element_obu_list,
                                    mix_presentation_obus=mix_presentation_obu_list)
    except Exception as err:
        return False, err

    try:
        iamf_data = Data(sync_obu = sync_obu,
                        audio_frame_obus=audio_frame_obu_list,
                        parameter_block_obus=parameter_block_obu_list,
                        temporal_delimiter_obus=temporal_delimiter_obu_list)
    except Exception as err:
        return False, err
                    
    try:
        iamf_bitstream = IAMFBitstream(descriptor=iamf_descriptor,
                                        data=iamf_data)
    except Exception as err:
        return False, err
    
    return True, None
