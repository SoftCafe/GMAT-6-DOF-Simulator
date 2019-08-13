import unittest
from hypothesis import note, settings
from hypothesis.stateful import RuleBasedStateMachine, rule, invariant
import matlab.engine

class AttitudeActuatorModelProperties(RuleBasedStateMachine):
    engine = None
    phi = 0
    theta = 0
    kappa = 0
    i = 0
    j = 0
    k = 0

    def __init__(self):
        super(AttitudeActuatorModelProperties, self).__init__()

    def __enter__(self):
        self.engine = matlab.engine.start_matlab()

    def __exit__(self):
        self.engine.quit()

    @rule()
    @precondition(lambda self: self.phi < 360 )
    def doSomething(self):
        self.engine.doSomething()

    @invariant()
    def quaternion_invariant_extended_kalman_filtering_for_spacecraft_attitude_estimation(self):
        assert true


TestTrees = AttitudeActuatorModelProperties.TestCase

# Set max_examples to the number you calculate from heoffdings inequality
AttitudeActuatorModelProperties.TestCase.settings = settings(
    max_examples=5000) 

if __name__ == '__main__':
    unittest.main()
