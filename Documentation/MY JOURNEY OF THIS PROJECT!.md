


Hey! SO as u all know, im doing this project . And my sole reason of doing this report thingy rn is to write a daily personal report or journal (sort of!) for myself, maybe because in the future (that is in 25 days thats my target), when i finally finish this project, i would like to look back at the process i went through of learning a lotta challenges, from setting up environment to handling the datasets to working out with the model and literally everything!! i am in my second year (gonna enter third) and unfortunately this is my first exciting projec that i will be working on! why unfortunately? cause i just wasted 1.5 years of my life waiting to get a compatible laptop for me, and fyi i still didnt! thanks to my bf, im using his laptop to start up with my projects very soon just so i dont get behind, thanks nithu <333 so yeah, BETTER LATE THAN NEVER IG!!

seems like an over buildup lmaoo but idky im pretty excited to work on my first project!! kay so lets get started!!


DAY-1 (April 8, 2026)
-----------------------------------------------
today, i worked on to setup the environment for the project, before that i cloned my gitup repository and saved my file locally

so the following libraries i installed for the environment setup today were:
1) rasterio (used to **open Sentinel-1 `.tif` SAR images**) 
2)  ultralytics (This gives you **YOLOv8 ship detection AI**)
3) matplotlib (Used to **display satellite images**)
4) pandas (Used for **AIS CSV ship location data**)
5) numpy (Used for matrix/image operations)
6) opencv-python (Useful later for image preprocessing , cropping ship tiles and drawing boxes)
7) folium (Used to show ships from Bay of Bengal Map)
8) streamlit (Used to build your **final dashboard UI** like map,alerts,darkvesselresult,future route)
9) streamlit-folium (This connects **Folium maps inside Streamlit dashboard**)


I might later install these (But depends on whether they are essentially important):
1) tensorflow
2)  scikit-learn
3) geopandas
4) shapely

So for now I installed those 9 and then to check if they were installed, i ran a test code (test_libs.py) and it successfully worked in the terminal, but not in vs code. when i check why, i realized i was working on a conda based environment, and vs code was running on system python. so i changed the python interpreter and then it successfully worked!
thats it!