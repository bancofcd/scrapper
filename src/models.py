from pydantic import BaseModel
from pathlib import Path
from datetime import datetime
from typing import Optional

class CompanyMetadata(BaseModel):
  """
  Clase con la metadata que se va a extraer
  """
  rut: Optional[str],
  razon_social: str,
  actuacion: str,
  nro_atencion: int,
  cve: Optional[str],
  
  fecha: Optional[datetime],
  
  
  
  
