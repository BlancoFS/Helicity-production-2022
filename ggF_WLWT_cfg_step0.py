from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.transferLogs = True
config.General.requestName  = 'HIG-RunIIFall18-GluGluHToWLWTTo2l2v_step0'
config.section_("General")
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'PrivateMC'
config.JobType.psetName    = '/afs/cern.ch/work/s/sblancof/private/POLARIZED_SAMPLES/NANOAOD_POL/CMSSW_10_2_22/src/Fastsim/GluGluHToWLWTTo2l2v-RunIIFall18wmLHEGS-00001_100000_cfg.py'
#config.JobType.numCores = 1
#config.JobType.inputFiles = ['/eos/user/s/sblancof/MC/LHE/WLWLTo2L2Nu_LO_Madgraph5_amnlo.lhe']
config.JobType.inputFiles = ['/eos/user/s/sblancof/MC/LHE/GluGluHToWLWTTo2l2nu_LO.lhe']
config.JobType.disableAutomaticOutputCollection = False

config.section_("Data")
config.Data.splitting       = 'EventBased'
config.Data.unitsPerJob     = 200
config.Data.totalUnits     = 100000
config.Data.outputDatasetTag = 'HIG-RunIIFall18-GluGluHToWLWTTo2l2v_step0'
config.Data.publication     = True
config.Data.outLFNDirBase = '/store/group/phys_higgs/cmshww/calderon/HToWXWX-2022/GEN-RAW-SIM'
config.Data.outputPrimaryDataset = 'CRAB_PrivateMC'

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.storageSite = 'T2_ES_IFCA'
#config.Site.whitelist = ['T2_ES_IFCA']
