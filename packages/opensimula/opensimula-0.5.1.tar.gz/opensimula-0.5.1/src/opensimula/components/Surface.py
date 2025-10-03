import math
import numpy as np
from opensimula.Component import Component
from opensimula.Message import Message
from opensimula.Parameters import Parameter_options, Parameter_float, Parameter_float_list
from shapely.geometry import Polygon
from opensimula.Variable import Variable


class Surface(Component):
    def __init__(self, name, project):
        Component.__init__(self, name, project)
        # Parameters
        self.parameter("type").value = "Surface"
        self.add_parameter(Parameter_float("azimuth", 0, "°", min=-180, max=180))  # Surface x vs Building x -> S: 0º, E: 90º, W: -90º, N: 180º
        self.add_parameter(Parameter_float("altitude", 0, "°", min=-90, max=90))  # Surface y vs Building y -> vertical: 0º, facing up: 90º, facing down: -90º
        self.add_parameter(Parameter_options(
            "shape", "RECTANGLE", ["RECTANGLE", "POLYGON"]))
        self.add_parameter(Parameter_float("width", 1, "m", min=0.0))
        self.add_parameter(Parameter_float("height", 1, "m", min=0.0))
        # Building Coordinate system
        self.add_parameter(Parameter_float_list(
            "ref_point", [0, 0, 0], "m", min=float("-inf")))
        self.add_parameter(Parameter_float_list(
            "x_polygon", [0, 10, 10, 0], "m", min=float("-inf")))
        self.add_parameter(Parameter_float_list(
            "y_polygon", [0, 0, 10, 10], "m", min=float("-inf")))
        
        # Variables
        self.add_variable(Variable("E_dir_sunny", "W/m²"))  # Without shadows
        self.add_variable(Variable("E_dir", "W/m²"))
        self.add_variable(Variable("E_dif_sunny", "W/m²"))  # Without shadows
        self.add_variable(Variable("E_dif", "W/m²"))

    def check(self):
        errors = super().check()
        # Test if Polygon shape that x_polygon and y_polygon has the same size
        if self.parameter("shape").value == "POLYGON":
            if len(self.parameter("x_polygon").value) != len(self.parameter("y_polygon").value):
                msg = f"{self.parameter('name').value}, x_polygo and y_polygon must have the same size."
                errors.append(Message(msg, "ERROR"))
        return errors

    def pre_simulation(self, n_time_steps, delta_t):
        super().pre_simulation(n_time_steps, delta_t)

    @property
    def area(self):
        if (self.parameter("shape").value == "RECTANGLE"):
            return self.parameter("width").value * self.parameter("height").value
        elif (self.parameter("shape").value == "POLYGON"):
            polygon = []
            n = len(self.parameter("x_polygon").value)
            for i in range(0, n):
                polygon.append([self.parameter("x_polygon").value[i],
                               self.parameter("y_polygon").value[i]])
            return Polygon(polygon).area

    # exterior normal vector
    def orientation_angle(self, angle, side, coordinate_system="global"):
        if angle == "azimuth":
            az = self.parameter("azimuth").value
            if self.get_building() is not None and coordinate_system == "global":
                    azi_building = self.get_building().parameter("azimuth").value
                    az = az + azi_building
            if side == 0:
                return az
            elif side == 1:
                if az > 0:
                    return az-180
                else:
                    return az+180
        elif angle == "altitude":
            alt = self.parameter("altitude").value
            if side == 0:
                return alt
            elif side == 1:
                return -alt

    def get_building(self): # Default no building
        return None
    
    def radiant_property(self, prop, radiation_type, side, theta=0):
        """It must be redefined by child classes

        Args:
            prop (_type_): _description_
            radiation_type (_type_): _description_
            side (_type_): _description_

        Returns:
            _type_: _description_
        """
        return 0

    def get_origin(self, coordinate_system="global"):
        if self.get_building() is not None:
            if coordinate_system == "global":
                az_b = math.radians(self.get_building().parameter("azimuth").value)
                local_origin = self.parameter("ref_point").value
                global_origin = [local_origin[0]*math.cos(az_b)-local_origin[1]*math.sin(az_b),
                             local_origin[0]*math.sin(az_b) +
                             local_origin[1]*math.cos(az_b),
                             local_origin[2]]
                return global_origin
            elif coordinate_system == "building":
                return np.array(self.parameter("ref_point").value)+ np.array(self.get_building().parameter("ref_point").value)
            else:
                return self.parameter("ref_point").value
        else:
            return self.parameter("ref_point").value

    def get_polygon_2D(self):  # Get polygon_2D
        if (self.parameter("shape").value == "RECTANGLE"):
            w = self.parameter("width").value
            h = self.parameter("height").value
            return [[0, 0], [w, 0], [w, h], [0, h]]
        elif (self.parameter("shape").value == "POLYGON"):
            polygon2D = []
            n = len(self.parameter("x_polygon").value)
            for i in range(0, n):
                polygon2D.append([self.parameter("x_polygon").value[i],
                                  self.parameter("y_polygon").value[i]])
            return polygon2D
        
    def get_polygon_3D(self): # Global coordenates
        return None

    
