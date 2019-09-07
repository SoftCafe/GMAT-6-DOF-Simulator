import unittest
from hypothesis import note, settings
from hypothesis.stateful import RuleBasedStateMachine, rule, invariant, precondition
import matlab.engine

class Simulation(RuleBasedStateMachine):
    matlab_engine = None
    gmat_engine = None

    """
        simulation_state can have the following values
        - NOT_RUNNING
        - RUNNING_CONTROL_LAWS
        - RUNNING_ATTITUDE_DETERMINATION
        - RUNNING_ATTITUDE_SENSOR_MODELS
        - RUNNING_SPACECRAFT_DYNAMICS_MODELS
        - RUNNING_SPACECRAFT_ACTUATOR_MODELS
        - RUNNING_DISTURBANCE_MODELS
        - ERROR
    """
    simulation_state = "NOT_RUNNING"

    """
        J_1 = Principal Moment of Inertia about X axis (slug-ft^2)
        J_2 = Principal Moment of Inertia about Y axis (slug-ft^2)
        J_3 = Principal Moment of Inertia about Z axis (slug-ft^2)
        J_T = Inertia Tensor (slug-ft^2)

        omega_1 = Inertial body rate about X axis (rad/sec)
        omega_2 = Inertial body rate about Y axis (rad/sec)
        omega_3 = Inertial body rate about Z axis (rad/sec)
        omega_T = Body rate vector with respect to inertial frame (rad/sec)

        T1_ext = External disturbance torque on X body axis (ft-lb)
        T2_ext = External disturbance torque on Y body axis (ft-lb)
        T3_ext = External disturbance torque on Z body axis (ft-lb)
        T_ext = External disturbance torque vector in body axes (ft-lb)

        u_1 = Control torque on X body axis (ft-lb)
        u_2 = Control torque on Y body axis (ft-lb)
        u_3 = Control torque on Z body axis (ft-lb)
    """

    J_1 = 0 
    J_2 = 0
    J_3 = 0
    J_T = 0

    omega_1 = 0
    omega_2 = 0
    omega_3 = 0
    omega_T = 0
    
    T1_ext = 0
    T2_ext = 0
    T3_ext = 0
    T_ext = 0

    u_1 = 0
    u_2 = 0
    u_3 = 0

    def __init__(self):
        super(Simulation, self).__init__()

    def __enter__(self):
        self.matlab_engine = matlab.engine.start_matlab()

    def __exit__(self, exception_type, exception_value, traceback):
        self.matlab_engine.quit()

    @rule()
    @precondition(lambda self: self.simulation_state == "RUNNING_CONTROL_LAWS" )
    def control_law_action1(self):
        # Fake action
        new_state = self.matlab_engine.action1(
            self.J_1,
            self.J_2,
            self.J_3,
            self.J_T,

            self.omega_1,
            self.omega_2,
            self.omega_3,
            self.omega_T,
            
            self.T1_ext,
            self.T2_ext,
            self.T3_ext,
            self.T_ext,

            self.u_1,
            self.u_2,
            self.u_3
        )

        # Fake Postconditions
        assert new_state.J_1 > 0
        assert new_state.J_2 > 0
        assert new_state.J_3 > 0
        assert new_state.J_T > 0

        # Update the system state
        self.J_1 = new_state.J_1
        self.J_2 = new_state.J_2
        self.J_3 = new_state.J_3
        self.J_T = new_state.J_T


    @rule()
    @precondition(lambda self: self.simulation_state == "RUNNING_ATTITUDE_DETERMINATION" )
    def attitude_determination_action1(self):
        pass

    @invariant()
    def simulation_will_not_be_in_an_error_state(self):
        assert self.simulation_state != "ERROR"

    @invariant()
    def quaternion_invariant_extended_kalman_filtering_for_spacecraft_attitude_estimation(self):
        # Fake invariant check
        assert True


TestTrees = Simulation.TestCase

# Set max_examples to the number you calculate from heoffdings inequality
Simulation.TestCase.settings = settings(
    max_examples=5000) 

if __name__ == '__main__':
    unittest.main()
