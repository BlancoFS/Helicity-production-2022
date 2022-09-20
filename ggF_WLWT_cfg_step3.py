from CRABClient.UserUtilities import config
config = config()

config.section_("General")
config.General.transferLogs = True
config.General.requestName = 'HIG-RunIIFall18-GluGluHToWLWTTo2l2v_step3' 
config.General.workArea = 'crab_projects'


config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName = '/afs/cern.ch/work/s/sblancof/private/POLARIZED_SAMPLES/NANOAOD_POL/CMSSW_10_2_22/src/Fastsim/GluGluHToWLWTTo2l2v-RunIIAutumn18MiniAOD-04075_1_cfg.py'
config.JobType.maxMemoryMB = 5000


config.section_("Data")
config.Data.splitting       = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outputDatasetTag = 'HIG-RunIIFall18-GluGluHToWLWTTo2l2v_step3'
config.Data.inputDBS = 'phys03'
config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshww/calderon/HToWXWX-2022/GEN-RAW-SIM-PREMIX' 
config.Data.publication = True
config.Data.inputDataset = '/CRAB_PrivateMC/phys_higgs-HIG-RunIIFall18-GluGluHToWLWTTo2l2v_step2-f05cb92b5b34cb391fbd529b66a95e89/USER'


config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
