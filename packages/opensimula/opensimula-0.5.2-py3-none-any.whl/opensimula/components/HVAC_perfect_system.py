from opensimula.Message import Message
from opensimula.Parameters import Parameter_component, Parameter_float, Parameter_variable_list, Parameter_math_exp
from opensimula.Component import Component
from opensimula.Variable import Variable
import psychrolib as sicro


class HVAC_perfect_system(Component):
    def __init__(self, name, project):
        Component.__init__(self, name, project)
        self.parameter("type").value = "HVAC_perfect_system"
        self.parameter("description").value = "HVAC Perfect system for cooling and heating load"
        self.add_parameter(Parameter_component("spaces", "not_defined", ["Space"])) 
        self.add_parameter(Parameter_variable_list("input_variables", []))
        self.add_parameter(Parameter_math_exp("outdoor_air_flow", "0", "m³/s"))
        self.add_parameter(Parameter_math_exp("heating_setpoint", "20", "°C"))
        self.add_parameter(Parameter_math_exp("cooling_setpoint", "25", "°C"))
        self.add_parameter(Parameter_math_exp("humidifying_setpoint", "0", "%"))
        self.add_parameter(Parameter_math_exp("dehumidifying_setpoint", "100", "%"))
        self.add_parameter(Parameter_math_exp("system_on_off", "1", "on/off"))
        # Variables
        self.add_variable(Variable("Q_total", unit="W"))
        self.add_variable(Variable("Q_sensible", unit="W"))
        self.add_variable(Variable("Q_latent", unit="W"))
        self.add_variable(Variable("outdoor_air_flow", unit="m³/s"))
        self.add_variable(Variable("heating_setpoint", unit="°C"))
        self.add_variable(Variable("cooling_setpoint", unit="°C"))
        self.add_variable(Variable("humidifying_setpoint", unit="%"))
        self.add_variable(Variable("dehumidifying_setpoint", unit="%"))
        self.add_variable(Variable("state", unit="flag")) # 0: 0ff, 1: Heating, -1: Cooling, 3: Venting 
    
    def check(self):
        errors = super().check()
        # Test space defined
        if self.parameter("spaces").value == "not_defined":
            msg =f"{self.parameter('name').value}, must define its space."
            errors.append(Message(msg, "ERROR"))
        # Test file_met defined
        if self.project().parameter("simulation_file_met").value == "not_defined":
            msg = f"{self.parameter('name').value}, file_met must be defined in the project 'simulation_file_met'."
            errors.append(Message(msg, "ERROR"))
        return errors

    def pre_simulation(self, n_time_steps, delta_t):
        super().pre_simulation(n_time_steps, delta_t)
        self._space = self.parameter("spaces").component
        self._file_met = self.project().parameter("simulation_file_met").component
        self.props = self._sim_.props

    def pre_iteration(self, time_index, date, daylight_saving):
        super().pre_iteration(time_index, date, daylight_saving)
        # variables dictonary
        var_dic = self.get_parameter_variable_dictionary(time_index)

        # outdoor air flow
        self._outdoor_air_flow = self.parameter("outdoor_air_flow").evaluate(var_dic)
        self.variable("outdoor_air_flow").values[time_index] = self._outdoor_air_flow
        # setpoints
        self.variable("heating_setpoint").values[time_index] = self.parameter("heating_setpoint").evaluate(var_dic)
        self.variable("cooling_setpoint").values[time_index] = self.parameter("cooling_setpoint").evaluate(var_dic)
        self.variable("humidifying_setpoint").values[time_index] = self.parameter("humidifying_setpoint").evaluate(var_dic)
        self.variable("dehumidifying_setpoint").values[time_index] = self.parameter("dehumidifying_setpoint").evaluate(var_dic)
         # on/off
        self._on_off = self.parameter("system_on_off").evaluate(var_dic)
        if self._on_off == 0:
            self.variable("state").values[time_index] = 0
            self._on_off = False
        else:
            self._on_off = True

        self._T_odb = self._file_met.variable("temperature").values[time_index]
        self._w_o = self._file_met.variable("abs_humidity").values[time_index]
        self._outdoor_rho = 1/sicro.GetMoistAirVolume(self._T_odb,self._w_o/1000,self.props["ATM_PRESSURE"])
        self._T_cool_sp = self.variable("cooling_setpoint").values[time_index]
        self._T_heat_sp = self.variable("heating_setpoint").values[time_index]
        self._HR_min = self.variable("humidifying_setpoint").values[time_index] 
        self._HR_max = self.variable("dehumidifying_setpoint").values[time_index] 

    def iteration(self, time_index, date, daylight_saving, n_iter):
        super().iteration(time_index, date, daylight_saving, n_iter)
        self._control_system = {"M_a": 0, "T_a": 0, "w_a":0, "Q_s":0, "M_w":0 }      
        if self._on_off:
            self._calculate_required_Q()
            self._calculate_required_M()
            self._control_system["Q_s"] = self._Q_spa
            self._control_system["M_w"] = self._M_spa
        self._space.set_control_system(self._control_system)
        return True
    
    def _calculate_required_Q(self):
        K_t,F_t = self._space.get_thermal_equation(False)
        K_ts = K_t + self._outdoor_air_flow * self._outdoor_rho * self.props["C_PA"]
        F_ts = F_t + self._outdoor_air_flow * self._outdoor_rho * self.props["C_PA"] * self._T_odb
        self._T_space = F_ts/K_ts
        if self._T_space > self._T_cool_sp:
            self._T_space = self._T_cool_sp
            self._Q_sys =  K_ts * self._T_space - F_ts
        elif self._T_space < self._T_heat_sp:
            self._T_space = self._T_heat_sp
            self._Q_sys =  K_ts * self._T_space - F_ts
        else: 
            self._Q_sys = 0
        self._Q_spa = K_t * self._T_space - F_t
    
    def _calculate_required_M(self):
        K_h,F_h = self._space.get_humidity_equation(False)
        K_hs = K_h + self._outdoor_air_flow * self._outdoor_rho
        F_hs = F_h + self._outdoor_air_flow * self._outdoor_rho * self._w_o 
        self._w_space = F_hs/K_hs
        if self._w_space < 0:
            self._w_space = 0
        hr_space = sicro.GetRelHumFromHumRatio(self._T_space, self._w_space/1000, self.props["ATM_PRESSURE"])*100
        if hr_space < self._HR_min:
            self._w_space = sicro.GetHumRatioFromRelHum(self._T_space, self._HR_min/100, self.props["ATM_PRESSURE"])*1000
            self._M_sys =  K_hs * self._w_space - F_hs
        elif hr_space > self._HR_max:
            self._w_space = sicro.GetHumRatioFromRelHum(self._T_space, self._HR_max/100, self.props["ATM_PRESSURE"])*1000
            self._M_sys =  K_hs * self._w_space - F_hs
        else:
            self._M_sys = 0
        self._M_spa = K_h * self._w_space - F_h


    def post_iteration(self, time_index, date, daylight_saving, converged):
        super().post_iteration(time_index, date, daylight_saving, converged)
        if self._on_off:
            self.variable("Q_sensible").values[time_index] = self._Q_sys  
            self.variable("Q_latent").values[time_index] = self._M_sys * self.props["LAMBDA"]
            self.variable("Q_total").values[time_index] = self._Q_sys + self._M_sys * self.props["LAMBDA"]
            if self._Q_sys > 0: # Heating, Cooling or Venting
                self.variable("state").values[time_index] = 1
            elif self._Q_sys < 0:
                self.variable("state").values[time_index] = -1
            else:
                self.variable("state").values[time_index] = 3


