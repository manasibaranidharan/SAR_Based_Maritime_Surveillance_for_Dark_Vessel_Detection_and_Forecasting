# SAR-Based Maritime Surveillance for Dark Vessel Detection and Forecasting
An AI-based maritime surveillance system that uses Sentinel-1 SAR imagery, YOLOv8, and AIS data fusion to detect dark vessels, classify ship types, and forecast vessel trajectories in the Bay of Bengal.





1. INTRODUCTION

Maritime surveillance plays a critical role in coastal security, fisheries regulation, illegal vessel detection, and search-and-rescue operations. A major challenge in ocean monitoring is the presence of dark vessels, which intentionally disable their Automatic Identification System (AIS) to avoid detection.

Conventional optical satellite imagery is often ineffective during nighttime or cloudy weather. To overcome this limitation, this project uses Sentinel-1 Synthetic Aperture Radar (SAR) imagery, which provides reliable all-weather, day-and-night ocean monitoring.

The proposed system integrates:

SAR-based vessel detection
ship type classification
AIS data fusion
suspicious vessel identification
trajectory forecasting
geospatial maritime intelligence

The Bay of Bengal near Chennai and the Tamil Nadu coast is selected as the primary region of interest.



2. PROBLEM STATEMENT

Illegal maritime activities such as unauthorized fishing, smuggling, piracy staging, and covert ship-to-ship transfer are difficult to detect when vessels switch off AIS.

The problem addressed in this work is:

To detect ships from Sentinel-1 SAR imagery, classify vessel types, identify suspicious dark vessels through AIS mismatch, and forecast their movement trajectories for proactive maritime surveillance.



3. OBJECTIVES

The objectives of the project are:

To detect ships from Sentinel-1 SAR imagery using deep learning.
To classify detected ships into operational vessel categories.
To compare detections with AIS streams for dark vessel identification.
To predict vessel trajectories and possible intrusion paths.
To identify suspicious zone violations and loitering behavior.
To develop an interactive surveillance dashboard for maritime intelligence.



4. DATA SOURCES

4.1 PRIMARY DATASET: xView3 SAR

The xView3 SAR dataset contains:

Sentinel-1 SAR scenes
VV and VH bands
vessel bounding boxes
dark vessel labels
metadata such as bathymetry and wind conditions

This dataset is highly suitable for vessel detection and classification tasks.

4.2 AIS DATA

AIS logs are used for:

vessel identity
speed
heading
historical route analysis
trajectory validation

Possible sources:

Global Fishing Watch
MarineCadastre
open AIS datasets

4.3 GEOSPATIAL BOUNDARIES

Additional shapefiles include:

Indian EEZ boundaries
marine protected zones
no-fishing regions
Tamil Nadu coastal waters
shipping lanes



5. METHODOLOGY

5.1 SHIP DETECTION FROM SAR IMAGERY 

A YOLOv8-based object detection model is trained on SAR tiles.

Input:

Sentinel-1 SAR image chips
VV/VH bands
ocean patches

Output:

vessel bounding boxes
confidence scores
vessel dimensions

This stage identifies all visible ships in the SAR scene.

5.2 SHIP CLASSIFICATION MODULE

After detection, each vessel is classified into categories such as:

fishing vessel
cargo ship
tanker
patrol vessel
unknown small craft
Model Options

The classification stage may use:

CNN-based image classifier
feature-based classifier using ship dimensions
AIS metadata-assisted classification
Features Used
vessel length and width
radar backscatter signature
wake pattern
speed profile from AIS
movement behavior

This module is especially useful for distinguishing fishing trawlers from cargo vessels, which is important for illegal fishing detection.

5.3 DARK VESSEL IDENTIFICATION

A detected vessel is flagged as suspicious if:

SAR detects a vessel
no matching AIS signal exists nearby

This indicates a potential:

dark fishing vessel
smuggling vessel
unauthorized coastal intruder

5.4 RESTRICTED ZONE VIOLATION DETECTION

Geofence intelligence is applied using polygon boundaries.

If a vessel enters:

marine reserves
protected fishing zones
defense-sensitive waters
cross-border restricted areas

it is marked as suspicious.

5.5 LOITERING AND SUSPICIOUS PATTERN ANALYSIS

Repeated detections across time are analyzed to detect:

circling behavior
repeated waiting
slow drift
unusual proximity to other ships

These behaviors may indicate:

illegal fishing
piracy preparation
covert cargo exchange
smuggling rendezvous

5.6 TRAJECTORY FORECASTING MODULE

A dedicated forecasting layer predicts future vessel paths.

Inputs
current position
speed
heading
historical AIS path
repeated SAR detections
ocean route constraints
Models

Trajectory prediction can be implemented using:

LSTM
Kalman Filters
GRU
Transformer-based sequence models
Output

The system predicts:

vessel position after 30–60 minutes
possible EEZ intrusion
route toward sensitive coastal areas
likely rendezvous points

This enables proactive maritime alerts instead of only reactive detection.



6. SYSTEM ARCHITECTURE

The complete pipeline may include:

Sentinel-1 SAR ingestion
preprocessing and tiling
YOLOv8 vessel detection
ship classification
AIS matching
dark vessel identification
trajectory forecasting
geofence violation checks
dashboard visualization
alert generation



7. SSOFTWARE AND TOOLS
AI and ML
Python
PyTorch
YOLOv8
TensorFlow (optional for LSTM)
OpenCV
Geospatial
Rasterio
GeoPandas
GDAL
Shapely
Dashboard
Streamlit
FastAPI
Folium / Leaflet
Data
Sentinel-1 SAR
xView3
AIS streams
maritime shapefiles



8. EXPECTED OUTPUTS

The final system produces:

vessel detections with bounding boxes
ship-type classification labels
AIS matched and unmatched vessels
predicted future vessel path lines
zone intrusion alerts
dark vessel hotspot maps
suspicious behavior reports



9. APPLICATIONS

9.1 COASTAL SECURITY

Supports:

Indian Coast Guard
Navy surveillance
maritime border protection
anti-smuggling

9.2 ILLEGAL FISHING PREVENTION

Detects:

unauthorized trawlers
cross-border fishing
repeated dark fishing activity

9.3 MARITIME TRAFFIC INTELLIGENCE

Ship classification and trajectory forecasting improve:

route monitoring
congestion prediction
suspicious path deviation detection

9.4 SEARCH AND RESCUE

Can assist in:

missing boat path prediction
cyclone rescue routing
probable drift zone estimation



10. FUTURE SCOPE

Possible extensions include:

SAR + optical satellite fusion
wake-based vessel behavior analysis
weather-aware routing intelligence
onboard satellite AI payload deployment
real-time Sentinel Hub integration
transformer-based long-range path prediction



11. CONCLUSION

This project presents an integrated maritime surveillance framework for:

dark vessel detection
ship classification
AIS mismatch analysis
trajectory forecasting
suspicious maritime behavior detection
