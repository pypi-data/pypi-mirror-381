# OpenEarth Python API

A Python client for the OpenEarth API that provides environmental data insights including weather, air quality, flood risk, wildfire monitoring, and more.

## Features

- **Weather Analysis**: Rain, precipitation, and weather pattern queries
- **Air Quality Monitoring**: AQI, PM2.5/PM10, ozone, smoke, and haze data
- **Flood Risk Assessment**: Flash flooding, inundation, and standing water analysis
- **Wildfire Monitoring**: Fire risk, evacuation routes, and air quality impact
- **Geographic Analysis**: Urban, suburban, and rural area-specific insights
- **Real-time Data**: Live environmental data from multiple sources

## Installation

```bash
pip install openearth
```

## Quick Start

```python
from openearth import OpenEarth

# Check API health
print(oe.health())

# Query environmental data
result = oe.query("What's the air quality in San Francisco?")
print(result)

# Close the client
oe.close()
```

## API Usage


### `query(query: str)`
Send a natural language query about environmental conditions.

```python
# Air quality queries  
result = oe.query("Is there smoke affecting air quality in Portland?")

# Flood risk queries
result = oe.query("Flash flooding potential in Miami?")

# Wildfire queries
result = oe.query("Evacuation routes for fire in Napa Valley?")
```

## Requirements

- Python 3.11+
- httpx >= 0.27.0

## License

Proprietary
