# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 14:35:34 2023

@author: svc_ccg
"""

import copy
import os
import numpy as np
import pandas as pd
import scipy
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['pdf.fonttype'] = 42
from DynamicRoutingAnalysisUtils import getPerformanceStats,getFirstExperimentSession,getSessionsToPass,getSessionData,pca,cluster,calcDprime


baseDir = r"\\allen\programs\mindscope\workgroups\dynamicrouting"

summarySheets = pd.read_excel(os.path.join(baseDir,'Sam','BehaviorSummary.xlsx'),sheet_name=None)
summaryDf = pd.concat((summarySheets['not NSB'],summarySheets['NSB']))

drSheets = pd.read_excel(os.path.join(baseDir,'DynamicRoutingTask','DynamicRoutingTraining.xlsx'),sheet_name=None)
nsbSheets = pd.read_excel(os.path.join(baseDir,'DynamicRoutingTask','DynamicRoutingTrainingNSB.xlsx'),sheet_name=None)

miceToIgnore = summaryDf['wheel fixed'] | summaryDf['cannula']

hasIndirectRegimen = np.array(summaryDf['stage 3 alt'] | summaryDf['stage 3 distract'] | summaryDf['stage 4'] | summaryDf['stage var'])

hitThresh = 100
dprimeThresh = 1.5

deltaLickProbLabels = ('5 rewarded targets',
                       '1 rewarded target',
                       '5 non-rewarded targets',
                       '1 non-rewarded target',
                       'rewarded target first',
                       'non-rewarded target first',
                       '5 rewards',
                       '5 catch trials')
deltaLickProb = {lbl: {targ: np.nan for targ in ('rewTarg','nonRewTarg')} for lbl in deltaLickProbLabels}


def plotLearning(mice,stage,xlim=None):
    hitCount = {lbl:[] for lbl in mice}
    dprime = {lbl:[] for lbl in mice}
    sessionsToPass = {lbl:[] for lbl in mice}
    for lbl,mouseIds in mice.items():
        for mid in mouseIds:
            df = drSheets[str(mid)] if str(mid) in drSheets else nsbSheets[str(mid)]
            sessions = np.where(np.array([str(stage) in task for task in df['task version']]) & ~np.array(df['ignore'].astype(bool)))[0]
            hitCount[lbl].append([])
            dprime[lbl].append([])
            for sessionInd in sessions:
                hits,dprimeSame,dprimeOther = getPerformanceStats(df,[sessionInd])
                hitCount[lbl][-1].append(hits[0][0])
                dprime[lbl][-1].append(dprimeSame[0][0])
            sessionsToPass[lbl].append(getSessionsToPass(mid,df,sessions,stage))
    
    print({lbl: np.median(sessionsToPass[lbl]) for lbl in sessionsToPass})
    
    if xlim is None:              
        xlim = (0.5,max(np.nanmax(ps) for ps in sessionsToPass.values())+0.5)
    xticks = np.arange(0,100,5) if xlim[1]>10 else np.arange(10)
    clrs = 'gm' if len(mice) > 1 else 'k'
                
    for data,thresh,ylbl in zip((hitCount,dprime),(hitThresh,dprimeThresh),('Hit count','d\'')):
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax.plot(xlim,[thresh]*2,'k--')
        for lbl,clr in zip(mice.keys(),clrs):
            m = np.full((len(data[lbl]),int(np.nanmax(sessionsToPass[lbl]))),np.nan)
            for i,d in enumerate(data[lbl]):
                d = d[:sessionsToPass[lbl][i]]
                m[i,:len(d)] = d
                ax.plot(np.arange(len(d))+1,d,color=clr,alpha=0.25,zorder=2)
                ax.plot(sessionsToPass[lbl][i],d[sessionsToPass[lbl][i]-1],'o',ms=12,color=clr,alpha=0.5,zorder=0)
            lbl += ' (n='+str(np.sum(~np.isnan(sessionsToPass[lbl])))+')'
            # ax.plot(np.arange(m.shape[1])+1,np.nanmean(m,axis=0),clr,lw=2,zorder=1)   
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False,labelsize=14)
        ax.set_xticks(xticks)
        ax.set_xlim(xlim)
        if ylbl=='d\'':
            ax.set_yticks(np.arange(-1,6))
            ax.set_ylim((-0.5,5) if stage==1 else (-0.5,4))
        ax.set_xlabel('Session',fontsize=16)
        ax.set_ylabel(ylbl,fontsize=16)
        plt.tight_layout()
        
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    for lbl,clr in zip(mice.keys(),clrs):
        dsort = np.sort(np.array(sessionsToPass[lbl])[~np.isnan(sessionsToPass[lbl])])
        cumProb = np.array([np.sum(dsort<=i)/dsort.size for i in dsort])
        lbl += ' (n='+str(dsort.size)+')'
        ax.plot(dsort,cumProb,color=clr,label=lbl)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=14)
    ax.set_xticks(xticks)
    ax.set_xlim(xlim)
    ax.set_ylim([0,1.01])
    ax.set_xlabel('Sessions to pass',fontsize=16)
    ax.set_ylabel('Cumalative fraction',fontsize=16)
    plt.legend(loc='lower right')
    plt.tight_layout()   
    
    
def plotStage5Learning(mice):
    dpSame = {lbl: [] for lbl in mice}
    dpOther = {lbl: [] for lbl in mice}
    sessionsToPass = {lbl: [] for lbl in mice}
    for lbl in mice:
        for mid in mice[lbl]:
            df = drSheets[str(mid)] if str(mid) in drSheets else nsbSheets[str(mid)]
            sessions = np.array(['stage 5' in task for task in df['task version']]) & ~np.array(df['ignore'].astype(bool))
            firstExperimentSession = getFirstExperimentSession(df)
            if firstExperimentSession is not None:
                sessions[firstExperimentSession:] = False
            sessions = np.where(sessions)[0]
            dpSame[lbl].append([])
            dpOther[lbl].append([])
            for sessionInd in sessions:
                hits,dprimeSame,dprimeOther = getPerformanceStats(df,[sessionInd])
                dpSame[lbl][-1].append(dprimeSame[0])
                dpOther[lbl][-1].append(dprimeOther[0])
            sessionsToPass[lbl].append(getSessionsToPass(mid,df,sessions,stage=5))
            
    print({lbl: np.median(sessionsToPass[lbl]) for lbl in sessionsToPass})

    xlim = (0.5,max(np.nanmax(ps) for ps in sessionsToPass.values())+0.75)
    xticks = np.arange(0,100,5)
    clrs = 'gmrbc'[:len(mice)] if len(mice) > 1 else 'k'
                
    for dp,ylbl in zip((dpSame,dpOther),('d\' (same modality)','d\' (cross-modality)')):
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax.plot(xlim,[dprimeThresh]*2,'k--')
        for lbl,clr in zip(mice.keys(),clrs):
            for d,ps in zip(dp[lbl],sessionsToPass[lbl]):
                d = np.nanmean(d,axis=1)
                ax.plot(np.arange(len(d))+1,d,color=clr,alpha=0.25,zorder=2)
                ax.plot(ps,d[ps-1],'o',ms=12,color=clr,alpha=0.5,zorder=0)
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False,labelsize=12)
        ax.set_xticks(xticks)
        ax.set_xlim(xlim)
        ax.set_yticks(np.arange(-1,5))
        ax.set_ylim([-1,4])
        ax.set_xlabel('Session',fontsize=14)
        ax.set_ylabel(ylbl,fontsize=14)
        plt.tight_layout()
        
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    for lbl,clr in zip(mice.keys(),clrs):
        dsort = np.sort(np.array(sessionsToPass[lbl])[~np.isnan(sessionsToPass[lbl])])
        cumProb = np.array([np.sum(dsort<=i)/dsort.size for i in dsort])
        lbl += ' (n='+str(dsort.size)+')'
        ax.plot(dsort,cumProb,color=clr,label=lbl)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=12)
    ax.set_xticks(xticks)
    ax.set_xlim(xlim)
    ax.set_ylim([0,1.01])
    ax.set_xlabel('Sessions to pass',fontsize=14)
    ax.set_ylabel('Cumalative fraction',fontsize=14)
    plt.legend(loc='lower right')
    plt.tight_layout()
    
    
## drop out summary
isDoneTraining = summaryDf['reason for early termination'].isnull()
for isNsb in (~summaryDf['nsb'],summaryDf['nsb']):
    stage1Mice = summaryDf['moving grating'] & summaryDf['timeouts'] & ~miceToIgnore & isNsb
    print(np.sum(stage1Mice & summaryDf['stage 1 pass']),'of',np.sum(stage1Mice),'passed')
    summaryDf[stage1Mice & ~summaryDf['stage 1 pass']]['reason for early termination']
    
    stage2Mice = stage1Mice & summaryDf['stage 1 pass'] & summaryDf['AM noise'] & isNsb
    print(np.sum(stage2Mice & summaryDf['stage 2 pass']),'of',np.sum(stage2Mice),'passed')
    summaryDf[stage2Mice & ~summaryDf['stage 2 pass']]['reason for early termination']

    stage5Mice = stage2Mice & summaryDf['stage 2 pass'] & ~(summaryDf['reason for early termination']=='ephys before stage 5') & ~hasIndirectRegimen & ~summaryDf['stage 5 repeats'] & isNsb
    print(np.sum(stage5Mice & summaryDf['stage 5 pass']),'of',np.sum(stage5Mice),'passed')
    summaryDf[stage5Mice & ~summaryDf['stage 5 pass']]['reason for early termination']

fig = plt.figure(figsize=(15,5))
ax = fig.add_subplot(1,1,1)
clrs = np.tile(plt.cm.tab10(np.linspace(0,1,10)),(int(np.ceil(stage5Mice.sum()/10)),1))[:stage5Mice.sum()]
for mid,clr in zip(summaryDf[stage5Mice]['mouse id'],clrs):
    df = drSheets[str(mid)] if str(mid) in drSheets else nsbSheets[str(mid)]
    sessions = np.array(['stage 5' in task for task in df['task version']]) & ~np.array(df['ignore'].astype(bool))
    firstExperimentSession = getFirstExperimentSession(df)
    if firstExperimentSession is not None:
        sessions[firstExperimentSession:] = False
    sessions = np.where(sessions)[0]
    sessionsToPass = getSessionsToPass(mid,df,sessions,stage=5)
    dpSame = []
    dpOther = []
    for i,sessionInd in enumerate(sessions):
        hits,dprimeSame,dprimeOther = getPerformanceStats(df,[sessionInd])
        dpSame.append(dprimeSame[0])
        dpOther.append(dprimeOther[0])
        j = np.timedelta64(np.random.choice([-12,12]),'h')
        if np.isnan(sessionsToPass) or i < sessionsToPass:
            ax.plot(df.loc[sessionInd,'start time']+j,i+1,'o',mec=clr,mfc='none',alpha=0.25)
        else:
            ax.plot(df.loc[sessionInd,'start time']+j,i+1,'o',mec=clr,mfc=clr,alpha=0.75)
            break
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False,labelsize=12)
ax.set_xlabel('Start date (stage 3)',fontsize=14)
ax.set_ylabel('Training day',fontsize=14)
plt.tight_layout()



## WHC vs HP-only
ind = summaryDf['stage 1 pass'] & summaryDf['moving grating'] & summaryDf['timeouts'] & ~miceToIgnore
mice = {'WHC':  np.array(summaryDf[ind & summaryDf['craniotomy']]['mouse id']),
        'HP-only': np.array(summaryDf[ind & ~summaryDf['craniotomy']]['mouse id'])}
plotLearning(mice,stage=1,xlim=None)

ind = summaryDf['stage 2 pass'] & summaryDf['AM noise'] & summaryDf['timeouts'] & ~miceToIgnore
mice = {'WHC':  np.array(summaryDf[ind & summaryDf['craniotomy']]['mouse id']),
        'HP-only': np.array(summaryDf[ind & ~summaryDf['craniotomy']]['mouse id'])}
plotLearning(mice,stage=2,xlim=None)

ind = ~hasIndirectRegimen & summaryDf['stage 5 pass'] & summaryDf['moving grating'] & summaryDf['AM noise'] & ~summaryDf['stage 5 repeats'] & ~miceToIgnore
mice = {'WHC':  np.array(summaryDf[ind & summaryDf['craniotomy']]['mouse id']),
        'HP-only': np.array(summaryDf[ind & ~summaryDf['craniotomy']]['mouse id'])}
plotStage5Learning(mice)

stage1Mice = summaryDf['moving grating'] & summaryDf['timeouts'] & ~miceToIgnore 
stage2Mice = stage1Mice & summaryDf['stage 1 pass'] & summaryDf['AM noise']
stage5Mice = stage2Mice & summaryDf['stage 2 pass'] & ~(summaryDf['reason for early termination']=='ephys before stage 5') & ~hasIndirectRegimen & ~summaryDf['stage 5 repeats']


print(np.sum(stage5Mice & summaryDf['craniotomy'] & summaryDf['stage 5 pass'] ),'of',np.sum(stage5Mice & summaryDf['craniotomy']),'WHC passed')
print(np.sum(stage5Mice & ~summaryDf['craniotomy'] & summaryDf['stage 5 pass'] ),'of',np.sum(stage5Mice & ~summaryDf['craniotomy']),'HP-only passed')


## standard regimen mice stage 1 and 2
ind = ~hasIndirectRegimen & summaryDf['moving grating'] & summaryDf['AM noise'] & ~summaryDf['stage 5 repeats'] & ~miceToIgnore   
mice = {'stage 1 pass': np.array(summaryDf[ind & summaryDf['stage 1 pass']]['mouse id'])}
plotLearning(mice,stage=1,xlim=None)
  
mice = {'stage 2 pass': np.array(summaryDf[ind & summaryDf['stage 2 pass']]['mouse id'])}
plotLearning(mice,stage=2,xlim=None)

mice = {'stage 5 pass': np.array(summaryDf[ind & summaryDf['stage 5 pass']]['mouse id'])}
plotStage5Learning(mice)



## stage 1, stationary gratings with or without timeouts
ind = summaryDf['stage 1 pass'] & summaryDf['stat grating'] & ~miceToIgnore
mice = {'stationary, timeouts': np.array(summaryDf[ind & summaryDf['timeouts']]['mouse id']),
        'stationary, no timeouts': np.array(summaryDf[ind & ~summaryDf['timeouts']]['mouse id'])}
plotLearning(mice,stage=1,xlim=(0.5,20.5))

# stage 1, stationary vs moving gratings, both with timeouts
ind = summaryDf['stage 1 pass'] & summaryDf['timeouts'] & ~miceToIgnore
mice = {'moving':  np.array(summaryDf[ind & summaryDf['moving grating']]['mouse id']),
        'stationary': np.array(summaryDf[ind & summaryDf['stat grating']]['mouse id'])}
plotLearning(mice,stage=1,xlim=(0.5,20.5))

# stage 1, moving gratings
ind = summaryDf['stage 1 pass'] & summaryDf['moving grating'] & summaryDf['timeouts'] & ~miceToIgnore
mice = {'moving': np.array(summaryDf[ind]['mouse id'])}
plotLearning(mice,stage=1,xlim=None)

# stage 1, moving gratings with or without reward clicks
ind = summaryDf['stage 1 pass'] & summaryDf['moving grating'] & summaryDf['timeouts'] & ~miceToIgnore
mice = {'moving, reward click': np.array(summaryDf[ind & summaryDf['reward click']]['mouse id']),
        'moving, no reward click':  np.array(summaryDf[ind & ~summaryDf['reward click']]['mouse id'])}
plotLearning(mice,stage=1,xlim=(0.5,20.5))

# stage 1, moving gratings with early or late autorewards
ind = summaryDf['stage 1 pass'] & summaryDf['moving grating'] & summaryDf['timeouts'] & ~miceToIgnore
mice = {'moving, early AR': np.array(summaryDf[ind & ~summaryDf['late autoreward (stage 1)']]['mouse id']),
        'moving, late AR':  np.array(summaryDf[ind & summaryDf['late autoreward (stage 1)']]['mouse id'])}
plotLearning(mice,stage=1,xlim=(0.5,20.5))
                

# stage 2, tones, timeouts with noise vs no timeouts
ind = summaryDf['stage 2 pass'] & summaryDf['tone'] & ~summaryDf['wheel fixed'] & ~miceToIgnore
mice = {'tones, timeouts': np.array(summaryDf[ind & summaryDf['timeouts']]['mouse id']),
        'tones, no timeouts':  np.array(summaryDf[ind  & ~summaryDf['timeouts']]['mouse id'])}
plotLearning(mice,stage=2)

# stage 2, tones with noise timeouts vs AMN with noiseless timeouts
ind = summaryDf['stage 2 pass'] & summaryDf['timeouts'] & ~summaryDf['wheel fixed'] & ~miceToIgnore
mice = {'tones': np.array(summaryDf[ind & summaryDf['tone']]['mouse id']),
        'AM noise':  np.array(summaryDf[ind & summaryDf['AM noise']]['mouse id'])}
plotLearning(mice,stage=2)

# stage 2, AMN
ind = summaryDf['stage 2 pass'] & summaryDf['AM noise'] & summaryDf['timeouts'] & ~miceToIgnore
mice = {'AM noise': np.array(summaryDf[ind]['mouse id'])}
plotLearning(mice,stage=2)

# stage 2, AMN with or without reward clicks
ind = summaryDf['stage 2 pass'] & summaryDf['AM noise'] & summaryDf['timeouts'] & ~miceToIgnore
mice = {'AM noise, reward click': np.array(summaryDf[ind & summaryDf['reward click']]['mouse id']),
        'AM noise, no reward click':  np.array(summaryDf[ind & ~summaryDf['reward click']]['mouse id'])}
plotLearning(mice,stage=2)

# stage 2, AMN with early or late autorewwards
ind = summaryDf['stage 2 pass'] & summaryDf['AM noise'] & summaryDf['timeouts'] & ~miceToIgnore
mice = {'AM noise, early AR': np.array(summaryDf[ind & ~summaryDf['late autoreward (stage 2)']]['mouse id']),
        'AM noise, late AR':  np.array(summaryDf[ind & summaryDf['late autoreward (stage 2)']]['mouse id'])}
plotLearning(mice,stage=2)


# stage 5, repeats vs no repeats
ind = ~hasIndirectRegimen & summaryDf['stage 5 pass'] & ~miceToIgnore
mice = {'no repeats': np.array(summaryDf[ind & ~summaryDf['stage 5 repeats']]['mouse id']),
        'repeats': np.array(summaryDf[ind & summaryDf['stage 5 repeats']]['mouse id'])}
plotStage5Learning(mice)

# stage 5, moving, AMN, no repeats
ind = ~hasIndirectRegimen & summaryDf['stage 5 pass'] & summaryDf['moving grating'] & summaryDf['AM noise'] & ~summaryDf['stage 5 repeats'] & ~miceToIgnore
mice = {'moving, AMN': np.array(summaryDf[ind]['mouse id'])}
plotStage5Learning(mice)

# stage 5, with or without reward clicks
ind = ~hasIndirectRegimen & summaryDf['stage 5 pass'] & summaryDf['moving grating'] & summaryDf['AM noise'] & ~summaryDf['stage 5 repeats'] & ~miceToIgnore
mice = {'reward click': np.array(summaryDf[ind & summaryDf['reward click']]['mouse id']),
        'no reward click':  np.array(summaryDf[ind & ~summaryDf['reward click']]['mouse id'])}
plotStage5Learning(mice)

# stage 5, early or late autorewards
ind = ~hasIndirectRegimen & summaryDf['stage 5 pass'] & summaryDf['moving grating'] & summaryDf['AM noise'] & ~summaryDf['stage 5 repeats'] & ~miceToIgnore
mice = {'early AR': np.array(summaryDf[ind & ~summaryDf['late autoreward (stage 5)']]['mouse id']),
        'late AR':  np.array(summaryDf[ind & summaryDf['late autoreward (stage 5)']]['mouse id'])}
plotStage5Learning(mice)


## moving to stationary grating switch
preSessions = 1
postSessions = 1
dprime = []
for mid in summaryDf[summaryDf['moving to stat']]['mouse id']:
    df = drSheets[str(mid)] if str(mid) in drSheets else nsbSheets[str(mid)]
    prevTask = None
    dprime.append([])
    for i,task in enumerate(df['task version']):
        if prevTask is not None and 'stage 5' in prevTask and 'stage 5' in task and 'moving' in prevTask and 'moving' not in task:
            for j in range(i-preSessions,i+postSessions+1):
                hits,dprimeSame,dprimeOther = getPerformanceStats(df,[j])
                if 'ori tone' in df.loc[j,'task version'] or 'ori AMN' in df.loc[j,'task version']:
                    dprime[-1].append(np.mean(dprimeSame[0][0:2:6]))
                else:
                    dprime[-1].append(np.mean(dprimeSame[0][1:2:6]))
            break
        prevTask = task

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
xticks = np.arange(-preSessions,postSessions+1)
for dp in dprime:
    ax.plot(xticks,dp,'k',alpha=0.25)
mean = np.mean(dprime,axis=0)
sem = np.std(dprime,axis=0)/(len(dprime)**0.5)
ax.plot(xticks,mean,'ko-',lw=2,ms=12)
for x,m,s in zip(xticks,mean,sem):
    ax.plot([x,x],[m-s,m+s],'k',lw=2)
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False,labelsize=12)
ax.set_xticks(xticks)
ax.set_xticklabels(['-1\nmoving','0\nstationary','1\nmoving'])
ax.set_xlim([-preSessions-0.5,postSessions+0.5])
ax.set_yticks(np.arange(5))
ax.set_ylim([0,4.1])
ax.set_xlabel('Session',fontsize=14)
ax.set_ylabel('d\'',fontsize=14)
plt.tight_layout()


## within modality d' after stage 2
ind = ~hasIndirectRegimen & summaryDf['stage 5 pass'] & summaryDf['moving grating'] & summaryDf['AM noise'] & ~summaryDf['stage 5 repeats'] & ~miceToIgnore
mice = np.array(summaryDf[ind]['mouse id'])

dprime = {'vis': [], 'aud': []}
for mid in mice:
    df = drSheets[str(mid)] if str(mid) in drSheets else nsbSheets[str(mid)]
    sessions = np.array(['stage 5' in task for task in df['task version']]) & ~np.array(df['ignore'].astype(bool))
    firstExperimentSession = getFirstExperimentSession(df)
    if firstExperimentSession is not None:
        sessions[firstExperimentSession:] = False
    sessions = np.where(sessions)[0]
    for lbl in dprime:
        dprime[lbl].append([])
        for sessionInd in sessions:
            hits,dprimeSame,dprimeOther = getPerformanceStats(df,[sessionInd])
            dprimeSame = dprimeSame[0]
            task = df.loc[sessionInd,'task version']
            if (lbl=='vis' and 'ori AMN' in task) or (lbl=='aud' and 'AMN ori' in task):
                dprime[lbl][-1].append(np.nanmean(dprimeSame[0:6:2]))
            else:
                dprime[lbl][-1].append(np.nanmean(dprimeSame[1:6:2]))

maxSessions = max(len(d) for lbl in dprime for d in dprime[lbl])
minMice = 8
            
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
xmax = 1000
for lbl,clr in zip(('vis','aud'),'gm'):
    y = np.full((len(dprime[lbl]),maxSessions+1),np.nan)
    for i,d in enumerate(dprime[lbl]):
        y[i,:len(d)] = d
    lb = 'visual-rewarded blocks' if lbl=='vis' else 'auditory-rewarded blocks'
    #lb += ' (n='+str(len(dprime[lbl]))+')'
    x = np.arange(y.shape[1])+1
    n = np.sum(~np.isnan(y),axis=0)
    xmax = min(xmax,x[n>=minMice][-1])
    m = np.nanmean(y,axis=0)
    s = np.nanstd(y,axis=0)/(len(y)**0.5)
    ax.plot(x,m,color=clr,label=lb)
    ax.fill_between(x,m+s,m-s,color=clr,alpha=0.25)
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False,labelsize=12)
ax.set_xlim([0.5,xmax])
ax.set_yticks(np.arange(-1,5))
ax.set_ylim([-1,4])
ax.set_xlabel('Session',fontsize=14)
ax.set_ylabel('d\' (same modality)',fontsize=14)
plt.legend(loc='lower right')
plt.tight_layout()


## transition to hab and ephys
ind = ~hasIndirectRegimen & summaryDf['stage 5 pass'] & summaryDf['moving grating'] & summaryDf['AM noise'] & ~summaryDf['stage 5 repeats'] & ~miceToIgnore
mice = tuple(summaryDf[ind]['mouse id'])
mice += (644864,644866,644867,681532,686176) # non-standard training
ephysMice = []
nSessions = 5
preHabSessions = []
habSessions = []
ephysSessions = []
for mid in mice:
    df = drSheets[str(mid)] if str(mid) in drSheets else nsbSheets[str(mid)]
    if df['hab'].any() and df['ephys'].any():
        ephysMice.append(mid)
        sessions = np.array(['stage 5' in task for task in df['task version']]) & ~np.array(df['ignore'].astype(bool))
        firstHab = np.where(df[sessions]['hab'])[0][0]
        preHabSessions.append([getSessionData(mid,startTime) for startTime in df.loc[np.where(sessions)[0][firstHab-nSessions:firstHab],'start time']])
        habSessions.append([getSessionData(mid,startTime) for startTime in df[np.array(df['hab']).astype(bool)]['start time']])
        ephysSessions.append([getSessionData(mid,startTime) for startTime in df[np.array(df['ephys']).astype(bool)]['start time']])


xticks = np.arange(nSessions*2)
xticklbls = xticks - nSessions
xticklbls[-nSessions:] += 1
for ylbl in ('Hit rate','Quiescent violations',
             'Cross-modal d\'','Cross-modal d\' (visual blocks)','Cross-modal d\' (auditory blocks)',
             'Within-modal d\' (visual)','Within-modal d\' (auditory)'):
    fig = plt.figure(figsize=(5,8))
    for axInd,(sessions,title) in enumerate(zip(((preHabSessions,habSessions),(habSessions,ephysSessions)),('hab','ephys'))):
        ax = fig.add_subplot(2,1,axInd+1)
        ax.plot([nSessions-0.5]*2,[-10000,10000],'k--')
        d = np.full((len(ephysMice),nSessions*2),np.nan)
        for i,(before,after) in enumerate(zip(*sessions)):
            if ylbl == 'Hit rate':
                b,a = [[np.nanmean(obj.hitRate) for obj in s] for s in (before,after)]
            elif ylbl == 'Quiescent violations':
                b,a = [[obj.quiescentViolationFrames.size for obj in s] for s in (before,after)]
            elif ylbl == 'Cross-modal d\'':
                b,a = [[np.nanmean(obj.dprimeOtherModalGo) for obj in s] for s in (before,after)]
            elif ylbl == 'Cross-modal d\' (visual blocks)':
                b,a = [[np.nanmean(np.array(obj.dprimeOtherModalGo)[obj.blockStimRewarded=='vis1']) for obj in s] for s in (before,after)]
            elif ylbl == 'Cross-modal d\' (auditory blocks)':
                b,a = [[np.nanmean(np.array(obj.dprimeOtherModalGo)[obj.blockStimRewarded=='sound1']) for obj in s] for s in (before,after)]
            elif ylbl == 'Within-modal d\' (visual)':
                b,a = [[np.nanmean(np.array(obj.dprimeSameModal)[obj.blockStimRewarded=='vis1']) for obj in s] for s in (before,after)]
            elif ylbl == 'Within-modal d\' (auditory)':
                b,a = [[np.nanmean(np.array(obj.dprimeSameModal)[obj.blockStimRewarded=='sound1']) for obj in s] for s in (before,after)]
            j = min(nSessions,len(b))
            d[i,nSessions-j:nSessions] = b[-j:]
            k = min(nSessions,len(a))
            d[i,nSessions:nSessions+k] = a[:k]
        for y in d:
            ax.plot(xticks,y,'k',alpha=0.1)
        m = np.nanmean(d,axis=0)
        s = np.nanstd(d,axis=0)/(len(d)**0.5)
        ax.plot(xticks,m,color='k',lw=2)
        ax.fill_between(xticks,m+s,m-s,color='k',alpha=0.3)
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False)
        ax.set_xticks(xticks)
        ax.set_xticklabels(xticklbls)
        ax.set_xlim([0,nSessions*2 - 1])
        if ylbl == 'Hit rate':
            ylim = [0,1.02]
        elif 'd\'' in ylbl:
            ylim = [0,4]
        else:
            ylim = [0,np.nanmax(d)+1]
        ax.set_ylim(ylim)
        ax.set_xlabel('Session')
        ax.set_ylabel(ylbl)
        ax.set_title('Switch to '+title)
    plt.tight_layout()
    

for ylbl in ('Cross-modal d\'','Within-modal d\' (auditory)'):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    x = []
    y = []
    for pre,hab,ephys in zip(preHabSessions,habSessions,ephysSessions):
            x.extend([obj.quiescentViolationFrames.size for obj in pre+hab+ephys])
            if ylbl == 'Cross-modal d\'':
                y.extend([np.nanmean(obj.dprimeOtherModalGo) for obj in pre+hab+ephys])
            else:
                y.extend([np.nanmean(np.array(obj.dprimeSameModal)[obj.blockStimRewarded=='sound1']) for obj in pre+hab+ephys])
    ax.plot(x,y,'ko')
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False)
    ax.set_xlim([0,max(x)*1.02])
    ax.set_ylim([min(y)-0.1,max(y)+0.1])
    ax.set_xlabel('Quiescent violations')
    ax.set_ylabel(ylbl)
    plt.tight_layout()


hitCount = np.concatenate([obj.hitCount for exps in ephysSessions for obj in exps])
dprime = np.concatenate([obj.dprimeOtherModalGo for exps in ephysSessions for obj in exps])

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(hitCount,dprime,'ko',alpha=0.2)
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False)
ax.set_xlabel('Block hit count')
ax.set_ylabel('Block cross-modal d\'')
plt.tight_layout()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
bins = np.arange(25)
ax.hist(hitCount,bins,color='k',align='left')
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False)
ax.set_xlabel('Hit count')
ax.set_ylabel('# blocks')
plt.tight_layout()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
bins = np.arange(-4,4.5,0.5)
ax.hist(dprime,bins,color='k')
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False)
ax.set_xlabel('Cross-modal d\'')
ax.set_ylabel('# blocks')
plt.tight_layout()


dpThreshRange = np.arange(0,3.5,0.5)
hitThreshRange = np.arange(0,21)
nBlockThresh = 4
nPassing = np.zeros((dpThreshRange.size,hitThreshRange.size))
for i,dpThresh in enumerate(dpThreshRange):
    for j,hitThresh in enumerate(hitThreshRange):
        nPassing[i,j] = sum([sum([h >= hitThresh and dp >= dpThresh for h,dp in zip(obj.hitCount,obj.dprimeOtherModalGo)]) >= nBlockThresh for exps in ephysSessions for obj in exps])
nSessions = sum(len(s) for s in ephysSessions)
    
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
im = ax.imshow(nPassing/nSessions,clim=(0,1),cmap='inferno',origin='lower')
cb = plt.colorbar(im,ax=ax,fraction=0.01,pad=0.04)
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False)
ax.set_xticks(np.arange(0,25,5))
ax.set_yticks(np.arange(dpThreshRange.size))
ax.set_yticklabels(dpThreshRange)
ax.set_xlabel('Hit count threshold')
ax.set_ylabel('Cross-modal d\' threshold')
ax.set_title('Fraction of sessions with at least 4 blocks > threshold')
plt.tight_layout()
    

    
## stage 0 responses
preStim = []
postStim = []
postStimRt =[]
postStimRtz = []
postReward = []
postRewardRt = []
postRewardRtz = []
for m,mid in enumerate(summaryDf['mouse id']):
    print(m)
    df = drSheets[str(mid)] if str(mid) in drSheets else nsbSheets[str(mid)]
    sessions = np.array(['stage 0' in task for task in df['task version']]) & ~np.array(df['ignore'].astype(bool))
    session = np.where(sessions)[0][0]
    startTime = df.loc[session,'start time']
    obj = getSessionData(mid,startTime)
    if obj.autoRewardOnsetFrame == 60:
        preStim.append([])
        postStim.append([])
        postStimRt.append([])
        postReward.append([])
        postRewardRt.append([])
        for t in obj.stimStartTimes:
            preStim[-1].append(np.any((obj.lickTimes > t-0.8) & (obj.lickTimes <= t+0.1)))
            
            licks = (obj.lickTimes > t+0.1) & (obj.lickTimes <= t+1)
            if np.any(licks):
                postStim[-1].append(True)
                postStimRt[-1].append(obj.lickTimes[licks][0] - t)
            else:
                postStim[-1].append(False)
                postStimRt[-1].append(np.nan)
            
            licks = (obj.lickTimes > t+1) & (obj.lickTimes <= t+1.9)
            if np.any(licks):
                postReward[-1].append(True)
                postRewardRt[-1].append(obj.lickTimes[licks][0] - (t+1))
            else:
                postReward[-1].append(False)
                postRewardRt[-1].append(np.nan)
        rt = np.array(postStimRt[-1])
        postStimRtz.append((rt-np.nanmean(rt))/np.nanstd(rt))
        rt = np.array(postRewardRt[-1])
        postRewardRtz.append((rt-np.nanmean(rt))/np.nanstd(rt))
            
x = np.arange(150) + 1
plt.plot(x,np.mean(preStim,axis=0),'r')
plt.plot(x,np.mean(postStim,axis=0),'g')
plt.plot(x,np.mean(postReward,axis=0),'b')

plt.plot([0,1],[0,1],'k--')
plt.plot(np.mean(preStim,axis=1),np.mean(postStim,axis=1),'ko')

plt.plot([0,1],[0,1],'k--')
plt.plot(np.mean(preStim,axis=1),np.mean(postReward,axis=1),'ko')

plt.plot(x,np.nanmean(postStimRt,axis=0),'g')
plt.plot(x,np.nanmean(postRewardRt,axis=0),'b')

plt.plot(x,np.nanmean(postStimRtz,axis=0),'g')
plt.plot(x,np.nanmean(postRewardRtz,axis=0),'b')



## stage 5 training
ind = ~hasIndirectRegimen & summaryDf['stage 5 pass'] & summaryDf['moving grating'] & summaryDf['AM noise'] & ~summaryDf['stage 5 repeats'] & ~miceToIgnore
mice = np.array(summaryDf[ind]['mouse id'])
hasLateAutorewards = np.array(summaryDf[ind]['late autoreward (stage 5)'])

dprime = {comp: {mod: [] for mod in ('all','vis','sound')} for comp in ('same','other')}
sessionsToPass = []
sessionData = []
for mid in mice:
    df = drSheets[str(mid)] if str(mid) in drSheets else nsbSheets[str(mid)]
    sessions = np.array(['stage 5' in task for task in df['task version']]) & ~np.array(df['ignore'].astype(bool))
    firstExperimentSession = getFirstExperimentSession(df)
    if firstExperimentSession is not None:
        sessions[firstExperimentSession:] = False
    sessions = np.where(sessions)[0]
    for sessionInd in sessions:
        hits,dprimeSame,dprimeOther = getPerformanceStats(df,[sessionInd])
        for dp,comp in zip((dprimeSame,dprimeOther),('same','other')):
            if sessionInd == sessions[0]:
                for mod in ('all','vis','sound'):
                    dprime[comp][mod].append([])
            dp = dp[0]
            dprime[comp]['all'][-1].append(dp)
            task = df.loc[sessionInd,'task version']
            visFirst = 'ori tone' in task or 'ori AMN' in task
            if visFirst:
                dprime[comp]['vis'][-1].append(dp[0:6:2])
                dprime[comp]['sound'][-1].append(dp[1:6:2])
            else:
                dprime[comp]['sound'][-1].append(dp[0:6:2])
                dprime[comp]['vis'][-1].append(dp[1:6:2])
    sessionsToPass.append(getSessionsToPass(mid,df,sessions,stage=5))
    try:
        sessionData.append([getSessionData(mid,startTime) for startTime in df.loc[sessions,'start time']])
    except:
        pass

           
mouseClrs = plt.cm.tab20(np.linspace(0,1,len(sessionsToPass)))

for comp in ('same','other'):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    dp = np.full((len(dprime[comp]['all']),max(len(d) for d in dprime[comp]['all'])),np.nan)
    for i,(d,clr) in enumerate(zip(dprime[comp]['all'],mouseClrs)):
        y = np.nanmean(d,axis=1)[:sessionsToPass[i]+5]
        ax.plot(np.arange(len(y))+1,y,color=clr,alpha=0.25,zorder=2)
        ax.plot(sessionsToPass[i],y[sessionsToPass[i]-1],'o',ms=12,color=clr,alpha=0.5,zorder=0)
        dp[i,:len(y)] = y
    # m = np.nanmean(dp,axis=0)
    # ax.plot(np.arange(len(m))+1,m,color='k',lw=2,zorder=1)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=16)
    ax.set_xlim([0,max(sessionsToPass)+6])
    ax.set_yticks(np.arange(-1,5))
    ax.set_ylim([-0.5,4])
    ax.set_xlabel('Session',fontsize=18)
    ax.set_ylabel(('Cross' if comp=='other' else 'Within')+'-modal '+'d\'',fontsize=18)
    plt.tight_layout()
    
for comp in ('same','other'):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    dp = np.full((len(dprime[comp]['all']),120),np.nan)
    xintp = np.linspace(0,1.2,120)
    for i,(d,clr) in enumerate(zip(dprime[comp]['all'],mouseClrs)):
        y = np.nanmean(d,axis=1)[:sessionsToPass[i]+5]
        x = np.linspace(0,1,sessionsToPass[i])
        x = np.concatenate((x,1+x[1:6]))
        if y.size < x.size:
            y = np.concatenate((y,[np.nan]*(x.size-y.size)))
        ax.plot(x,y,color=clr,alpha=0.25,zorder=2)
        ax.plot(1,y[sessionsToPass[i]-1],'o',ms=12,color=clr,alpha=0.5,zorder=0)
        dp[i] = np.interp(xintp,x,y)
    m = np.nanmean(dp,axis=0)
    ax.plot(xintp,m,color='k',lw=2,zorder=1)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=12)
    # ax.set_xlim([0,max(sessionsToPass)+2])
    ax.set_ylim([-0.5,4])
    ax.set_xlabel('Session normalized to passing session',fontsize=14)
    ax.set_ylabel('d\' '+comp+' modality',fontsize=14)
    plt.tight_layout()
    
for comp in ('same','other'):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    dp = np.full((len(dprime[comp]['all']),100),np.nan)
    xintp = np.linspace(0,1,100)
    for i,(d,clr) in enumerate(zip(dprime[comp]['all'],mouseClrs)):
        y = np.nanmean(d,axis=1)[:sessionsToPass[i]+5]
        x = np.linspace(0,1,len(y))
        ax.plot(x,y,color=clr,alpha=0.25,zorder=2)
        ax.plot(x[sessionsToPass[i]-1],y[sessionsToPass[i]-1],'o',ms=12,color=clr,alpha=0.5,zorder=0)
        dp[i] = np.interp(xintp,x,y)
    m = np.nanmean(dp,axis=0)
    s = np.nanstd(dp,axis=0)/(len(dp)**0.5)
    ax.plot(xintp,m,color='k',lw=2,zorder=1)
    ax.fill_between(xintp,m+s,m-s,color='k',alpha=0.25)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=16)
    # ax.set_xlim([0,max(sessionsToPass)+2])
    ax.set_yticks(np.arange(-1,5))
    ax.set_ylim([-0.5,4])
    ax.set_xlabel('Normalized session',fontsize=18)
    ax.set_ylabel(('Cross' if comp=='other' else 'Within')+'-modal '+'d\'',fontsize=18)
    plt.tight_layout()

for comp in ('same','other'):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    for mod,clr in zip(('vis','sound'),'gm'):
        dp = np.full((len(dprime[comp][mod]),max(len(d) for d in dprime[comp][mod])),np.nan)
        for i,d in enumerate(dprime[comp][mod]):
            y = np.nanmean(d,axis=1)
            ax.plot(np.arange(len(y))+1,y,color=clr,alpha=0.25,zorder=2)
            dp[i,:len(y)] = y
        m = np.nanmean(dp,axis=0)
        lbl = 'visual-rewarded blocks' if mod=='vis' else 'auditory-rewarded blocks'
        ax.plot(np.arange(len(m))+1,m,color=clr,lw=2,zorder=1,label=lbl)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=12)
    ax.set_xlim([0,max(sessionsToPass)+2])
    ax.set_ylim([-3,4])
    ax.set_xlabel('Session',fontsize=14)
    lbl = ' (same modal)' if comp=='same' else ' (cross-modal)'
    ax.set_ylabel('d\''+lbl,fontsize=14)
    plt.legend(loc='lower right')
    plt.tight_layout()
   
for comp in ('same','other'):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    dp = np.full((len(dprime[comp]['all']),100),np.nan)
    xintp = np.linspace(0,1,100)
    for mod,clr in zip(('vis','sound'),'gm'):
        for i,d in enumerate(dprime[comp][mod]):
            y = np.nanmean(d,axis=1)[:sessionsToPass[i]+5]
            x = np.linspace(0,1,len(y))
            # ax.plot(x,y,color=clr,alpha=0.25,zorder=2)
            dp[i] = np.interp(xintp,x,y)
        m = np.nanmean(dp,axis=0)
        s = np.nanstd(dp,axis=0)/(len(dp)**0.5)
        ax.plot(xintp,m,color=clr,lw=2,zorder=0,label=('visual' if mod=='vis' else 'auditory')+' rewarded blocks')
        ax.fill_between(xintp,m+s,m-s,color=clr,alpha=0.25)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=16)
    ax.set_yticks((np.arange(4) if comp=='same' else np.arange(-0.5,3,0.5)))
    ax.set_ylim(([0,3.5] if comp=='same' else [-0.5,2]))
    ax.set_xlabel('Normalized session',fontsize=18)
    ax.set_ylabel(('Cross' if comp=='other' else 'Within')+'-modal '+'d\'',fontsize=18)
    plt.legend(loc='lower right',fontsize=14)
    plt.tight_layout()
    
for comp in ('same','other'):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    dp = np.full((len(dprime[comp]['all']),100),np.nan)
    xintp = np.linspace(0,1,100)
    for i,(v,a,clr) in enumerate(zip(dprime[comp]['vis'],dprime[comp]['sound'],mouseClrs)):
        y = (np.nanmean(a,axis=1) - np.nanmean(v,axis=1))[:sessionsToPass[i]+5]
        # y = scipy.ndimage.median_filter(y,3,mode='nearest')
        # y = np.convolve(y,np.ones(5)/5,mode='same')
        y = scipy.ndimage.gaussian_filter(y,1,mode='nearest')
        x = np.linspace(0,1,len(y))
        ax.plot(x,y,color=clr,alpha=0.25)
        dp[i] = np.interp(xintp,x,y)
    m = np.nanmean(dp,axis=0)
    s = np.nanstd(dp,axis=0)/(len(dp)**0.5)
    ax.plot(xintp,m,color='k',lw=2)
    ax.fill_between(xintp,m+s,m-s,color='k',alpha=0.25)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=16)
    # ax.set_ylim([-3,4])
    ax.set_xlabel('Normalized session',fontsize=18)
    ax.set_ylabel('Difference in '+('cross' if comp=='other' else 'within')+'-modal '+'d\'\n(auditory - visual)',fontsize=18)
    plt.tight_layout()

    
# zig-zag plot
x = np.arange(6)+1
for phase in ('initial training','after learning'):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    hr = []
    fr = []
    for exps,s in zip(sessionData,sessionsToPass):
        h = []
        f = []
        for obj in (exps[:5] if phase=='initial training' else exps[s:]):
            r = np.zeros(6)
            r[::2] = obj.hitRate[::2]
            r[1::2] = obj.falseAlarmOtherModalGo[1::2]
            h.append(r)
            r = np.zeros(6)
            r[1::2] = obj.hitRate[1::2]
            r[::2] = obj.falseAlarmOtherModalGo[::2]
            f.append(r)
        hr.append(np.nanmean(h,axis=0))
        fr.append(np.nanmean(f,axis=0))
    for h,f in zip(hr,fr):
        ax.plot(x,h,'g',alpha=0.05)
        ax.plot(x,f,'m',alpha=0.05)
    ax.plot(x,np.nanmean(hr,axis=0),'g-o',label='odd-block rewarded target')
    ax.plot(x,np.nanmean(fr,axis=0),'m-o',label='even-block rewarded target')
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=16)
    ax.set_xticks(x)
    ax.set_yticks([0,0.5,1])
    ax.set_xlim([0.5,6.5])
    ax.set_ylim([0,1.01])
    ax.set_xlabel('Block #',fontsize=18)
    ax.set_ylabel('Response rate',fontsize=18)
    ax.legend(loc='lower center',fontsize=16)
    # ax.set_title(phase+' (n='+str(len(hr))+' mice)',fontsize=12)
    plt.tight_layout()
    
for phase in ('initial training','after learning'):
    for firstRewStim in ('vis1','sound1'):
        hc,fc = 'gm' if firstRewStim=='vis1' else 'mg'
        for stim in ('target','non-target'):
            fig = plt.figure()
            ax = fig.add_subplot(1,1,1)
            hr = []
            fr = []
            for exps,sp in zip(sessionData,sessionsToPass):
                h = []
                f = []
                for obj in (exps[:5] if phase=='initial training' else exps[sp:]):
                    if obj.blockStimRewarded[0] == firstRewStim:
                        r = np.zeros(6)
                        r[::2] = obj.hitRate[::2] if stim=='target' else obj.falseAlarmSameModal[::2]
                        r[1::2] = obj.falseAlarmOtherModalGo[1::2] if stim=='target' else obj.falseAlarmOtherModalNogo[1::2]
                        h.append(r)
                        r = np.zeros(6)
                        r[1::2] = obj.hitRate[1::2] if stim=='target' else obj.falseAlarmSameModal[1::2]
                        r[::2] = obj.falseAlarmOtherModalGo[::2] if stim=='target' else obj.falseAlarmOtherModalNogo[::2]
                        f.append(r)
                hr.append(np.nanmean(h,axis=0))
                fr.append(np.nanmean(f,axis=0))
            for h,f in zip(hr,fr):
                ax.plot(x,h,hc,alpha=0.05)
                ax.plot(x,f,fc,alpha=0.05)
            ax.plot(x,np.nanmean(hr,axis=0),hc+'-o',label=('visual ' if firstRewStim=='vis1' else 'auditory ')+stim)
            ax.plot(x,np.nanmean(fr,axis=0),fc+'-o',label=('auditory ' if firstRewStim=='vis1' else 'visual ')+stim)
            for side in ('right','top'):
                ax.spines[side].set_visible(False)
            ax.tick_params(direction='out',top=False,right=False,labelsize=16)
            ax.set_xticks(x)
            ax.set_yticks([0,0.5,1])
            ax.set_xlim([0.5,6.5])
            ax.set_ylim([0,1.01])
            ax.set_xlabel('Block #',fontsize=18)
            ax.set_ylabel('Response rate',fontsize=18)
            ax.legend(loc=('lower right' if stim=='target' else 'upper right'),fontsize=16)
            # ax.set_title(phase+' (n='+str(len(hr))+' mice)',fontsize=12)
            plt.tight_layout()
        
    
# compare early training and after learning
nSessions = 5
stimNames = ('vis1','sound1','vis2','sound2')
stimLabels = ('visual target','auditory target','visual non-target','auditory non-target')
preTrials = 5
postTrials = 20
x = np.arange(-preTrials,postTrials+1) 
for phase in ('initial training','after learning'):
    for ylbl,yticks,ylim,stimInd in zip(('Response rate','Response time (s)'),([0,0.5,1],[0.3,0.4,0.5,0.6]),([0,1.02],[0.3,0.6]),(slice(0,4),slice(0,2))):
        resp = {}
        respAll = {}
        for rewardStim,blockLabel in zip(('vis1','sound1'),('visual rewarded blocks','auditory rewarded blocks')):
            fig = plt.figure(figsize=(8,4.5))
            ax = fig.add_subplot(1,1,1)
            ax.add_patch(matplotlib.patches.Rectangle([-0.5,-1],width=5,height=2,facecolor='0.5',edgecolor=None,alpha=0.2,zorder=0))
            resp[rewardStim] = {}
            respAll[rewardStim] = {}
            for stim,stimLbl,clr,ls in zip(stimNames[stimInd],stimLabels[stimInd],'gmgm'[stimInd],('-','-','--','--')[stimInd]):
                y = []
                yall = []
                for mouseInd,(exps,s) in enumerate(zip(sessionData,sessionsToPass)):
                    if len(exps)>0:# and hasLateAutorewards[mouseInd]:
                        if phase=='initial training':
                            exps = exps[:nSessions]
                        elif phase=='after learning':
                            exps = exps[s:]
                        y.append([])
                        yall.append([])
                        for obj in exps:
                            trials = (obj.trialStim==stim)
                            r = obj.trialResponse if 'rate' in ylbl else obj.responseTimes
                            for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                                if blockInd > 0 and rewStim==rewardStim:
                                    y[-1].append(np.full(preTrials+postTrials+1,np.nan))
                                    pre = r[(obj.trialBlock==blockInd) & trials]
                                    i = min(preTrials,pre.size)
                                    y[-1][-1][preTrials-i:preTrials] = pre[-i:]
                                    post = r[(obj.trialBlock==blockInd+1) & trials]
                                    if stim==rewStim:
                                        i = min(postTrials,post.size)
                                        y[-1][-1][preTrials:preTrials+i] = post[:i]
                                    else:
                                        i = min(postTrials-5,post.size)
                                        y[-1][-1][preTrials+5:preTrials+5+i] = post[:i]
                                    yall[-1].append([np.nanmean(pre[5:]),np.nanmean(post[5:])])
                        y[-1] = np.nanmean(y[-1],axis=0)
                        yall[-1] = np.mean(yall[-1],axis=0)
                if stim in ('vis1','sound1'):
                    resp[rewardStim][stim] = y
                    respAll[rewardStim][stim] = yall
                m = np.nanmean(y,axis=0)
                s = np.nanstd(y,axis=0)/(len(y)**0.5)
                ax.plot(x[:preTrials],m[:preTrials],color=clr,ls=ls,label=stimLbl)
                ax.fill_between(x[:preTrials],(m+s)[:preTrials],(m-s)[:preTrials],color=clr,alpha=0.25)
                ax.plot(x[preTrials:],m[preTrials:],ls=ls,color=clr)
                ax.fill_between(x[preTrials:],(m+s)[preTrials:],(m-s)[preTrials:],color=clr,alpha=0.25)
            for side in ('right','top'):
                ax.spines[side].set_visible(False)
            ax.tick_params(direction='out',top=False,right=False,labelsize=10)
            ax.set_xticks([-5,-1,5,9,14,19])
            ax.set_xticklabels([-5,-1,1,5,10,15])
            ax.set_yticks(yticks)
            ax.set_xlim([-preTrials-0.5,postTrials-0.5])
            ax.set_ylim(ylim)
            ax.set_xlabel('Trials of indicated type after block switch',fontsize=12)
            ax.set_ylabel(ylbl,fontsize=12)
            ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=12)
            ax.set_title(phase+' (n='+str(len(y))+' mice)'+'\n'+blockLabel,fontsize=12)
            plt.tight_layout()
        
        if 'time' in ylbl:
            ylim = [0,1]
            yticks = [0,1]
        for rewardStim,blockLabel in zip(('vis1','sound1'),('visual rewarded blocks','auditory rewarded blocks')):
            fig = plt.figure()
            fig.suptitle(blockLabel)
            axs = []
            gs = matplotlib.gridspec.GridSpec(2,2)
            xticks = (0,1)
            for rr,i,j,clr in zip((respAll[rewardStim][rewardStim],
                                   np.array(resp[rewardStim][rewardStim])[:,[preTrials-1,preTrials+5]],
                                   respAll[rewardStim]['vis1' if rewardStim=='sound1' else 'sound1'],
                                   np.array(resp[rewardStim]['vis1' if rewardStim=='sound1' else 'sound1'])[:,[preTrials-1,preTrials+5]]),
                                  (0,0,1,1),(0,1,0,1),['g' if rewardStim=='vis1' else 'm']*2+['m' if rewardStim=='vis1' else 'g']*2):
                ax = fig.add_subplot(gs[i,j])
                for r in rr:
                    ax.plot(xticks,r,'o-',color=clr,mec=clr,mfc='none',ms=6,lw=1,alpha=0.2)
                mean = np.nanmean(rr,axis=0)
                sem = np.nanstd(rr,axis=0)/(len(rr)**0.5)
                ax.plot(xticks,mean,'o-',color=clr,mec=clr,mfc=clr,ms=10,lw=2)
                for xt,m,s in zip(xticks,mean,sem):
                    ax.plot([xt,xt],[m-s,m+s],color=clr,lw=2)
                for side in ('right','top'):
                    ax.spines[side].set_visible(False)
                ax.tick_params(direction='out',top=False,right=False,labelsize=10)
                ax.set_xticks(xticks)
                ax.set_yticks(yticks)
                if i==1 and j==0:
                    ax.set_xticklabels(('all trials\nprevious block','all trials'))
                elif i==1 and j==1:
                    ax.set_xticklabels(('last trial\nprevious block','first trial\nafter switch trials'))
                else:
                    ax.set_xticklabels([])
                if j==0:
                    ax.set_ylabel(ylbl)
                else:
                    ax.set_yticklabels([])
                ax.set_xlim([-0.2,1.2])
                ax.set_ylim(ylim)
            plt.tight_layout()

# first block
x = np.arange(postTrials+1) 
for phase in ('initial training','after learning'):
    for ylbl,yticks,ylim,stimInd in zip(('Response rate','Response time (z score)'),([0,0.5,1],[-0.5,0,0.5,1]),([0,1.02],[-0.6,1.1]),(slice(0,4),slice(0,2))):
        resp = {}
        for rewardStim,blockLabel in zip(('vis1','sound1'),('visual rewarded blocks','auditory rewarded blocks')):
            fig = plt.figure(figsize=(8,4.5))
            ax = fig.add_subplot(1,1,1)
            ax.add_patch(matplotlib.patches.Rectangle([-0.5,-1],width=5,height=2,facecolor='0.5',edgecolor=None,alpha=0.2,zorder=0))
            resp[rewardStim] = {}
            for stim,stimLbl,clr,ls in zip(stimNames[stimInd],stimLabels[stimInd],'gmgm'[stimInd],('-','-','--','--')[stimInd]):
                y = []
                for mouseInd,(exps,s) in enumerate(zip(sessionData,sessionsToPass)):
                    if len(exps)>0:
                        if phase=='initial training':
                            exps = exps[:nSessions]
                        elif phase=='after learning':
                            exps = exps[s:s+nSessions]
                        y.append([])
                        yall.append([])
                        for obj in exps:
                            trials = (obj.trialStim==stim) # & ~obj.autoRewardScheduled
                            r = obj.trialResponse if 'rate' in ylbl else (obj.responseTimes-np.nanmean(obj.responseTimes[trials]))/np.nanstd(obj.responseTimes[trials])
                            for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                                if blockInd == 0 and rewStim==rewardStim:
                                    y[-1].append(np.full(postTrials+1,np.nan))
                                    post = r[(obj.trialBlock==blockInd+1) & trials]
                                    if stim==rewStim:
                                        i = min(postTrials,post.size)
                                        y[-1][-1][:i] = post[:i]
                                    else:
                                        i = min(postTrials-5,post.size)
                                        y[-1][-1][5:5+i] = post[:i]
                                    yall[-1].append(np.nanmean(post[5:]))
                        y[-1] = np.nanmean(y[-1],axis=0)
                if stim in ('vis1','sound1'):
                    resp[rewardStim][stim] = y
                m = np.nanmean(y,axis=0)
                s = np.nanstd(y,axis=0)/(len(y)**0.5)
                ax.plot(x,m,color=clr,ls=ls,label=stimLbl)
                ax.fill_between(x,m+s,m-s,color=clr,alpha=0.25)
            for side in ('right','top'):
                ax.spines[side].set_visible(False)
            ax.tick_params(direction='out',top=False,right=False,labelsize=10)
            ax.set_xticks([-5,-1,5,9,14,19])
            ax.set_xticklabels([-5,-1,1,5,10,15])
            ax.set_yticks(yticks)
            ax.set_xlim([-0.5,postTrials+0.5])
            ax.set_ylim(ylim)
            ax.set_xlabel('Trials of indicated type after block start',fontsize=12)
            ax.set_ylabel(ylbl,fontsize=12)
            ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=12)
            ax.set_title(phase+' (n='+str(len(y))+' mice)'+'\n'+blockLabel,fontsize=12)
            plt.tight_layout()

            
# block switch plot, target stimuli only
for phase in ('initial training','after learning'):
    fig = plt.figure(figsize=(12,6))
    ax = fig.add_subplot(1,1,1)
    preTrials = 5
    postTrials = 20
    x = np.arange(-preTrials,postTrials)    
    ax.add_patch(matplotlib.patches.Rectangle([-0.5,0],width=5,height=1,facecolor='0.5',edgecolor=None,alpha=0.2,zorder=0))
    for stimLbl,clr,ls in zip(('rewarded target stim','unrewarded target stim','non-target (rewarded modality)','non-target (unrewarded modality'),'gmgm',('-','-','--','--')):
        y = []
        for mouseInd,(exps,s) in enumerate(zip(sessionData,sessionsToPass)):
            # if not hasLateAutorewards[mouseInd]:
            #     continue
            exps = (exps[:5] if phase == 'initial training' else exps[s:])
            y.append([])
            for obj in exps:
                for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                    if blockInd > 0:
                        stim = np.setdiff1d(obj.blockStimRewarded,rewStim)[0] if 'unrewarded' in stimLbl else rewStim
                        if 'non-target' in stimLbl:
                            stim = stim[:-1]+'2'
                        trials = (obj.trialStim==stim) #& ~obj.autoRewardScheduled
                        y[-1].append(np.full(preTrials+postTrials,np.nan))
                        pre = obj.trialResponse[(obj.trialBlock==blockInd) & trials]
                        i = min(preTrials,pre.size)
                        y[-1][-1][preTrials-i:preTrials] = pre[-i:]
                        post = obj.trialResponse[(obj.trialBlock==blockInd+1) & trials]
                        if stim==rewStim:
                            i = min(postTrials,post.size)
                            y[-1][-1][preTrials:preTrials+i] = post[:i]
                        else:
                            i = min(postTrials-5,post.size)
                            y[-1][-1][preTrials+5:preTrials+5+i] = post[:i]
            y[-1] = np.nanmean(y[-1],axis=0)
        if stimLbl=='unrewarded target stim':
            nonRewTargResp = y
        m = np.nanmean(y,axis=0)
        s = np.nanstd(y,axis=0)/(len(y)**0.5)
        ax.plot(x[:preTrials],m[:preTrials],color=clr,ls=ls,label=stimLbl)
        ax.fill_between(x[:preTrials],(m+s)[:preTrials],(m-s)[:preTrials],color=clr,alpha=0.25)
        ax.plot(x[preTrials:],m[preTrials:],ls=ls,color=clr)
        ax.fill_between(x[preTrials:],(m+s)[preTrials:],(m-s)[preTrials:],color=clr,alpha=0.25)
        if stimLbl in ('rewarded target stim','unrewarded target stim'):
            key = 'rewTarg' if stimLbl == 'rewarded target stim' else 'nonRewTarg'
            deltaLickProb['5 rewarded targets'][key] = np.array(y)[:,[preTrials-1,preTrials+5]]
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=18)
    ax.set_xticks([-5,-1,5,9,14,19])
    ax.set_xticklabels([-5,-1,1,5,10,15])
    ax.set_yticks([0,0.5,1])
    ax.set_xlim([-preTrials-0.5,postTrials-0.5])
    ax.set_ylim([0,1.01])
    ax.set_xlabel('Trials of indicated type after block switch',fontsize=20)
    ax.set_ylabel('Response rate',fontsize=20)
    ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=18)
    # ax.set_title(phase+', '+str(len(y))+' mice',fontsize=16)
    plt.tight_layout()
    
    fig = plt.figure(figsize=(4,4))
    ax = fig.add_subplot(1,1,1)
    rr = np.array(nonRewTargResp)[:,[preTrials-1,preTrials+5]]
    for r in rr:
        ax.plot([0,1],r,'o-',color='m',mec='m',mfc='none',ms=6,lw=1,alpha=0.2)
    mean = np.nanmean(rr,axis=0)
    sem = np.nanstd(rr,axis=0)/(len(rr)**0.5)
    ax.plot([0,1],mean,'o-',color='m',mec='m',mfc='m',ms=10,lw=2)
    # for x,m,s in zip([0,1],mean,sem):
    #     ax.plot([x,x],[m-s,m+s],color='m',lw=2)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=14)
    ax.set_xticks([0,1])
    ax.set_yticks([0,0.5,1])
    ax.set_xticklabels(('last trial of\nprevious block','first trial of\nnew block'))
    ax.set_ylabel('Response rate',fontsize=16)
    ax.set_xlim([-0.2,1.2])
    ax.set_ylim([0,1.01])
    plt.tight_layout()
    
    fig = plt.figure(figsize=(8,4))
    ax = fig.add_subplot(1,1,1)
    preTrials = 5
    postTrials = 20
    x = np.arange(-preTrials,postTrials)    
    ax.add_patch(matplotlib.patches.Rectangle([-0.5,-1],width=5,height=2,facecolor='0.5',edgecolor=None,alpha=0.2,zorder=0))
    for stimLbl,clr in zip(('rewarded target stim','unrewarded target stim'),'gm'):
        y = []
        for mouseInd,(exps,s) in enumerate(zip(sessionData,sessionsToPass)):
            # if not hasLateAutorewards[mouseInd]:
            #     continue
            exps = (exps[:5] if phase == 'initial training' else exps[s:])
            y.append([])
            for obj in exps:
                for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                    if blockInd > 0:
                        stim = np.setdiff1d(obj.blockStimRewarded,rewStim) if 'unrewarded' in stimLbl else rewStim
                        trials = (obj.trialStim==stim) #& ~obj.autoRewardScheduled
                        rt = obj.responseTimes - np.nanmean(obj.responseTimes[trials])
                        y[-1].append(np.full(preTrials+postTrials,np.nan))
                        pre = rt[(obj.trialBlock==blockInd) & trials]
                        i = min(preTrials,pre.size)
                        y[-1][-1][preTrials-i:preTrials] = pre[-i:]
                        post = rt[(obj.trialBlock==blockInd+1) & trials]
                        if stim==rewStim:
                            i = min(postTrials,post.size)
                            y[-1][-1][preTrials:preTrials+i] = post[:i]
                        else:
                            i = min(postTrials-5,post.size)
                            y[-1][-1][preTrials+5:preTrials+5+i] = post[:i]                        
            y[-1] = np.nanmean(y[-1],axis=0)
        m = np.nanmean(y,axis=0)
        s = np.nanstd(y,axis=0)/(len(y)**0.5)
        ax.plot(x[:preTrials],m[:preTrials],color=clr,label=stimLbl)
        ax.fill_between(x[:preTrials],(m+s)[:preTrials],(m-s)[:preTrials],color=clr,alpha=0.25)
        ax.plot(x[preTrials:],m[preTrials:],color=clr)
        ax.fill_between(x[preTrials:],(m+s)[preTrials:],(m-s)[preTrials:],color=clr,alpha=0.25)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=12)
    ax.set_xticks([-5,-1,5,9,14,19])
    ax.set_xticklabels([-5,-1,1,5,10,15])
    ax.set_xlim([-preTrials-0.5,postTrials-0.5])
    ax.set_yticks([-0.1,-0.05,0,0.05,0.1])
    ax.set_ylim([-0.105,0.105])
    ax.set_xlabel('Trials of indicated type after block switch',fontsize=14)
    ax.set_ylabel('Response time\n(difference from mean, s)',fontsize=14)
    ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=12)
    # ax.set_title(phase+', '+str(len(y))+' mice',fontsize=12)
    plt.tight_layout()


for lbl in ('all blocks','first trial lick','first trial no lick'):
    fig = plt.figure(figsize=(8,5))
    ax = fig.add_subplot(1,1,1)
    preTrials = 15
    postTrials = 15
    x = np.arange(-preTrials,postTrials+1)    
    ax.plot([0,0],[0,1],'--',color='0.5')
    for stimLbl,clr in zip(('rewarded target stim','unrewarded target stim'),'gm'):
        y = []
        for mouseInd,(exps,s) in enumerate(zip(sessionData,sessionsToPass)):
            exps = exps[s:]
            y.append([])
            for obj in exps:
                for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                    if blockInd > 0:
                        stim = np.setdiff1d(obj.blockStimRewarded,rewStim) if 'unrewarded' in stimLbl else rewStim
                        trials = (obj.trialStim==stim)
                        firstTrialResp = obj.trialResponse[(obj.trialBlock==blockInd+1) & (obj.trialStim==rewStim)][0]
                        if (lbl=='first trial lick' and not firstTrialResp) or (lbl=='first trial no lick' and firstTrialResp):
                            continue
                        y[-1].append(np.full(preTrials+postTrials+1,np.nan))
                        pre = obj.trialResponse[(obj.trialBlock==blockInd) & trials]
                        i = min(preTrials,pre.size)
                        y[-1][-1][preTrials-i:preTrials] = pre[-i:]
                        post = obj.trialResponse[(obj.trialBlock==blockInd+1) & trials]
                        i = min(postTrials,post.size)
                        y[-1][-1][preTrials+1:preTrials+1+i] = post[:i]
            if len(y[-1]) > 0:
                y[-1] = np.nanmean(y[-1],axis=0)
            else:
                y[-1] = np.full(preTrials+postTrials+1,np.nan)
        m = np.nanmean(y,axis=0)
        s = np.nanstd(y,axis=0)/(len(y)**0.5)
        ax.plot(x,m,color=clr,label=stimLbl)
        ax.fill_between(x,m+s,m-s,color=clr,alpha=0.25)
        if lbl == 'all blocks' and stimLbl == 'rewarded target stim':
            deltaLickProb['1 rewarded target']['rewTarg'] = np.array(y)[:,[preTrials-1,preTrials+2]]
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=10)
    ax.set_xticks(np.arange(-20,21,5))
    ax.set_yticks([0,0.5,1])
    ax.set_xlim([-preTrials-0.5,postTrials+0.5])
    ax.set_ylim([0,1.01])
    ax.set_xlabel('Trials of indicated type after block switch',fontsize=12)
    ax.set_ylabel('Response rate',fontsize=12)
    ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=12)
    ax.set_title(lbl+', '+str(len(y))+' mice',fontsize=12)
    plt.tight_layout()
    
    
# combine block types and normalize response rate by mean
postTrials = 18
x = np.arange(postTrials)
fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(1,1,1)
for stimLbl,clr,ls in zip(('rewarded target stim','unrewarded target stim','non-target (rewarded modality)','non-target (unrewarded modality'),'gmgm',('-','-','--','--')):
    y = []
    for exps,s in zip(sessionData,sessionsToPass):
        exps = exps[s:]
        y.append([])
        for obj in exps:
            for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                stim = np.setdiff1d(obj.blockStimRewarded,rewStim)[0] if 'unrewarded' in stimLbl else rewStim
                if 'non-target' in stimLbl:
                    stim = stim[:-1]+'2'
                trials = (obj.trialStim==stim) #& ~obj.autoRewardScheduled
                y[-1].append(np.full(postTrials,np.nan))
                post = obj.trialResponse[(obj.trialBlock==blockInd+1) & trials]
                i = min(postTrials,post.size)
                if not np.any(post):
                    y[-1][-1][:i] = 1
                else:
                    y[-1][-1][:i] = post[:i] / post[:i].mean()
        y[-1] = np.nanmean(y[-1],axis=0)
    m = np.nanmean(y,axis=0)
    s = np.nanstd(y,axis=0)/(len(y)**0.5)
    if stimLbl=='rewarded target stim':
        m[0] = 1
        s[0] = 0
    ax.plot(x,m,color=clr,ls=ls)
    ax.fill_between(x,(m+s),(m-s),color=clr,alpha=0.25)
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False,labelsize=18)
ax.set_xlim([-0.5,postTrials-0.5])
ax.set_xlabel('Trials after block switch',fontsize=20)
ax.set_ylabel('Response rate',fontsize=20)
plt.tight_layout()


# response times and performance
respTime = {phase: {stim: {lbl: [] for lbl in ('rewarded','non-rewarded')} for stim in ('vis1','sound1')} for phase in ('initial training','after learning','all')}
dprime = copy.deepcopy(respTime)
for phase in ('initial training','after learning','all'):
    for mouseInd,(exps,s) in enumerate(zip(sessionData,sessionsToPass)):
        if phase=='initial training':
            exps = exps[:nSessions]
        elif phase=='after learning':
            exps = exps[s:]
        for stim in ('vis1','sound1'):
            for d in (respTime,dprime):
                for lbl in ('rewarded','non-rewarded'):
                    d[phase][stim][lbl].append([[] for _ in range(len(exps))])
            for sessionInd,obj in enumerate(exps):
                stimTrials = (obj.trialStim==stim) & ~obj.autoRewardScheduled
                rt = obj.responseTimes
                for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                    lbl = 'rewarded' if stim==rewStim else 'non-rewarded'
                    trials = stimTrials & (obj.trialBlock==blockInd+1)
                    respTime[phase][stim][lbl][mouseInd][sessionInd].append(rt[trials])
                    dprime[phase][stim][lbl][mouseInd][sessionInd].append(obj.dprimeOtherModalGo[blockInd])

for stim in ('vis1','sound1'):
    for phase in ('initial training','after learning'):
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax.plot([0,1],[0,1],'k--')
        for x,y in zip(respTime[phase][stim]['rewarded'],respTime[phase][stim]['non-rewarded']):
            x,y = [np.nanmean(np.concatenate([np.concatenate(s) for s in m])) for m in (x,y)]
            ax.plot(x,y,'ko',alpha=0.2)
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False,labelsize=12)
        ax.set_xlim([0,1])
        ax.set_ylim([0,1])
        ax.set_aspect('equal')
        ax.set_xlabel('Response time in rewarded blocks (s)',fontsize=14)
        ax.set_ylabel('Response time in non-rewarded blocks (s)',fontsize=14)
        ax.set_title(('visual target' if stim=='vis1' else 'auditory target'),fontsize=14)
        plt.tight_layout()
                    
for stim in ('vis1','sound1'):
    for lbl in ('rewarded','non-rewarded'):
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax.plot([0,1],[0,1],'k--')
        for x,y in zip(respTime['initial training'][stim][lbl],respTime['after learning'][stim][lbl]):
            x,y = [np.nanmean(np.concatenate([np.concatenate(s) for s in m])) for m in (x,y)]
            ax.plot(x,y,'ko',alpha=0.2)
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False)
        ax.set_xlim([0,1])
        ax.set_ylim([0,1])
        ax.set_aspect('equal')
        ax.set_xlabel('Response time, intitial training (s)')
        ax.set_ylabel('Response time, after learning (s)')
        ax.set_title(stim+' '+lbl)
        plt.tight_layout()

for phase in ('initial training','after learning','all'):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot([-1,1],[0,0],'k--')
    ax.plot([0,0],[-1,1],'k--')
    rRew = []
    rNonrew = []
    for r,lbl,clr in zip((rRew,rNonrew),('rewarded','non-rewarded'),'gr'):
        for stim in ('vis1','sound1'):
            for dp,rt in zip(dprime[phase][stim][lbl],respTime[phase][stim][lbl]):
                x = []
                y = []
                for xs,ys in zip(dp,rt):
                    for xb,yb in zip(xs,ys):
                        x.append(xb)
                        y.append(np.nanmean(yb))
                notNan = ~np.isnan(y)
                x = np.array(x)[notNan]
                y = np.array(y)[notNan]
                slope,yint,rval,pval,stderr = scipy.stats.linregress(x,y)
                r.append(rval)
    ax.plot(rRew,rNonrew,'ko',alpha=0.2)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False)
    # ax.set_xlim([-2,4])
    # ax.set_ylim([0,1])
    ax.set_xlabel('Correlation between cross-modal dprime and response time to rewarded target')
    ax.set_ylabel('Correlation between cross-modal dprime and response time to non-rewarded target')
    plt.tight_layout()

for phase in ('initial training','after learning','all'):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    xall = []
    yall = []
    for mouseInd in range(len(sessionsToPass)):
        x = np.nanmean(np.concatenate([dprime[phase]['vis1'][lbl][mouseInd] for lbl in ('rewarded','non-rewarded')],axis=1),axis=1)
        y = []
        for stim in ('vis1','sound1'):
            rew,nonrew = [np.array([np.nanmean(np.concatenate(rt)) for rt in respTime[phase][stim][lbl][mouseInd]]) for lbl in ('rewarded','non-rewarded')]
            y.append(nonrew - rew)
        y = np.nanmean(y,axis=0)
        xall.append(x)
        yall.append(y)
    x = np.concatenate(xall)
    y = np.concatenate(yall)
    notNan = ~np.isnan(y)
    x = x[notNan]
    y = y[notNan]
    ax.plot(x,y,'ko',alpha=0.2)
    slope,yint,rval,pval,stderr = scipy.stats.linregress(x,y)
    xrng = np.array([min(x),max(x)])
    ax.plot(xrng,slope*xrng+yint,'-',color='r')
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False)
    ax.set_xlim([-1,4])
    ax.set_ylim([-0.25,0.5])
    ax.set_xlabel('Cross-modal dprime')
    ax.set_ylabel('Difference in response time,\nnon-rewarded - rewarded (s)')
    ax.set_title('r = '+str(np.round(rval,2))+', p = '+'{0:1.1e}'.format(pval))
    plt.tight_layout()

binWidth = 1 
binCenters = np.arange(0,4,binWidth)       
for phase in ('initial training','after learning','all'):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    xall = []
    yall = []
    for mouseInd in range(len(sessionsToPass)):
        x = np.nanmean(np.concatenate([dprime[phase]['vis1'][lbl][mouseInd] for lbl in ('rewarded','non-rewarded')],axis=1),axis=1)
        y = []
        for stim in ('vis1','sound1'):
            rew,nonrew = [np.array([np.nanmean(np.concatenate(rt)) for rt in respTime[phase][stim][lbl][mouseInd]]) for lbl in ('rewarded','non-rewarded')]
            y.append(nonrew - rew)
        y = np.nanmean(y,axis=0)
        xall.append(x)
        yall.append(y)
    x = np.concatenate(xall)
    y = np.concatenate(yall)
    notNan = ~np.isnan(y)
    x = x[notNan]
    y = y[notNan]
    ym = []
    ys = []
    for b in binCenters:
        i = (x > b-binWidth/2) & (x < b+binWidth/2)
        ym.append(np.median(y[i]))
        ys.append(np.std(y[i]) / (i.sum()**0.5))
    ax.plot(binCenters,ym,'ko')
    for b,m,s in zip(binCenters,ym,ys):
        ax.plot([b,b],[m-s,m+s],'k')
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False)
    ax.set_xlim([-1,4])
    ax.set_ylim([-0.005,0.065])
    ax.set_xlabel('Cross-modal dprime')
    ax.set_ylabel('Difference in response time,\nnon-rewarded - rewarded (s)')
    plt.tight_layout()


# run speed
runSpeed = {phase: {blockType: [] for blockType in ('vis rewarded','aud rewarded')} for phase in ('initial training','after learning','all')}
dprime = copy.deepcopy(runSpeed)
for phase in ('initial training','after learning','all'):
    for mouseInd,(exps,s) in enumerate(zip(sessionData,sessionsToPass)):
        if phase=='initial training':
            exps = exps[:nSessions]
        elif phase=='after learning':
            exps = exps[s:]
        for blockType in ('vis rewarded','aud rewarded'):
            for d in (runSpeed,dprime):
                d[phase][blockType].append([[] for _ in range(len(exps))])
            for sessionInd,obj in enumerate(exps):
                stimTrials = np.in1d(obj.trialStim,('vis1','sound1')) & ~obj.autoRewardScheduled
                for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                    if (blockType=='vis rewarded' and rewStim=='vis1') or (blockType=='aud rewarded' and rewStim=='sound1'):
                        trials = stimTrials & (obj.trialBlock==blockInd+1)
                        runSpeed[phase][blockType][mouseInd][sessionInd].append(np.nanmean(obj.quiescentRunSpeed[trials]))  
                        dprime[phase][blockType][mouseInd][sessionInd].append(obj.dprimeOtherModalGo[blockInd])
                        
for phase in ('initial training','after learning'):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    alim = [-5,85]
    ax.plot(alim,alim,'k--')
    x,y = [np.nanmean(np.concatenate(runSpeed[phase][blockType]),axis=1) for blockType in ('vis rewarded','aud rewarded')]
    ax.plot(x,y,'ko',alpha=0.2)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=12)
    ax.set_xlim(alim)
    ax.set_ylim(alim)
    ax.set_aspect('equal')
    ax.set_xlabel('Run speed, visual rewarded blocks (cm/s)',fontsize=14)
    ax.set_ylabel('Run speed, auditory rewarded blocks (cm/s)',fontsize=14)
    ax.set_title(phase+' ('+str(len(x))+' sessions)',fontsize=14)
    plt.tight_layout()
    
for phase in ('initial training','after learning'):
    for blockType in ('vis rewarded','aud rewarded'):
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        x,y = [np.nanmean(np.concatenate(d[phase][blockType]),axis=1) for d in (runSpeed,dprime)]
        ax.plot(x,y,'ko',alpha=0.2)
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False,labelsize=12)
        ax.set_xlim([-5,85])
        ax.set_ylim([-3,4])
        ax.set_xlabel('Run speed (cm/s)',fontsize=14)
        ax.set_ylabel('Cross-modal d''',fontsize=14)
        ax.set_title(phase+', '+blockType+' ('+str(len(x))+' sessions)',fontsize=14)
        plt.tight_layout()
    

# run speed dynamics
runSpeed = {phase: {blockType: [] for blockType in ('vis rewarded','aud rewarded')} for phase in ('initial training','after learning','all')}
nFrames = int(5 * 60)
for phase in ('initial training','after learning','all'):
    for mouseInd,(exps,s) in enumerate(zip(sessionData,sessionsToPass)):
        if phase=='initial training':
            exps = exps[:nSessions]
        elif phase=='after learning':
            exps = exps[s:]
        for blockType in ('vis rewarded','aud rewarded'):
            runSpeed[phase][blockType].append([])
            for sessionInd,obj in enumerate(exps):
                trials = ~obj.autoRewardScheduled & (obj.trialStim==('vis1' if blockType=='vis rewarded' else 'sound1'))
                runSpeed[phase][blockType][-1].append(np.nanmean([scipy.ndimage.median_filter(obj.runningSpeed[sf-nFrames:sf],3,mode='nearest') for sf in obj.stimStartFrame[trials]],axis=0))

t = -(np.arange(nFrames)/60)[::-1]
for phase in ('initial training','after learning'):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    for blockType,clr in zip(('vis rewarded','aud rewarded'),'gm'):
        r = [np.nanmean(r,axis=0) for r in runSpeed[phase][blockType]]
        m = np.mean(r,axis=0)
        s = np.std(r,axis=0) / (len(r)**0.5)
        ax.plot(t,m,color=clr,label=blockType)
        ax.fill_between(t,m+s,m-s,color=clr,alpha=0.25)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=12)
    # ax.set_xlim([-5,85])
    ax.set_ylim([15,35])
    ax.set_xlabel('Time before stimulus onset (s)',fontsize=14)
    ax.set_ylabel('Run speed (cm/s)',fontsize=14)
    ax.set_title(phase,fontsize=14)
    ax.legend()
    plt.tight_layout()
    

# intra-block resp rate correlations
def getBlockTrials(obj,block,epoch):
    blockTrials = (obj.trialBlock==block) & ~obj.autoRewardScheduled
    n = blockTrials.sum()
    half = int(n/2)
    startTrial = half if epoch=='last half' else 0
    endTrial = half if epoch=='first half' else n
    return np.where(blockTrials)[0][startTrial:endTrial]

def detrend(r,order=2):
    x = np.arange(r.size)
    return r - np.polyval(np.polyfit(x,r,order),x)

def getCorrelation(r1,r2,rs1,rs2,corrSize=200,detrendOrder=None):
    if detrendOrder is not None:
        r1 = detrend(r1,detrendOrder)
        r2 = detrend(r2,detrendOrder)
        rs1 = rs1.copy()
        rs2 = rs2.copy()
        for z in range(rs1.shape[1]):
            rs1[:,z] = detrend(rs1[:,z],detrendOrder)
            rs2[:,z] = detrend(rs2[:,z],detrendOrder)
    c = np.correlate(r1,r2,'full') / (np.linalg.norm(r1) * np.linalg.norm(r2))   
    cs = np.mean([np.correlate(rs1[:,z],rs2[:,z],'full') / (np.linalg.norm(rs1[:,z]) * np.linalg.norm(rs2[:,z])) for z in range(rs1.shape[1])],axis=0)
    n = c.size // 2 + 1
    corrRaw = np.full(corrSize,np.nan)
    corrRaw[:n] = c[-n:]
    corr = np.full(corrSize,np.nan)
    corr[:n] = (c-cs)[-n:] 
    return corr,corrRaw

trainingPhases = ('initial training','after learning')
blockRewStim = ('vis1','sound1','all')
blockEpochs = ('first half','last half','full')
stimNames = ('vis1','sound1','vis2','sound2')
autoCorr = {phase: {blockRew: {epoch: [[[] for _  in range(len(sessionData))] for _ in range(4)] for epoch in blockEpochs} for blockRew in blockRewStim} for phase in trainingPhases}
autoCorrRaw = copy.deepcopy(autoCorr)
autoCorrDetrend = copy.deepcopy(autoCorr)
respRate = copy.deepcopy(autoCorr)
corrWithin = {phase: {blockRew: {epoch: [[[[] for _  in range(len(sessionData))] for _ in range(4)] for _ in range(4)] for epoch in blockEpochs} for blockRew in blockRewStim} for phase in trainingPhases}
corrWithinRaw = copy.deepcopy(corrWithin)
corrWithinDetrend = copy.deepcopy(corrWithin)
corrAcross = copy.deepcopy(corrWithin)
autoCorrMat = {phase: {blockRew: {epoch: np.zeros((4,len(sessionData),100)) for epoch in blockEpochs} for blockRew in blockRewStim} for phase in trainingPhases}
autoCorrRawMat = copy.deepcopy(autoCorrMat)
autoCorrDetrendMat = copy.deepcopy(autoCorrMat)
respRateMat = copy.deepcopy(autoCorrMat)
corrWithinMat = {phase: {blockRew: {epoch: np.zeros((4,4,len(sessionData),200)) for epoch in blockEpochs} for blockRew in blockRewStim} for phase in trainingPhases}
corrWithinRawMat = copy.deepcopy(corrWithinMat)
corrWithinDetrendMat = copy.deepcopy(corrWithinMat)
corrAcrossMat = copy.deepcopy(corrWithinMat)
minTrials = 3
nShuffles = 10
for phase in trainingPhases:
    for blockRew in blockRewStim:
        for epoch in blockEpochs:
            for m,(exps,sp) in enumerate(zip(sessionData,sessionsToPass)):
                for obj in (exps[:5] if phase=='initial training' else exps[sp:]):
                    
                    resp = np.zeros((4,obj.nTrials))
                    respShuffled = np.zeros((4,obj.nTrials,nShuffles))
                    for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                        blockTrials = getBlockTrials(obj,blockInd+1,epoch)
                        for i,s in enumerate(stimNames if rewStim=='vis1' else ('sound1','vis1','sound2','vis2')):
                            stimTrials = np.intersect1d(blockTrials,np.where(obj.trialStim==s)[0])
                            if len(stimTrials) < minTrials:
                                continue
                            r = obj.trialResponse[stimTrials].astype(float)
                            r[r<1] = -1
                            resp[i,stimTrials] = r
                            for z in range(nShuffles):
                                respShuffled[i,stimTrials,z] = np.random.permutation(r)
                    
                    for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                        if blockRew not in ('all',rewStim):
                            continue
                        blockTrials = getBlockTrials(obj,blockInd+1,epoch)
                        for i,s in enumerate(stimNames if rewStim=='vis1' else ('sound1','vis1','sound2','vis2')):
                            stimTrials = np.intersect1d(blockTrials,np.where(obj.trialStim==s)[0])
                            if len(stimTrials) < minTrials:
                                continue
                            r = resp[i,stimTrials]
                            rs = respShuffled[i,stimTrials]
                            respRate[phase][blockRew][epoch][i][m].append(r.mean())
                            corr,corrRaw = getCorrelation(r,r,rs,rs,100)
                            autoCorr[phase][blockRew][epoch][i][m].append(corr)
                            autoCorrRaw[phase][blockRew][epoch][i][m].append(corrRaw)
                            corrDetrend,corrRawDetrend = getCorrelation(r,r,rs,rs,100,detrendOrder=2)
                            autoCorrDetrend[phase][blockRew][epoch][i][m].append(corrDetrend)
                        
                        r = resp[:,blockTrials]
                        rs = respShuffled[:,blockTrials]
                        for i,(r1,rs1) in enumerate(zip(r,rs)):
                            for j,(r2,rs2) in enumerate(zip(r,rs)):
                                if np.count_nonzero(r1) >= minTrials and np.count_nonzero(r2) >= minTrials:
                                    corr,corrRaw = getCorrelation(r1,r2,rs1,rs2)
                                    corrWithin[phase][blockRew][epoch][i][j][m].append(corr)
                                    corrWithinRaw[phase][blockRew][epoch][i][j][m].append(corrRaw)
                                    corrDetrend,corrRawDetrend = getCorrelation(r1,r2,rs1,rs2,detrendOrder=2)
                                    corrWithinDetrend[phase][blockRew][epoch][i][j][m].append(corrDetrend)

                        otherBlocks = [0,2,4] if blockInd in [0,2,4] else [1,3,5]
                        otherBlocks.remove(blockInd)
                        for k,b in enumerate(otherBlocks):
                            bTrials = getBlockTrials(obj,b+1,epoch)
                            r = resp[:,bTrials]
                            rs = respShuffled[:,bTrials]
                            for i,(r1,rs1) in enumerate(zip(r,rs)):
                                for j,(r2,rs2) in enumerate(zip(r,rs)):
                                    if np.count_nonzero(r1) >= minTrials and np.count_nonzero(r2) >= minTrials:
                                        corr,corrRaw = getCorrelation(r1,r2,rs1,rs2)
                                        corrAcross[phase][blockRew][epoch][i][j][m].append(corr)
                        
            for i in range(4):
                for m in range(len(sessionData)):
                    autoCorrMat[phase][blockRew][epoch][i,m] = np.nanmean(autoCorr[phase][blockRew][epoch][i][m],axis=0)
                    autoCorrRawMat[phase][blockRew][epoch][i,m] = np.nanmean(autoCorrRaw[phase][blockRew][epoch][i][m],axis=0)
                    autoCorrDetrendMat[phase][blockRew][epoch][i,m] = np.nanmean(autoCorrDetrend[phase][blockRew][epoch][i][m],axis=0)
                    respRateMat[phase][blockRew][epoch][i,m] = np.nanmean(respRate[phase][blockRew][epoch][i][m],axis=0)
                    
            for i in range(4):
                for j in range(4):
                    for m in range(len(sessionData)):
                        corrWithinMat[phase][blockRew][epoch][i,j,m] = np.nanmean(corrWithin[phase][blockRew][epoch][i][j][m],axis=0)
                        corrWithinRawMat[phase][blockRew][epoch][i,j,m] = np.nanmean(corrWithinRaw[phase][blockRew][epoch][i][j][m],axis=0)
                        corrWithinDetrendMat[phase][blockRew][epoch][i,j,m] = np.nanmean(corrWithinDetrend[phase][blockRew][epoch][i][j][m],axis=0)
                        corrAcrossMat[phase][blockRew][epoch][i,j,m] = np.nanmean(corrAcross[phase][blockRew][epoch][i][j][m],axis=0)

stimLabels = ('rewarded target','unrewarded target','non-target\n(rewarded modality)','non-target\n(unrewarded modality)')

fig = plt.figure(figsize=(4,6))           
gs = matplotlib.gridspec.GridSpec(4,1)
x = np.arange(100)
for i,lbl in enumerate(stimLabels):
    ax = fig.add_subplot(gs[i])
    for phase,clr in zip(trainingPhases,'mg'):
        mat = autoCorrMat[phase]['all']['full']
        m = np.nanmean(mat[i],axis=0)
        s = np.nanstd(mat[i],axis=0) / (len(mat[i]) ** 0.5)
        ax.plot(x,m,color=clr)
        ax.fill_between(x,m-s,m+s,color=clr,alpha=0.25)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False)
    ax.set_xticks(np.arange(0,20,5))
    ax.set_xlim([-1,15])
    ax.set_ylim([-0.04,0.11])
    if i==3:
        ax.set_xlabel('Lag (trials)')
    if i==0:
        ax.set_ylabel('Auto-correlation')
    ax.set_title(lbl)
plt.tight_layout()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
bw = 0.1
for phase,clr in zip(trainingPhases,'mg'):
    r = np.concatenate([np.concatenate(respRate[phase]['all']['full'][i]) for i in range(4)])
    c = np.concatenate([np.concatenate([np.array(c)[:,1] for c in autoCorrDetrend[phase]['all']['full'][i]]) for i in range(4)])
    # ax.plot(r,c,'o',mec=clr,mfc='none',alpha=0.1,label=phase)
    for b in (np.arange(bw,1,bw)):
        d = c[(r>b-bw) & (r<b+bw)]
        m = np.mean(d)
        s = np.std(d)/(len(d)**0.5)
        ax.plot(b,m,'o',mec=clr,mfc='none')
        ax.plot([b,b],[m-s,m+s],color=clr)
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False,labelsize=12)
# ax.set_ylim([0,1.01])
ax.set_xlabel('Response rate',fontsize=14)
ax.set_ylabel('Correlation',fontsize=14)
plt.legend(loc='lower right')
plt.tight_layout()

for mat,ylim in zip((corrWithinRawMat,corrWithinMat,corrWithinDetrendMat),([-0.2,0.2],[-0.03,0.06],[-0.03,0.06])):
    fig = plt.figure(figsize=(10,10))          
    gs = matplotlib.gridspec.GridSpec(4,4)
    x = np.arange(1,200)
    for i,ylbl in enumerate(stimLabels):
        for j,xlbl in enumerate(stimLabels[:4]):
            ax = fig.add_subplot(gs[i,j])
            d = mat['after learning']['all']['full'][i,j][:,1:]
            m = np.nanmean(d,axis=0)
            s = np.nanstd(d,axis=0) / (len(d) ** 0.5)
            ax.plot(x,m,'k',label=phase)
            ax.fill_between(x,m-s,m+s,color='k',alpha=0.25)
            for side in ('right','top'):
                ax.spines[side].set_visible(False)
            ax.tick_params(direction='out',top=False,right=False,labelsize=9)
            ax.set_xlim([0,20])
            ax.set_ylim(ylim)
            if i==3:
                ax.set_xlabel('Lag (trials)',fontsize=11)
            if j==0:
                ax.set_ylabel(ylbl,fontsize=11)
            if i==0:
                ax.set_title(xlbl,fontsize=11)

fig = plt.figure(figsize=(8,8))          
gs = matplotlib.gridspec.GridSpec(4,4)
x = np.arange(200)
for i,ylbl in enumerate(stimLabels):
    for j,xlbl in enumerate(stimLabels[:4]):
        ax = fig.add_subplot(gs[i,j])
        for phase,clr in zip(trainingPhases,'mg'):
            mat = corrWithinDetrendMat[phase]['all']['full']
            m = np.nanmean(mat[i,j],axis=0)
            s = np.nanstd(mat[i,j],axis=0) / (len(mat[i,j]) ** 0.5)
            ax.plot(x,m,clr,label=phase)
            ax.fill_between(x,m-s,m+s,color=clr,alpha=0.25)
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False,labelsize=9)
        ax.set_xlim([-1,20])
        ax.set_ylim([-0.025,0.09])
        if i==3:
            ax.set_xlabel('Lag (trials)',fontsize=11)
        if j==0:
            ax.set_ylabel(ylbl,fontsize=11)
        if i==0:
            ax.set_title(xlbl,fontsize=11)
        if i==0 and j==1:
            ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=11)
plt.tight_layout()

fig = plt.figure(figsize=(8,8))          
gs = matplotlib.gridspec.GridSpec(4,2)
x = np.arange(200)
for i,ylbl in enumerate(stimLabels):
    for j,xlbl in enumerate(stimLabels[:2]):
        ax = fig.add_subplot(gs[i,j])
        for phase,clr in zip(trainingPhases,'mg'):
            mat = corrWithinRawMat[phase]['all']['full']
            m = np.nanmean(mat[i,j],axis=0)
            s = np.nanstd(mat[i,j],axis=0) / (len(mat[i,j]) ** 0.5)
            ax.plot(x,m,clr,label=phase)
            ax.fill_between(x,m-s,m+s,color=clr,alpha=0.25)
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False,labelsize=9)
        ax.set_xlim([-1,20])
        # ax.set_ylim([-0.025,0.09])
        if i==3:
            ax.set_xlabel('Lag (trials)',fontsize=11)
        if j==0:
            ax.set_ylabel(ylbl,fontsize=11)
        if i==0:
            ax.set_title(xlbl,fontsize=11)
        if i==0 and j==1:
            ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=11)
plt.tight_layout()

for phase in trainingPhases:
    fig = plt.figure(figsize=(8,8))          
    gs = matplotlib.gridspec.GridSpec(4,2)
    x = np.arange(200)
    for i,ylbl in enumerate(stimLabels):
        for j,xlbl in enumerate(stimLabels[:2]):
            ax = fig.add_subplot(gs[i,j])
            for blockRew,clr in zip(blockRewStim[:2],'gm'):
                mat = corrWithinDetrendMat[phase][blockRew]['full']
                m = np.nanmean(mat[i,j],axis=0)
                s = np.nanstd(mat[i,j],axis=0) / (len(mat[i,j]) ** 0.5)
                ax.plot(x,m,clr,label=('visual' if blockRew=='vis1' else 'auditory')+' rewarded')
                ax.fill_between(x,m-s,m+s,color=clr,alpha=0.25)
            for side in ('right','top'):
                ax.spines[side].set_visible(False)
            ax.tick_params(direction='out',top=False,right=False,labelsize=9)
            ax.set_xlim([-1,20])
            ax.set_ylim([-0.04,0.12] if phase=='initial training' else [-0.025,0.045])
            if i==3:
                ax.set_xlabel('Lag (trials)',fontsize=11)
            if j==0:
                ax.set_ylabel(ylbl,fontsize=11)
            if i==0:
                ax.set_title(xlbl,fontsize=11)
            if i==0 and j==1:
                ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=11)
    plt.tight_layout()

for phase in trainingPhases:       
    fig = plt.figure(figsize=(8,8))          
    gs = matplotlib.gridspec.GridSpec(4,2)
    x = np.arange(200)
    for i,ylbl in enumerate(stimLabels):
        for j,xlbl in enumerate(stimLabels[:2]):
            ax = fig.add_subplot(gs[i,j])
            for epoch,clr in zip(('first half','last half'),'gm'):
                mat = corrWithinDetrendMat[phase]['all'][epoch]
                m = np.nanmean(mat[i,j],axis=0)
                s = np.nanstd(mat[i,j],axis=0) / (len(mat[i,j]) ** 0.5)
                ax.plot(x,m,clr,label=epoch)
                ax.fill_between(x,m-s,m+s,color=clr,alpha=0.25)
            for side in ('right','top'):
                ax.spines[side].set_visible(False)
            ax.tick_params(direction='out',top=False,right=False,labelsize=9)
            ax.set_xlim([0,20])
            ax.set_ylim([-0.025,0.09] if phase=='initial training' else [-0.02,0.03])
            if i==3:
                ax.set_xlabel('Lag (trials)',fontsize=11)
            if j==0:
                ax.set_ylabel(ylbl,fontsize=11)
            if i==0:
                ax.set_title(xlbl,fontsize=11)
            if i==0 and j==1:
                ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=11)
    plt.tight_layout()

for i in range(4):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot([0,0],[0,1],'k--')
    for phase,clr in zip(trainingPhases,'mg'):
        d = corrWithinDetrendMat[phase]['all']['full'][i,i,:,1]
        dsort = np.sort(d)
        cumProb = np.array([np.sum(dsort<=i)/dsort.size for i in dsort])
        ax.plot(dsort,cumProb,color=clr,label=phase)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=12)
    ax.set_xlim([-0.05,0.08])
    ax.set_ylim([0,1.01])
    ax.set_xlabel('Auto-correlation of responses to non-rewarded target',fontsize=14)
    ax.set_ylabel('Cumalative fraction of mice',fontsize=14)
    plt.legend(loc='lower right')
    plt.tight_layout() 

for corr in (corrWithinRaw,corrWithin,corrWithinDetrend):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    bw = 0.1
    for phase,clr in zip(trainingPhases,'mg'):
        r = np.concatenate([np.concatenate(respRate[phase]['all']['full'][i]) for i in range(4)])
        c = np.concatenate([np.concatenate([np.array(c)[:,1] for c in corr[phase]['all']['full'][i][i]]) for i in range(4)])
        # ax.plot(r,c,'o',mec=clr,mfc='none',alpha=0.1,label=phase)
        for b in (np.arange(bw,1,bw)):
            d = c[(r>b-bw) & (r<b+bw)]
            m = np.mean(d)
            s = np.std(d)/(len(d)**0.5)
            ax.plot(b,m,'o',mec=clr,mfc='none')
            ax.plot([b,b],[m-s,m+s],color=clr)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=12)
    # ax.set_ylim([0,1.01])
    ax.set_xlabel('Response rate',fontsize=14)
    ax.set_ylabel('Correlation',fontsize=14)
    plt.legend(loc='lower right')
    plt.tight_layout() 

for i in range(4):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    bw = 0.1
    for phase,clr in zip(trainingPhases,'mg'):
        r = np.concatenate(respRate[phase]['all']['full'][i])
        c = np.concatenate([np.array(c)[:,1] for c in corrWithin[phase]['all']['full'][i][i]])
        # ax.plot(r,c,'o',mec=clr,mfc='none',alpha=0.1,label=phase)
        for b in (np.arange(bw,1,bw)):
            d = c[(r>b-bw) & (r<b+bw)]
            m = np.mean(d)
            s = np.std(d)/(len(d)**0.5)
            ax.plot(b,m,'o',mec=clr,mfc='none')
            ax.plot([b,b],[m-s,m+s],color=clr)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=12)
    # ax.set_ylim([0,1.01])
    ax.set_xlabel('Response rate',fontsize=14)
    ax.set_ylabel('Correlation',fontsize=14)
    plt.legend(loc='lower right')
    plt.tight_layout()
   
    
# example trial responses
for mouse,session in zip((664851,702131,708016),(-1,-1,-3)):
    exps = sessionData[np.where(mice==mouse)[0][0]]
    obj = exps[session]
    blockStarts = np.where(obj.blockTrial==0)[0]
    
    fig = plt.figure(figsize=(4,8))
    for i,(stim,stimLbl) in enumerate(zip(('vis1','sound1','vis2','sound2')[:2],('visual\ntarget','auditory\ntarget'))):
        ax = fig.add_subplot(1,2,i+1)
        for b,rewStim in enumerate(obj.blockStimRewarded):
            if rewStim == 'vis1':
                h = blockStarts[b+1] - blockStarts[b] if b < 5 else obj.nTrials - blockStarts[b]
                ax.add_patch(matplotlib.patches.Rectangle([0,blockStarts[b]+1],width=1.5,height=h,facecolor='0.5',edgecolor=None,alpha=0.1,zorder=0))
            for trial in np.where((obj.trialBlock==b+1) & (obj.trialStim==stim))[0]:
                if obj.trialResponse[trial]:
                    ax.plot(0.5,trial+1,'o',mec=('b' if stim==rewStim else 'r'),mfc='none',ms=4)
                else:
                    ax.plot(1,trial+1,'o',mec='k',mfc='none',ms=4)
        ax.tick_params(direction='out',top=False,right=False,labelsize=14)
        for side in ('right','top','bottom'):
            ax.spines[side].set_visible(False)
        if i>0:
            ax.spines['left'].set_visible(False)
            ax.set_yticks([])
        else:
            ax.set_ylabel('Trial',fontsize=16)
        ax.set_xticks([0.5,1])
        ax.set_xticklabels(('lick','no\nlick'))
        ax.set_xlim([0.25,1.25])
        ax.set_ylim([obj.nTrials+1,0])
        ax.set_title(stimLbl,fontsize=16)
    plt.tight_layout()


# response times for repeat vs non-repeat responses
rtRepeat = {phase: {stim: [] for stim in ('rewarded target','non-rewarded target')} for phase in ('initial training','after learning')}
rtNoRepeat = copy.deepcopy(rtRepeat)
for phase in ('initial training','after learning'):
    for exps,s in zip(sessionData,sessionsToPass):
        exps = (exps[:5] if phase=='initial training' else exps[s:])
        for stim in rtRepeat[phase]:
            rtRepeat[phase][stim].append([])
            rtNoRepeat[phase][stim].append([])
            for obj in exps:
                for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                    nonRewStim = np.setdiff1d(obj.blockStimRewarded,rewStim)
                    s = rewStim if stim=='rewarded target' else nonRewStim
                    stimTrials = np.where(obj.trialStim==s)[0]
                    rtz = (obj.responseTimes - np.nanmean(obj.responseTimes[stimTrials])) / np.nanstd(obj.responseTimes[stimTrials])
                    blockTrials = np.where((obj.trialBlock==blockInd+1) & (~obj.autoRewardScheduled))[0]
                    trials = np.intersect1d(stimTrials,blockTrials)
                    rewStimTrials = np.where(obj.trialStim==rewStim)[0]
                    nonRewStimTrials = np.where(obj.trialStim==nonRewStim)[0]
                    ind = np.searchsorted(nonRewStimTrials,trials)
                    valid = ind > np.searchsorted(rewStimTrials,trials)
                    prevNonRewResp = obj.trialResponse[nonRewStimTrials[ind - 1]] & valid
                    rtRepeat[phase][stim][-1].extend(rtz[trials][prevNonRewResp])
                    rtNoRepeat[phase][stim][-1].extend(rtz[trials][~prevNonRewResp])

for phase in rtRepeat:                  
    fig = plt.figure(figsize=(7.5,5))
    ax = fig.add_subplot(1,1,1)
    alim = (-1,1)
    ax.plot(alim,alim,'k--')
    for stim,clr in zip(rtRepeat[phase],'gm'):
        for repeat,noRepeat in zip(rtRepeat[phase][stim],rtNoRepeat[phase][stim]):
            ax.plot(np.nanmean(repeat),np.nanmean(noRepeat),'o',mec=clr,mfc='none')
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=10)
    ax.set_xlim(alim)
    ax.set_ylim(alim)
    ax.set_aspect('equal')
    ax.set_xlabel('Response time (repeated response)',fontsize=12)
    ax.set_ylabel('Response time (non-repeated response)',fontsize=12)
    # ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=12)
    plt.tight_layout()

                            
         
# effect of prior reward or response
prevTrialTypes = ('rewarded','unrewarded','unrewarded target','response to non-target','response to any stimulus','no response','response same stimulus','no response same stimulus')
prevTrialTypes = ('rewarded','unrewarded target','response to non-target','response same stimulus')
stimNames = ('vis1','sound1','vis2','sound2')
stimLabels = ('visual target','auditory target','visual non-target','auditory non-target')
resp = {phase: {prevTrialType: {blockType: {stim: [[] for _ in range(5)] for stim in stimNames} for blockType in ('visual','auditory')} for prevTrialType in prevTrialTypes} for phase in ('initial training','after learning')}
respShuffled = copy.deepcopy(resp)
respTime = copy.deepcopy(resp)
respTimeShuffled = copy.deepcopy(resp)
for phase in ('initial training','after learning'):
    for prevTrialType in prevTrialTypes:
        for rewardStim,blockType in zip(('vis1','sound1'),('visual','auditory')):
            for stim in stimNames:
                for exps,s in zip(sessionData,sessionsToPass):
                    exps = (exps[:5] if phase=='initial training' else exps[s:])
                    for i in range(5):
                        r = []
                        rShuffled = []
                        rt = []
                        rtShuffled = []
                        for obj in exps:
                            stimTrials = np.where(obj.trialStim==stim)[0]
                            rtz = (obj.responseTimes - np.nanmean(obj.responseTimes[stimTrials])) / np.nanstd(obj.responseTimes[stimTrials])
                            for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                                if obj.hitRate[blockInd] < 0.85:
                                    continue
                                if rewStim==rewardStim:
                                    blockTrials = np.where(~obj.autoRewardScheduled & (obj.trialBlock==blockInd+1))[0]
                                    # blockTrials = blockTrials[20:] # ignore trials at beginning of block
                                    trials = np.intersect1d(stimTrials,blockTrials)
                                    if prevTrialType == 'rewarded':
                                        ind = obj.trialRewarded
                                    elif prevTrialType == 'unrewarded':
                                        ind = obj.trialResponse & ~obj.trialRewarded
                                    elif prevTrialType == 'unrewarded target':
                                        ind = obj.trialResponse & np.in1d(obj.trialStim,obj.blockStimRewarded) & ~obj.trialRewarded
                                    elif prevTrialType == 'response to non-target':
                                        ind = obj.trialResponse & ~np.in1d(obj.trialStim,obj.blockStimRewarded)
                                    elif prevTrialType == 'response to any stimulus':
                                        ind = obj.trialResponse
                                    elif prevTrialType == 'no response':
                                        ind = ~obj.trialResponse
                                    elif prevTrialType == 'response same stimulus':
                                        ind = obj.trialResponse & (obj.trialStim == stim)
                                    elif prevTrialType == 'no response same stimulus':
                                        ind = ~obj.trialResponse & (obj.trialStim == stim)
                                    r.append(obj.trialResponse[trials][ind[trials-(i+1)]])
                                    rt.append(rtz[trials][ind[trials-(i+1)]])
                                    rShuffled.append([obj.trialResponse[trials].mean()])
                                    rtShuffled.append([np.nanmean(rtz[trials])])
                                    # for _ in range(10):
                                    #     ind = np.random.choice(trials,len(r[-1]))
                                    #     rShuffled.append(obj.trialResponse[ind])
                                    #     rtShuffled.append(rtz[ind])
                        if len(r) > 0:
                            r = np.concatenate(r)
                            rShuffled = np.concatenate(rShuffled)
                            rt = np.concatenate(rt)
                            rtShuffled = np.concatenate(rtShuffled)
                        resp[phase][prevTrialType][blockType][stim][i].append(np.nanmean(r))
                        respShuffled[phase][prevTrialType][blockType][stim][i].append(np.nanmean(rShuffled))
                        respTime[phase][prevTrialType][blockType][stim][i].append(np.nanmean(rt))
                        respTimeShuffled[phase][prevTrialType][blockType][stim][i].append(np.nanmean(rtShuffled))


# respConsecRew = {blockType: {stim: [] for stim in stimNames} for blockType in ('visual','auditory')}
# rtConsecRew = copy.deepcopy(respConsecRew)
# for rewardStim,blockType in zip(('vis1','sound1'),('visual','auditory')):
#     for stim in stimNames:
#         for exps,s in zip(sessionData,sessionsToPass):
#             #exps[:nSessions]
#             exps = exps[s:]
#             r = [[] for _ in range(11)]
#             rt = [[] for _ in range(11)]
#             for obj in exps:
#                 stimTrials = np.where(obj.trialStim==stim)[0]
#                 rtz = (obj.responseTimes - np.nanmean(obj.responseTimes[stimTrials])) / np.nanstd(obj.responseTimes[stimTrials])
#                 for blockInd,rewStim in enumerate(obj.blockStimRewarded):
#                     if rewStim==rewardStim:
#                         blockTrials = np.where(~obj.autoRewardScheduled & (obj.trialBlock==blockInd+1))[0]
#                         blockTrials = blockTrials[5:] # ignore first 5 trials after cue trials
#                         trials = np.intersect1d(stimTrials,blockTrials)
#                         for i in trials:
#                             val,g = next(itertools.groupby(obj.trialRewarded[i-1::-1]))
#                             k = sum(1 for _ in g) if val else 0
#                             r[k].append(obj.trialResponse[i])
#                             rt[k].append(rtz[i])
#             respConsecRew[blockType][stim].append([np.mean(a) for a in r])
#             rtConsecRew[blockType][stim].append([np.nanmean(a) for a in rt])



alim = (0,1.02)
for phase in ('initial training','after learning'):
    for prevTrialType in prevTrialTypes:
        for blockType in ('visual','auditory'):
            fig = plt.figure(figsize=(7.5,5))
            ax = fig.add_subplot(1,1,1)
            ax.plot(alim,alim,'k--')
            for stim,stimLbl,mec,mfc in zip(stimNames,stimLabels,'gmgm',('g','m','none','none')):
                ax.plot(respShuffled[phase][prevTrialType][blockType][stim][0],resp[phase][prevTrialType][blockType][stim][0],'o',color=mec,mec=mec,mfc=mfc,label=stimLbl)
            for side in ('right','top'):
                ax.spines[side].set_visible(False)
            ax.tick_params(direction='out',top=False,right=False,labelsize=10)
            ax.set_xlim(alim)
            ax.set_ylim(alim)
            ax.set_aspect('equal')
            ax.set_xlabel('Response rate'+'\nrandom trials',fontsize=12)
            ax.set_ylabel('Response rate'+'\nprevious trial '+prevTrialType,fontsize=12)
            ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=12)
            ax.set_title(phase + ', ' + blockType+' rewarded blocks')
            plt.tight_layout()

alim = (-1.2,1.2)
for phase in ('initial training','after learning'):
    for prevTrialType in prevTrialTypes:
        for blockType in ('visual','auditory'):
            fig = plt.figure(figsize=(7.5,5))
            ax = fig.add_subplot(1,1,1)
            ax.plot(alim,alim,'k--')
            for stim,stimLbl,mec,mfc in zip(stimNames,stimLabels,'gmgm',('g','m','none','none')):
                if '1' in stim:
                    ax.plot(respTimeShuffled[phase][prevTrialType][blockType][stim][0],respTime[phase][prevTrialType][blockType][stim][0],'o',color=mec,mec=mec,mfc=mfc,label=stimLbl)
            for side in ('right','top'):
                ax.spines[side].set_visible(False)
            ax.tick_params(direction='out',top=False,right=False,labelsize=10)
            ax.set_xlim(alim)
            ax.set_ylim(alim)
            ax.set_aspect('equal')
            ax.set_xlabel('Response time (z score)'+'\nrandom trials',fontsize=12)
            ax.set_ylabel('Response time (z score)'+'\nprevious trial '+prevTrialType,fontsize=12)
            ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=12)
            ax.set_title(blockType+' rewarded blocks')
            plt.tight_layout()

for phase in ('initial training','after learning'):        
    for prevTrialType in prevTrialTypes:
        for blockType in ('visual','auditory'):
            fig = plt.figure(figsize=(7.5,5))
            ax = fig.add_subplot(1,1,1)
            for stim,stimLbl,mec,mfc in zip(stimNames,stimLabels,'gmgm',('g','m','none','none')):
                for i in range(5):
                    r = np.array(resp[phase][prevTrialType][blockType][stim][i]) - np.array(respShuffled[phase][prevTrialType][blockType][stim][i])
                    ax.plot(-i-1,np.nanmean(r),'o',mec=mec,mfc=mfc)
            for side in ('right','top'):
                ax.spines[side].set_visible(False)
            ax.tick_params(direction='out',top=False,right=False,labelsize=10)
            ax.set_xlabel('Response rate'+'\nrandom trials',fontsize=12)
            ax.set_ylabel('Response rate'+'\nprevious trial '+prevTrialType,fontsize=12)
            ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=12)
            ax.set_title(blockType+' rewarded blocks')
            plt.tight_layout()

for prevTrialType in prevTrialTypes:
    for blockType in ('visual','auditory'):
        fig = plt.figure(figsize=(7.5,5))
        ax = fig.add_subplot(1,1,1)
        for stim,stimLbl,mec,mfc in zip(stimNames,stimLabels,'gmgm',('g','m','none','none')):
            for i in range(5):
                r = np.array(respTime[prevTrialType][blockType][stim][i])# - np.array(respTimeShuffled[prevTrialType][blockType][stim][i])
                ax.plot(-i-1,np.nanmean(r),'o',mec=mec,mfc=mfc)
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False,labelsize=10)
        ax.set_xlabel('Response rate'+'\nrandom trials',fontsize=12)
        ax.set_ylabel('Response rate'+'\nprevious trial '+prevTrialType,fontsize=12)
        ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=12)
        ax.set_title(blockType+' rewarded blocks')
        plt.tight_layout()


            
stimNames = ('vis1','sound1','vis2','sound2')
stimLabels = ('visual target','auditory target','visual non-target','auditory non-target')
for prevTrialType in ('rewarded','unrewarded target'):
    for lbl,alim in zip(('Response rate','Response time (z score)'),((0,1.02),(-1.2,1.2))):
        for rewardStim,blockLabel in zip(('vis1','sound1'),('visual rewarded blocks','auditory rewarded blocks')):
            fig = plt.figure(figsize=(7.5,5))
            ax = fig.add_subplot(1,1,1)
            ax.plot(alim,alim,'k--')
            for stim,stimLbl,mec,mfc in zip(stimNames,stimLabels,'gmgm',('g','m','none','none')):
                if ('time' in lbl and '2' in stim) or ('same' in prevTrialType and ('2' in stim or stim==rewardStim)):
                    continue
                resp = []
                respShuffled = []
                for exps,s in zip(sessionData,sessionsToPass):
                    #exps[:nSessions]
                    exps = exps[s:]
                    r = []
                    rShuffled = []
                    for obj in exps:
                        stimTrials = np.where(obj.trialStim==stim)[0]
                        if 'time' in lbl:
                            d = (obj.responseTimes - np.nanmean(obj.responseTimes[stimTrials])) / np.nanstd(obj.responseTimes[stimTrials])
                        else:
                            d = obj.trialResponse
                        for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                            if rewStim==rewardStim:
                                blockTrials = np.where(~obj.autoRewardScheduled & (obj.trialBlock==blockInd+1))[0]
                                blockTrials = blockTrials[5:] # ignore first 5 trials after cue trials
                                trials = np.intersect1d(stimTrials,blockTrials)
                                if prevTrialType == 'response to any stimulus':
                                    ind = obj.trialResponse
                                elif prevTrialType == 'rewarded':
                                    ind = obj.trialRewarded
                                elif prevTrialType == 'unrewarded':
                                    ind = obj.trialResponse & ~obj.trialRewarded
                                elif prevTrialType == 'unrewarded target':
                                    ind = obj.trialResponse & np.in1d(obj.trialStim,obj.blockStimRewarded) & ~obj.trialRewarded
                                elif prevTrialType == 'no response':
                                    ind = ~obj.trialResponse
                                elif prevTrialType == 'response same stimulus':
                                    ind = obj.trialResponse & (obj.trialStim == stim)
                                elif prevTrialType == 'no response same stimulus':
                                    ind = ~obj.trialResponse & (obj.trialStim == stim)
                                r.append(d[trials][ind[trials-1]])
                                for _ in range(10):
                                    rShuffled.append(np.random.choice(d[trials],len(r[-1])))
                    r = np.concatenate(r)
                    rShuffled = np.concatenate(rShuffled)
                    resp.append(np.nanmean(r))
                    respShuffled.append(np.nanmean(rShuffled))
                ax.plot(respShuffled,resp,'o',color=mec,mec=mec,mfc=mfc,label=stimLbl)
            for side in ('right','top'):
                ax.spines[side].set_visible(False)
            ax.tick_params(direction='out',top=False,right=False,labelsize=10)
            ax.set_xlim(alim)
            ax.set_ylim(alim)
            ax.set_aspect('equal')
            ax.set_xlabel(lbl+'\nrandom trials',fontsize=12)
            ax.set_ylabel(lbl+'\nprevious trial '+prevTrialType,fontsize=12)
            ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=12)
            ax.set_title(blockLabel)
            plt.tight_layout()

x = np.arange(-5,0)            
for trialType in ('response','no response'):
    for rewardStim,blockLabel in zip(('vis1','sound1'),('visual rewarded blocks','auditory rewarded blocks')):
        fig = plt.figure(figsize=(7.5,5))
        ax = fig.add_subplot(1,1,1)
        y = []
        for stim,stimLbl,clr,ls in zip(stimNames,stimLabels,'gmgm',('-','-','--','--')):
            r = []
            rShuffled = []
            for exps,s in zip(sessionData,sessionsToPass):
                #exps[:nSessions]
                exps = exps[s:]
                r = []
                rShuffled = []
                for obj in exps:
                    stimTrials = np.where(obj.trialStim==stim)[0]
                    for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                        if rewStim==rewardStim:
                            blockTrials = np.where(~obj.autoRewardScheduled & (obj.trialBlock==blockInd+1))[0]
                            blockTrials = blockTrials[5:] # ignore first 5 trials after cue trials
                            trials = np.intersect1d(stimTrials,blockTrials)
                            n = 0
                            for i in trials:
                                if (trialType=='response' and obj.trialResponse[i]) or (trialType=='no response' and not obj.trialResponse[i]):
                                    r.append(obj.trialRewarded[i-5:i])
                                    n += 1
                            if n > 0:
                                for i in np.random.choice(blockTrials,n*10):
                                    rShuffled.append(obj.trialRewarded[i-5:i])
                            else:
                                r.append(np.full(5,np.nan))
                                rShuffled.append(np.full(5,np.nan))
                y.append(np.nanmean(r,axis=0))# - np.nanmean(rShuffled,axis=0))
            # m = np.nanmean(r,axis=0) #- np.nanmean(rShuffled,axis=0)
            m = np.nanmean(y,axis=0)
            s = np.nanstd(y,axis=0)/(len(y)**0.5)
            ax.plot(x,m,color=clr,ls=ls,label=stimLbl)
            ax.fill_between(x,m+s,m-s,color=clr,alpha=0.25)
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False,labelsize=10)
        ax.set_xlabel('Trials previous',fontsize=12)
        ax.set_ylabel('Change in probability of prior reward given ' + trialType + '\ncompared to random trials in the same block',fontsize=12)
        ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=12)
        ax.set_title(blockLabel)
        plt.tight_layout()
        

# time dependence of effect of prior reward or response (avg across mice)
stimType = ('rewarded target','non-rewarded target','non-target (rewarded modality)','non-target (unrewarded modality)')
prevTrialTypes = ('response to rewarded target','response to non-rewarded target','response to non-target')
trainingPhases = ('initial training','after learning')
blockEpochs = ('first half','last half','full')
resp = {phase: {epoch: {s: [] for s in stimType} for epoch in blockEpochs} for phase in trainingPhases}
respNorm = copy.deepcopy(resp)
respTime = copy.deepcopy(resp)
trialsSince = {phase: {epoch: {prevTrial: {s: [] for s in stimType} for prevTrial in prevTrialTypes} for epoch in blockEpochs} for phase in trainingPhases}
timeSince = copy.deepcopy(trialsSince)
for phase in trainingPhases:
    for epoch in blockEpochs:
        for exps,sp in zip(sessionData,sessionsToPass):
            for i,obj in enumerate(exps[:5] if phase=='initial training' else exps[sp:]):
                for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                    # if obj.hitRate[blockInd] < 0.8:
                    #     continue
                    blockTrials = getBlockTrials(obj,blockInd+1,epoch)
                    blockTrials = np.setdiff1d(blockTrials,np.where(obj.catchTrials)[0])
                    rewTargetTrials = np.intersect1d(blockTrials,np.where(obj.trialStim==rewStim)[0])
                    otherModalTarget = np.setdiff1d(obj.blockStimRewarded,rewStim)[0]
                    nonRewTargetTrials = np.intersect1d(blockTrials,np.where(obj.trialStim==otherModalTarget)[0])
                    targetTrials = np.concatenate((rewTargetTrials,nonRewTargetTrials))
                    nonTargetTrials = np.setdiff1d(blockTrials,targetTrials)
                    for s in stimType:
                        if i == 0 and blockInd == 0:
                            resp[phase][epoch][s].append([])
                            respNorm[phase][epoch][s].append([])
                            respTime[phase][epoch][s].append([])
                        if s=='rewarded target':
                            stim = rewStim
                        elif s=='non-rewarded target':
                            stim = otherModalTarget
                        elif s=='non-target (rewarded modality)':
                            stim = rewStim[:-1]+'2'
                        else:
                            stim = otherModalTarget[:-1]+'2'
                        stimTrials = obj.trialStim == stim
                        rt = obj.responseTimes - np.nanmean(obj.responseTimes[stimTrials])
                        stimTrials = np.intersect1d(blockTrials,np.where(stimTrials)[0])
                        if len(stimTrials) < 1:
                            continue
                        for prevTrialType,trials in zip(prevTrialTypes,(rewTargetTrials,nonRewTargetTrials,nonTargetTrials)):
                            if i == 0 and blockInd == 0:
                                trialsSince[phase][epoch][prevTrialType][s].append([])
                                timeSince[phase][epoch][prevTrialType][s].append([])
                            r = ~obj.trialResponse if 'non-response' in prevTrialType else obj.trialResponse
                            respTrials = np.intersect1d(trials,np.where(r)[0])
                            if len(respTrials) > 0:
                                prevRespTrial = respTrials[np.searchsorted(respTrials,stimTrials) - 1]
                                anyTargetTrials = np.array([np.any(np.in1d(obj.trialStim[p+1:s],(rewStim,otherModalTarget))) for s,p in zip(stimTrials,prevRespTrial)])
                                anyQuiescentViolations = np.array([np.any(obj.trialQuiescentViolations[p+1:s]) for s,p in zip(stimTrials,prevRespTrial)])
                                notValid = (stimTrials <= respTrials[0]) | (stimTrials > trials[-1]) | anyTargetTrials #| anyQuiescentViolations
                                tr = stimTrials - prevRespTrial
                                tr[notValid] = -1
                                tm = obj.stimStartTimes[stimTrials] - obj.stimStartTimes[prevRespTrial]
                                tm[notValid] = np.nan
                                trialsSince[phase][epoch][prevTrialType][s][-1].extend(tr)
                                timeSince[phase][epoch][prevTrialType][s][-1].extend(tm)
                            else:
                                trialsSince[phase][epoch][prevTrialType][s][-1].extend(np.full(len(stimTrials),np.nan))
                                timeSince[phase][epoch][prevTrialType][s][-1].extend(np.full(len(stimTrials),np.nan))
                        resp[phase][epoch][s][-1].extend(obj.trialResponse[stimTrials])
                        respNorm[phase][epoch][s][-1].extend(obj.trialResponse[stimTrials] - obj.trialResponse[stimTrials].mean())
                        respTime[phase][epoch][s][-1].extend(rt[stimTrials])
    
        for i,prevTrialType in enumerate(prevTrialTypes):
            for s in stimType:
                trialsSince[phase][epoch][prevTrialType][s] = [np.array(a) for a in trialsSince[phase][epoch][prevTrialType][s]]
                timeSince[phase][epoch][prevTrialType][s] = [np.array(a) for a in timeSince[phase][epoch][prevTrialType][s]]
                if i==0:
                    resp[phase][epoch][s] = [np.array(a) for a in resp[phase][epoch][s]]
                    respNorm[phase][epoch][s] = [np.array(a) for a in respNorm[phase][epoch][s]]
                    respTime[phase][epoch][s] = [np.array(a) for a in respTime[phase][epoch][s]]


trialBins = np.arange(20)
epoch = 'full'
for phase in ('initial training','after learning'):
    for prevTrialType in prevTrialTypes:
        fig = plt.figure(figsize=(8,4.5))
        ax = fig.add_subplot(1,1,1)
        for stim,clr,ls in zip(stimType,'gmgm',('-','-','--','--')):
            n = []
            p = []
            for d,r in zip(trialsSince[phase][epoch][prevTrialType][stim],respNorm[phase][epoch][stim]):
                n.append(np.full(trialBins.size,np.nan))
                p.append(np.full(trialBins.size,np.nan))
                for i in trialBins:
                    j = d==i
                    n[-1][i] = j.sum()
                    p[-1][i] = r[j].sum() / n[-1][i]
            m = np.nanmean(p,axis=0)
            s = np.nanstd(p,axis=0) / (len(p)**0.5)
            ax.plot(trialBins,m,color=clr,ls=ls,label=stim)
            ax.fill_between(trialBins,m-s,m+s,color=clr,alpha=0.25)
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False)
        ax.set_xlim([0,6])
        ax.set_ylim([-0.2,0.2])
        ax.set_xlabel('Trials (non-target) since last '+prevTrialType)
        ax.set_ylabel('Response rate')
        ax.legend(bbox_to_anchor=(1,1),loc='upper left')
        plt.tight_layout()
        
for phase in ('initial training','after learning'):
    for prevTrialType in prevTrialTypes:
        fig = plt.figure()#(figsize=(8,4.5))
        ax = fig.add_subplot(1,1,1)
        for stim,clr,ls in zip(stimType[:4],'gmgm',('-','-','--','--')):
            n = []
            p = []
            for d,r in zip(trialsSince[phase][epoch][prevTrialType][stim],respTime[phase][epoch][stim]):
                n.append(np.full(trialBins.size,np.nan))
                p.append(np.full(trialBins.size,np.nan))
                for i in trialBins:
                    j = d==i
                    j = j & ~np.isnan(r)
                    n[-1][i] = j.sum()
                    p[-1][i] = r[j].sum() / n[-1][i]
            m = np.nanmean(p,axis=0)
            s = np.nanstd(p,axis=0) / (len(p)**0.5)
            ax.plot(trialBins,m,color=clr,ls=ls,label=stim)
            ax.fill_between(trialBins,m-s,m+s,color=clr,alpha=0.25)
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False,labelsize=10)
        ax.set_xlim([0,6])
        ax.set_ylim([-0.08,0.08])
        ax.set_yticks(np.arange(-0.08,0.1,0.04))
        ax.set_xlabel('Trials (non-target) since last '+prevTrialType,fontsize=12)
        ax.set_ylabel('Response time (difference from mean, s)',fontsize=12)
        # ax.legend(bbox_to_anchor=(1,1),loc='upper left')
        plt.tight_layout()
        
timeBins = np.array([0,5,10,15,20,35,50,80])
x = timeBins[:-1] + np.diff(timeBins)/2
epoch = 'full'
for phase in trainingPhases:
    y = {prevTrial: {} for prevTrial in prevTrialTypes}
    for prevTrialType in prevTrialTypes:    
        fig = plt.figure(figsize=(12,6))
        ax = fig.add_subplot(1,1,1)
        for stim,clr,ls in zip(stimType,'gmgm',('-','-','--','--')):
            n = []
            p = []
            for d,r in zip(timeSince[phase][epoch][prevTrialType][stim],respNorm[phase][epoch][stim]):
                n.append(np.full(x.size,np.nan))
                p.append(np.full(x.size,np.nan))
                for i,t in enumerate(timeBins[:-1]):
                    j = (d >= t) & (d < timeBins[i+1])
                    n[-1][i] = j.sum()
                    p[-1][i] = r[j].sum() / n[-1][i]
            m = np.nanmean(p,axis=0)
            s = np.nanstd(p,axis=0) / (len(p)**0.5)
            ax.plot(x,m,color=clr,ls=ls,label=stim)
            ax.fill_between(x,m-s,m+s,color=clr,alpha=0.25)
            y[prevTrialType][stim] = {'mean': m, 'sem': s}
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False,labelsize=16)
        # ax.set_xlim([0,47.5])
        ax.set_yticks(np.arange(-0.5,0.5,0.1))
        ax.set_ylim([-0.1,0.2])
        ax.set_xlabel('Time since last '+prevTrialType+' (s)',fontsize=18)
        ax.set_ylabel('Response rate (minus within-block mean)',fontsize=18)
        ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=16)
        plt.tight_layout()

stim = 'non-rewarded target'        
for phase in ('after learning',):
    for prevTrialType in prevTrialTypes:    
        fig = plt.figure(figsize=(10,6))
        ax = fig.add_subplot(1,1,1)
        for epoch,clr in zip(blockEpochs,'rbk'):
            n = []
            p = []
            for d,r in zip(timeSince[phase][epoch][prevTrialType][stim],resp[phase][epoch][stim]):
                n.append(np.full(x.size,np.nan))
                p.append(np.full(x.size,np.nan))
                for i,t in enumerate(timeBins[:-1]):
                    j = (d >= t) & (d < timeBins[i+1])
                    n[-1][i] = j.sum()
                    p[-1][i] = r[j].sum() / n[-1][i]
            m = np.nanmean(p,axis=0)
            s = np.nanstd(p,axis=0) / (len(p)**0.5)
            ax.plot(x,m,color=clr,label=(epoch+' block' if epoch=='full' else epoch+' of block'))
            ax.fill_between(x,m-s,m+s,color=clr,alpha=0.25)
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False,labelsize=16)
        # ax.set_xlim([0,47.5])
        ax.set_yticks(np.arange(0,1,0.1))
        ax.set_ylim([0.35,0.65])
        ax.set_xlabel('Time since last '+prevTrialType+' (s)',fontsize=18)
        ax.set_ylabel('Response rate',fontsize=18)
        ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=16)
        plt.tight_layout()
        
for prevTrialType in prevTrialTypes:    
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    n = []
    p = []
    for d,r in zip(timeSince[phase]['full'][prevTrialType][stim],resp[phase]['full'][stim]):
        n.append(np.full(x.size,np.nan))
        p.append(np.full(x.size,np.nan))
        for i,t in enumerate(timeBins[:-1]):
            j = (d >= t) & (d < timeBins[i+1])
            n[-1][i] = j.sum()
            p[-1][i] = r[j].sum() / n[-1][i]
    m = np.nanmean(p,axis=0)
    s = np.nanstd(p,axis=0) / (len(p)**0.5)
    ax.plot(x,m,color='k')
    ax.fill_between(x,m-s,m+s,color='k',alpha=0.25)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=14)
    ax.set_xlim([0,47.5])
    ax.set_ylim([0.3,0.8])
    ax.set_xlabel('Time since last '+prevTrialType+' (s)',fontsize=16)
    ax.set_ylabel('Response rate',fontsize=16)
    plt.tight_layout()


fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(1,1,1)
t = x
m,s = [y['response to rewarded target']['non-rewarded target'][key] for key in ('mean','sem')]
m,s = [y['response to non-rewarded target']['non-rewarded target'][key] for key in ('mean','sem')]
f1 = lambda t,tau,a,b: a * np.exp(-t/tau) + b
f2 = lambda t,tau,a,b: b - a * np.exp(-t/tau)
func = lambda t,tau1,tau2,a1,b1,a2,b2: (a1 * np.exp(-t/tau1) + b1) + (b2 - a2 * np.exp(-t/tau2))
tau1,tau2,a1,b1,a2,b2 = scipy.optimize.curve_fit(func,t[1:],m[1:],p0=(10,100,0.1,0,1,0.8),bounds=((3,20,0,0,0,0),(30,200,1,0.0001,1,1)))[0]
tau1,tau2,a1,b1,a2,b2 = scipy.optimize.curve_fit(func,t[1:],m[1:],p0=(10,100,0.5,0.1,0.5,0.5),bounds=((1,10,0,0.1,0,0),(200,200,1,0.1001,1,1)))[0]
# ax.plot(t,m,'m',lw=3,label='non-rewarded target')
ax.fill_between(t,m-s,m+s,color='m',alpha=0.25,label='non-rewarded target')
ax.plot(t[1:],func(t[1:],tau1,tau2,a1,b1,a2,b2),'k',label='fit (2 exponential functions)          ')
ax.plot(t[1:],f1(t[1:],tau1,a1,b1),'r--',label='effect of reward bias')
ax.plot(t[1:],f2(t[1:],tau2,a2,b2),'b--',label='effect of context forgetting')
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False,labelsize=16)
# ax.set_xlim([0,47.5])
ax.set_yticks(np.arange(-0.5,0.5,0.1))
ax.set_ylim([-0.1,0.2])
ax.set_xlabel('Time since last response to rewarded target (s)',fontsize=18)
ax.set_ylabel('Response rate (minus within-block mean)',fontsize=18)
ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=16)
plt.tight_layout()


for phase in ('initial training','after learning'):
    for prevTrialType in prevTrialTypes:
        for epoch in ('full',):#blockEpochs:
            fig = plt.figure()#(figsize=(8,4.5))
            ax = fig.add_subplot(1,1,1)
            for stim,clr,ls in zip(stimType[:2],'gmgm',('-','-','--','--')):
                n = []
                p = []
                for d,r in zip(timeSince[phase][epoch][prevTrialType][stim],respTime[phase][epoch][stim]):
                    n.append(np.full(x.size,np.nan))
                    p.append(np.full(x.size,np.nan))
                    for i,t in enumerate(timeBins[:-1]):
                        j = (d >= t) & (d < timeBins[i+1])
                        j = j & ~np.isnan(r)
                        n[-1][i] = j.sum()
                        p[-1][i] = r[j].sum() / n[-1][i]
                m = np.nanmean(p,axis=0)
                s = np.nanstd(p,axis=0) / (len(p)**0.5)
                ax.plot(x,m,color=clr,ls=ls,label=stim)
                ax.fill_between(x,m-s,m+s,color=clr,alpha=0.25)
            for side in ('right','top'):
                ax.spines[side].set_visible(False)
            ax.tick_params(direction='out',top=False,right=False,labelsize=10)
            # ax.set_xlim([0,47.5])
            ax.set_ylim([-0.08,0.08])
            ax.set_yticks(np.arange(-0.08,0.1,0.04))
            ax.set_xlabel('Time since last '+prevTrialType+' (s)',fontsize=12)
            ax.set_ylabel('Response time (difference from mean, s)',fontsize=12)
            # ax.set_title(epoch)
            # ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=10)
            plt.tight_layout()
        



# time dependence of effect of prior reward or response (pooled across mice)
stimType = ('rewarded target','non-rewarded target','non-target (rewarded modality)','non-target (unrewarded modality)')
prevTrialTypes = ('response to rewarded target','response to non-rewarded target','response to either target','response to non-target')
resp = {phase: {s: [] for s in stimType} for phase in ('initial training','after learning')}
respTime = copy.deepcopy(resp)
trialsSince = {phase: {prevTrial: {s: [] for s in stimType} for prevTrial in prevTrialTypes} for phase in ('initial training','after learning')}
timeSince = copy.deepcopy(trialsSince)
for phase in ('initial training','after learning'):
    for obj in [obj for exps,s in zip(sessionData,sessionsToPass) for obj in (exps[:5] if phase=='initial training' else exps[s:])]:
        for blockInd,rewStim in enumerate(obj.blockStimRewarded):
            # if obj.hitRate[blockInd] < 0.85:
            #     continue
            otherModalTarget = np.setdiff1d(obj.blockStimRewarded,rewStim)[0]
            blockTrials = (obj.trialBlock==blockInd+1) & ~obj.catchTrials & ~obj.autoRewardScheduled
            rewTargetTrials = blockTrials & (obj.trialStim==rewStim)
            nonRewTargetTrials = blockTrials & (obj.trialStim==otherModalTarget)
            targetTrials = rewTargetTrials | nonRewTargetTrials
            nonTargetTrials = blockTrials & ~targetTrials
            for s in stimType:
                if s=='rewarded target':
                    stim = rewStim
                elif s=='non-rewarded target':
                    stim = otherModalTarget
                elif s=='non-target (rewarded modality)':
                    stim = rewStim[:-1]+'2'
                else:
                    stim = otherModalTarget[:-1]+'2'
                stimTrials = obj.trialStim == stim
                rtz = (obj.responseTimes - np.nanmean(obj.responseTimes[stimTrials])) / np.nanstd(obj.responseTimes[stimTrials])
                stimTrials = np.where(blockTrials & stimTrials)[0]
                for prevTrialType,trials in zip(prevTrialTypes,(rewTargetTrials,nonRewTargetTrials,targetTrials,nonTargetTrials)):
                    respTrials = np.where(trials & obj.trialResponse)[0]
                    if len(respTrials) > 0:
                        prevRespTrial = respTrials[np.searchsorted(respTrials,stimTrials) - 1]
                        anyTargetTrials = np.array([np.any(np.in1d(obj.trialStim[p+1:s],(rewStim,otherModalTarget))) for s,p in zip(stimTrials,prevRespTrial)])
                        anyQuiescentViolations = np.array([np.any(obj.trialQuiescentViolations[p+1:s]) for s,p in zip(stimTrials,prevRespTrial)])
                        notValid = (stimTrials <= respTrials[0]) | (stimTrials > np.where(trials)[0][-1]) | anyTargetTrials #| anyQuiescentViolations
                        tr = stimTrials - prevRespTrial
                        tr[notValid] = -1
                        tm = obj.stimStartTimes[stimTrials] - obj.stimStartTimes[prevRespTrial]
                        tm[notValid] = np.nan
                        trialsSince[phase][prevTrialType][s].extend(tr)
                        timeSince[phase][prevTrialType][s].extend(tm)
                    else:
                        trialsSince[phase][prevTrialType][s].extend(np.full(len(stimTrials),np.nan))
                        timeSince[phase][prevTrialType][s].extend(np.full(len(stimTrials),np.nan))
                resp[phase][s].extend(obj.trialResponse[stimTrials] - np.mean(obj.trialResponse[stimTrials]))
                respTime[phase][s].extend(rtz[stimTrials])

    for i,prevTrialType in enumerate(prevTrialTypes):
        for s in stimType:
            trialsSince[phase][prevTrialType][s] = np.array(trialsSince[phase][prevTrialType][s])
            timeSince[phase][prevTrialType][s] = np.array(timeSince[phase][prevTrialType][s])
            if i==0:
                resp[phase][s] = np.array(resp[phase][s])
                respTime[phase][s] = np.array(respTime[phase][s])


trialBins = np.arange(20)
for phase in ('initial training','after learning'):
    for prevTrialType in prevTrialTypes:
        fig = plt.figure(figsize=(8,4.5))
        ax = fig.add_subplot(1,1,1)
        for s,clr,ls in zip(stimType,'gmgm',('-','-','--','--')):
            n = np.zeros(trialBins.size)
            p = np.zeros(trialBins.size)
            for i in trialBins:
                j = trialsSince[phase][prevTrialType][s]==i
                n[i] = j.sum()
                p[i] = resp[phase][s][j].sum() / n[i]
            print(n)
            ci = np.array([[b/n[i] for b in scipy.stats.binom.interval(0.95,n[i],p[i])] for i in trialBins])
            ax.plot(trialBins,p,color=clr,ls=ls,label=s)
            ax.fill_between(trialBins,ci[:,0],ci[:,1],color=clr,alpha=0.25)
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False)
        # ax.set_xlim([0,6])
        # ax.set_ylim([0,1.01])
        ax.set_xlabel('Trials (non-target) since last '+prevTrialType)
        ax.set_ylabel('Response rate')
        ax.legend(bbox_to_anchor=(1,1),loc='upper left')
        plt.tight_layout()

for phase in ('initial training','after learning'):    
    for prevTrialType in prevTrialTypes:
        fig = plt.figure(figsize=(5,4))
        ax = fig.add_subplot(1,1,1)
        for s,clr,ls in zip(stimType[:2],'gm',('-','-')):
            n = np.zeros(trialBins.size)
            p = np.zeros(trialBins.size)
            sem = np.zeros(trialBins.size)
            for i in trialBins:
                j = trialsSince[phase][prevTrialType][s]==i
                j = j & ~np.isnan(respTime[phase][s])
                n[i] = j.sum()
                p[i] = respTime[phase][s][j].sum() / n[i]
                sem[i] = np.std(respTime[phase][s][j]) / (n[i]**0.5)
            ax.plot(trialBins,p,color=clr,ls=ls,label=s)
            ax.fill_between(trialBins,p-sem,p+sem,color=clr,alpha=0.25)
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False,labelsize=14)
        ax.set_xlim([0,6])
        ax.set_yticks([-1,-0.5,0,0.5,1])
        ax.set_ylim([-1,1])
        ax.set_xlabel('Trials (non-target) since last '+prevTrialType,fontsize=16)
        ax.set_ylabel('Response time (z score)',fontsize=16)
        # ax.legend(bbox_to_anchor=(1,1),loc='upper left')
        plt.tight_layout()


timeBins = np.array([0,5,10,15,20,25,35,45,55,65,100])
x = timeBins[:-1] + np.diff(timeBins)/2
for phase in ('initial training','after learning'):
    y = {prevTrial: {} for prevTrial in prevTrialTypes}
    for prevTrialType in prevTrialTypes:    
        fig = plt.figure(figsize=(8,4.5))
        ax = fig.add_subplot(1,1,1)
        for s,clr,ls in zip(stimType,'gmgm',('-','-','--','--')):
            n = np.zeros(x.size)
            p = np.zeros(x.size)
            for i,t in enumerate(timeBins[:-1]):
                j = (timeSince[phase][prevTrialType][s] >= t) & (timeSince[phase][prevTrialType][s] < timeBins[i+1])
                n[i] = j.sum()
                p[i] = resp[phase][s][j].sum() / n[i]
            print(n)
            ci = np.array([[b/n[i] for b in scipy.stats.binom.interval(0.95,n[i],p[i])] for i in range(x.size)])
            ax.plot(x,p,color=clr,ls=ls,label=s)
            ax.fill_between(x,ci[:,0],ci[:,1],color=clr,alpha=0.25)
            y[prevTrialType][s] = p
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False,labelsize=10)
        ax.set_xlim([0,60])
        # ax.set_yticks([0,0.5,1])
        # ax.set_ylim([0,1.01])
        ax.set_xlabel('Time since last '+prevTrialType+' (s)',fontsize=12)
        ax.set_ylabel('Response rate',fontsize=12)
        ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=10)
        plt.tight_layout()

for phase in ('initial training','after learning'):
    for prevTrialType in prevTrialTypes:    
        fig = plt.figure(figsize=(8,4.5))
        ax = fig.add_subplot(1,1,1)
        for s,clr,ls in zip(stimType[:2],'gm',('-','-')):
            n = np.zeros(x.size)
            p = np.zeros(x.size)
            sem = np.zeros(x.size)
            for i,t in enumerate(timeBins[:-1]):
                j = (timeSince[phase][prevTrialType][s] >= t) & (timeSince[phase][prevTrialType][s] < timeBins[i+1])
                j = j & ~np.isnan(respTime[phase][s])
                n[i] = j.sum()
                p[i] = respTime[phase][s][j].sum() / n[i]
                sem[i] = np.std(respTime[phase][s][j]) / (n[i]**0.5)
            ax.plot(x,p,color=clr,ls=ls,label=s)
            ax.fill_between(x,p-sem,p+sem,color=clr,alpha=0.25)
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False,labelsize=10)
        ax.set_xlim([0,60])
        ax.set_ylim([-0.5,1])
        ax.set_yticks([-0.5,0,0.5,1])
        ax.set_xlabel('Time since last '+prevTrialType+' (s)',fontsize=12)
        ax.set_ylabel('Response time (z score)',fontsize=12)
        ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=10)
        plt.tight_layout()

    
fig = plt.figure(figsize=(8,4.5))
ax = fig.add_subplot(1,1,1)
t = x
p = y['response to rewarded target']['non-rewarded target']
f1 = lambda t,tau,a,b: a * np.exp(-t/tau) + b
f2 = lambda t,tau,a,b: b - a * np.exp(-t/tau)
func = lambda t,tau1,tau2,a1,b1,a2,b2: (a1 * np.exp(-t/tau1) + b1) + (b2 - a2 * np.exp(-t/tau2))
tau1,tau2,a1,b1,a2,b2 = scipy.optimize.curve_fit(func,t[1:],p[1:],p0=(10,100,1,0,1,1),bounds=((1,10,0,0,0,0),(30,300,1,1,1,1)))[0]
ax.plot(t,p,'m',lw=2,label='non-rewarded target                   ')
ax.plot(t[1:],func(t[1:],tau1,tau2,a1,b1,a2,b2),'k--',label='fit')
ax.plot(t[1:],f1(t[1:],tau1,a1,b1),'r')
ax.plot(t[1:],f2(t[1:],tau2,a2,b2),'b')
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False,labelsize=10)
ax.set_xlim([0,52.5])
# ax.set_ylim([0.35,0.6])
ax.set_xlabel('Time since last response to rewarded target (s)',fontsize=12)
ax.set_ylabel('Response rate',fontsize=12)
ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=10)
plt.tight_layout()

for s in stimType:
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.hist(timeSince['response to rewarded target'][s],bins=timeBins)
    ax.set_yscale('log')
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False)
    plt.tight_layout()


# performance by block number
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
x = np.arange(6)+1
for rewardStim,clr,blockLbl in zip(('vis1','sound1'),'gm',('visual rewarded','auditory rewarded')):
    for lbl,ls in zip(('cross-modality','within modality'),('-','--')):
        dp = []
        for exps,s in zip(sessionData,sessionsToPass):
            d = np.full((len(exps),6),np.nan)
            for i,obj in enumerate(exps[s:]):
                j = obj.blockStimRewarded==rewardStim
                a = obj.dprimeSameModal if 'within' in lbl else obj.dprimeOtherModalGo
                d[i,j] = np.array(a)[j]
            dp.append(np.nanmean(d,axis=0))
        m = np.nanmean(dp,axis=0)
        s = np.nanstd(dp,axis=0)/(len(dp)**0.5)
        ax.plot(x,m,color=clr,ls=ls,label=blockLbl+', '+lbl)
        ax.fill_between(x,m+s,m-s,color=clr,alpha=0.25)
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False)
ax.set_yticks(np.arange(5))
ax.set_ylim([0,4])
ax.set_xlabel('Block')
ax.set_ylabel('d\'')
ax.legend(loc='lower right')
ax.set_title(str(len(sessionData))+' mice')
plt.tight_layout()

# catch rate and quiescent violations
for stage in ('initial training','after learning'):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    x = np.arange(6)+1
    for rewardStim,clr,lbl in zip(('vis1','sound1'),'gm',('visual rewarded','auditory rewarded')):
        rr = []
        for exps,s in zip(sessionData,sessionsToPass):
            exps = exps[:5] if stage=='initial training' else exps[s:]
            r = np.full((len(exps),6),np.nan)
            for i,obj in enumerate(exps):
                j = obj.blockStimRewarded==rewardStim
                r[i,j] = np.array(obj.catchResponseRate)[j]
            rr.append(np.nanmean(r,axis=0))
        m = np.nanmean(rr,axis=0)
        s = np.nanstd(rr,axis=0)/(len(rr)**0.5)
        ax.plot(x,m,color=clr,label=lbl+' blocks')
        ax.fill_between(x,m+s,m-s,color=clr,alpha=0.25)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=12)
    ax.set_ylim([0,0.1])
    ax.set_xlabel('Block',fontsize=14)
    ax.set_ylabel('Catch trial response rate',fontsize=14)
    ax.legend(loc='upper right',fontsize=12)
    ax.set_title(stage+' ('+str(len(sessionData))+' mice)',fontsize=14)
    plt.tight_layout()
    
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    x = np.arange(6)+1
    for rewardStim,clr,lbl in zip(('vis1','sound1'),'gm',('visual rewarded','auditory rewarded')):
        rr = []
        for exps,s in zip(sessionData,sessionsToPass):
            exps = exps[:5] if stage=='initial training' else exps[s:]
            r = np.full((len(exps),6),np.nan)
            for i,obj in enumerate(exps):
                for blockInd,blockRewardStim in enumerate(obj.blockStimRewarded):
                    if blockRewardStim==rewardStim:
                        trials = obj.trialBlock==blockInd+1
                        r[i,blockInd] = np.array(obj.trialQuiescentViolations)[trials].sum() / trials.sum()
            rr.append(np.nanmean(r,axis=0))
        m = np.nanmean(rr,axis=0)
        s = np.nanstd(rr,axis=0)/(len(rr)**0.5)
        ax.plot(x,m,color=clr,label=lbl+' blocks')
        ax.fill_between(x,m+s,m-s,color=clr,alpha=0.25)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=12)
    ax.set_ylim([0,0.5])
    ax.set_xlabel('Block',fontsize=14)
    ax.set_ylabel('Quiescent violations per trial',fontsize=14)
    ax.legend(loc='upper right',fontsize=12)
    ax.set_title(stage+' ('+str(len(sessionData))+' mice)',fontsize=14)
    plt.tight_layout()
    
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    x = np.arange(6)+1
    for rewardStim,clr,lbl in zip(('vis1','sound1'),'gm',('visual rewarded','auditory rewarded')):
        rr = []
        for exps,s in zip(sessionData,sessionsToPass):
            exps = exps[:5] if stage=='initial training' else exps[s:]
            r = np.full((len(exps),6),np.nan)
            for i,obj in enumerate(exps):
                for blockInd,blockRewardStim in enumerate(obj.blockStimRewarded):
                    if blockRewardStim==rewardStim:
                        trials = obj.trialBlock==blockInd+1
                        r[i,blockInd] = np.nanmean(obj.quiescentRunSpeed[trials])
            rr.append(np.nanmean(r,axis=0))
        m = np.nanmean(rr,axis=0)
        s = np.nanstd(rr,axis=0)/(len(rr)**0.5)
        ax.plot(x,m,color=clr,label=lbl+' blocks')
        ax.fill_between(x,m+s,m-s,color=clr,alpha=0.25)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=12)
    ax.set_ylim([15,35])
    ax.set_xlabel('Block',fontsize=14)
    ax.set_ylabel('Run speed (cm/s)',fontsize=14)
    ax.legend(loc='upper right',fontsize=12)
    ax.set_title(stage+' ('+str(len(sessionData))+' mice)',fontsize=14)
    plt.tight_layout()


# performance variability
varWithinSession = [np.mean([np.nanstd(obj.dprimeOtherModalGo) for obj in exps[s:]]) for exps,s in zip(sessionData,sessionsToPass)]
varAcrossSessions = []
for exps,s in zip(sessionData,sessionsToPass):
    visBlockDp = []
    audBlockDp = []
    for obj in exps[s:]:
        dp = np.array(obj.dprimeOtherModalGo)
        visBlockDp.append(dp[obj.blockStimRewarded=='vis1'])
        audBlockDp.append(dp[obj.blockStimRewarded=='sound1'])
    visBlockDp = np.concatenate(visBlockDp)
    audBlockDp = np.concatenate(audBlockDp)
    varAcrossSessions.append(np.mean([np.nanstd(np.concatenate([np.random.choice(dp,3) for dp in (visBlockDp,audBlockDp)])) for _ in range(1000)]))


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot([0,2],[0,2],'k--')
ax.plot(varWithinSession,varAcrossSessions,'ko',alpha=0.5)
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False)
ax.set_xlim([0.25,1.25])
ax.set_ylim([0.25,1.25])
ax.set_aspect('equal')
ax.set_xlabel('Within session performance variability')
ax.set_ylabel('Across session performance variability')
plt.tight_layout()



# cluster session performance
stimNames = ('vis1','vis2','sound1','sound2')
clustData = {key: [] for key in ('nSessions','mouseId','sessionStartTime','mouse','session','passed','block','firstRewardStim','hitRate','falseAlarmRate','dprime','clustData')}
tintp = np.arange(600)
nMice = len(sessionData)
nExps = [len(s) for s in sessionData]
for m,(exps,s) in enumerate(zip(sessionData,sessionsToPass)):
    #exps = exps[s:] # exps[:s+nSessions]
    for i,obj in enumerate(exps):
        clustData['nSessions'].append(len(exps))
        clustData['mouseId'].append(obj.subjectName)
        clustData['sessionStartTime'].append(obj.startTime)
        clustData['mouse'].append(m)
        clustData['session'].append(i)
        clustData['passed'].append(s-2<i)
        clustData['firstRewardStim'].append(obj.blockStimRewarded[0])
        hitRate = []
        falseAlarmRate = []
        dprime = []
        for blockInd,rew in enumerate(obj.blockStimRewarded):
            blockTrials = (obj.trialBlock == blockInd + 1) & (~obj.trialRepeat)
            goTrials = obj.goTrials[blockTrials].sum()
            hitRate.append(obj.hitTrials[blockTrials].sum() / goTrials)
            otherModalGo = blockTrials & obj.otherModalGoTrials
            nogoTrials = otherModalGo.sum()
            falseAlarmRate.append(obj.falseAlarmTrials[otherModalGo].sum() / nogoTrials)
            dprime.append(calcDprime(hitRate[-1],falseAlarmRate[-1],goTrials,nogoTrials))
        clustData['hitRate'].append(hitRate)
        clustData['falseAlarmRate'].append(falseAlarmRate)
        clustData['dprime'].append(dprime)
        clustData['clustData'].append(np.concatenate((hitRate,falseAlarmRate)))

for key in clustData:
    clustData[key] = np.array(clustData[key])
    
pcaData,eigVal,eigVec = pca(clustData['clustData'])

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(np.arange(1,eigVal.size+1),eigVal.cumsum()/eigVal.sum(),'k')
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False)
ax.set_xlim([0,13])
ax.set_ylim((0,1.02))
ax.set_xlabel('PC')
ax.set_ylabel('Cumulative Fraction of Variance Explained')
plt.tight_layout()


clustColors = [clr for clr in 'rgkbmcy']+['0.6']
nClust = 6
clustId,linkageMat = cluster(clustData['clustData'],nClusters=nClust)
clustLabels = np.unique(clustId)

newClustOrder = [4,5,1,3,2,6]
newClustId = clustId.copy()
for i,c in enumerate(newClustOrder):
    newClustId[clustId==c] = i+1
clustId = newClustId


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
colorThresh = 0 if nClust<2 else linkageMat[::-1,2][nClust-2]
scipy.cluster.hierarchy.set_link_color_palette(list(clustColors))
scipy.cluster.hierarchy.dendrogram(linkageMat,ax=ax,truncate_mode=None,p=7,color_threshold=colorThresh,above_threshold_color='k',labels=None,no_labels=True)
scipy.cluster.hierarchy.set_link_color_palette(None)
ax.plot([0,1000000],[0.85*colorThresh]*2,'k--')
ax.set_yticks([])
for side in ('right','top','left','bottom'):
    ax.spines[side].set_visible(False)
plt.tight_layout()
    
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
k = np.arange(linkageMat.shape[0])+2
ax.plot(k,linkageMat[::-1,2],'ko-',mfc='none',ms=10,mew=2,linewidth=2)
ax.plot([0,100],[0.85*colorThresh]*2,'k--')
ax.set_xlim([0,30.4])
ax.set_xlabel('Cluster')
ax.set_ylabel('Linkage Distance')
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False)
plt.tight_layout()

        
x = np.arange(6)+1
for clust in clustLabels:
    for firstRewardStim,sessionLabel in zip(('vis1','sound1'),('visual rewarded first','auditory rewarded first')):
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        i = (clustData['firstRewardStim']==firstRewardStim) & (clustId==clust)
        hr = clustData['hitRate'][i]
        fr = clustData['falseAlarmRate'][i]
        for clr,lbl in zip('gm',('visual target','auditory target')):
            r = np.zeros((i.sum(),6))
            if (firstRewardStim=='vis1' and lbl=='visual target') or (firstRewardStim=='sound1' and lbl=='auditory target'):
                r[:,::2] = hr[:,::2]
                r[:,1::2] = fr[:,1::2]
            else:
                r[:,::2] = fr[:,::2]
                r[:,1::2] = hr[:,1::2]
            m = np.nanmean(r,axis=0)
            s = np.nanstd(r)/(len(r)**0.5)
            ax.plot(x,m,color=clr,label=lbl)
            ax.fill_between(x,m+s,m-s,color=clr,alpha=0.25)
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False,labelsize=16)
        ax.set_xticks(x)
        ax.set_yticks([0,0.5,1])
        ax.set_xlim([0.5,6.5])
        ax.set_ylim([0,1.01])
        ax.set_xlabel('Block #',fontsize=18)
        ax.set_ylabel('Response rate',fontsize=18)
        ax.legend(loc='lower center',fontsize=16)
        ax.set_title('cluster '+str(clust)+', '+sessionLabel+' (n='+str(len(r))+' sessions)',fontsize=12)
        plt.tight_layout()

x = np.arange(6)+1        
for clust in clustLabels:
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    for firstRewardStim,clr,lbl in zip(('vis1','sound1'),'gm',('visual rewarded first','auditory rewarded first')):
        r = clustData['dprime'][(clustData['firstRewardStim']==firstRewardStim) & (clustId==clust)]
        m = np.nanmean(r,axis=0)
        s = np.nanstd(r)/(len(r)**0.5)
        ax.plot(x,m,color=clr,label=lbl)
        ax.fill_between(x,m+s,m-s,color=clr,alpha=0.25)
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False,labelsize=16)
        ax.set_xticks(x)
        ax.set_xlim([0.5,6.5])
        ax.set_ylim([0,2.5])
        ax.set_xlabel('Block #',fontsize=18)
        ax.set_ylabel('Cross-modal d\'',fontsize=18)
        ax.legend(fontsize=16)
        ax.set_title('cluster '+str(clust),fontsize=12)
        plt.tight_layout()
        
        
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
for firstRewStim,offset,clr in zip(('vis1','sound1'),(-0.2,0.2),'gm'):
    i = clustData['firstRewardStim']==firstRewStim
    for clust in clustLabels:
        n = np.sum(i & (clustId==clust))
        lbl = ('visual rewarded first' if firstRewStim=='vis1' else 'auditory rewarded first') if clust==1 else None
        ax.bar(clust+offset,n,width=0.4,color=clr,label=lbl)
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out')
ax.set_xticks(clustLabels)
ax.set_xticklabels(clustLabels)
# ax.set_ylim((0,0.6))
ax.set_xlabel('Cluster')
ax.set_ylabel('Number of sessions')
ax.legend()
plt.tight_layout()


for ind in (clustData['session']<5,(clustData['session']>=5) & ~clustData['passed'],clustData['passed']):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    for firstRewStim,offset,clr in zip(('vis1','sound1'),(-0.2,0.2),'gm'):
        i = ind * (clustData['firstRewardStim']==firstRewStim)
        for clust in clustLabels:
            p = np.sum(i & (clustId==clust)) / i.sum()
            lbl = ('visual rewarded first' if firstRewStim=='vis1' else 'auditory rewarded first') if clust==1 else None
            ax.bar(clust+offset,p,width=0.4,color=clr,label=lbl)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out')
    ax.set_xticks(clustLabels)
    ax.set_xticklabels(clustLabels)
    ax.set_ylim((0,0.7))
    ax.set_xlabel('Cluster')
    ax.set_ylabel('Fraction of sessions')
    ax.legend()
    plt.tight_layout()


mouseClustProb = np.zeros((3,3,nMice,nClust))
for l,si in enumerate((np.ones(clustData['firstRewardStim'].size,dtype=bool),clustData['firstRewardStim']=='vis1',clustData['firstRewardStim']=='sound1')):
    for k,ind in enumerate((clustData['session']<5,(clustData['session']>=5) & ~clustData['passed'],clustData['passed'])):
        for i,m in enumerate(np.argsort(sessionsToPass)):
            for j,clust in enumerate(clustLabels):
                s = clustId[(clustData['mouse']==m) & ind & si]
                mouseClustProb[l,k,i,j] = np.sum(s==clust)/s.size

for k in (0,1,2):
    fig = plt.figure(figsize=(10,8))
    fig.suptitle('Cluster probability')
    for i,(p,lbl) in enumerate(zip(mouseClustProb[0],('intitial training','later training','after learning'))):            
        ax = fig.add_subplot(1,3,i+1) 
        im = ax.imshow(p,cmap='magma',clim=(0,np.nanmax(p)))
        cb = plt.colorbar(im,ax=ax,fraction=0.026,pad=0.04)
        ax.set_xticks(np.arange(nClust))
        ax.set_xticklabels(np.arange(nClust)+1)
        ax.set_yticks([])
        if i==1:
            ax.set_xlabel('Cluster')
        if i==0:
            ax.set_ylabel('Mouse')
        ax.set_title(lbl)
        plt.tight_layout()
        
fig = plt.figure()
fig.suptitle('Cluster probability')
for i,(p,lbl) in enumerate(zip(mouseClustProb[1]-mouseClustProb[2],('intitial training','later training','after learning'))):            
    ax = fig.add_subplot(1,3,i+1)
    cmax = np.absolute(p).max()
    im = ax.imshow(p,cmap='bwr',clim=(-cmax,cmax))
    cb = plt.colorbar(im,ax=ax,fraction=0.026,pad=0.04)
    ax.set_xticks(np.arange(nClust))
    ax.set_xticklabels(np.arange(nClust)+1)
    ax.set_yticks([])
    if i==1:
        ax.set_xlabel('Cluster')
    if i==0:
        ax.set_ylabel('Mouse')
    ax.set_title(lbl)
    plt.tight_layout()

        
sessionClust = np.full((nMice,max(clustData['nSessions'])),np.nan)
for i,m in enumerate(np.argsort(sessionsToPass)):
    c = clustId[clustData['mouse']==m]
    sessionClust[i,:c.size] = c
        
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
cmap = matplotlib.cm.viridis.copy()
cmap.set_bad(color=[0.5]*3)
im = ax.imshow(sessionClust,cmap=cmap)
cb = plt.colorbar(im,ax=ax,fraction=0.01,pad=0.04)
cb.set_ticks(np.arange(nClust)+1)
for i,m in enumerate(np.argsort(sessionsToPass)):
    ax.plot([sessionsToPass[m]-0.5]*2,[i-0.4,i+0.4],'w')
ax.set_xticks(np.arange(10,sessionClust.shape[1],10)-1)
ax.set_xticklabels(np.arange(10,sessionClust.shape[1],10))
ax.set_yticks([])
ax.set_xlabel('Session')
ax.set_ylabel('Mouse')
ax.set_title('Session cluster\n(white line = passed learning criteria)')
plt.tight_layout()


sessionClustAlt = np.full((nMice,max(clustData['nSessions'])),np.nan)
for i,m in enumerate(np.argsort(sessionsToPass)):
    c = clustId[clustData['mouse']==m]
    sessionClustAlt[i,:c.size] = 0
    sessionClustAlt[i,:c.size][c==4] = 1
    sessionClustAlt[i,:c.size][c==5] = -1

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
cmap = matplotlib.cm.bwr.copy()
cmap.set_bad(color=[0.5]*3)
im = ax.imshow(sessionClustAlt,cmap=cmap)
cb = plt.colorbar(im,ax=ax,fraction=0.01,pad=0.04)
cb.set_ticks((-1,0,1))
cb.set_ticklabels(('4','other','5'))
for i,m in enumerate(np.argsort(sessionsToPass)):
    ax.plot([sessionsToPass[m]-0.5]*2,[i-0.4,i+0.4],'k')
ax.set_xticks(np.arange(10,sessionClustAlt.shape[1],10)-1)
ax.set_xticklabels(np.arange(10,sessionClustAlt.shape[1],10))
ax.set_yticks([])
ax.set_xlabel('Session')
ax.set_ylabel('Mouse')
ax.set_title('Session cluster\n(black line = passed learning criteria)')
plt.tight_layout() 


# fraction clust 4 vis first or clust 5 aud first or vice versa
probPoorAudSuppress = []
probPoorVisSuppress = []
for m in range(len(sessionsToPass)):
    mi = clustData['mouse'] == m
    p.append([])
    for firstRewStim in ('vis1','sound1'):
        poorAud = mi & (((clustId==4) & (clustData['firstRewardStim']=='vis1')) | ((clustId==5) & (clustData['firstRewardStim']=='sound1')))
        poorVis = mi & (((clustId==4) & (clustData['firstRewardStim']=='sound1')) | ((clustId==5) & (clustData['firstRewardStim']=='vis1')))
        probPoorAudSuppress.append(np.sum(poorAud)/mi.sum())
        probPoorVisSuppress.append(np.sum(poorVis)/mi.sum())
    
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1,1,1)
alim = [-0.05,0.75]
ax.plot(alim,alim,'--',color='k')
ax.plot(probPoorVisSuppress,probPoorAudSuppress,'ko',alpha=0.25)
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out')
ax.set_xlim(alim)
ax.set_ylim(alim)
ax.set_aspect('equal')
ax.set_xlabel('Weak suppression of responses to visual target (fraction of sessions\ncluster 4 aud rewarded first or cluster 5 vis rewarded first)')
ax.set_ylabel('Weak suppression of responses to auditory target (fraction of sessions\ncluster 4 vis rewarded first or cluster 5 aud rewarded first)')
plt.tight_layout()
        

prevClustProb = np.zeros((3,3,len(clustLabels),len(clustLabels)))
prevClustChance = np.zeros((3,3,nClust))
nextClustProb = prevClustProb.copy()
nextClustChance = prevClustChance.copy()
for l,si in enumerate((np.ones(clustData['firstRewardStim'].size,dtype=bool),clustData['firstRewardStim']=='vis1',clustData['firstRewardStim']=='sound1')):
    for k,ind in enumerate((clustData['session']<5,(clustData['session']>=5) & ~clustData['passed'],clustData['passed'])):
        sessions = np.where(ind & si & (clustData['session']>0))[0]
        for j,clust in enumerate(clustLabels):
            prevClustChance[l,k,j] = np.sum(clustId[sessions-1]==clust)/len(sessions)
            c = clustId[sessions]==clust
            for i,prevClust in enumerate(clustLabels):
                prevClustProb[l,k,i,j] = np.sum(clustId[sessions-1][c]==prevClust)/c.sum()
    
        sessions = np.where(ind & si & (clustData['session']+1<clustData['nSessions']))[0]
        for j,clust in enumerate(clustLabels):
            nextClustChance[l,k,j] = np.sum(clustId[sessions+1]==clust)/len(sessions)
            c = clustId[sessions]==clust
            for i,nextClust in enumerate(clustLabels):
                nextClustProb[l,k,i,j] = np.sum(clustId[sessions+1][c]==nextClust)/c.sum()

for l,blockType in enumerate(('all','vis rewarded first','aud rewarded first')):
    for k,stage in enumerate(('intitial training','later training','after learning')):
        for transProb,lbl in zip((prevClustProb[l,k],nextClustProb[l,k]),('Previous','Next')):
            fig = plt.figure()
            ax = fig.add_subplot(1,1,1) 
            im = ax.imshow(transProb,cmap='magma',clim=(0,transProb.max()),origin='lower')
            cb = plt.colorbar(im,ax=ax,fraction=0.026,pad=0.04)
            ax.set_xticks(np.arange(len(clustLabels)))
            ax.set_yticks(np.arange(len(clustLabels)))
            ax.set_xticklabels(clustLabels)
            ax.set_yticklabels(clustLabels)
            ax.set_xlabel('Session cluster')
            ax.set_ylabel(lbl+' session cluster')
            ax.set_title('Probability'+'\n'+stage+', '+blockType)
            plt.tight_layout()

for k in range(3):
    for transProb,chanceProb,lbl in zip((prevClustProb[k],nextClustProb[k]),(prevClustChance[k],nextClustChance[k]),('Previous','Next')):
        for diff in ('Absolute',):#'Relative'):
            fig = plt.figure()
            ax = fig.add_subplot(1,1,1)
            a = transProb-chanceProb[:,None]
            if diff=='Relative':
                a /= chanceProb[:,None]
            amax = np.absolute(a).max()
            im = ax.imshow(a,clim=(-amax,amax),cmap='bwr',origin='lower')
            cb = plt.colorbar(im,ax=ax,fraction=0.026,pad=0.04)
            ax.set_xticks(np.arange(len(clustLabels)))
            ax.set_yticks(np.arange(len(clustLabels)))
            ax.set_xticklabels(clustLabels)
            ax.set_yticklabels(clustLabels)
            ax.set_xlabel('Session cluster')
            ax.set_ylabel(lbl+' session cluster')
            ax.set_title(diff+' difference from chance probability')
            plt.tight_layout()


            
# cluster block performance
stimNames = ('vis1','vis2','sound1','sound2')
clustData = {key: [] for key in ('nSessions','mouseId','sessionStartTime','mouse','session','passed','block','rewardStim','nBlockTrials','hitRate','falseAlarmOtherModalGo','clustData')}
clustData['response'] = {stim: [] for stim in stimNames}
clustData['smoothedResponse'] = {stim: [] for stim in stimNames}
clustData['responseTime'] = {stim: [] for stim in stimNames}
clustData['responseTimeNorm'] = {stim: [] for stim in stimNames}
smoothSigma = 4
tintp = np.arange(600)
nMice = len(sessionData)
nExps = [len(s) for s in sessionData]
for m,(exps,s) in enumerate(zip(sessionData,sessionsToPass)):
    #exps = exps[s:] # exps[:s+nSessions]
    clustData['nSessions'].append(len(exps))
    for i,obj in enumerate(exps):
        for blockInd,rewardStim in enumerate(obj.blockStimRewarded):
            clustData['mouseId'].append(obj.subjectName)
            clustData['sessionStartTime'].append(obj.startTime)
            clustData['mouse'].append(m)
            clustData['session'].append(i)
            clustData['passed'].append(s-2<i)
            clustData['block'].append(blockInd)
            clustData['rewardStim'].append(rewardStim)
            blockTrials = obj.trialBlock==blockInd+1
            clustData['nBlockTrials'].append(blockTrials.sum())
            clustData['hitRate'].append(obj.hitRate[blockInd])
            clustData['falseAlarmOtherModalGo'].append(obj.falseAlarmOtherModalGo[blockInd])
            for stim in stimNames:
                stimTrials = (obj.trialStim==stim) & ~obj.autoRewardScheduled
                trials = blockTrials & stimTrials
                if trials.sum() > 0:
                    clustData['response'][stim].append(obj.trialResponse[trials])
                    clustData['responseTime'][stim].append(obj.responseTimes[trials])
                    clustData['responseTimeNorm'][stim].append(obj.responseTimes[trials]-np.nanmean(obj.responseTimes[stimTrials]))
                    
                    stimTime = obj.stimStartTimes[trials] - obj.trialStartTimes[trials][0]
                    r = scipy.ndimage.gaussian_filter(obj.trialResponse[trials].astype(float),smoothSigma)
                    r = np.interp(tintp,stimTime,r)
                    clustData['smoothedResponse'][stim].append(r)
                else:
                    clustData['response'][stim].append(np.array([]))
                    clustData['smoothedResponse'][stim].append(np.full(tintp.size,np.nan))
                    clustData['responseTime'][stim].append(np.array([]))
                    clustData['responseTimeNorm'][stim].append(np.array([]))
                   
            # sn = stimNames[:4] if rewardStim=='vis1' else stimNames[2:4]+stimNames[:2]
            sn = ('vis1','sound1') if rewardStim=='vis1' else ('sound1','vis1')
            clustData['clustData'].append(np.concatenate([clustData['smoothedResponse'][stim][-1] for stim in sn]))

for key in clustData:
    if isinstance(clustData[key],dict):
        for k in clustData[key]:
            if max(len(d) for d in clustData[key][k]) != len(clustData[key][k][0]):
                clustData[key][k] = np.array(clustData[key][k],dtype='O')
            else:
                clustData[key][k] = np.array(clustData[key][k])
    else:
        clustData[key] = np.array(clustData[key])


# clustId,linkageMat = cluster(clustData['clustData'],nClusters=nClust)

pcaData,eigVal,eigVec = pca(clustData['clustData'])

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(np.arange(1,eigVal.size+1),eigVal.cumsum()/eigVal.sum(),'k')
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False)
ax.set_xlim([0,10])
ax.set_ylim((0,1.02))
ax.set_xlabel('PC')
ax.set_ylabel('Cumulative Fraction of Variance Explained')
plt.tight_layout()

nPC = np.where((np.cumsum(eigVal)/eigVal.sum())>0.99)[0][0]+1
clustColors = [clr for clr in 'rgkbmcy']+['0.6']
nClust = 6
clustId,linkageMat = cluster(pcaData[:,:nPC],nClusters=nClust)
clustLabels = np.unique(clustId)

newClustOrder = [2,4,1,5,3,6]
newClustId = clustId.copy()
for i,c in enumerate(newClustOrder):
    newClustId[clustId==c] = i+1
clustId = newClustId

clustData['clustId'] = clustId
clustData['trialCluster'] = {}
for m in np.unique(clustData['mouseId']):
    clustData['trialCluster'][m] = {}
    mi = clustData['mouseId']==m
    for s in np.unique(clustData['sessionStartTime'][mi]):
        clustData['trialCluster'][m][s] = []
        si = clustData['sessionStartTime']==s
        for n,c in zip(clustData['nBlockTrials'][mi & si],clustId[mi & si]):
            clustData['trialCluster'][m][s].extend(np.zeros(n)+c)
        clustData['trialCluster'][m][s] = np.array(clustData['trialCluster'][m][s])
            
#np.save(os.path.join(baseDir,'Sam','clustData.npy'),clustData)


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
colorThresh = 0 if nClust<2 else linkageMat[::-1,2][nClust-2]
scipy.cluster.hierarchy.set_link_color_palette(list(clustColors))
scipy.cluster.hierarchy.dendrogram(linkageMat,ax=ax,truncate_mode=None,p=7,color_threshold=colorThresh,above_threshold_color='k',labels=None,no_labels=True)
scipy.cluster.hierarchy.set_link_color_palette(None)
ax.plot([0,1000000],[0.85*colorThresh]*2,'k--')
ax.set_yticks([])
for side in ('right','top','left','bottom'):
    ax.spines[side].set_visible(False)
plt.tight_layout()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
colorThresh = 0 if nClust<2 else linkageMat[::-1,2][nClust-2]
scipy.cluster.hierarchy.set_link_color_palette(list(clustColors))
scipy.cluster.hierarchy.dendrogram(linkageMat,ax=ax,truncate_mode=None,p=7,color_threshold=colorThresh,above_threshold_color='k',labels=None,no_labels=False)
scipy.cluster.hierarchy.set_link_color_palette(None)
ax.plot([0,1000000],[0.85*colorThresh]*2,'k--')
ax.set_yticks([])
for side in ('right','top','left','bottom'):
    ax.spines[side].set_visible(False)
plt.tight_layout()
    
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
k = np.arange(linkageMat.shape[0])+2
ax.plot(k,linkageMat[::-1,2],'ko-',mfc='none',ms=10,mew=2,linewidth=2)
ax.plot([0,100],[0.85*colorThresh]*2,'k--')
ax.set_xlim([0,30.4])
ax.set_xlabel('Cluster')
ax.set_ylabel('Linkage Distance')
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False)
plt.tight_layout()
    

stimNames = ('vis1','vis2','sound1','sound2')
postTrials = 15
x = np.arange(postTrials)+1
for clust in clustLabels:
    for rewardStim,blockLabel in zip(('vis1','sound1'),('visual rewarded blocks','auditory rewarded blocks')):
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        for stim,clr,ls in zip(stimNames,'ggmm',('-','--','-','--')):
            resp = []
            for r in clustData['response'][stim][(clustData['rewardStim']==rewardStim) & (clustId==clust)]:
                j = min(postTrials,r.size)
                resp.append(np.full(postTrials,np.nan))
                resp[-1][:j] = r[:j]
            m = np.nanmean(resp,axis=0)
            s = np.nanstd(resp)/(len(resp)**0.5)
            ax.plot(x,m,color=clr,ls=ls,label=stim)
            ax.fill_between(x,m+s,m-s,color=clr,alpha=0.25)
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False)
        ax.set_xlim([0.5,postTrials+0.5])
        ax.set_ylim([0,1.01])
        ax.set_xlabel('Trials after block switch cue trials')
        ax.set_ylabel('Response rate')
        if clust==1:
            ax.legend(loc='upper right')
        ax.set_title('Cluster '+str(clust)+', '+blockLabel+' (n='+str(len(resp))+')')
        plt.tight_layout()
        
for clust in clustLabels:
    for rewardStim,blockLabel in zip(('vis1','sound1'),('visual rewarded blocks','sound rewarded blocks')):
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        for stim,clr in zip(('vis1','sound1'),'gm'):
            resp = []
            for r in clustData['responseTimeNorm'][stim][(clustData['rewardStim']==rewardStim) & (clustId==clust)]:
                j = min(postTrials,r.size)
                resp.append(np.full(postTrials,np.nan))
                resp[-1][:j] = r[:j]
            m = np.nanmean(resp,axis=0)
            s = np.nanstd(resp)/(len(resp)**0.5)
            ax.plot(x,m,color=clr,label=stim)
            ax.fill_between(x,m+s,m-s,color=clr,alpha=0.25)
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False)
        ax.set_xlim([0.5,postTrials+0.5])
        ax.set_ylim([-0.1,0.15])
        ax.set_xlabel('Trials after block switch cue trials')
        ax.set_ylabel('Response time (diff. from mean)')
        ax.legend(loc='lower right')
        ax.set_title('Cluster '+str(clust)+', '+blockLabel+' (n='+str(len(resp))+')')
        plt.tight_layout()
        
        
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
for rewStim,offset,clr in zip(('vis1','sound1'),(-0.2,0.2),'gm'):
    i = clustData['rewardStim']==rewStim
    for clust in clustLabels:
        n = np.sum(i & (clustId==clust))
        lbl = ('visual rewarded' if rewStim=='vis1' else 'auditory rewarded') if clust==1 else None
        ax.bar(clust+offset,n,width=0.4,color=clr,label=lbl)
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out')
ax.set_xticks(clustLabels)
ax.set_xticklabels(clustLabels)
# ax.set_ylim((0,0.7))
ax.set_xlabel('Cluster')
ax.set_ylabel('Number of blocks')
ax.legend()
plt.tight_layout()


for k,ind in enumerate((clustData['session']<5,(clustData['session']>=5) & ~clustData['passed'],clustData['passed'])):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    for rewStim,offset,clr in zip(('vis1','sound1'),(-0.2,0.2),'gm'):
        i = ind & (clustData['rewardStim']==rewStim)
        for clust in clustLabels:
            p = np.sum(i & (clustId==clust)) / i.sum()
            lbl = ('visual rewarded' if rewStim=='vis1' else 'auditory rewarded') if clust==1 else None
            ax.bar(clust+offset,p,width=0.4,color=clr,label=lbl)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out')
    ax.set_xticks(clustLabels)
    ax.set_xticklabels(clustLabels)
    ax.set_ylim((0,0.7))
    ax.set_xlabel('Cluster')
    ax.set_ylabel('Fraction of blocks')
    ax.legend()
    plt.tight_layout()


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
for c,clr in zip(clustLabels,clustColors):
    i = clustId==c
    ax.plot(clustData['hitRate'][i],clustData['falseAlarmOtherModalGo'][i],'o',mec=clr,mfc='none',alpha=0.5,label='cluster '+str(c))
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out')
ax.set_xlim([-0.05,1.05])
ax.set_ylim([-0.05,1.05])
ax.set_aspect('equal')
ax.set_xlabel('Rewarded target response rate')
ax.set_ylabel('Non-rewarded target response rate')
ax.legend(bbox_to_anchor=(1,1),loc='upper left')
plt.tight_layout()
        

blockClustProb = np.zeros((3,6,nClust))
for k,ind in enumerate((clustData['session']<5,(clustData['session']>=5) & ~clustData['passed'],clustData['passed'])):
    for i in range(6):
        blocks = ind & (clustData['block']==i)
        for j,clust in enumerate(clustLabels):
            blockClustProb[k,i,j] = np.sum(blocks & (clustId==clust))/blocks.sum()


for i,(p,lbl) in enumerate(zip(blockClustProb,('intitial training','later training','after learning'))):    
    fig = plt.figure() 
    ax = fig.add_subplot(1,1,1) 
    im = ax.imshow(p,cmap='magma',clim=(0,blockClustProb.max()),origin='lower')
    cb = plt.colorbar(im,ax=ax,fraction=0.026,pad=0.04)
    for side in ('right','top','left','bottom'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',labelsize=12)
    ax.set_xticks(np.arange(nClust))
    ax.set_yticks(np.arange(6))
    ax.set_xticklabels(clustLabels)
    ax.set_xlabel('Cluster',fontsize=14)
    ax.set_yticklabels(np.arange(6)+1)
    ax.set_ylabel('Block',fontsize=14)
    ax.set_title('Cluster probability, '+lbl,fontsize=14)
    plt.tight_layout()
    
    
sessionClustProb = np.zeros((3,nClust,nClust))
for k,ind in enumerate((clustData['session']<5,(clustData['session']>=5) & ~clustData['passed'],clustData['passed'])):
    for i,sc in enumerate(clustLabels):
        for j,clust in enumerate(clustLabels):
            c = ind & (clustId==clust)
            b = 0
            bc = 0
            for m,s in zip(clustData['mouse'][c],clustData['session'][c]):
                b += 1
                if clustIdSessions[(clustDataSessions['mouse']==m) & (clustDataSessions['session']==s)] == sc:
                    bc += 1
            clustData['session']
            sessionClustProb[k,i,j] = bc / b

fig = plt.figure()
fig.suptitle('Cluster probability')
for i,(p,lbl) in enumerate(zip(sessionClustProb,('intitial training','later training','after learning'))):            
    ax = fig.add_subplot(1,3,i+1) 
    im = ax.imshow(p,cmap='magma',clim=(0,mouseClustProb.max()),origin='lower')
    cb = plt.colorbar(im,ax=ax,fraction=0.026,pad=0.04)
    ax.set_xticks(np.arange(nClust))
    ax.set_xticklabels(np.arange(nClust)+1)
    ax.set_yticks(np.arange(nClust))
    ax.set_yticklabels(np.arange(nClust)+1)
    if i==1:
        ax.set_xlabel('Block cluster')
    if i==0:
        ax.set_ylabel('Session cluster')
    ax.set_title(lbl)
    plt.tight_layout()


mouseClustProb = np.zeros((3,nMice,nClust))
for k,ind in enumerate((clustData['session']<5,(clustData['session']>=5) & ~clustData['passed'],clustData['passed'])):
    for i,m in enumerate(np.argsort(sessionsToPass)):
        for j,clust in enumerate(clustLabels):
            b = clustId[(clustData['mouse']==m) & ind]
            mouseClustProb[k,i,j] = np.sum(b==clust)/b.size

fig = plt.figure(figsize=(10,8))
fig.suptitle('Cluster probability')
for i,(p,lbl) in enumerate(zip(mouseClustProb,('intitial training','later training','after learning'))):            
    ax = fig.add_subplot(1,3,i+1) 
    im = ax.imshow(p,cmap='magma',clim=(0,np.nanmax(mouseClustProb)))
    cb = plt.colorbar(im,ax=ax,fraction=0.026,pad=0.04)
    ax.set_xticks(np.arange(nClust))
    ax.set_xticklabels(np.arange(nClust)+1)
    ax.set_yticks([])
    if i==1:
        ax.set_xlabel('Cluster')
    if i==0:
        ax.set_ylabel('Mouse')
    ax.set_title(lbl)
    plt.tight_layout()
    
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
p = mouseClustProb[-1]
for clust,clr in enumerate(clustColors[:nClust]):
    dsort = np.sort(p[:,clust])
    cumProb = np.array([np.sum(dsort<=i)/dsort.size for i in dsort])
    ax.plot(dsort,cumProb,color=clr,label='cluster '+str(clust+1))
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False,labelsize=14)
ax.set_xlim([0,0.8])
ax.set_ylim([0,1.01])
ax.set_xlabel('Fraction of blocks in each cluster after learning',fontsize=16)
ax.set_ylabel('Cumalative fraction of mice',fontsize=16)
ax.legend()
plt.tight_layout()
    

fig = plt.figure(figsize=(4.5,10))
fig.suptitle('Within session cluster probability for each mouse\n(white line = passed learning criteria)')
for i,m in enumerate(np.argsort(sessionsToPass)):
    ax = fig.add_subplot(nMice,1,i+1)
    mi = clustData['mouse']==m
    p = np.full((nClust,clustData['nSessions'][m]),np.nan)
    for s in range(clustData['nSessions'][m]):
        si = clustData['session']==s
        assert(np.sum(mi & si)==6)
        for j,c in enumerate(clustLabels):
            p[j,s] = np.sum(clustId[mi & si] == c) / 6
    im = ax.imshow(p,cmap='magma',clim=(0,1),interpolation='none')
    ax.plot([sessionsToPass[m]-0.5]*2,[-0.5,6.5],'w')
    for side in ('right','top','left','bottom'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',labelsize=10)
    ax.set_xticks([])
    if i==0:
        ax.set_yticks([0,nClust-1])
        ax.set_yticklabels([1,nClust])
        ax.set_ylabel('Cluster',fontsize=12)
        cb = plt.colorbar(im,ax=ax)
    else:
        ax.set_yticks([])
    if i==nMice-1:
        ax.set_xlabel('Session',fontsize=12)
    ax.set_anchor('W')
plt.tight_layout()


mostFreqClust = np.full((nMice,max(clustData['nSessions'])),np.nan)
for i,m in enumerate(np.argsort(sessionsToPass)):
    mi = clustData['mouse']==m
    for s in range(clustData['nSessions'][m]):
        si = clustData['session']==s
        c,n = np.unique(clustId[mi & si],return_counts=True)
        mostFreqClust[i,s] = c[np.argmax(n)]
        
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
cmap = matplotlib.cm.viridis.copy()
cmap.set_bad(color=[0.5]*3)
im = ax.imshow(mostFreqClust,cmap=cmap)
cb = plt.colorbar(im,ax=ax,fraction=0.01,pad=0.04)
cb.set_ticks(np.arange(nClust)+1)
for i,m in enumerate(np.argsort(sessionsToPass)):
    ax.plot([sessionsToPass[m]-0.5]*2,[i-0.4,i+0.4],'w')
ax.set_xticks(np.arange(10,70,10)-1)
ax.set_xticklabels(np.arange(10,70,10))
ax.set_yticks([])
ax.set_xlabel('Session')
ax.set_ylabel('Mouse')
ax.set_title('Most frequent cluster in session\n(white line = passed learning criteria)')
plt.tight_layout()


numDiffClust = np.full((nMice,max(clustData['nSessions'])),np.nan)
for i,m in enumerate(np.argsort(sessionsToPass)):
    mi = clustData['mouse']==m
    for s in range(clustData['nSessions'][m]):
        si = clustData['session']==s
        np.unique(clustId[mi & si])
        numDiffClust[i,s] = np.unique(clustId[mi & si]).size
        
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
cmap = matplotlib.cm.plasma.copy()
cmap.set_bad(color=[0.5]*3)
im = ax.imshow(numDiffClust,cmap=cmap)
cb = plt.colorbar(im,ax=ax,fraction=0.01,pad=0.04)
cb.set_ticks(np.arange(nClust)+1)
for i,m in enumerate(np.argsort(sessionsToPass)):
    ax.plot([sessionsToPass[m]-0.5]*2,[i-0.4,i+0.4],'w')
ax.set_xticks(np.arange(10,70,10)-1)
ax.set_xticklabels(np.arange(10,70,10))
ax.set_yticks([])
ax.set_xlabel('Session')
ax.set_ylabel('Mouse')
ax.set_title('Number of different clusters in session\n(white line = passed learning criteria)')
plt.tight_layout()


for k,ind in enumerate((clustData['session']<5,(clustData['session']>=5) & ~clustData['passed'],clustData['passed'])):
    chanceProb = np.array([np.sum(ind & (clustId==clust))/np.sum(ind) for clust in clustLabels])
    for lbl in ('Absolute','Relative'):
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        a = blockClustProb[k]-chanceProb
        if lbl=='Relative':
            a /= chanceProb
        amax = np.absolute(a).max()
        im = ax.imshow(a,clim=(-amax,amax),cmap='bwr',origin='lower')
        cb = plt.colorbar(im,ax=ax,fraction=0.026,pad=0.04)
        ax.set_xticks(np.arange(nClust))
        ax.set_yticks(np.arange(6))
        ax.set_xticklabels(clustLabels)
        ax.set_yticklabels(np.arange(6)+1)
        ax.set_xlabel('Cluster')
        ax.set_ylabel('Block')
        ax.set_title(lbl+' difference from chance probability')
        plt.tight_layout()
        

prevClustProb = np.zeros((3,len(clustLabels),len(clustLabels)))
prevClustChance = np.zeros((3,nClust))
nextClustProb = prevClustProb.copy()
nextClustChance = prevClustChance.copy()
for k,ind in enumerate((clustData['session']<5,(clustData['session']>=5) & ~clustData['passed'],clustData['passed'])):
    blocks = np.where(ind & (clustData['block']>0))[0]
    for j,clust in enumerate(clustLabels):
        prevClustChance[k,j] = np.sum(clustId[blocks-1]==clust)/len(blocks)
        c = clustId[blocks]==clust
        for i,prevClust in enumerate(clustLabels):
            prevClustProb[k,i,j] = np.sum(clustId[blocks-1][c]==prevClust)/c.sum()

    blocks = np.where(ind & (clustData['block']<5))[0]
    for j,clust in enumerate(clustLabels):
        nextClustChance[k,j] = np.sum(clustId[blocks+1]==clust)/len(blocks)
        c = clustId[blocks]==clust
        for i,nextClust in enumerate(clustLabels):
            nextClustProb[k,i,j] = np.sum(clustId[blocks+1][c]==nextClust)/c.sum()

for k in range(3):
    for transProb,lbl in zip((prevClustProb[k],nextClustProb[k]),('Previous','Next')):
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1) 
        im = ax.imshow(transProb,cmap='magma',clim=(0,transProb.max()),origin='lower')
        cb = plt.colorbar(im,ax=ax,fraction=0.026,pad=0.04)
        ax.set_xticks(np.arange(len(clustLabels)))
        ax.set_yticks(np.arange(len(clustLabels)))
        ax.set_xticklabels(clustLabels)
        ax.set_yticklabels(clustLabels)
        ax.set_xlabel('Current block cluster')
        ax.set_ylabel(lbl+' block cluster')
        ax.set_title('Probability')
        plt.tight_layout()

for k in range(3):
    for transProb,chanceProb,lbl in zip((prevClustProb[k],nextClustProb[k]),(prevClustChance[k],nextClustChance[k]),('Previous','Next')):
        for diff in ('Absolute','Relative'):
            fig = plt.figure()
            ax = fig.add_subplot(1,1,1)
            a = transProb-chanceProb[:,None]
            if diff=='Relative':
                a /= chanceProb[:,None]
            amax = np.absolute(a).max()
            im = ax.imshow(a,clim=(-amax,amax),cmap='bwr',origin='lower')
            cb = plt.colorbar(im,ax=ax,fraction=0.026,pad=0.04)
            ax.set_xticks(np.arange(len(clustLabels)))
            ax.set_yticks(np.arange(len(clustLabels)))
            ax.set_xticklabels(clustLabels)
            ax.set_yticklabels(clustLabels)
            ax.set_xlabel('Current block cluster')
            ax.set_ylabel(lbl+' block cluster')
            ax.set_title(diff+' difference from chance probability')
            plt.tight_layout()
            
# intra-block resp rate correlations for clusters
trainingPhases = ('initial training','after learning','all')
stimNames = ('vis1','sound1','vis2','sound2')
stimLabels = ('rewarded target','unrewarded target','non-target\n(rewarded modality)','non-target\n(unrewarded modality)')
nShuffles = 10
startTrial = 5
autoCorr = {phase: {clust: [[[] for _  in range(len(sessionData))] for _ in range(4)] for clust in clustLabels} for phase in trainingPhases}
corrWithin = {phase: {clust: [[[[] for _  in range(len(sessionData))] for _ in range(4)] for _ in range(4)] for clust in clustLabels} for phase in trainingPhases}
corrWithinDetrend = copy.deepcopy(corrWithin)
corrAcross = copy.deepcopy(corrWithin)
autoCorrMat = {phase: {clust: np.zeros((4,len(sessionData),100)) for clust in clustLabels} for phase in trainingPhases}
corrWithinMat = {phase: {clust: np.zeros((4,4,len(sessionData),200)) for clust in clustLabels} for phase in trainingPhases}
corrWithinDetrendMat = copy.deepcopy(corrWithinMat)
corrAcrossMat = copy.deepcopy(corrWithinMat)

for phase in trainingPhases:    
    for clust in clustLabels:
        for m,(exps,sp) in enumerate(zip(sessionData,sessionsToPass)):
            if phase=='initial training':
                exps = exps[:5]
            elif phase=='after learning':
                exps = exps[sp:]
            for obj in exps:
                trialCluster = clustData['trialCluster'][obj.subjectName][obj.startTime]
                if clust not in trialCluster:
                    continue
                
                resp = np.zeros((4,obj.nTrials))
                respShuffled = np.zeros((4,obj.nTrials,nShuffles))
                for blockInd in range(6):
                    blockTrials = np.where(obj.trialBlock==blockInd+1)[0][startTrial:]
                    for i,s in enumerate(stimNames):
                        stimTrials = np.intersect1d(blockTrials,np.where(obj.trialStim==s)[0])
                        r = obj.trialResponse[stimTrials].astype(float)
                        r[r<1] = -1
                        resp[i,stimTrials] = r
                        for z in range(nShuffles):
                            respShuffled[i,stimTrials,z] = np.random.permutation(r)
                
                for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                    blockTrials = np.where(obj.trialBlock==blockInd+1)[0][startTrial:]
                    if not np.all(trialCluster[blockTrials]==clust):
                        continue
                    for i,s in enumerate(stimNames if rewStim=='vis1' else ('sound1','vis1','sound2','vis2')):
                        stimTrials = np.intersect1d(blockTrials,np.where(obj.trialStim==s)[0])
                        if len(stimTrials) < 1:
                            continue
                        r = obj.trialResponse[stimTrials].astype(float)
                        c = np.correlate(r,r,'full')
                        norm = np.linalg.norm(r)**2
                        cc = []
                        for _ in range(nShuffles):
                            rs = np.random.permutation(r)
                            cs = np.correlate(rs,rs,'full')
                            cc.append(c - cs)
                            cc[-1] /= norm
                        n = c.size // 2 + 1
                        a = np.full(100,np.nan)
                        a[:n] = np.mean(cc,axis=0)[-n:]
                        autoCorr[phase][clust][i][m].append(a)
                    
                    r = resp[:,blockTrials]
                    mean = r.mean(axis=1)
                    r = r - mean[:,None]
                    rs = respShuffled[:,blockTrials] - mean[:,None,None]
                    if rewStim == 'sound1':
                        r = r[[1,0,3,2]]
                        rs = rs[[1,0,3,2]]
                    for i,(r1,rs1) in enumerate(zip(r,rs)):
                        for j,(r2,rs2) in enumerate(zip(r,rs)):
                            c = np.correlate(r1,r2,'full')
                            norm = np.linalg.norm(r1) * np.linalg.norm(r2)
                            cc = []
                            for z in range(nShuffles):
                                cs = np.correlate(rs1[:,z],rs2[:,z],'full')
                                cc.append(c - cs)
                                cc[-1] /= norm
                            n = c.size // 2 + 1
                            a = np.full(200,np.nan)
                            a[:n] = np.mean(cc,axis=0)[-n:]
                            corrWithin[phase][clust][i][j][m].append(a)
                            
                            x = np.arange(r1.size)
                            rd1,rd2 = [y - np.polyval(np.polyfit(x,y,2),x) for y in (r1,r2)]
                            c = np.correlate(rd1,rd2,'full')
                            norm = np.linalg.norm(rd1) * np.linalg.norm(rd2)
                            c /= norm
                            cc = []
                            for z in range(nShuffles):
                                rsd1,rsd2 = [y - np.polyval(np.polyfit(x,y,2),x) for y in (rs1[:,z],rs2[:,z])]
                                cs = np.correlate(rsd1,rsd2,'full')
                                norm = np.linalg.norm(rsd1) * np.linalg.norm(rsd2)
                                cs /= norm
                                cc.append(c - cs)
                            n = c.size // 2 + 1
                            a = np.full(200,np.nan)
                            a[:n] = np.mean(cc,axis=0)[-n:]
                            corrWithinDetrend[phase][clust][i][j][m].append(a)
                            
                    otherBlocks = [0,2,4] if blockInd in [0,2,4] else [1,3,5]
                    otherBlocks.remove(blockInd)
                    a = np.full((2,200),np.nan)
                    for k,b in enumerate(otherBlocks):
                        bTrials = np.where(obj.trialBlock==b+1)[0][startTrial:]
                        if not np.all(trialCluster[bTrials]==clust):
                            continue
                        rOther = resp[:,bTrials]
                        rsOther = respShuffled[:,bTrials]
                        if rewStim == 'sound1':
                            rOther = rOther[[1,0,3,2]]
                            rsOther = rsOther[[1,0,3,2]]
                        for i,(r1,rs1) in enumerate(zip(rOther,rsOther)):
                            for j,(r2,rs2) in enumerate(zip(r,rs)):
                                c = np.correlate(r1,r2,'full')
                                norm = np.linalg.norm(r1) * np.linalg.norm(r2)
                                cc = []
                                for z in range(nShuffles):
                                    cs = np.correlate(rs1[:,z],rs2[:,z],'full')
                                    cc.append(c - cs)
                                    cc[-1] /= norm
                                n = c.size // 2 + 1
                                a = np.full(200,np.nan)
                                a[:n] = np.mean(cc,axis=0)[-n:]
                                corrAcross[phase][clust][i][j][m].append(a)                          
                    
        for i in range(4):
            for m in range(len(sessionData)):
                autoCorrMat[phase][clust][i,m] = np.nanmean(autoCorr[phase][clust][i][m],axis=0)
                
        for i in range(4):
            for j in range(4):
                for m in range(len(sessionData)):
                    corrWithinMat[phase][clust][i,j,m] = np.nanmean(corrWithin[phase][clust][i][j][m],axis=0)
                    corrWithinDetrendMat[phase][clust][i,j,m] = np.nanmean(corrWithinDetrend[phase][clust][i][j][m],axis=0)
                    corrAcrossMat[phase][clust][i,j,m] = np.nanmean(corrAcross[phase][clust][i][j][m],axis=0)

for clust in clustLabels:
    fig = plt.figure(figsize=(8,8))          
    gs = matplotlib.gridspec.GridSpec(4,2)
    x = np.arange(200)
    for i,ylbl in enumerate(stimLabels):
        for j,xlbl in enumerate(stimLabels[:2]):
            ax = fig.add_subplot(gs[i,j])
            mat = corrWithinDetrendMat['all'][clust]
            m = np.nanmean(mat[i,j],axis=0)
            s = np.nanstd(mat[i,j],axis=0) / (len(mat[i,j]) ** 0.5)
            ax.plot(x,m,'k')
            ax.fill_between(x,m-s,m+s,color='k',alpha=0.25)
            for side in ('right','top'):
                ax.spines[side].set_visible(False)
            ax.tick_params(direction='out',top=False,right=False,labelsize=9)
            ax.set_xlim([-1,20])
            ax.set_ylim([-0.03,0.05])
            if i==3:
                ax.set_xlabel('Lag (trials)',fontsize=11)
            if j==0:
                ax.set_ylabel(ylbl,fontsize=11)
            if i==0:
                ax.set_title(xlbl,fontsize=11)
    plt.tight_layout()
    
for clust in clustLabels:
    fig = plt.figure(figsize=(8,8))          
    gs = matplotlib.gridspec.GridSpec(4,2)
    x = np.arange(200)
    for i,ylbl in enumerate(stimLabels):
        for j,xlbl in enumerate(stimLabels[:2]):
            ax = fig.add_subplot(gs[i,j])
            for phase,clr in zip(trainingPhases[:2],'mgk'):
                mat = corrWithinDetrendMat[phase][clust]
                m = np.nanmean(mat[i,j],axis=0)
                s = np.nanstd(mat[i,j],axis=0) / (len(mat[i,j]) ** 0.5)
                ax.plot(x,m,clr,label=phase)
                ax.fill_between(x,m-s,m+s,color=clr,alpha=0.25)
            for side in ('right','top'):
                ax.spines[side].set_visible(False)
            ax.tick_params(direction='out',top=False,right=False,labelsize=9)
            ax.set_xlim([-1,20])
            ax.set_ylim([-0.03,0.05])
            if i==3:
                ax.set_xlabel('Lag (trials)',fontsize=11)
            if j==0:
                ax.set_ylabel(ylbl,fontsize=11)
            if i==0:
                ax.set_title(xlbl,fontsize=11)
            if i==0 and j==1:
                ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=11)
    plt.tight_layout()

for clust in clustLabels:
    fig = plt.figure(figsize=(8,8))          
    gs = matplotlib.gridspec.GridSpec(4,2)
    x = np.arange(200) + 1
    for i,ylbl in enumerate(stimLabels):
        for j,xlbl in enumerate(stimLabels[:2]):
            ax = fig.add_subplot(gs[i,j])
            for mat,clr,lbl in zip((corrWithinMat,corrAcrossMat,corrWithinDetrendMat),'brk',('within block','across blocks','within block detrended')):
                mat = mat['all'][clust]
                m = np.nanmean(mat[i,j],axis=0)
                s = np.nanstd(mat[i,j],axis=0) / (len(mat[i,j]) ** 0.5)
                ax.plot(x,m,clr,alpha=0.5,label=lbl)
                ax.fill_between(x,m-s,m+s,color='k',alpha=0.25)
            for side in ('right','top'):
                ax.spines[side].set_visible(False)
            ax.tick_params(direction='out',top=False,right=False,labelsize=9)
            ax.set_xlim([0,30])
            ax.set_ylim([-0.05,0.1])
            if i==3:
                ax.set_xlabel('Lag (trials)',fontsize=11)
            if j==0:
                ax.set_ylabel(ylbl,fontsize=11)
            if i==0:
                ax.set_title(xlbl,fontsize=11)
            if i==0 and j==1:
                ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=11)
    plt.tight_layout()          


## nogo, noAR, rewardOnly, and catchOnly
mice = {'nogo': np.array(summaryDf[summaryDf['nogo']]['mouse id']),
        'noAR': np.array(summaryDf[summaryDf['noAR']]['mouse id']),
        'oneReward': np.array(summaryDf[summaryDf['oneReward']]['mouse id']),
        'rewardOnly': np.array(summaryDf[summaryDf['rewardOnly']]['mouse id']),
        'catchOnly': np.array(summaryDf[summaryDf['catchOnly']]['mouse id'])}

sessionDataVariants = {lbl: [] for lbl in mice}
isFirstExpType = {lbl: [] for lbl in mice}
for lbl,mouseIds in mice.items():
    for mid in mouseIds:
        df = drSheets[str(mid)] if str(mid) in drSheets else nsbSheets[str(mid)]
        sessions = np.array([lbl in task for task in df['task version']]) & ~np.array(df['ignore'].astype(bool))
        sessionDataVariants[lbl].append([getSessionData(mid,startTime) for startTime in df.loc[sessions,'start time']])
        for task in df['task version']:
            if 'stage 5' in task and any(key in task for key in mice):
                isFirstExpType[lbl].append(lbl in task)
                break

useFirstExpType = False
useFirstExp = False

# block transition intervals
blockTransitionIntervals = []
for lbl in ('rewardOnly','catchOnly'):
    for exps in sessionDataVariants[lbl]:
        for obj in exps:
            for b in range(5):
                blockTransitionIntervals.append(obj.trialStartTimes[obj.trialBlock==b+2][5] - obj.trialStartTimes[obj.trialBlock==b+1][-1])

print(np.min(blockTransitionIntervals),np.max(blockTransitionIntervals),np.median(blockTransitionIntervals),np.mean(blockTransitionIntervals))

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.hist(blockTransitionIntervals,bins=np.arange(20,100,5),color='k')
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False)
ax.set_xlabel('Time between trials at block transition (s)')
ax.set_ylabel('Count')
plt.tight_layout()
    
            
# block switch plot, all stimuli
stimNames = ('vis1','vis2','sound1','sound2')
stimLabels = ('visual target','visual non-target','auditory target','auditory non-target')
preTrials = 15
postTrials = 15
x = np.arange(-preTrials,postTrials+1) 
respRate = {'vis1': {}, 'sound1': {}}
for lbl in sessionDataVariants:
    for rewardStim,blockLabel in zip(('vis1','sound1'),('visual rewarded blocks','auditory rewarded blocks')):
        fig = plt.figure(figsize=(8,4.5))
        ax = fig.add_subplot(1,1,1)
        ax.plot([0,0],[0,1],'--',color='0.5')
        for stim,stimLbl,clr,ls in zip(stimNames,stimLabels,'ggmm',('-','--','-','--')):
            y = []
            for exps,isFirstType in zip(sessionDataVariants[lbl],isFirstExpType[lbl]):
                if len(exps)>0 and ((useFirstExpType and isFirstType) or not useFirstExpType):
                    if useFirstExp:
                        exps = [exps[0]]
                    y.append([])
                    for obj in exps:
                        for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                            if blockInd > 0 and rewStim==rewardStim:
                                trials = obj.trialStim==stim
                                y[-1].append(np.full(preTrials+postTrials+1,np.nan))
                                pre = obj.trialResponse[(obj.trialBlock==blockInd) & trials]
                                i = min(preTrials,pre.size)
                                y[-1][-1][preTrials-i:preTrials] = pre[-i:]
                                post = obj.trialResponse[(obj.trialBlock==blockInd+1) & trials]
                                i = min(postTrials,post.size)
                                y[-1][-1][preTrials+1:preTrials+1+i] = post[:i]
                    y[-1] = np.nanmean(y[-1],axis=0)
            if lbl=='nogo':
                respRate[rewardStim][stim] = y
            m = np.nanmean(y,axis=0)
            s = np.nanstd(y,axis=0)/(len(y)**0.5)
            ax.plot(x,m,color=clr,ls=ls,label=stimLbl)
            ax.fill_between(x,m+s,m-s,color=clr,alpha=0.25)
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False,labelsize=10)
        ax.set_xticks(np.arange(-20,20,5))
        ax.set_yticks([0,0.5,1])
        ax.set_xlim([-preTrials-0.5,postTrials+0.5])
        ax.set_ylim([0,1.01])
        ax.set_xlabel('Trials of indicated type after block switch',fontsize=12)
        ax.set_ylabel('Response Rate',fontsize=12)
        ax.legend(bbox_to_anchor=(1,1),fontsize=12)
        ax.set_title(lbl+' ('+str(len(mice[lbl]))+' mice)\n'+blockLabel,fontsize=12)
        plt.tight_layout()
        
#
inc = []
dec = []
for rewStim in ('vis1','sound1'):
    for stim in ('vis1','sound1'):
        r = np.array(respRate[rewStim][stim])
        pre = r[:,preTrials-1]
        if rewStim==stim:
            inc.append(r[:,preTrials+1]-pre)
        else:
            dec.append(r[:,preTrials+5]-pre)
            
audDiff = np.array(respRate['sound1']['sound1'])[:,postTrials+6:].mean(axis=1) - np.array(respRate['sound1']['sound2'])[:,postTrials+6:].mean(axis=1)

visDprime,audDprime = [[np.mean([np.array(obj.dprimeSameModal)[obj.blockStimRewarded==stim] for obj in exps]) for exps in sessionDataVariants['nogo']] for stim in ('vis1','sound1')]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
alim = (1,4)
ax.plot(alim,alim,'--',color='0.5')
ax.plot(audDprime,visDprime,'ko')
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False,labelsize=10)
ax.set_xlim(alim)
ax.set_ylim(alim)
ax.set_aspect('equal')
ax.set_xlabel('d\' auditory',fontsize=12)
ax.set_ylabel('d\' visual',fontsize=12)
plt.tight_layout()


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
alim = (-0.6,0.2)
ax.plot(alim,alim,'--',color='0.5')
ax.plot(dec[0],dec[1],'ko')
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False,labelsize=10)
ax.set_xlim(alim)
ax.set_ylim(alim)
ax.set_aspect('equal')
ax.set_xlabel(r'$\Delta$ response rate to previously rewarded'+'\nvisual target',fontsize=12)
ax.set_ylabel(r'$\Delta$ response rate to previously rewarded'+'\nauditory target',fontsize=12)
plt.tight_layout()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
alim = (0,0.8)
ax.plot(alim,alim,'--',color='0.5')
ax.plot(inc[0],inc[1],'ko')
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False,labelsize=10)
ax.set_xlim(alim)
ax.set_ylim(alim)
ax.set_aspect('equal')
ax.set_xlabel(r'$\Delta$ response rate to previously non-rewarded'+'\nvisual target',fontsize=12)
ax.set_ylabel(r'$\Delta$ response rate to previously non-rewarded'+'\nauditory target',fontsize=12)
plt.tight_layout()


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
x = audDprime
y = dec[0]
plt.plot(x,y,'ko')
slope,yint,rval,pval,stderr = scipy.stats.linregress(x,y)
xrng = np.array([min(x),max(x)])
plt.plot(xrng,slope*xrng+yint,'--',color='k')
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False,labelsize=10)
ax.set_xlim([1.5,3.5])
# ax.set_ylim([0,0.7])
ax.set_xlabel('d\' auditory',fontsize=12)
ax.set_ylabel(r'$\Delta$ response rate to previously rewarded'+'\nauditory target',fontsize=12)
ax.set_title('r = '+str(round(rval,2)))
plt.tight_layout()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
x = audDprime
y = inc[0]
plt.plot(x,y,'ko')
slope,yint,rval,pval,stderr = scipy.stats.linregress(x,y)
xrng = np.array([min(x),max(x)])
plt.plot(xrng,slope*xrng+yint,'--',color='k')
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False,labelsize=10)
ax.set_xlim([1.5,3.5])
# ax.set_ylim([0,0.7])
ax.set_xlabel('d\' auditory',fontsize=12)
ax.set_ylabel(r'$\Delta$ response rate to previously non-rewarded'+'\nvisual target',fontsize=12)
ax.set_title('r = '+str(round(rval,2)))
plt.tight_layout()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
x = audDprime
y = dec[1]
plt.plot(x,y,'ko')
slope,yint,rval,pval,stderr = scipy.stats.linregress(x,y)
xrng = np.array([min(x),max(x)])
plt.plot(xrng,slope*xrng+yint,'--',color='k')
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False,labelsize=10)
ax.set_xlim([1.5,3.5])
# ax.set_ylim([0,0.7])
ax.set_xlabel('d\' auditory',fontsize=12)
ax.set_ylabel(r'$\Delta$ response rate to previously rewarded'+'\nvisual target',fontsize=12)
ax.set_title('r = '+str(round(rval,2)))
plt.tight_layout()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
x = audDprime
y = inc[1]
plt.plot(x,y,'ko')
slope,yint,rval,pval,stderr = scipy.stats.linregress(x,y)
xrng = np.array([min(x),max(x)])
plt.plot(xrng,slope*xrng+yint,'--',color='k')
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False,labelsize=10)
ax.set_xlim([1.5,3.5])
# ax.set_ylim([0,0.7])
ax.set_xlabel('d\' auditory',fontsize=12)
ax.set_ylabel(r'$\Delta$ response rate to previously non-rewarded'+'\nauditory target',fontsize=12)
ax.set_title('r = '+str(round(rval,2)))
plt.tight_layout()
        

# response times
stimNames = ('vis1','sound1')
stimLabels = ('visual target','auditory target')
preTrials = 15
postTrials = 15
x = np.arange(-preTrials,postTrials+1)
for lbl in sessionDataVariants:
    for rewardStim,blockLabel in zip(('vis1','sound1'),('visual rewarded blocks','auditory rewarded blocks')):
        fig = plt.figure(figsize=(8,4.5))
        ax = fig.add_subplot(1,1,1)
        ax.plot([0,0],[-2,2],'--',color='0.5')
        for stim,stimLbl,clr,ls in zip(stimNames,stimLabels,'gm',('-','-')):
            y = []
            for exps,isFirstType in zip(sessionDataVariants[lbl],isFirstExpType[lbl]):
                if len(exps)>0 and ((useFirstExpType and isFirstType) or not useFirstExpType):
                    if useFirstExp:
                        exps = [exps[0]]
                    y.append([])
                    for obj in exps:
                        for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                            if blockInd > 0 and rewStim==rewardStim:
                                trials = (obj.trialStim==stim) & ~obj.autoRewardScheduled
                                r = (obj.responseTimes-np.nanmean(obj.responseTimes[trials]))/np.nanstd(obj.responseTimes[trials])
                                y[-1].append(np.full(preTrials+postTrials+1,np.nan))
                                pre = r[(obj.trialBlock==blockInd) & trials]
                                i = min(preTrials,pre.size)
                                y[-1][-1][preTrials-i:preTrials] = pre[-i:]
                                post = r[(obj.trialBlock==blockInd+1) & trials]
                                i = min(postTrials,post.size)
                                y[-1][-1][preTrials+1:preTrials+1+i] = post[:i]
                    y[-1] = np.nanmean(y[-1],axis=0)
            m = np.nanmean(y,axis=0)
            s = np.nanstd(y,axis=0)/(len(y)**0.5)
            ax.plot(x,m,color=clr,ls=ls,label=stimLbl)
            ax.fill_between(x,m+s,m-s,color=clr,alpha=0.25)
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False,labelsize=10)
        ax.set_xticks(np.arange(-20,20,5))
        ax.set_yticks([-1,-0.5,0,0.5,1]) # [-1,0,1]
        ax.set_xlim([-preTrials-0.5,postTrials+0.5])
        ax.set_ylim([-0.6,1]) # [-1.5,1.5]
        ax.set_xlabel('Trials of indicated type after block switch',fontsize=12)
        ax.set_ylabel('Response time (z score)',fontsize=12)
        ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=12)
        ax.set_title(lbl+' ('+str(len(mice[lbl]))+' mice)\n'+blockLabel,fontsize=12)
        plt.tight_layout()
            
# block switch plot, target stimuli only
for lbl,title in zip(('nogo','rewardOnly'),('block switch cued with non-rewarded target trials','block switch cued with reward only')):
    for getDeltaLickProb in (False,True):
        if lbl == 'nogo' or not getDeltaLickProb:
            fig = plt.figure(figsize=(8,4))
            ax = fig.add_subplot(1,1,1)
            preTrials = 5
            postTrials = 20
            x = np.arange(-preTrials,postTrials)    
            # ax.plot([0,0],[0,1],'--',color='0.5')
            ax.add_patch(matplotlib.patches.Rectangle([-0.5,0],width=5,height=1,facecolor='0.5',edgecolor=None,alpha=0.2,zorder=0))
            for stimLbl,clr in zip(('rewarded target stim','unrewarded target stim'),'gm'):
                y = []
                for exps,isFirstType in zip(sessionDataVariants[lbl],isFirstExpType[lbl]):
                    if len(exps)>0 and ((useFirstExpType and isFirstType) or not useFirstExpType):
                        if useFirstExp:
                            exps = [exps[0]]
                        y.append([])
                        for obj in exps:
                            for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                                if blockInd > 0:
                                    stim = np.setdiff1d(obj.blockStimRewarded,rewStim) if 'unrewarded' in stimLbl else rewStim
                                    trials = (obj.trialStim==stim)
                                    if getDeltaLickProb and stim != rewStim:
                                        blockTrials = (obj.trialBlock==blockInd+1)
                                        firstReward = np.where(blockTrials & (obj.trialStim==rewStim))[0][0]
                                        if np.where(blockTrials & trials)[0][obj.newBlockNogoTrials] > firstReward:
                                            continue
                                    y[-1].append(np.full(preTrials+postTrials,np.nan))
                                    pre = obj.trialResponse[(obj.trialBlock==blockInd) & trials]
                                    i = min(preTrials,pre.size)
                                    y[-1][-1][preTrials-i:preTrials] = pre[-i:]
                                    post = obj.trialResponse[(obj.trialBlock==blockInd+1) & trials]
                                    if lbl=='nogo' and stim!=rewStim:
                                        i = min(postTrials,post.size)
                                        y[-1][-1][preTrials:preTrials+i] = post[:i]
                                    else:
                                        i = min(postTrials-5,post.size)
                                        y[-1][-1][preTrials+5:preTrials+5+i] = post[:i]
                        y[-1] = np.nanmean(y[-1],axis=0)
                        if lbl=='nogo' and not getDeltaLickProb and stimLbl=='rewarded target stim':
                            rewTargResp = y
                m = np.nanmean(y,axis=0)
                s = np.nanstd(y,axis=0)/(len(y)**0.5)
                ax.plot(x[:preTrials],m[:preTrials],color=clr,label=stimLbl)
                ax.fill_between(x[:preTrials],(m+s)[:preTrials],(m-s)[:preTrials],color=clr,alpha=0.25)
                ax.plot(x[preTrials:],m[preTrials:],color=clr)
                ax.fill_between(x[preTrials:],(m+s)[preTrials:],(m-s)[preTrials:],color=clr,alpha=0.25)
                if getDeltaLickProb:
                    if stimLbl == 'rewarded target stim':
                        deltaLickProb['5 non-rewarded targets']['rewTarg'] = np.array(y)[:,[preTrials-1,preTrials+5]]
                    else:
                        deltaLickProb['5 non-rewarded targets']['nonRewTarg'] = np.array(y)[:,[preTrials-1,preTrials+5]]
                        deltaLickProb['1 non-rewarded target']['nonRewTarg'] = np.array(y)[:,[preTrials-1,preTrials+1]]
            for side in ('right','top'):
                ax.spines[side].set_visible(False)
            ax.tick_params(direction='out',top=False,right=False,labelsize=12)
            ax.set_xticks([-5,-1,5,9,14,19])
            ax.set_xticklabels([-5,-1,1,5,10,15])
            ax.set_yticks([0,0.5,1])
            ax.set_xlim([-preTrials-0.5,postTrials-0.5])
            ax.set_ylim([0,1.01])
            ax.set_xlabel('Trials of indicated type after block switch',fontsize=14)
            ax.set_ylabel('Response rate',fontsize=14)
            ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=14)
            # ax.set_title(title+' ('+str(len(y))+' mice)',fontsize=16)
            plt.tight_layout()

fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(1,1,1)
rr = np.array(rewTargResp)[:,[preTrials-1,preTrials+5]]
for r in rr:
    ax.plot([0,1],r,'o-',color='g',mec='g',mfc='none',ms=6,lw=1,alpha=0.2)
mean = np.nanmean(rr,axis=0)
sem = np.nanstd(rr,axis=0)/(len(rr)**0.5)
ax.plot([0,1],mean,'o-',color='g',mec='g',mfc='g',ms=10,lw=2)
# for x,m,s in zip([0,1],mean,sem):
#     ax.plot([x,x],[m-s,m+s],color='m',lw=2)
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False,labelsize=14)
ax.set_xticks([0,1])
ax.set_yticks([0,0.5,1])
ax.set_xticklabels(('last trial of\nprevious block','first trial of\nnew block'))
ax.set_ylabel('Response rate',fontsize=16)
ax.set_xlim([-0.2,1.2])
ax.set_ylim([0,1.01])
plt.tight_layout()

# block switch plot aligned to first reward
for lbl,title in zip(('nogo',),('block switch begins with non-rewarded target trials',)):
    fig = plt.figure(figsize=(8,4))
    ax = fig.add_subplot(1,1,1)
    preTrials = 5
    postTrials = 15
    x = np.arange(-preTrials,postTrials+1)    
    ax.plot([0,0],[0,1],'--',color='0.5')
    for stimLbl,clr in zip(('rewarded target stim','unrewarded target stim'),'gm'):
        y = []
        for exps,isFirstType in zip(sessionDataVariants[lbl],isFirstExpType[lbl]):
            if len(exps)>0 and ((useFirstExpType and isFirstType) or not useFirstExpType):
                if useFirstExp:
                    exps = [exps[0]]
                y.append([])
                for obj in exps:
                    for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                        if blockInd > 0:
                            stim = np.setdiff1d(obj.blockStimRewarded,rewStim) if 'unrewarded' in stimLbl else rewStim
                            stimTrials = np.where(obj.trialStim==stim)[0]
                            blockTrials = np.where(obj.trialBlock==blockInd+1)[0]
                            firstReward = blockTrials[obj.trialRewarded[blockTrials] & ~obj.catchTrials[blockTrials]][0]
                            lastPreTrial = np.where(stimTrials<firstReward)[0][-1]
                            y[-1].append(np.full(preTrials+postTrials+1,np.nan))
                            pre = obj.trialResponse[stimTrials[lastPreTrial-preTrials:lastPreTrial+1]]
                            i = min(preTrials,pre.size)
                            y[-1][-1][preTrials-i:preTrials] = pre[-i:]
                            firstPostTrial = np.where(stimTrials>firstReward)[0][0]
                            post = obj.trialResponse[stimTrials[firstPostTrial:max(firstPostTrial+postTrials,blockTrials[-1])]]
                            i = min(postTrials,post.size)
                            y[-1][-1][preTrials+1:preTrials+1+i] = post[:i]
                y[-1] = np.nanmean(y[-1],axis=0)
        m = np.nanmean(y,axis=0)
        s = np.nanstd(y,axis=0)/(len(y)**0.5)
        ax.plot(x,m,color=clr,label=stimLbl)
        ax.fill_between(x,m+s,m-s,color=clr,alpha=0.25)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=12)
    ax.set_xticks(np.arange(-20,21,5))
    ax.set_yticks([0,0.5,1])
    ax.set_xlim([-preTrials-0.5,postTrials+0.5])
    ax.set_ylim([0,1.01])
    ax.set_xlabel('Trials of indicated type after first rewarded trial',fontsize=14)
    ax.set_ylabel('Response rate',fontsize=14)
    ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=14)
    # ax.set_title(title+' ('+str(len(y))+' mice)',fontsize=14)
    plt.tight_layout()
    
# block switch plots by first target and response type
for lbl in ('noAR',):#('noAR','rewardOnly','catchOnly'):
    for firstTarget in ('rewarded','non-rewarded'):
        for firstTrialLick,lickLbl in zip((True,False),('lick','no lick')):
            for nTarg in range(1,3):
                fig = plt.figure(figsize=(8,4))
                ax = fig.add_subplot(1,1,1)
                preTrials = 5
                transTrials = 0 if lbl=='noAR' else 5
                postTrials = 16
                x = np.arange(-preTrials,transTrials+postTrials)    
                ax.add_patch(matplotlib.patches.Rectangle([-0.5,0],width=transTrials+nTarg,height=1,facecolor='0.5',edgecolor=None,alpha=0.2,zorder=0))
                for stimLbl,clr in zip(('rewarded target stim','unrewarded target stim'),'gm'):
                    n = 0
                    y = []
                    for exps,isFirstType in zip(sessionDataVariants[lbl],isFirstExpType[lbl]):
                        if len(exps)>0 and ((useFirstExpType and isFirstType) or not useFirstExpType):
                            if useFirstExp:
                                exps = [exps[0]]
                            y.append([])
                            for obj in exps:
                                for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                                    if blockInd > 0:
                                        nonRewStim = np.setdiff1d(obj.blockStimRewarded,rewStim)
                                        blockTrials = obj.trialBlock==blockInd+1
                                        rewStimTrials = np.where(blockTrials & (obj.trialStim==rewStim))[0]
                                        nonRewStimTrials = np.where(blockTrials & (obj.trialStim==nonRewStim))[0]
                                        if ((firstTarget=='rewarded' and rewStimTrials[nTarg-1] < nonRewStimTrials[0] < rewStimTrials[nTarg]) or
                                            (firstTarget=='non-rewarded' and nonRewStimTrials[nTarg-1] < rewStimTrials[0] < nonRewStimTrials[nTarg])):
                                            firstTargetTrial = rewStimTrials[:nTarg] if firstTarget=='rewarded' else nonRewStimTrials[:nTarg]
                                            if np.all(obj.trialResponse[firstTargetTrial] == firstTrialLick):
                                                stim = nonRewStim if 'unrewarded' in stimLbl else rewStim
                                                trials = obj.trialStim==stim
                                                y[-1].append(np.full(preTrials+transTrials+postTrials,np.nan))
                                                pre = obj.trialResponse[(obj.trialBlock==blockInd) & trials]
                                                i = min(preTrials,pre.size)
                                                y[-1][-1][preTrials-i:preTrials] = pre[-i:]
                                                post = obj.trialResponse[blockTrials & trials]
                                                if (firstTarget=='rewarded' and stim==rewStim) or (firstTarget=='non-rewarded' and stim==nonRewStim):
                                                    i = min(postTrials,post.size)
                                                    y[-1][-1][preTrials+transTrials:preTrials+transTrials+i] = post[:i]
                                                else:
                                                    i = min(postTrials-1,post.size) - (nTarg-1)
                                                    y[-1][-1][preTrials+transTrials+nTarg:preTrials+transTrials+nTarg+i] = post[:i]
                            if len(y[-1]) > 0:
                                n += len(y[-1])
                                y[-1] = np.nanmean(y[-1],axis=0)
                            else:
                                y[-1] = np.full(preTrials+transTrials+postTrials,np.nan)
                    if len(y)>0:
                        m = np.nanmean(y,axis=0)
                        s = np.nanstd(y,axis=0)/(len(y)**0.5)
                        ax.plot(x[:preTrials],m[:preTrials],color=clr,label=stimLbl)
                        ax.fill_between(x[:preTrials],(m+s)[:preTrials],(m-s)[:preTrials],color=clr,alpha=0.25)
                        ax.plot(x[preTrials:],m[preTrials:],color=clr)
                        ax.fill_between(x[preTrials:],(m+s)[preTrials:],(m-s)[preTrials:],color=clr,alpha=0.25)
                        # if lbl == 'noAR' and firstTrialLick:
                        #     if firstTrialRewStim and stimLbl == 'unrewarded target stim' :
                        #         deltaLickProb['rewarded target first']['nonRewTarg'] = np.array(y)[:,[preTrials-1,preTrials+1]]
                        #     elif not firstTrialRewStim and stimLbl == 'rewarded target stim':
                        #         deltaLickProb['non-rewarded target first']['rewTarg'] = np.array(y)[:,[preTrials-1,preTrials+1]]
                for side in ('right','top'):
                    ax.spines[side].set_visible(False)
                ax.tick_params(direction='out',top=False,right=False,labelsize=12)
                ax.set_xticks([-5,-1]+[transTrials+nTarg-1+i for i in (1,5,10,15)])
                ax.set_xticklabels([-5,-1,1,5,10,15])
                ax.set_yticks([0,0.5,1])
                ax.set_xlim([-preTrials-0.5,transTrials+postTrials-0.5])
                ax.set_ylim([0,1.01])
                ax.set_xlabel('Trials of indicated type after block switch',fontsize=14)
                ax.set_ylabel('Response rate',fontsize=14)
                ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=14)
                ax.set_title(lbl+'\n'+firstTarget+' target first, '+lickLbl+', '+str(len(y))+' mice, '+str(n)+' blocks')
                plt.tight_layout()
                
for lbl in ('noAR',):#('noAR','rewardOnly','catchOnly'):
    for firstTarget in ('rewarded','non-rewarded'):
        for firstTrialLick,lickLbl in zip((True,False),('lick','no lick')):
            for nTarg in range(1,3):
                fig = plt.figure(figsize=(8,4))
                ax = fig.add_subplot(1,1,1)
                preTrials = 5
                transTrials = 0 if lbl=='noAR' else 5
                postTrials = 16
                x = np.arange(-preTrials,transTrials+postTrials)    
                ax.add_patch(matplotlib.patches.Rectangle([-0.5,0],width=transTrials+nTarg,height=1,facecolor='0.5',edgecolor=None,alpha=0.2,zorder=0))
                for stimLbl,clr in zip(('rewarded target stim','unrewarded target stim'),'gm'):
                    y = []
                    for exps,isFirstType in zip(sessionDataVariants[lbl],isFirstExpType[lbl]):
                        if len(exps)>0 and ((useFirstExpType and isFirstType) or not useFirstExpType):
                            if useFirstExp:
                                exps = [exps[0]]
                            for obj in exps:
                                for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                                    if blockInd > 0:
                                        nonRewStim = np.setdiff1d(obj.blockStimRewarded,rewStim)
                                        blockTrials = obj.trialBlock==blockInd+1
                                        rewStimTrials = np.where(blockTrials & (obj.trialStim==rewStim))[0]
                                        nonRewStimTrials = np.where(blockTrials & (obj.trialStim==nonRewStim))[0]
                                        if ((firstTarget=='rewarded' and rewStimTrials[nTarg-1] < nonRewStimTrials[0] < rewStimTrials[nTarg]) or
                                            (firstTarget=='non-rewarded' and nonRewStimTrials[nTarg-1] < rewStimTrials[0] < nonRewStimTrials[nTarg])):
                                            firstTargetTrial = rewStimTrials[:nTarg] if firstTarget=='rewarded' else nonRewStimTrials[:nTarg]
                                            if np.all(obj.trialResponse[firstTargetTrial] == firstTrialLick):
                                                stim = nonRewStim if 'unrewarded' in stimLbl else rewStim
                                                trials = obj.trialStim==stim
                                                y.append(np.full(preTrials+transTrials+postTrials,np.nan))
                                                pre = obj.trialResponse[(obj.trialBlock==blockInd) & trials]
                                                i = min(preTrials,pre.size)
                                                y[-1][preTrials-i:preTrials] = pre[-i:]
                                                post = obj.trialResponse[blockTrials & trials]
                                                if (firstTarget=='rewarded' and stim==rewStim) or (firstTarget=='non-rewarded' and stim==nonRewStim):
                                                    i = min(postTrials,post.size)
                                                    y[-1][preTrials+transTrials:preTrials+transTrials+i] = post[:i]
                                                else:
                                                    i = min(postTrials-1,post.size) - (nTarg-1)
                                                    y[-1][preTrials+transTrials+nTarg:preTrials+transTrials+nTarg+i] = post[:i]
                    if len(y)>0:
                        p = np.nanmean(y,axis=0)
                        n = len(y)
                        ci = [b/n for b in scipy.stats.binom.interval(0.95,n,p)]
                        ci[0][p==1] = 1
                        ci[1][p==1] = 1
                        ax.plot(x[:preTrials],p[:preTrials],color=clr,label=stimLbl)
                        ax.fill_between(x[:preTrials],ci[1][:preTrials],ci[0][:preTrials],color=clr,alpha=0.25)
                        ax.plot(x[preTrials:],p[preTrials:],color=clr)
                        ax.fill_between(x[preTrials:],ci[1][preTrials:],ci[0][preTrials:],color=clr,alpha=0.25)
                        # if lbl == 'noAR' and firstTrialLick:
                        #     if firstTrialRewStim and stimLbl == 'unrewarded target stim' :
                        #         deltaLickProb['rewarded target first']['nonRewTarg'] = np.array(y)[:,[preTrials-1,preTrials+1]]
                        #     elif not firstTrialRewStim and stimLbl == 'rewarded target stim':
                        #         deltaLickProb['non-rewarded target first']['rewTarg'] = np.array(y)[:,[preTrials-1,preTrials+1]]
                for side in ('right','top'):
                    ax.spines[side].set_visible(False)
                ax.tick_params(direction='out',top=False,right=False,labelsize=12)
                ax.set_xticks([-5,-1]+[transTrials+nTarg-1+i for i in (1,5,10,15)])
                ax.set_xticklabels([-5,-1,1,5,10,15])
                ax.set_yticks([0,0.5,1])
                ax.set_xlim([-preTrials-0.5,transTrials+postTrials-0.5])
                ax.set_ylim([0,1.01])
                ax.set_xlabel('Trials of indicated type after block switch',fontsize=14)
                ax.set_ylabel('Response rate',fontsize=14)
                ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=14)
                ax.set_title(lbl+'\n'+firstTarget+' target first, '+lickLbl+', '+str(len(sessionDataVariants[lbl]))+' mice, '+str(n)+' blocks')
                plt.tight_layout()

# block switch plots by first target type
for lbl in ('rewardOnly',):#('noAR','rewardOnly','catchOnly'):
    for firstTarget in ('rewarded','non-rewarded'):
        fig = plt.figure(figsize=(8,4))
        ax = fig.add_subplot(1,1,1)
        preTrials = 5
        transTrials = 0 if lbl=='noAR' else 5
        postTrials = 16
        x = np.arange(-preTrials,transTrials+postTrials)    
        ax.add_patch(matplotlib.patches.Rectangle([-0.5,0],width=transTrials+1,height=1,facecolor='0.5',edgecolor=None,alpha=0.2,zorder=0))
        for stimLbl,clr in zip(('rewarded target stim','unrewarded target stim'),'gm'):
            n = 0
            y = []
            for exps,isFirstType in zip(sessionDataVariants[lbl],isFirstExpType[lbl]):
                if len(exps)>0 and ((useFirstExpType and isFirstType) or not useFirstExpType):
                    if useFirstExp:
                        exps = [exps[0]]
                    y.append([])
                    for obj in exps:
                        for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                            if blockInd > 0:
                                nonRewStim = np.setdiff1d(obj.blockStimRewarded,rewStim)
                                blockTrials = obj.trialBlock==blockInd+1
                                rewStimTrials = np.where(blockTrials & (obj.trialStim==rewStim))[0]
                                nonRewStimTrials = np.where(blockTrials & (obj.trialStim==nonRewStim))[0]
                                if ((firstTarget=='rewarded' and rewStimTrials[0] < nonRewStimTrials[0]) or
                                    (firstTarget=='non-rewarded' and nonRewStimTrials[0] < rewStimTrials[0])):
                                    stim = nonRewStim if 'unrewarded' in stimLbl else rewStim
                                    trials = obj.trialStim==stim
                                    y[-1].append(np.full(preTrials+transTrials+postTrials,np.nan))
                                    pre = obj.trialResponse[(obj.trialBlock==blockInd) & trials]
                                    i = min(preTrials,pre.size)
                                    y[-1][-1][preTrials-i:preTrials] = pre[-i:]
                                    post = obj.trialResponse[blockTrials & trials]
                                    if (firstTarget=='rewarded' and stim==rewStim) or (firstTarget=='non-rewarded' and stim==nonRewStim):
                                        i = min(postTrials,post.size)
                                        y[-1][-1][preTrials+transTrials:preTrials+transTrials+i] = post[:i]
                                    else:
                                        i = min(postTrials-1,post.size)
                                        y[-1][-1][preTrials+transTrials+1:preTrials+transTrials+1+i] = post[:i]
                    if len(y[-1]) > 0:
                        n += len(y[-1])
                        y[-1] = np.nanmean(y[-1],axis=0)
                    else:
                        y[-1] = np.full(preTrials+transTrials+postTrials,np.nan)
            if len(y)>0:
                m = np.nanmean(y,axis=0)
                s = np.nanstd(y,axis=0)/(len(y)**0.5)
                ax.plot(x[:preTrials],m[:preTrials],color=clr,label=stimLbl)
                ax.fill_between(x[:preTrials],(m+s)[:preTrials],(m-s)[:preTrials],color=clr,alpha=0.25)
                ax.plot(x[preTrials:],m[preTrials:],color=clr)
                ax.fill_between(x[preTrials:],(m+s)[preTrials:],(m-s)[preTrials:],color=clr,alpha=0.25)
                # if lbl == 'noAR' and firstTrialLick:
                #     if firstTrialRewStim and stimLbl == 'unrewarded target stim' :
                #         deltaLickProb['rewarded target first']['nonRewTarg'] = np.array(y)[:,[preTrials-1,preTrials+1]]
                #     elif not firstTrialRewStim and stimLbl == 'rewarded target stim':
                #         deltaLickProb['non-rewarded target first']['rewTarg'] = np.array(y)[:,[preTrials-1,preTrials+1]]
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False,labelsize=12)
        ax.set_xticks([-5,-1]+[transTrials+i for i in (1,5,10,15)])
        ax.set_xticklabels([-5,-1,1,5,10,15])
        ax.set_yticks([0,0.5,1])
        ax.set_xlim([-preTrials-0.5,transTrials+postTrials-0.5])
        ax.set_ylim([0,1.01])
        ax.set_xlabel('Trials of indicated type after block switch',fontsize=14)
        ax.set_ylabel('Response rate',fontsize=14)
        ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=14)
        ax.set_title(lbl+'\n'+firstTarget+' target first, '+str(len(y))+' mice, '+str(n)+' blocks')
        plt.tight_layout()
            
# block switch plots with non-target trials first
for lbl,title in zip(('rewardOnly','catchOnly'),('block switch cued with reward only','catch only')):
    fig = plt.figure(figsize=(5,4))
    ax = fig.add_subplot(1,1,1)
    preTrials = 5
    postTrials = 15
    x = np.arange(-preTrials,postTrials+1)
    # ax.plot([0,0],[0,1],'--',color='0.5')
    ax.add_patch(matplotlib.patches.Rectangle([-0.5,0],width=1,height=1,facecolor='0.5',edgecolor=None,alpha=0.2,zorder=0))
    for stimLbl,clr in zip(('non-target (rewarded modality)','non-target (unrewarded modality'),'gm'):
        n = 0
        y = []
        for exps,isFirstType in zip(sessionDataVariants[lbl],isFirstExpType[lbl]):
            if len(exps)>0 and ((useFirstExpType and isFirstType) or not useFirstExpType):
                if useFirstExp:
                    exps = [exps[0]]
                y.append([])
                for obj in exps:
                    for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                        if blockInd > 0:
                            blockTrials = obj.trialBlock==blockInd+1
                            nonRewStim = np.setdiff1d(obj.blockStimRewarded,rewStim)[0]
                            stim = nonRewStim[:-1]+'2' if 'unrewarded' in stimLbl else rewStim[:-1]+'2'
                            trials = obj.trialStim==stim
                            firstTrial = np.where(blockTrials & trials)[0][0]
                            firstTarget = np.where(blockTrials & np.in1d(obj.trialStim,(rewStim,nonRewStim)))[0][0]
                            if firstTrial > firstTarget:
                                continue
                            y[-1].append(np.full(preTrials+postTrials+1,np.nan))
                            pre = obj.trialResponse[(obj.trialBlock==blockInd) & trials]
                            i = min(preTrials,pre.size)
                            y[-1][-1][preTrials-i:preTrials] = pre[-i:]
                            post = obj.trialResponse[blockTrials & trials]
                            i = min(postTrials,post.size)
                            y[-1][-1][preTrials:preTrials+i] = post[:i]
                if len(y[-1]) > 0:
                    n += len(y[-1])
                    y[-1] = np.nanmean(y[-1],axis=0)
                else:
                    y[-1] = np.full(preTrials+postTrials,np.nan)
        if len(y)>0:
            m = np.nanmean(y,axis=0)
            s = np.nanstd(y,axis=0)/(len(y)**0.5)
            ax.plot(x,m,color=clr,ls='--',label=stimLbl)
            ax.fill_between(x,m+s,m-s,color=clr,alpha=0.25)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=12)
    ax.set_xticks(np.arange(-20,21,5))
    ax.set_yticks([0,0.5,1])
    ax.set_xlim([-preTrials-0.5,postTrials-0.5])
    ax.set_ylim([0,1.01])
    ax.set_xlabel('Trials of indicated type after block switch',fontsize=14)
    ax.set_ylabel('Response rate',fontsize=14)
    # ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=14)
    ax.set_title(title+'\n'+'non-target first'+', '+str(len(y))+' mice, '+str(n)+' blocks')
    plt.tight_layout()
    
# block switch plots for one reward variant
lbl = 'oneReward'
for firstTrialLick,lickLbl in zip((True,False),('lick','no lick')):
    for nTarg in range(1,4):
        fig = plt.figure(figsize=(8,4))
        ax = fig.add_subplot(1,1,1)
        preTrials = 5
        postTrials = 16
        x = np.arange(-preTrials,postTrials)    
        ax.add_patch(matplotlib.patches.Rectangle([-0.5,0],width=nTarg,height=1,facecolor='0.5',edgecolor=None,alpha=0.2,zorder=0))
        for stimLbl,clr in zip(('rewarded target stim','unrewarded target stim'),'gm'):
            n = 0
            y = []
            for exps,isFirstType in zip(sessionDataVariants[lbl],isFirstExpType[lbl]):
                if len(exps)>0 and ((useFirstExpType and isFirstType) or not useFirstExpType):
                    if useFirstExp:
                        exps = [exps[0]]
                    y.append([])
                    for obj in exps:
                        for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                            if blockInd > 0:
                                nonRewStim = np.setdiff1d(obj.blockStimRewarded,rewStim)
                                blockTrials = obj.trialBlock==blockInd+1
                                rewStimTrials = np.where(blockTrials & (obj.trialStim==rewStim))[0]
                                nonRewStimTrials = np.where(blockTrials & (obj.trialStim==nonRewStim))[0]
                                if rewStimTrials[nTarg-1] < nonRewStimTrials[0] < rewStimTrials[nTarg] and (nTarg==1 or np.all(obj.trialResponse[rewStimTrials[1:nTarg+1]])):
                                    if obj.trialResponse[blockTrials][0] == firstTrialLick:
                                        stim = nonRewStim if 'unrewarded' in stimLbl else rewStim
                                        trials = obj.trialStim==stim
                                        y[-1].append(np.full(preTrials+postTrials,np.nan))
                                        pre = obj.trialResponse[(obj.trialBlock==blockInd) & trials]
                                        i = min(preTrials,pre.size)
                                        y[-1][-1][preTrials-i:preTrials] = pre[-i:]
                                        post = obj.trialResponse[blockTrials & trials]
                                        if stim==rewStim:
                                            i = min(postTrials,post.size)
                                            y[-1][-1][preTrials:preTrials+i] = post[:i]
                                        else:
                                            i = min(postTrials-1,post.size) - (nTarg-1)
                                            y[-1][-1][preTrials+nTarg:preTrials+nTarg+i] = post[:i]
                    if len(y[-1]) > 0:
                        n += len(y[-1])
                        y[-1] = np.nanmean(y[-1],axis=0)
                    else:
                        y[-1] = np.full(preTrials+postTrials,np.nan)
            if len(y)>0:
                m = np.nanmean(y,axis=0)
                s = np.nanstd(y,axis=0)/(len(y)**0.5)
                ax.plot(x[:preTrials],m[:preTrials],color=clr,label=stimLbl)
                ax.fill_between(x[:preTrials],(m+s)[:preTrials],(m-s)[:preTrials],color=clr,alpha=0.25)
                ax.plot(x[preTrials:],m[preTrials:],color=clr)
                ax.fill_between(x[preTrials:],(m+s)[preTrials:],(m-s)[preTrials:],color=clr,alpha=0.25)
                # if lbl == 'noAR' and firstTrialLick:
                #     if firstTrialRewStim and stimLbl == 'unrewarded target stim' :
                #         deltaLickProb['rewarded target first']['nonRewTarg'] = np.array(y)[:,[preTrials-1,preTrials+1]]
                #     elif not firstTrialRewStim and stimLbl == 'rewarded target stim':
                #         deltaLickProb['non-rewarded target first']['rewTarg'] = np.array(y)[:,[preTrials-1,preTrials+1]]
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False,labelsize=12)
        ax.set_xticks([-5,-1]+[nTarg-1+i for i in (1,5,10,15)])
        ax.set_xticklabels([-5,-1,1,5,10,15])
        ax.set_yticks([0,0.5,1])
        ax.set_xlim([-preTrials-0.5,transTrials+postTrials-0.5])
        ax.set_ylim([0,1.01])
        ax.set_xlabel('Trials of indicated type after block switch',fontsize=14)
        ax.set_ylabel('Response rate',fontsize=14)
        ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=14)
        ax.set_title(lbl+'\n'+firstTarget+' target first, '+lickLbl+', '+str(len(y))+' mice, '+str(n)+' blocks')
        plt.tight_layout()
        
lbl = 'oneReward'
for firstTrialLick,lickLbl in zip((True,False),('lick','no lick')):
    for nTarg in range(1,4):
        fig = plt.figure(figsize=(8,4))
        ax = fig.add_subplot(1,1,1)
        preTrials = 5
        postTrials = 16
        x = np.arange(-preTrials,postTrials)    
        ax.add_patch(matplotlib.patches.Rectangle([-0.5,0],width=nTarg,height=1,facecolor='0.5',edgecolor=None,alpha=0.2,zorder=0))
        for stimLbl,clr in zip(('rewarded target stim','unrewarded target stim'),'gm'):
            y = []
            for exps,isFirstType in zip(sessionDataVariants[lbl],isFirstExpType[lbl]):
                if len(exps)>0 and ((useFirstExpType and isFirstType) or not useFirstExpType):
                    if useFirstExp:
                        exps = [exps[0]]
                    for obj in exps:
                        for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                            if blockInd > 0:
                                nonRewStim = np.setdiff1d(obj.blockStimRewarded,rewStim)
                                blockTrials = obj.trialBlock==blockInd+1
                                rewStimTrials = np.where(blockTrials & (obj.trialStim==rewStim))[0]
                                nonRewStimTrials = np.where(blockTrials & (obj.trialStim==nonRewStim))[0]
                                if rewStimTrials[nTarg-1] < nonRewStimTrials[0] < rewStimTrials[nTarg] and (nTarg==1 or np.all(obj.trialResponse[rewStimTrials[1:nTarg+1]])):
                                    if obj.trialResponse[blockTrials][0] == firstTrialLick:
                                        stim = nonRewStim if 'unrewarded' in stimLbl else rewStim
                                        trials = obj.trialStim==stim
                                        y.append(np.full(preTrials+postTrials,np.nan))
                                        pre = obj.trialResponse[(obj.trialBlock==blockInd) & trials]
                                        i = min(preTrials,pre.size)
                                        y[-1][preTrials-i:preTrials] = pre[-i:]
                                        post = obj.trialResponse[blockTrials & trials]
                                        if stim==rewStim:
                                            i = min(postTrials,post.size)
                                            y[-1][preTrials:preTrials+i] = post[:i]
                                        else:
                                            i = min(postTrials-1,post.size) - (nTarg-1)
                                            y[-1][preTrials+nTarg:preTrials+nTarg+i] = post[:i]
            if len(y)>0:
                p = np.nanmean(y,axis=0)
                n = len(y)
                ci = [b/n for b in scipy.stats.binom.interval(0.95,n,p)]
                ci[0][p==1] = 1
                ci[1][p==1] = 1
                ax.plot(x[:preTrials],p[:preTrials],color=clr,label=stimLbl)
                ax.fill_between(x[:preTrials],ci[1][:preTrials],ci[0][:preTrials],color=clr,alpha=0.25)
                ax.plot(x[preTrials:],p[preTrials:],color=clr)
                ax.fill_between(x[preTrials:],ci[1][preTrials:],ci[0][preTrials:],color=clr,alpha=0.25)
                # if lbl == 'noAR' and firstTrialLick:
                #     if firstTrialRewStim and stimLbl == 'unrewarded target stim' :
                #         deltaLickProb['rewarded target first']['nonRewTarg'] = np.array(y)[:,[preTrials-1,preTrials+1]]
                #     elif not firstTrialRewStim and stimLbl == 'rewarded target stim':
                #         deltaLickProb['non-rewarded target first']['rewTarg'] = np.array(y)[:,[preTrials-1,preTrials+1]]
        for side in ('right','top'):
            ax.spines[side].set_visible(False)
        ax.tick_params(direction='out',top=False,right=False,labelsize=12)
        ax.set_xticks([-5,-1]+[nTarg-1+i for i in (1,5,10,15)])
        ax.set_xticklabels([-5,-1,1,5,10,15])
        ax.set_yticks([0,0.5,1])
        ax.set_xlim([-preTrials-0.5,postTrials-0.5])
        ax.set_ylim([0,1.01])
        ax.set_xlabel('Trials of indicated type after block switch',fontsize=14)
        ax.set_ylabel('Response rate',fontsize=14)
        ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=14)
        ax.set_title(lbl+'\n'+'first trial '+lickLbl+', '+str(len(sessionDataVariants[lbl]))+' mice, '+str(n)+' blocks')
        plt.tight_layout()
        
# response times to non-contingent reward
rt = []
for exps in sessionDataVariants['oneReward']:
    rt.append([])
    for obj in exps:
        for blockInd,rewStim in enumerate(obj.blockStimRewarded):
            trial = np.where(obj.trialBlock==blockInd+1)[0][0]
            if not obj.trialResponse[trial]:
                rewTime = obj.rewardTimes[np.searchsorted(obj.rewardTimes,obj.stimStartTimes[trial])]
                lickInd = np.searchsorted(obj.lickTimes,rewTime)
                lickTime = obj.lickTimes[lickInd]
                rt[-1].append(lickTime-rewTime)
            
# first rewarded target trial on blocks starting with at least 5 non-target trials
for firstTrialRewStim,blockLbl in zip((True,False),('rewarded target first','non-rewarded target first')):
    fig = plt.figure(figsize=(8,4.5))
    ax = fig.add_subplot(1,1,1)
    preTrials = 15
    postTrials = 15
    x = np.arange(-preTrials,postTrials+1)    
    ax.plot([0,0],[0,1],'--',color='0.5')
    for stimLbl,clr in zip(('rewarded target stim','unrewarded target stim'),'gm'):
        n = 0
        y = []
        for exps in sessionDataVariants['noAR']:
                y.append([])
                for obj in exps:
                    for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                        if blockInd > 0:
                            nonRewStim = np.setdiff1d(obj.blockStimRewarded,rewStim)
                            blockTrials = obj.trialBlock==blockInd+1
                            if np.any(np.in1d(obj.trialStim[blockTrials][:5],(rewStim,nonRewStim))):
                                continue
                            firstRewStim = np.where(blockTrials & (obj.trialStim==rewStim))[0][0]
                            firstNonRewStim = np.where(blockTrials & (obj.trialStim==nonRewStim))[0][0]
                            if ((firstTrialRewStim and firstRewStim > firstNonRewStim) or
                                (not firstTrialRewStim and firstRewStim < firstNonRewStim)):
                                continue
                            stim = nonRewStim if 'unrewarded' in stimLbl else rewStim
                            trials = obj.trialStim==stim
                            y[-1].append(np.full(preTrials+postTrials+1,np.nan))
                            pre = obj.trialResponse[(obj.trialBlock==blockInd) & trials]
                            i = min(preTrials,pre.size)
                            y[-1][-1][preTrials-i:preTrials] = pre[-i:]
                            post = obj.trialResponse[blockTrials & trials]
                            i = min(postTrials,post.size)
                            y[-1][-1][preTrials+1:preTrials+1+i] = post[:i]
                if len(y[-1]) > 0:
                    n += len(y[-1])
                    y[-1] = np.nanmean(y[-1],axis=0)
                else:
                    y[-1] = np.full(preTrials+postTrials+1,np.nan)
        if len(y)>0:
            m = np.nanmean(y,axis=0)
            s = np.nanstd(y,axis=0)/(len(y)**0.5)
            ax.plot(x,m,color=clr,label=stimLbl)
            ax.fill_between(x,m+s,m-s,color=clr,alpha=0.25)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=10)
    ax.set_xticks(np.arange(-20,21,5))
    ax.set_yticks([0,0.5,1])
    ax.set_xlim([-preTrials-0.5,postTrials+0.5])
    ax.set_ylim([0,1.01])
    ax.set_xlabel('Trials of indicated type after block switch',fontsize=12)
    ax.set_ylabel('Response rate',fontsize=12)
    ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=12)
    ax.set_title(str(len(y))+' mice, '+str(n)+' blocks')
    plt.tight_layout()


# change in lick prob summary
xlabels = []
for lbl in deltaLickProbLabels[:-2]:
    for c in ('auto','target','(',','):
        if 'no target' not in lbl or c!='target':
            if c in lbl:
                i = lbl.find(c)
                lbl = lbl[:i] + '\n' + lbl[i:]
    xlabels.append(lbl)

fig = plt.figure(figsize=(12,4))
ax = fig.add_subplot(1,1,1)
xlim = [-0.5,len(xlabels)-0.5]
ax.plot(xlim,[0,0],'k--')
for x,lbl in enumerate(deltaLickProbLabels):
    for stim,clr in zip(('rewTarg','nonRewTarg'),'gm'):
        if not np.all(np.isnan(deltaLickProb[lbl][stim])):
            d = np.diff(deltaLickProb[lbl][stim],axis=1)
            m = d.mean()
            s = d.std()/(len(d)**0.5)
            ax.plot(x,m,'o',color=clr)
            ax.plot([x,x],[m-s,m+s],clr)
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False,labelsize=10)
ax.set_xticks(np.arange(len(xlabels)))
ax.set_xticklabels(xlabels)
ax.set_xlim(xlim)
ax.set_ylabel(r'$\Delta$ Response rate',fontsize=12)
plt.tight_layout()

fig = plt.figure(figsize=(12,4))
ax = fig.add_subplot(1,1,1)
xlim = [-0.5,len(xlabels)-0.5]
for x,lbl in enumerate(deltaLickProbLabels):
    for stim,clr in zip(('rewTarg','nonRewTarg'),'gm'):
        if not np.all(np.isnan(deltaLickProb[lbl][stim])):
            d = deltaLickProb[lbl][stim]
            mean = d.mean(axis=0)
            sem = d.std(axis=0)/(len(d)**0.5)
            ax.plot([x-0.25,x+0.25],mean,'o-',color=clr,mec=clr,mfc=clr)
            for dx,m,s in zip((x-0.25,x+0.25),mean,sem):
                ax.plot([dx,dx],[m-s,m+s],clr)
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False,labelsize=14)
ax.set_xticks(np.arange(len(xlabels)))
ax.set_xticklabels(xlabels)
ax.set_xlim(xlim)
ax.set_yticks([0,0.5,1])
ax.set_ylim([0,1])
ax.set_ylabel('Response rate',fontsize=16)
plt.tight_layout()


# change in lick prob matrix
labels = ('5 rewarded targets','5 non-rewarded targets','1 rewarded target','1 non-rewarded target')
xlabels = ('5 rewarded\ntarget trials','5 non-rewarded\ntarget trials','1 rewarded\ntarget trial','1 non-rewarded\ntarget trial')

fig = plt.figure(figsize=(9,4))
ax = fig.add_subplot(1,1,1)
xlim = [-0.5,len(xlabels)-0.5]
for x,lbl in enumerate(labels):
    for stim,clr in zip(('rewTarg','nonRewTarg'),'gm'):
        if lbl=='1 rewarded target' and stim=='nonRewTarg':
            key = 'rewarded target first'
        elif lbl=='1 non-rewarded target' and stim=='rewTarg':
            key = 'non-rewarded target first'
        else:
            key = lbl
        d = deltaLickProb[key][stim]
        mean = d.mean(axis=0)
        sem = d.std(axis=0)/(len(d)**0.5)
        ax.plot([x-0.25,x+0.25],mean,'o-',color=clr,mec=clr,mfc=clr)
        for dx,m,s in zip((x-0.25,x+0.25),mean,sem):
            ax.plot([dx,dx],[m-s,m+s],clr)
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False,labelsize=14)
ax.set_xticks(np.arange(len(xlabels)))
ax.set_xticklabels(xlabels)
ax.set_xlim(xlim)
ax.set_yticks([0,0.5,1])
ax.set_ylim([0,1])
ax.set_ylabel('Response rate',fontsize=16)
plt.tight_layout()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
d = np.zeros((2,2))
d[0,0] = np.mean(np.diff(deltaLickProb['1 rewarded target']['rewTarg'],axis=1))
d[0,1] = np.mean(np.diff(deltaLickProb['1 non-rewarded target']['nonRewTarg'],axis=1))
d[1,0] = np.mean(np.diff(deltaLickProb['rewarded target first']['nonRewTarg'],axis=1))
d[1,1] = np.mean(np.diff(deltaLickProb['non-rewarded target first']['rewTarg'],axis=1))
im = ax.imshow(d,cmap='bwr',clim=(-1,1))
for i in (0,1):
    for j in (0,1):
        txt = round(d[i,j],2)
        if txt > 0:
            txt = '+' + str(txt)
        ax.text(j,i,txt,ha='center',va='center',fontsize=12)
cb = plt.colorbar(im,ax=ax,fraction=0.02,pad=0.04)
cb.set_ticks([-1,-0.5,0,0.5,1])
for side in ('right','top','left','bottom'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False,labelsize=12)
ax.set_xticks([0,1])
ax.set_xticklabels(['Reward','No reward'])
ax.set_xlabel('Previous trial outcome',fontsize=14)
ax.set_yticks([0,1])
ax.set_yticklabels(['Same as\ncurrent trial','Different from\ncurrent trial'])
ax.set_ylabel('Previous trial stimulus modality',fontsize=14)
ax.set_title('Change in response prob. to current trial stimulus',fontsize=14)
plt.tight_layout()


# change in lick prob summary (reward only or catch only)
labels = ('5 rewarded targets','5 rewards')
xlabels = ('5 rewarded\ntarget trials','5 rewards\n(no stimulus)')

labels = ('5 non-rewarded targets','5 catch trials')
xlabels = ('5 non-rewarded\ntarget trials','5 catch trials\n(no stimulus or reward)')

fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(1,1,1)
xlim = [-0.5,len(xlabels)-0.5]
for x,lbl in enumerate(labels):
    for stim,clr in zip(('rewTarg','nonRewTarg'),'gm'):
        if not np.all(np.isnan(deltaLickProb[lbl][stim])):
            d = deltaLickProb[lbl][stim]
            mean = d.mean(axis=0)
            sem = d.std(axis=0)/(len(d)**0.5)
            ax.plot([x-0.25,x+0.25],mean,'o-',color=clr,mec=clr,mfc=clr)
            for dx,m,s in zip((x-0.25,x+0.25),mean,sem):
                ax.plot([dx,dx],[m-s,m+s],clr)
for side in ('right','top'):
    ax.spines[side].set_visible(False)
ax.tick_params(direction='out',top=False,right=False,labelsize=14)
ax.set_xticks(np.arange(len(xlabels)))
ax.set_xticklabels(xlabels)
ax.set_xlim(xlim)
ax.set_yticks([0,0.5,1])
ax.set_ylim([0,1])
ax.set_ylabel('Response rate',fontsize=16)
plt.tight_layout()


## no reward blocks
mice = np.array(summaryDf[summaryDf['no reward']]['mouse id'])

sessionDataNoRew = []
for mid in mice:
    df = drSheets[str(mid)] if str(mid) in drSheets else nsbSheets[str(mid)]
    sessions = np.array(['no reward' in task for task in df['task version']]) & ~np.array(df['ignore'].astype(bool))
    sessionDataNoRew.append([getSessionData(mid,startTime) for startTime in df.loc[sessions,'start time']])

# block switch plot, target stimuli only
for blockRewarded,title in zip((True,False),('switch to rewarded block','switch to unrewarded block')):
    fig = plt.figure(figsize=(8,4.5))
    ax = fig.add_subplot(1,1,1)
    preTrials = 15
    postTrials = 15
    x = np.arange(-preTrials,postTrials+1)    
    ax.plot([0,0],[0,1],'--',color='0.5')
    for stimLbl,clr in zip(('previously rewarded target stim','other target stim'),'mg'):
        y = []
        for exps in sessionDataNoRew:
            y.append([])
            for obj in exps:
                for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                    if blockInd > 0 and ((blockRewarded and rewStim != 'none') or (not blockRewarded and rewStim == 'none')):
                        if blockRewarded:
                            stim = np.setdiff1d(('vis1','sound1'),rewStim) if 'previously' in stimLbl else rewStim
                        else:
                            prevRewStim = obj.blockStimRewarded[blockInd-1]
                            stim = np.setdiff1d(('vis1','sound1'),prevRewStim) if 'other' in stimLbl else prevRewStim
                        trials = (obj.trialStim==stim)
                        y[-1].append(np.full(preTrials+postTrials+1,np.nan))
                        pre = obj.trialResponse[(obj.trialBlock==blockInd) & trials]
                        i = min(preTrials,pre.size)
                        y[-1][-1][preTrials-i:preTrials] = pre[-i:]
                        post = obj.trialResponse[(obj.trialBlock==blockInd+1) & trials]
                        i = min(postTrials,post.size)
                        y[-1][-1][preTrials+1:preTrials+1+i] = post[:i]
            y[-1] = np.nanmean(y[-1],axis=0)
        m = np.nanmean(y,axis=0)
        s = np.nanstd(y,axis=0)/(len(y)**0.5)
        ax.plot(x,m,color=clr,label=stimLbl)
        ax.fill_between(x,m+s,m-s,color=clr,alpha=0.25)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=10)
    ax.set_xticks(np.arange(-20,21,5))
    ax.set_yticks([0,0.5,1])
    ax.set_xlim([-preTrials-0.5,postTrials+0.5])
    ax.set_ylim([0,1.01])
    ax.set_xlabel('Trials of indicated type after block switch',fontsize=12)
    ax.set_ylabel('Response rate',fontsize=12)
    ax.legend(bbox_to_anchor=(1,1),loc='upper left')
    ax.set_title(title+' ('+str(len(y))+' mice)',fontsize=12)
    plt.tight_layout()
    
for blockRewarded,title in zip((True,False),('switch to rewarded block','switch to unrewarded block')):
    fig = plt.figure(figsize=(8,4.5))
    ax = fig.add_subplot(1,1,1)
    preTrials = 15
    postTrials = 15
    x = np.arange(-preTrials,postTrials+1)    
    ax.plot([0,0],[-2,2],'--',color='0.5')
    for stimLbl,clr in zip(('previously rewarded target stim','other target stim'),'mg'):
        y = []
        for exps in sessionDataNoRew:
            y.append([])
            for obj in exps:
                for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                    if blockInd > 0 and ((blockRewarded and rewStim != 'none') or (not blockRewarded and rewStim == 'none')):
                        if blockRewarded:
                            stim = np.setdiff1d(('vis1','sound1'),rewStim) if 'previously' in stimLbl else rewStim
                        else:
                            prevRewStim = obj.blockStimRewarded[blockInd-1]
                            stim = np.setdiff1d(('vis1','sound1'),prevRewStim) if 'other' in stimLbl else prevRewStim
                        trials = (obj.trialStim==stim)
                        rt = obj.responseTimes - np.nanmean(obj.responseTimes[trials])
                        y[-1].append(np.full(preTrials+postTrials+1,np.nan))
                        pre = rt[(obj.trialBlock==blockInd) & trials]
                        i = min(preTrials,pre.size)
                        y[-1][-1][preTrials-i:preTrials] = pre[-i:]
                        post = rt[(obj.trialBlock==blockInd+1) & trials]
                        i = min(postTrials,post.size)
                        y[-1][-1][preTrials+1:preTrials+1+i] = post[:i]
            y[-1] = np.nanmean(y[-1],axis=0)
        m = np.nanmean(y,axis=0)
        s = np.nanstd(y,axis=0)/(len(y)**0.5)
        ax.plot(x,m,color=clr,label=stimLbl)
        ax.fill_between(x,m+s,m-s,color=clr,alpha=0.25)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=10)
    ax.set_xticks(np.arange(-20,21,5))
    ax.set_xlim([-preTrials-0.5,postTrials+0.5])
    ax.set_yticks(np.arange(-0.2,0.2,0.05))
    ax.set_ylim([-0.16,0.15])
    ax.set_xlabel('Trials of indicated type after block switch',fontsize=12)
    ax.set_ylabel('Response time\n(difference from mean, s)',fontsize=12)
    ax.legend(bbox_to_anchor=(1,1),loc='upper left')
    ax.set_title(title+' ('+str(len(y))+' mice)',fontsize=12)
    plt.tight_layout()
    
# resp rate correlations comparing reward and no reward blocks
blockTypes = ('rewarded','unrewarded')
stimNames = ('vis1','sound1','vis2','sound2')
corrWithin = {blockType: [[[[] for _  in range(len(sessionDataNoRew))] for _ in range(4)] for _ in range(4)] for blockType in blockTypes}
corrWithinDetrend = copy.deepcopy(corrWithin)
corrWithinMat = {blockType: np.zeros((4,4,len(sessionDataNoRew),200)) for blockType in blockTypes}
corrWithinDetrendMat = copy.deepcopy(corrWithinMat)
nShuffles = 10
for blockType in blockTypes:
    for m,exps in enumerate(sessionDataNoRew):
        for obj in exps:
            resp = np.zeros((4,obj.nTrials))
            respShuffled = np.zeros((4,obj.nTrials,nShuffles))
            for blockInd in range(6):
                blockTrials = getBlockTrials(obj,blockInd+1,'full')
                for i,s in enumerate(stimNames):
                    stimTrials = np.intersect1d(blockTrials,np.where(obj.trialStim==s)[0])
                    r = obj.trialResponse[stimTrials].astype(float)
                    r[r<1] = -1
                    resp[i,stimTrials] = r
                    for z in range(nShuffles):
                        respShuffled[i,stimTrials,z] = np.random.permutation(r)
            
            for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                if (blockType=='rewarded' and rewStim=='none') or (blockType=='unrewarded' and rewStim!='none'):
                    continue
                blockTrials = getBlockTrials(obj,blockInd+1,'full')
                r = resp[:,blockTrials]
                mean = r.mean(axis=1)
                r = r - mean[:,None]
                rs = respShuffled[:,blockTrials] - mean[:,None,None]
                if rewStim=='sound1' or (rewStim=='none' and obj.blockStimRewarded[blockInd-1]=='sound1'):
                    r = r[[1,0,3,2]]
                    rs = rs[[1,0,3,2]]
                for i,(r1,rs1) in enumerate(zip(r,rs)):
                    for j,(r2,rs2) in enumerate(zip(r,rs)):
                        c = np.correlate(r1,r2,'full')
                        norm = np.linalg.norm(r1) * np.linalg.norm(r2)
                        cc = []
                        for z in range(nShuffles):
                            cs = np.correlate(rs1[:,z],rs2[:,z],'full')
                            cc.append(c - cs)
                            cc[-1] /= norm
                        n = c.size // 2 + 1
                        a = np.full(200,np.nan)
                        a[:n] = np.mean(cc,axis=0)[-n:]
                        corrWithin[blockType][i][j][m].append(a)
                        
                        x = np.arange(r1.size)
                        rd1,rd2 = [y - np.polyval(np.polyfit(x,y,2),x) for y in (r1,r2)]
                        c = np.correlate(rd1,rd2,'full')
                        norm = np.linalg.norm(rd1) * np.linalg.norm(rd2)
                        c /= norm
                        cc = []
                        for z in range(nShuffles):
                            rsd1,rsd2 = [y - np.polyval(np.polyfit(x,y,2),x) for y in (rs1[:,z],rs2[:,z])]
                            cs = np.correlate(rsd1,rsd2,'full')
                            norm = np.linalg.norm(rsd1) * np.linalg.norm(rsd2)
                            cs /= norm
                            cc.append(c - cs)
                        n = c.size // 2 + 1
                        a = np.full(200,np.nan)
                        a[:n] = np.mean(cc,axis=0)[-n:]
                        corrWithinDetrend[blockType][i][j][m].append(a)
    
    for i in range(4):
        for j in range(4):
            for m in range(len(sessionDataNoRew)):
                corrWithinMat[blockType][i,j,m] = np.nanmean(corrWithin[blockType][i][j][m],axis=0)
                corrWithinDetrendMat[blockType][i,j,m] = np.nanmean(corrWithinDetrend[blockType][i][j][m],axis=0)

stimLabels = {'rewarded': ('rewarded target','unrewarded target','non-target\n(rewarded modality)','non-target\n(unrewarded modality)'),
              'unrewarded': ('previously rewarded target','other target','non-target\n(previously rewarded modality)','non-target\n(other modality)')}

for blockType in blockTypes:
    fig = plt.figure(figsize=(8,8))          
    gs = matplotlib.gridspec.GridSpec(4,2)
    x = np.arange(200)
    for i,ylbl in enumerate(stimLabels[blockType]):
        for j,xlbl in enumerate(stimLabels[blockType][:2]):
            ax = fig.add_subplot(gs[i,j])
            for mat,clr,lbl in zip((corrWithinMat,corrWithinDetrendMat),'rb',('within block','within block detrended')):
                mat = mat[blockType]
                m = np.nanmean(mat[i,j],axis=0)
                s = np.nanstd(mat[i,j],axis=0) / (len(mat[i,j]) ** 0.5)
                ax.plot(x,m,clr,alpha=0.5,label=lbl)
                ax.fill_between(x,m-s,m+s,color='k',alpha=0.25)
            for side in ('right','top'):
                ax.spines[side].set_visible(False)
            ax.tick_params(direction='out',top=False,right=False,labelsize=9)
            ax.set_xlim([-1,30])
            ax.set_ylim([-0.025,0.075])
            if i==3:
                ax.set_xlabel('Lag (trials)',fontsize=11)
            if j==0:
                ax.set_ylabel(ylbl,fontsize=11)
            if i==0:
                ax.set_title(xlbl,fontsize=11)
            if i==0 and j==1:
                ax.legend(bbox_to_anchor=(1,1),loc='upper left',fontsize=11)
    plt.tight_layout()



## extinction
mice = np.array(summaryDf[summaryDf['extinction']]['mouse id'])

sessionDataExtinct = []
for mid in mice:
    df = drSheets[str(mid)] if str(mid) in drSheets else nsbSheets[str(mid)]
    sessions = np.array(['extinction' in task for task in df['task version']]) & ~np.array(df['ignore'].astype(bool))
    sessionDataExtinct.append([getSessionData(mid,startTime) for startTime in df.loc[sessions,'start time']])

# block switch plot, target stimuli only
smoothSigma = None
for blockRewarded,title,preTrials,postTrials in zip((True,False),('switch to rewarded block','switch to unrewarded block'),
                                                    (60,15),(15,60)):
    fig = plt.figure(figsize=(8,5))
    ax = fig.add_subplot(1,1,1)
    x = np.arange(-preTrials,postTrials+1)    
    ax.plot([0,0],[0,1],'--',color='0.5')
    for stimLbl,clr in zip(('previously rewarded target stim','other target stim'),'mg'):
        y = []
        for exps in sessionDataExtinct:
            y.append([])
            for obj in exps:
                for blockInd,rewStim in enumerate(obj.blockStimRewarded):
                    if blockInd > 0 and ((blockRewarded and rewStim != 'none') or (not blockRewarded and rewStim == 'none')):
                        if blockRewarded:
                            stim = np.setdiff1d(('vis1','sound1'),rewStim) if 'previously' in stimLbl else rewStim
                        else:
                            prevRewStim = obj.blockStimRewarded[blockInd-1]
                            stim = np.setdiff1d(('vis1','sound1'),prevRewStim) if 'other' in stimLbl else prevRewStim
                        trials = (obj.trialStim==stim)
                        y[-1].append(np.full(preTrials+postTrials+1,np.nan))
                        pre = obj.trialResponse[(obj.trialBlock==blockInd) & trials]
                        if smoothSigma is not None:
                            pre = scipy.ndimage.gaussian_filter(pre.astype(float),smoothSigma)
                        i = min(preTrials,pre.size)
                        y[-1][-1][preTrials-i:preTrials] = pre[-i:]
                        post = obj.trialResponse[(obj.trialBlock==blockInd+1) & trials]
                        if smoothSigma is not None:
                            post = scipy.ndimage.gaussian_filter(post.astype(float),smoothSigma)
                        i = min(postTrials,post.size)
                        y[-1][-1][preTrials+1:preTrials+1+i] = post[:i]
            y[-1] = np.nanmean(y[-1],axis=0)
        m = np.nanmean(y,axis=0)
        s = np.nanstd(y,axis=0)/(len(y)**0.5)
        ax.plot(x,m,color=clr,label=stimLbl)
        ax.fill_between(x,m+s,m-s,color=clr,alpha=0.25)
    for side in ('right','top'):
        ax.spines[side].set_visible(False)
    ax.tick_params(direction='out',top=False,right=False,labelsize=10)
    ax.set_xticks(np.arange(-80,80,10))
    ax.set_yticks([0,0.5,1])
    ax.set_xlim([-preTrials-0.5,postTrials+0.5])
    ax.set_ylim([0,1.01])
    ax.set_xlabel('Trials of indicated type after block switch',fontsize=12)
    ax.set_ylabel('Response rate',fontsize=12)
    ax.legend(bbox_to_anchor=(1,1),loc='upper left')
    ax.set_title(title+' ('+str(len(y))+' mice)',fontsize=12)
    plt.tight_layout()

