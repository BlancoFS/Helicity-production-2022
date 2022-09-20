# Helicity-production-2022
Production steps from LHE to nanoAOD for ggF, VBF and WW processes


# Samples generation

Generation and post-processing of Legacy polarized samples from madgraph5 to NanoAODSIM

```
RELEASE = CMSSW_10_2_22
CONDITIONS = 102X_upgrade2018_realistic_v15
```

Generation of LHE events with polarized bosons using Madgraph5.

**For WW production (MG > 2.6.X):**

```
generate p p > w+{0/T} w-{0/T} > (w+ > l+ vl), (w- > l- vl~)
```

**For Higgs production, we use HPO PO model for ggH at LO:**

```
import model HPOprodMFV_UFO
generate p p > h, (h > w+{0/T} w-{0/T}, (w+ > l+ vl), (w- > l- vl~))
```


Then, just launch and generate LHE file or create a gridpack (link for gridpack generation at CMS [1](https://twiki.cern.ch/twiki/bin/view/Main/YuanChaoMCprod15)) and run:

```
./runcmsgrid.sh 10000 $RANDOM 1
```

# Sample processing

## GEN-SIM

First, if you want to create a ROOT file from **LHE** one:

```
cmsDriver.py Configuration/GenProduction/python/EXO-RunIIFall18wmLHEGS-05557-fragment.py --filein file:GluGluHToWLWLTo2l2nu_LO.lhe --fileout file:GluGluHToWLWLTo2l2nu_step0.root --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 102X_upgrade2018_realistic_v15 --beamspot Realistic25ns13TeVEarly2018Collision --step GEN,SIM --nThreads 1 --geometry DB:Extended --era Run2_2018 --python_filename /afs/cern.ch/work/s/sblancof/private/POLARIZED_SAMPLES/CMSSW_10_2_22/src/Fastsim/HToW0W0To2l2v-RunIIFall18wmLHEGS-00001_500_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 100000
```

Then:

```
crab submit -c ggF_WLWL_cfg_step0.py
```



## GEN-SIM-RAW Premix

Add HLT and PU from Neutrino_E-10_gun:

```
cmsDriver.py --filein file:GluGluHToWLWLTo2l2nu_step0.root --fileout file:GluGluHToWLWLTo2l2nu_step1.root --pileup_input dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-PUAutumn18_102X_upgrade2018_realistic_v15-v1/GEN-SIM-DIGI-RAW --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 102X_upgrade2018_realistic_v15 --step DIGI,DATAMIX,L1,DIGI2RAW,HLT:@relval2018 --procModifiers premix_stage2 --nThreads 1 --geometry DB:Extended --datamix PreMix --era Run2_2018 --python_filename /afs/cern.ch/work/s/sblancof/private/POLARIZED_SAMPLES/CMSSW_10_2_22/src/Fastsim/EXO-RunIIAutumn18DRPremix-04066_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 100000
```

And run again:

```
crab submit -c ggF_WLWL_cfg_step1.py
```

## AOD

At this point an AOD file can be generated from the GEN-SIM-RAW ROOT file:

```
cmsDriver.py step1 --filein file:GluGluHToWLWLTo2l2nu_step1.root --fileout file:GluGluHToWLWLTo2l2nu_step2.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 102X_upgrade2018_realistic_v15 --step RAW2DIGI,RECO,RECOSIM,EI --nThreads 1 --era Run2_2018 --python_filename /afs/cern.ch/work/s/sblancof/private/POLARIZED_SAMPLES/CMSSW_10_2_22/src/Fastsim/RunIIAutumn18AOD-04075_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 100000
```

Run:

```
crab submit -c ggF_WLWL_cfg_step2.py
```

## MiniAOD

From AOD we move to MiniAOD format:

```
cmsDriver.py step2 --filein file:GluGluHToWLWLTo2l2nu_step2.root --fileout file:GluGluHToWLWLTo2l2nu_step3.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 102X_upgrade2018_realistic_v15 --step PAT --nThreads 8 --geometry DB:Extended --era Run2_2018 --python_filename /afs/cern.ch/work/s/sblancof/private/POLARIZED_SAMPLES/CMSSW_10_2_22/src/Fastsim/RunIIAutumn18MiniAOD-04075_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 100000
```

Run it:

```
crab submit -c ggF_WLWL_cfg_step3.py
```


## NanoAOD (nanoAODv7)

Finally, we obtain the nanoAOD file from MiniAOD by:

```
cmsDriver.py step3 -s NANO --mc --eventcontent NANOAODSIM --datatier NANOAODSIM --filein file:GluGluHToWLWLTo2l2nu_step3.root --fileout file:GluGluHToWLWLTo2l2nu_nanoAOD.root --conditions auto:phase1_2018_realistic --step NANO --nThreads 2 --era Run2_2018,run2_nanoAOD_102Xv1 --python_filename /afs/cern.ch/work/s/sblancof/private/POLARIZED_SAMPLES/CMSSW_10_2_22/src/Fastsim/RunIIAutumn18NanoAOD-04075_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 100000
```

And it runs as:

```
crab submit -c ggF_WLWL_cfg_step4.py
```


