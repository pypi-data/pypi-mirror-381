from OpenSimula.components.Test_component import Test_component
from OpenSimula.components.Material import Material
from OpenSimula.components.Glazing import Glazing
from OpenSimula.components.Frame import Frame
from OpenSimula.components.Construction import Construction
from OpenSimula.components.Opening_type import Opening_type
from OpenSimula.components.File_data import File_data
from OpenSimula.components.Day_schedule import Day_schedule
from OpenSimula.components.Week_schedule import Week_schedule
from OpenSimula.components.Year_schedule import Year_schedule
from OpenSimula.components.File_met import File_met
from OpenSimula.components.Space_type import Space_type
from OpenSimula.components.Building import Building
from OpenSimula.components.Space import Space
from OpenSimula.components.Building_surface import Building_surface
from OpenSimula.components.Solar_surface import Solar_surface
from OpenSimula.components.Opening import Opening
from OpenSimula.components.Calculator import Calculator
from OpenSimula.components.HVAC_DX_equipment import HVAC_DX_equipment
from OpenSimula.components.HVAC_coil_equipment import HVAC_coil_equipment
from OpenSimula.components.HVAC_fan_equipment import HVAC_fan_equipment
from OpenSimula.components.HVAC_DX_system import HVAC_DX_system
from OpenSimula.components.HVAC_SZW_system import HVAC_SZW_system
from OpenSimula.components.HVAC_MZW_system import HVAC_MZW_system
from OpenSimula.components.HVAC_perfect_system import HVAC_perfect_system

DEFAULT_COMPONENTS_ORDER = [
                    "Space_type",
                    "Building_surface",
                    "Solar_surface",
                    "Opening",
                    "Space",
                    "Building",
                    "HVAC_MZW_system",
                    "HVAC_perfect_system",
                    "HVAC_DX_system",
                    "HVAC_SZW_system",
                    "Calculator"
                ]

