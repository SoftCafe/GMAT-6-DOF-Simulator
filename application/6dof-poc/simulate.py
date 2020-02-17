"""
    This application demonstrates a simple design for instrumenting 
    telemetry into a 6dof simulation program.
"""

import elasticapm
from elasticapm import Client
from datetime import datetime
import random

client = Client(
        service_name="6dof_simulation",
        debug = False)

#@elasticapm.capture_span()
def handle_attitude_sensor(token):
    with elasticapm.capture_span('attitude_sensor_log', labels=token):
        pass

    return {
        "name": "attitude_sensor_done",
        "payload": {
            "attitude_sensor": {
                "attribute1": str(random.random()),
                "attribute2": str(random.random()),
                "attribute3": str(random.random()),
            }
        }
    }

#@elasticapm.capture_span()
def handle_attitude_sensor_drivers(token):
    with elasticapm.capture_span('attitude_sensor_drivers_log', labels=token):
        pass

    return {
        "name": "attitude_sensor_driver_done",
        "payload": {
            "attitude_sensor_drivers": {
                "attribute1": str(random.random()),
                "attribute2": str(random.random()),
                "attribute3": str(random.random()),
            }
        }
    }

#@elasticapm.capture_span()
def handle_attitude_sensor_data_integration(token):
    with elasticapm.capture_span('attitude_sensor_data_integration_log', labels=token):
        pass

    return {
        "name": "attitude_sensor_data_integration_done",
        "payload": {
            "attitude_sensor_data_integration_log_attribute1": str(random.random()),
            "attitude_sensor_data_integration_log_attribute2": str(random.random()),
            "attitude_sensor_data_integration_log_attribute3": str(random.random()),
        }
    }

#@elasticapm.capture_span()
def handle_command_and_control(token):
    with elasticapm.capture_span('command_and_control_log', labels=token):
        pass

    return {
        "name": "command_and_control_done",
        "payload": {
            "command_and_control_attribute1": str(random.random()),
            "command_and_control_attribute2": str(random.random()),
            "command_and_control_attribute3": str(random.random()),
        }
    }

#@elasticapm.capture_span()
def handle_high_level_attitude_command_integrator(token):
    with elasticapm.capture_span('high_level_attitude_command_log', labels=token):
        pass

    return {
        "name": "high_level_attitude_command_integrator_done",
        "payload": {
            "high_level_attitude_command_integrator_attribute1": str(random.random()),
            "high_level_attitude_command_integrator_attribute2": str(random.random()),
            "high_level_attitude_command_integrator_attribute3": str(random.random()),
        }
    }

#@elasticapm.capture_span()
def handle_attitude_actuator_drivers(token):
    with elasticapm.capture_span('attitude_actuator_driver_log', labels=token):
        pass

    return {
        "name": "attitude_actuator_drivers_done",
        "payload": {
            "actuator_driver_attribute1": str(random.random()),
            "actuator_driver_attribute2": str(random.random()),
            "actuator_driver_attribute3": str(random.random()),
        }
    }

#@elasticapm.capture_span()
def handle_attitude_actuator_controller(token):
    with elasticapm.capture_span('attitude_actuator_contoller_log', labels=token):
        pass

    return {
        "name": "attitude_actuator_controller_done",
        "payload": {
            "attitude_actuator_controller1": str(random.random()),
            "attitude_actuator_controller2": str(random.random()),
            "attitude_actuator_controller3": str(random.random()),
        }
    }

#@elasticapm.capture_span()
def run_simulation():

    task_for_token = {
        "start": handle_attitude_sensor,
        "attitude_sensor_done": handle_attitude_sensor_drivers,
        "attitude_sensor_driver_done": handle_attitude_sensor_data_integration,
        "attitude_sensor_data_integration_done": handle_command_and_control,
        "command_and_control_done": handle_high_level_attitude_command_integrator,
        "high_level_attitude_command_integrator_done": handle_attitude_actuator_drivers,
        "attitude_actuator_drivers_done": handle_attitude_actuator_controller

    }

    now = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    transaction_type = "epoch-"+now

    for i in range(10):
        client.begin_transaction(
                transaction_type=transaction_type)

        token = {
            "name": "start",
            "payload": {}
        }

        while True:
            if token["name"] in task_for_token:
                client.capture_message(token)
                token = task_for_token[token["name"]](token)
            else:
                break


        client.end_transaction("epoch-" + str(i))

 
    url = "http://localhost:5601/app/apm#/services/6dof_simulation/transactions?transactionType=" + transaction_type
    import webbrowser
    webbrowser.open(url, new=2)

    print("url: ", url)


run_simulation()
