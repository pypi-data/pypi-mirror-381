import json
from os.path import join, isdir
import numpy as np
import os
_CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))

env_names = [
    'AbandonedCable', 
    'AbandonedFactory', 
    'AbandonedFactory2', 
    'AbandonedSchool', 
    'AmericanDiner', 
    'AmusementPark', 
    'AncientTowns', 
    'Antiquity3D', 
    'Apocalyptic', 
    'ArchVizTinyHouseDay', 
    'ArchVizTinyHouseNight', 
    'BrushifyMoon', 
    'CarWelding', 
    'CastleFortress', 
    'CoalMine', 
    'ConstructionSite', 
    'CountryHouse', 
    'CyberPunkDowntown', 
    'Cyberpunk', 
    'DesertGasStation', 
    'Downtown', 
    'EndofTheWorld', 
    'FactoryWeather', 
    'Fantasy', 
    'ForestEnv', 
    'Gascola', 
    'GothicIsland', 
    'GreatMarsh', 
    'HQWesternSaloon', 
    'HongKong', 
    'Hospital', 
    'House', 
    'IndustrialHangar', 
    'JapaneseAlley', 
    'JapaneseCity', 
    'MiddleEast', 
    'ModUrbanCity', 
    'ModernCityDowntown', 
    'ModularNeighborhood', 
    'ModularNeighborhoodIntExt', 
    'NordicHarbor', 
    'Ocean', 
    'Office', 
    'OldBrickHouseDay', 
    'OldBrickHouseNight', 
    'OldIndustrialCity', 
    'OldScandinavia', 
    'OldTownFall', 
    'OldTownNight', 
    'OldTownSummer', 
    'OldTownWinter', 
    'PolarSciFi', 
    'Prison', 
    'Restaurant', 
    'RetroOffice', 
    'Rome', 
    'Ruins', 
    'SeasideTown', 
    'SeasonalForestAutumn', 
    'SeasonalForestSpring', 
    'SeasonalForestSummerNight', 
    'SeasonalForestWinter', 
    'SeasonalForestWinterNight', 
    'Sewerage', 
    'ShoreCaves', 
    'Slaughter', 
    'SoulCity', 
    'Supermarket', 
    'TerrainBlending', 
    'UrbanConstruction', 
    'VictorianStreet', 
    'WaterMillDay', 
    'WaterMillNight', 
    'WesternDesertTown',
]

def convert_one_seg_file(envdir, seglabelfile, ind_to_color):
    with open(seglabelfile,'r') as f:
        seglabels = json.load(f)

    for key,  value in seglabels["name_map"].items():
        seglabels["name_map"][key] = int(ind_to_color[value])

    newseglabelfile = join(envdir, 'seg_label_map.json')
    with open(newseglabelfile,'w') as f:
        json.dump(seglabels, f, indent=4)


def convert_seg_file(data_root):
    seg_colors = np.loadtxt(_CURRENT_PATH + '/seg_rgbs.txt', delimiter=',',dtype=np.uint8)
    ind_to_color = {k: seg_colors[k][2] for k in range(seg_colors.shape[0])}

    for env in env_names:
        envdir = join(data_root, env)

        if not isdir(envdir):
            print("Cannot find", envdir)
            continue

        seglabelfile = join(envdir, 'seg_label.json')

        convert_one_seg_file(envdir, seglabelfile, ind_to_color)

if __name__=="__main__":
    # convert_seg_file('/data/tartanair_v2')

    seg_colors = np.loadtxt(_CURRENT_PATH + '/seg_rgbs.txt', delimiter=',',dtype=np.uint8)
    ind_to_color = {k: seg_colors[k][2] for k in range(seg_colors.shape[0])}
    convert_one_seg_file('./', 'seg_label.json', ind_to_color)