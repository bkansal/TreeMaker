class Scenario:
    def __init__(self,sname):
        self.known = True
        dir="TreeMaker/Production/test/"
        ### OUTDATED
        if sname == "Phys14":
            self.set_vars("PHYS14_25_V2","PAT",True,False,False,"","","",False,"Run2_25ns")
        elif sname == "Spring15":
            self.set_vars("MCRUN2_74_V9","PAT",True,False,False,"","data/Summer15_25nsV5_MC","",False,"Run2_25ns")
        elif sname == "Spring15sig":
            self.set_vars("MCRUN2_74_V9","PAT",True,False,True,"","data/Summer15_25nsV5_MC","",False,"Run2_25ns")
        elif sname == "Spring15Fast":
            self.set_vars("MCRUN2_74_V9","PAT",True,True,True,"","data/Summer15_25nsV2_MC","",False,"Run2_25ns")
        elif sname == "2015B":
            self.set_vars("74X_dataRun2_Prompt_v1","RECO",False,False,False,"data/Cert_246908-255031_13TeV_PromptReco_Collisions15_50ns_JSON.txt","data/Summer15_50nsV5_DATA","",True,"Run2_50ns")
        elif sname == "re2015B":
            self.set_vars("74X_dataRun2_Prompt_v1","PAT",False,False,False,"data/Cert_246908-255031_13TeV_PromptReco_Collisions15_50ns_JSON.txt","data/Summer15_50nsV5_DATA","",True,"Run2_50ns")
        elif sname == "2015C":
            self.set_vars("74X_dataRun2_Prompt_v1","RECO",False,False,False,"data/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON.txt","data/Summer15_25nsV5_DATA","",True,"Run2_25ns")
        elif sname == "2015D":
            self.set_vars("74X_dataRun2_Prompt_v1","RECO",False,False,False,"data/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON.txt","data/Summer15_25nsV5_DATA","",True,"Run2_25ns")
        ### CURRENT
        elif sname == "Spring15v2":
            self.set_vars("74X_mcRun2_asymptotic_v2","PAT",True,False,False,"","data/Summer15_25nsV6_MC",dir+"data/Summer15_25nsV6_MC_UncertaintySources_AK4PFchs.txt",False,"Run2_25ns")
        elif sname == "Spring15v2sig":
            self.set_vars("74X_mcRun2_asymptotic_v2","PAT",True,False,True,"","data/Summer15_25nsV6_MC",dir+"data/Summer15_25nsV6_MC_UncertaintySources_AK4PFchs.txt",False,"Run2_25ns")
        elif sname == "Spring15Fastv2":
            self.set_vars("74X_mcRun2_asymptotic_v2","PAT",True,True,True,"","data/MCRUN2_74_V9","",False,"Run2_25ns")
        elif sname == "re2015C":
            self.set_vars("74X_dataRun2_v4","RECO",False,False,False,"data/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON.txt","data/Summer15_25nsV6_DATA",dir+"data/Summer15_25nsV6_MC_UncertaintySources_AK4PFchs.txt",True,"Run2_25ns")
        elif sname == "re2015D":
            self.set_vars("74X_dataRun2_reMiniAOD_v0","PAT",False,False,False,"data/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON.txt","data/Summer15_25nsV6_DATA",dir+"data/Summer15_25nsV6_MC_UncertaintySources_AK4PFchs.txt",True,"Run2_25ns")
        elif sname == "2015Db":
            self.set_vars("74X_dataRun2_Prompt_v4","RECO",False,False,False,"data/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON.txt","data/Summer15_25nsV6_DATA",dir+"data/Summer15_25nsV6_MC_UncertaintySources_AK4PFchs.txt",True,"Run2_25ns")
        else: #if no recognized scenario, set defaults
            self.known = False
            self.set_vars("74X_dataRun2_Prompt_v4","RECO",False,False,False,"","","",False,"Run2_25ns")

    def set_vars(self, globaltag, tagname, geninfo, fastsim, signal, jsonfile, jecfile, jecuncfile, residual, era):
        self.globaltag  = globaltag
        self.tagname    = tagname
        self.geninfo    = geninfo
        self.fastsim    = fastsim
        self.signal     = signal
        self.jsonfile   = jsonfile
        self.jecfile    = jecfile
        self.jecuncfile = jecuncfile
        self.residual   = residual
        self.era        = era
