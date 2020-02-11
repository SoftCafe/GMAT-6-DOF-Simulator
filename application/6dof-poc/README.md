# 6 Degrees of Freedom Telemetry Demonstration

## Purpose

We want telemetry into a running simulation program. 

This demonstrates how you can use elasticsearch, kibana,
and elastic apm to get telemetry into a python application.

The python application is a simple 6 degrees of freedom 
simulator.

## Operating System Dependencies 

 * python3
 * pip3
 * docker 18


## Steps to Run

### Install elasticapm through pip

```bash
pip install elasticapm
```

### Run Docker Compose

```bash
docker-compose up -d
```

### Run Simulation Script

```
python simulate.py
```

## Visualize Telemetry

We use Kibana to visualize our telemetry data. Visit the following url to open 
the apm dashboard in kibana http://localhost:5601/app/apm

You should see a service named 6do_simulation under the services tab. Click it
to see telemetry into the collection of epochs of the simulation. 

If you run multiple simulations you will see that there are multiple transaction
types. You can filter them in the filters section. 

Each transaction has the format of "epoch%Y-%m-%d-%H-%M-%S". 

Each transaction has multiple epochs that has the format of "epoch-%i"

Each epoch has multiple "spans" that you can click on to gather telemetry into 
the python methods you instrumented with telemetry.

In this case we use fake data.

