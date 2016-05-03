# Stream data generator

## Scripts
The default `generate.py` contains the color sensor data. The `generate_alert_enabled.sh` script contains the so called alert enabled (alertEnabled) data. It generates 1 or 0 as value attribute. Both scripts has the same parameters.

## Usage
### Paramters
```bash
python generate.py <backoff in seconds> <number of events per iteration>  <folder to generate in>
```
### Example
```bash
python generate.py 1 10 ~/stream-data/
```

