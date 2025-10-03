# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:48:22 2021

@author: svc_ccg
"""

import argparse
import datetime
import json
import os
import subprocess
import requests
import yaml


def download_raw_text_from_github(github_uri, path):
    """Intended for python 2.7
    """
    response = requests.get(github_uri)
    if not response.status_code in (200, ):
        response.raise_for_status()

    with open(path, "wb") as f:
        f.write(response.content)
    return path


def download_local_package(output_dir, asset_map):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    package_dir = os.path.abspath(os.path.join(
       output_dir,
        "DynamicRoutingTaskPackage-{}".format(timestamp),
    ))
    os.mkdir(package_dir)
    local_assets = {}
    for asset_name, asset in asset_map.items():
        filename = os.path.basename(asset)
        local_path = os.path.abspath(
            os.path.join(
                package_dir,
                filename,
            )
        )
        local_assets[asset_name] = download_raw_text_from_github(
            asset,
            local_path
        )
    return local_assets


env = 'DynamicRoutingTaskDev'

parser = argparse.ArgumentParser()
parser.add_argument('params')
parser.add_argument('-o')

args = parser.parse_args()

paramsPath = args.params
paramsDir = os.path.dirname(paramsPath)

with open(paramsPath,'r') as f:
    params = json.load(f)

ghTaskScriptParams = params.get('GHTaskScriptParams')
if ghTaskScriptParams:
    local_assets = download_local_package(paramsDir, ghTaskScriptParams)
    params['taskScript'] = local_assets['taskScript']
    if 'analysisScript' in ghTaskScriptParams:
        params['analysisScript'] = local_assets['analysisScript']
    
if 'useCamstimConfig' in params and params['useCamstimConfig']:
    import time
    import uuid
    from camstim.zro.agent import CAMSTIM_CONFIG_PATH, OUTPUT_DIR
    from camstim.misc import CAMSTIM_CONFIG
    
    params['userName'] = params['user_id']
    params['subjectName'] = params['mouse_id']
    
    taskName = os.path.splitext(os.path.basename(params['taskScript']))[0]
    params['startTime'] = time.strftime('%Y%m%d_%H%M%S',time.localtime())
    params['savePath'] = os.path.join(OUTPUT_DIR,taskName + '_' + params['subjectName'] + '_' + params['startTime'] + '.hdf5')
    foraging_id = uuid.uuid4()
    params['sessionId'] = foraging_id.hex
    params['limsUpload'] = params['limsUpload'] if 'limsUpload' in params else True
                                  
    params['configPath'] = CAMSTIM_CONFIG_PATH
    if CAMSTIM_CONFIG_PATH.endswith('yml'):
        with open(CAMSTIM_CONFIG_PATH,'r') as f:
            config = yaml.safe_load(f)
        params['rotaryEncoderSerialPort'] = config['shared']['DigitalEncoder']['serial_device']
        params['behavNidaqDevice'] = config['Behavior']['nidevice']
        params['rewardLines'] = config['shared']['Reward']['reward_lines']
        params['lickLines'] = config['shared']['Licksensing']['lick_lines']
    elif CAMSTIM_CONFIG_PATH.endswith('cfg'):
        import ConfigParser
        config = ConfigParser.ConfigParser()
        config.read(CAMSTIM_CONFIG_PATH)
        params['rotaryEncoderSerialPort'] = eval(config.get('DigitalEncoder','serial_device'))
        params['behavNidaqDevice'] = eval(config.get('Behavior','nidevice'))
        params['rewardLines'] = eval(config.get('Reward','reward_lines'))
        params['lickLines'] = eval(config.get('Licksensing','lick_lines'))
    
    params['computerName'] = os.environ['aibs_comp_id']
    params['rigName'] = os.environ['aibs_rig_id']
    
    waterCalibration = CAMSTIM_CONFIG['shared']['water_calibration'][params['computerName']]
    params['waterCalibrationSlope'] = waterCalibration['slope']
    params['waterCalibrationIntercept'] = waterCalibration['intercept']
    
    soundCalibration = CAMSTIM_CONFIG['sound_calibration']
    params['soundCalibrationFit'] = [soundCalibration[param] for param in 'abc']
    
    paramsPath = os.path.join(paramsDir,'taskParams.json')
    with open(paramsPath,'w') as f:
        json.dump(params,f)


toRun = ('"C:\\Program Files\\AIBS_MPE\\SetVol\\SetVol.exe" unmute 100' + '\n' +
         'call activate ' + env + '\n' +
         'python ' + '"' + params['taskScript'] + '" ' + '"' + paramsPath + '"')

batFile = os.path.join(paramsDir,'toRun.bat')

with open(batFile,'w') as f:
    f.write(toRun)
    
p = subprocess.Popen([batFile])
p.wait()


if 'limsUpload' in params and params['limsUpload']:
    from shutil import copyfile
    from camstim.lims import LimsInterface, write_behavior_trigger_file
    
    try:
        if 'analysisScript' in params:
            postAnalysis = ('call activate ' + env + '\n' +
                            'python ' + '"' + params['analysisScript'] + '" ' + '"' + params['savePath'] + '"')
            batFile = os.path.join(paramsDir,'postAnalysis.bat')
            with open(batFile,'w') as f:
                f.write(postAnalysis)  
            p = subprocess.Popen([batFile])
            p.wait()
    except:
        pass
    
    lims = LimsInterface()
    triggerDir = lims.get_trigger_dir(params['subjectName'])
    incomingDir = os.path.dirname(triggerDir.rstrip('/'))
    outputFileName = os.path.basename(params['savePath'])
    outputPath = os.path.join(incomingDir,outputFileName)
    triggerFileName = os.path.splitext(outputFileName)[0] + '.bt'
    triggerPath = os.path.join(triggerDir,triggerFileName)
    copyfile(params['savePath'],outputPath)
    write_behavior_trigger_file(triggerPath,params['subjectName'],params['sessionId'],params['userName'],outputPath)

    import imp
    mtrain_uploader = imp.load_source('mtrain_uploader', '//allen/programs/mindscope/workgroups/dynamicrouting/DynamicRoutingTask/dynamicrouting_behavior_session_mtrain_upload.py')
    mtrain_uploader.add_behavior_session_to_mtrain_upload_queue(filename=outputFileName, foraging_id=str(foraging_id))