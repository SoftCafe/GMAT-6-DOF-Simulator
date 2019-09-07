import unittest
from hypothesis import note, settings
from hypothesis.stateful import RuleBasedStateMachine, rule, invariant, precondition
import matlab.engine

class ControlLawsProperties(RuleBasedStateMachine):
    engine = None
    i = 0
    j = 0
    k = 0
    phi = 0
    theta = 0
    kappa = 0

    def __init__(self):
        super(ControlLawsProperties, self).__init__()

    def __enter__(self):
        self.engine = matlab.engine.start_matlab()

    def __exit__(self, exception_type, exception_value, traceback):
        self.engine.quit()

    @rule()
    @precondition(lambda self: self.phi < 360 )
    def doSomething(self):
        i, j, k, phi, theta, kappa = self.engine.doSomething(
            self.i,
            self.j,
            self.k,
            self.phi,
            self.theta,
            self.kappa)

        self.i = i
        self.j = j
        self.k = k
        self.phi = phi
        self.theta = theta
        self.kappa = kappa

    @invariant()
    def quaternion_invariant_extended_kalman_filtering_for_spacecraft_attitude_estimation(self):
        assert True


TestTrees = ControlLawsProperties.TestCase

# Set max_examples to the number you calculate from heoffdings inequality
ControlLawsProperties.TestCase.settings = settings(
    max_examples=5000) 

if __name__ == '__main__':
    unittest.main()
