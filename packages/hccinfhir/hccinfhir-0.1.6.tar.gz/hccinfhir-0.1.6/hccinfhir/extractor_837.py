from typing import List, Optional, Dict
from pydantic import BaseModel
from hccinfhir.datamodels import ServiceLevelData

CLAIM_TYPES = {
    "005010X222A1": "837P",     # Professional
    "005010X223A2": "837I"      # Institutional
}

class ClaimData(BaseModel):
    """Container for claim-level data"""
    claim_id: Optional[str] = None
    patient_id: Optional[str] = None
    performing_provider_npi: Optional[str] = None
    billing_provider_npi: Optional[str] = None
    provider_specialty: Optional[str] = None
    facility_type: Optional[str] = None
    service_type: Optional[str] = None
    claim_type: str
    dx_lookup: Dict[str, str] = {}

def parse_date(date_str: str) -> Optional[str]:
    """Convert 8-digit date string to ISO format YYYY-MM-DD"""
    if not isinstance(date_str, str) or len(date_str) != 8:
        return None
    try:
        year, month, day = int(date_str[:4]), int(date_str[4:6]), int(date_str[6:8])
        if not (1900 <= year <= 2100 and 1 <= month <= 12 and 1 <= day <= 31):
            return None
        return f"{year:04d}-{month:02d}-{day:02d}"
    except ValueError:
        return None

def parse_amount(amount_str: str) -> Optional[float]:
    """Convert string to float, return None if invalid"""
    try:
        return float(amount_str)
    except (ValueError, TypeError):
        return None

def get_segment_value(segment: List[str], 
                      index: int, 
                      default: Optional[str] = None) -> Optional[str]:
    """Safely get value from segment at given index"""
    return segment[index] if len(segment) > index else default

def parse_diagnosis_codes(segment: List[str]) -> Dict[str, str]:
    """Extract diagnosis codes from HI segment"""
    dx_lookup = {}
    for pos, element in enumerate(segment[1:], 1):
        if ':' not in element:
            continue
        qualifier, code = element.split(':')[:2]
        if qualifier in {'ABK', 'ABF', 'ABJ'}:  # ICD-10 qualifiers
            # ABK: Primary Diagnosis
            # ABF: Secondary Diagnosis
            # ABJ: Admitting Diagnosis
            # NOTE: In Risk Adjustment, we do not differentiate between primary and secondary diagnoses
            dx_lookup[str(pos)] = code
    return dx_lookup

def process_service_line(segments: List[List[str]], start_index: int) -> tuple[Optional[str], Optional[str]]:
    """Extract NDC and service date from service line segments"""
    ndc = None
    service_date = None
    
    for seg in segments[start_index:]:
        if seg[0] in ['LX', 'CLM', 'SE']:
            break
        if len(seg) > 3:
            if seg[0] == 'LIN' and seg[2] == 'N4':
                ndc = seg[3]
            elif (seg[0] == 'DTP' and 
                  seg[1] in {'472', '434'} and
                  seg[2].endswith('D8')):
                # 472: Service Date
                # 434: From Date in 837I
                # These are not included currently: 435: To Date in 837I, 096 Discharge Date            
                if seg[3]:
                    service_date = parse_date(seg[3][:8] if len(seg[3]) >= 8 else seg[3])
        if ndc and service_date:
            break
            
    return ndc, service_date

def split_into_claims(segments: List[List[str]]) -> List[List[List[str]]]:
    """Split segments into individual claims based on ST/SE boundaries.
    
    Each ST...SE block represents one complete claim.
    Returns a list of claim segment lists.
    """
    claims = []
    current_claim = []
    in_transaction = False
    st_control_number = None
    
    for segment in segments:
        if len(segment) < 1:
            continue
            
        seg_id = segment[0]
        
        if seg_id == 'ST':
            # Start new claim transaction
            if current_claim:  # Save previous claim if exists (shouldn't happen with valid X12)
                claims.append(current_claim)
            current_claim = [segment]
            in_transaction = True
            st_control_number = segment[2] if len(segment) > 2 else None
            
        elif seg_id == 'SE':
            # End current claim transaction
            if in_transaction:
                current_claim.append(segment)
                
                # Validate control numbers match (ST02 == SE02)
                se_control_number = segment[2] if len(segment) > 2 else None
                if st_control_number != se_control_number:
                    print(f"Warning: ST/SE control numbers don't match: {st_control_number} != {se_control_number}")
                
                claims.append(current_claim)
                current_claim = []
                in_transaction = False
                st_control_number = None
                
        elif in_transaction:
            # Add segment to current claim
            current_claim.append(segment)
    
    # Handle case where file doesn't end with SE (malformed)
    if current_claim:
        print("Warning: Unclosed transaction found (missing SE)")
        claims.append(current_claim)
    
    return claims

def parse_837_claim_to_sld(segments: List[List[str]], claim_type: str) -> List[ServiceLevelData]:
    """Extract service level data from 837 Professional or Institutional claims

    Structure:
    Billing Provider (2000A)
    └── Subscriber (2000B)
        └── Patient (2000C) [if needed]
            └── Claim (2300)
                ├── Service Line 1 (2400)
                ├── Service Line 2 (2400)
                └── Service Line N (2400)
    
    """
    slds = []
    current_data = ClaimData(claim_type=claim_type)
    in_claim_loop = False
    in_rendering_provider_loop = False
    claim_control_number = None

    for i, segment in enumerate(segments):
        if len(segment) < 2:
            continue
            
        seg_id = segment[0]
        
        # Process NM1 segments (Provider and Patient info)
        if seg_id == 'ST':
            claim_control_number = segment[2] if len(segment) > 2 else None

        elif seg_id == 'NM1' and len(segment) > 1:
            if segment[1] == 'IL':  # Subscriber/Patient
                current_data.patient_id = get_segment_value(segment, 9)
                in_claim_loop = False
                in_rendering_provider_loop = False
            elif segment[1] == '82' and len(segment) > 8 and segment[8] == 'XX':  # Rendering Provider
                current_data.performing_provider_npi = get_segment_value(segment, 9)
                in_rendering_provider_loop = True
            elif segment[1] == '85' and len(segment) > 8 and segment[8] == 'XX':  # Billing Provider
                current_data.billing_provider_npi = get_segment_value(segment, 9)
                
        # Process Provider Specialty
        elif seg_id == 'PRV' and len(segment) > 1 and segment[1] == 'PE' and in_rendering_provider_loop:
            current_data.provider_specialty = get_segment_value(segment, 3)
            
        # Process Claim Information
        elif seg_id == 'CLM':
            in_claim_loop = True
            in_rendering_provider_loop = False
            current_data.claim_id = segment[1] if len(segment) > 1 else None
            
            # Parse facility and service type for institutional claims
            if claim_type == "837I" and len(segment) > 5 and segment[5] and ':' in segment[5]:
                current_data.facility_type = segment[5][0] if segment[5] else None
                current_data.service_type = segment[5][1] if len(segment[5]) > 1 else None

        # Process Diagnosis Codes
        elif seg_id == 'HI' and in_claim_loop:
            # In 837I, there can be multiple HI segments in the claim
            # Also, in 837I, diagnosis position does not matter
            # We will use continuous numbering for diagnosis codes
            # use the last dx_lookup position as the starting position, and update
            hi_segment = parse_diagnosis_codes(segment)
            hi_segment_realigned = {
                str(int(pos) + len(current_data.dx_lookup)): code
                for pos, code in hi_segment.items()
            }
            current_data.dx_lookup.update(hi_segment_realigned)
            
        # Process Service Lines
        # 
        # SV1 (Professional Services):
        #   SV101 (Required) - Procedure Code Composite: HC qualifier + 5-digit HCPCS code, supports up to 4 HCPCS modifiers
        #   SV102 (Required) - Charge Amount: Format 99999999.99
        #   SV103 (Required) - Unit Type: F2 (International Unit) or UN (Units)
        #   SV104 (Required) - Unit Count: Format 9999.99 (decimals allowed)
        #   SV105 (Situational) - Place of Service Code: Required for First Steps claims
        #   SV107 (Situational) - Diagnosis Code Pointer: Links to HI segment in 2300 loop, valid values 1-8
        #
        # SV2 (Institutional Services):
        #   SV201 (Required) - Revenue Code: Facility-specific revenue code for service rendered
        #   SV202 (Required) - Procedure Code Composite: HC qualifier + 5-digit HCPCS code, supports up to 4 HCPCS modifiers
        #   SV203 (Required) - Charge Amount: Format 99999999.99
        #   SV204 (Required) - Unit Type: DA (Days) or UN (Units)
        #   SV205 (Required) - Unit Count: Format 9999999.999 (whole numbers only - fractional quantities not recognized)
        #   NOTE: Diagnosis Code Pointer is not supported for SV2
        #
        elif seg_id in ['SV1', 'SV2'] and in_claim_loop:
            
            linked_diagnoses = []
            
            if seg_id == 'SV1':
                # SV1 Professional Service: SV101=procedure, SV104=quantity, SV106=place_of_service
                proc_info = get_segment_value(segment, 1, '').split(':')
                procedure_code = proc_info[1] if len(proc_info) > 1 else None
                modifiers = proc_info[2:] if len(proc_info) > 2 else []
                quantity = parse_amount(get_segment_value(segment, 4))
                place_of_service = get_segment_value(segment, 5)
                # Get diagnosis pointers and linked diagnoses
                dx_pointers = get_segment_value(segment, 7, '')
                linked_diagnoses = [
                    current_data.dx_lookup[pointer]
                    for pointer in (dx_pointers.split(':') if dx_pointers else [])
                    if pointer in current_data.dx_lookup
                ]
            else:
                # SV2 Institutional Service: SV201=revenue, SV202=procedure, SV205=quantity
                # Revenue code in SV201
                revenue_code = get_segment_value(segment, 1)
                # Procedure code in SV202
                proc_info = get_segment_value(segment, 2, '').split(':')
                procedure_code = proc_info[1] if len(proc_info) > 1 else None
                modifiers = proc_info[2:] if len(proc_info) > 2 else []
                # Quantity in SV205
                quantity = parse_amount(get_segment_value(segment, 5))
                place_of_service = None  # Not applicable for institutional
                # linked diagnoses are not supported for SV2
                
            
            # Get service line details
            ndc, service_date = process_service_line(segments, i)
            
            # Create service level data
            service_data = ServiceLevelData(
                claim_id=current_data.claim_id,
                procedure_code=procedure_code,
                linked_diagnosis_codes=linked_diagnoses,
                claim_diagnosis_codes=list(current_data.dx_lookup.values()), # this is used for risk adjustment
                claim_type=current_data.claim_type,
                provider_specialty=current_data.provider_specialty,
                performing_provider_npi=current_data.performing_provider_npi,
                billing_provider_npi=current_data.billing_provider_npi,
                patient_id=current_data.patient_id,
                facility_type=current_data.facility_type,
                service_type=current_data.service_type,
                service_date=service_date,
                place_of_service=place_of_service,
                quantity=quantity,
                modifiers=modifiers,
                ndc=ndc,
                allowed_amount=None
            )
            slds.append(service_data)
    
    return slds


def extract_sld_837(content: str) -> List[ServiceLevelData]:
   
    if not content:
        raise ValueError("Input X12 data cannot be empty")
    
    # Split content into segments
    segments = [seg.strip().split('*') 
                for seg in content.split('~') if seg.strip()]
    
    # Detect claim type from GS segment
    claim_type = None
    for segment in segments:
        if segment[0] == 'GS' and len(segment) > 8:
            claim_type = CLAIM_TYPES.get(segment[8])
            break
    
    if not claim_type:
        raise ValueError("Invalid or unsupported 837 format")
    
    split_segments = split_into_claims(segments)
    slds = []
    for claim_segments in split_segments:
        slds.extend(parse_837_claim_to_sld(claim_segments, claim_type))
    
    return slds
    
