from typing import List, Dict, Set, Tuple, Optional
from hccinfhir.datamodels import ModelName
from hccinfhir.utils import load_dx_to_cc_mapping

# Load default mappings from csv file
mapping_file_default = 'ra_dx_to_cc_2026.csv'
dx_to_cc_default = load_dx_to_cc_mapping(mapping_file_default)

def get_cc(
    diagnosis_code: str,
    model_name: ModelName = "CMS-HCC Model V28",
    dx_to_cc_mapping: Dict[Tuple[str, ModelName], Set[str]] = dx_to_cc_default
) -> Optional[Set[str]]:
    """
    Get CC for a single diagnosis code.

    Args:
        diagnosis_code: ICD-10 diagnosis code
        model_name: HCC model name to use for mapping
        dx_to_cc_mapping: Optional custom mapping dictionary

    Returns:
        CC code if found, None otherwise
    """
    return dx_to_cc_mapping.get((diagnosis_code, model_name))

def apply_mapping(
    diagnoses: List[str],
    model_name: ModelName = "CMS-HCC Model V28", 
    dx_to_cc_mapping: Dict[Tuple[str, ModelName], Set[str]] = dx_to_cc_default
) -> Dict[str, Set[str]]:
    """
    Apply ICD-10 to CC mapping for a list of diagnosis codes.
    
    Args:
        diagnoses: List of ICD-10 diagnosis codes
        model_name: HCC model name to use for mapping
        dx_to_cc_mapping: Optional custom mapping dictionary
        
    Returns:
        Dictionary mapping CCs to lists of diagnosis codes that map to them
    """
    cc_to_dx: Dict[str, Set[str]] = {}
    
    for dx in set(diagnoses):
        dx = dx.upper().replace('.', '')
        ccs = get_cc(dx, model_name, dx_to_cc_mapping)
        if ccs is not None:
            for cc in ccs:
                if cc not in cc_to_dx:
                    cc_to_dx[cc] = set()
                cc_to_dx[cc].add(dx)
                
    return cc_to_dx
