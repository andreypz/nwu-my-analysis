//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Wed Jun 19 18:10:37 2013 by ROOT version 5.32/00
// from TTree eventTree/eventTree
//////////////////////////////////////////////////////////

#ifndef fourLeptons_h
#define fourLeptons_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TSelector.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cstring>
#include <string>

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TSelector.h>
#include <TH2.h>
#include <TStyle.h>
#include <TString.h>
#include <TKey.h>
#include <TList.h>
#include <TLorentzVector.h>
#include <TVector3.h>
#include <TVector2.h>
#include <TProfile.h>
#include <TRandom3.h>

#include "../interface/TCPhysObject.h"
#include "../interface/TCJet.h"
#include "../interface/TCMET.h"
#include "../interface/TCEGamma.h"
#include "../interface/TCTrack.h"
#include "../interface/TCElectron.h"
#include "../interface/TCPhoton.h"
#include "../interface/TCMuon.h"
#include "../interface/TCTau.h"
#include "../interface/TCGenParticle.h"
#include "../interface/TCGenJet.h"
#include "../interface/TCPrimaryVtx.h"
#include "../interface/TCTriggerObject.h"

#include "../plugins/WeightUtils.h"
#include "../plugins/TriggerSelector.h"
#include "../plugins/rochcor2012v2.h"
#include "../plugins/ZGAngles.h"
#include "../plugins/HistManager.h"
#include "../plugins/PhotonScaleCorrections.hh"
//#include "../plugins/PhosphorCorrectorFunctor.hh"
// Header file for the classes stored in the TTree if any.
#include <TClonesArray.h>
#include <TVector3.h>


#define nC 16
struct muIdAndIsoCuts{
  Bool_t IsPF;
  Bool_t IsGLB;
  Float_t ptErrorOverPt;
  Int_t TrackLayersWithMeasurement;
  Int_t PixelLayersWithMeasurement;
  Int_t NumberOfValidMuonHits;
  Int_t NumberOfValidTrackerHits;
  Int_t NumberOfValidPixelHits;
  Int_t NumberOfMatches;
  Int_t NumberOfMatchedStations;
  Float_t NormalizedChi2;
  Float_t NormalizedChi2_tracker;
  Float_t dxy;
  Float_t dz;
  Float_t chIso04;
  Float_t nhIso04;
  Float_t phIso04;
  Float_t pfIso04;
};

struct elIdAndIsoCuts{
  //broken into [0] barrel and [1] endcap
  Float_t ptErrorOverPt[2];
  Float_t dEtaIn[2];
  Float_t dPhiIn[2];
  Float_t sigmaIetaIeta[2];
  Float_t HadOverEm[2];
  Float_t dxy[2];
  Float_t dz[2];
  Float_t fabsEPDiff[2];
  Int_t ConversionMissHits[2];
  Int_t PassedConversionProb[2];
  Float_t pfIso04[2];
};

struct phIdAndIsoCuts{
  //broken into [0] barrel and [1] endcap
  Int_t PassedEleSafeVeto[2];
  Float_t sigmaIetaIeta[2];
  Float_t HadOverEm[2];
  float chIso03[2];
  float nhIso03[2];
  float phIso03[2];
};

muIdAndIsoCuts muIdAndIsoCutsTight, muIdAndIsoCutsLoose, muIdAndIsoCutsSoft;
elIdAndIsoCuts elIdAndIsoCutsTight, elIdAndIsoCutsLoose;
phIdAndIsoCuts phIdAndIsoCutsHZG,   phIdAndIsoCutsTight, phIdAndIsoCutsLoose;

class fourLeptons : public TSelector {
 private:
  TFile* histoFile;
  TTree* thisTree;

  ZGAngles *ang;
  TriggerSelector *triggerSelector;
  HistManager *hists;
  WeightUtils *weighter;
  rochcor2012 *roch;
  UInt_t nEvents[nC];
  UInt_t totEvents;

  TRandom3 *myRandom;
  ofstream fout;

  //auto_ptr<ammagz::PhosphorCorrectionFunctor> phoCorrector;

  TTree* _mvaTree;
  Float_t mva_SCPhiWidth, mva_SCEtaWidth, mva_SigmaIEtaIEta, mva_SigmaIPhiIPhi;
  Float_t mva_fabsEPDiff, mva_EoP, mva_fbrem, mva_SCdPhi, mva_SCdEta;
  Float_t mva_SCEta, mva_R9, mva_HadOverEm, mva_ome1x5oe5x5;
  Int_t nVtx, nVtxTotal;
  Float_t nDofVtx1, nDofVtx2;


  TTree* _apzTree;
  Double_t apz_dr12, apz_dr34, apz_dr1234;
  Double_t apz_pt12, apz_pt34;
  Double_t apz_pt1, apz_pt2, apz_pt3, apz_pt4;
  Double_t apz_m12, apz_m34, apz_m4l;

  TTree* _fitTree;
  Double_t fit_m_llg, fit_m_ll, fit_phEta, fit_weight;
  Double_t fit_m_4l, fit_m_ll2;
  Double_t fit_phPt, fit_diPt;
  Bool_t fit_isLowPt;

  string period;
  string sample;
  string selection;
  string trigger;
  string gen;
  bool   makeGen;


 public :
  TTree          *fChain;   //!pointer to the analyzed TTree or TChain

   // Declaration of leaf types
   TClonesArray    *recoJets;
   //TClonesArray    *recoJPT;
   TClonesArray    *recoElectrons;
   TClonesArray    *recoMuons;
   TClonesArray    *recoPhotons;
   TCMET           *recoMET;
   TClonesArray    *triggerObjects;
   TClonesArray    *genJets;
   TClonesArray    *genParticles;
   TClonesArray    *primaryVtx;
   TVector3        *beamSpot;
   Int_t           nPUVertices;
   Float_t         nPUVerticesTrue;
   Bool_t          isRealData;
   UInt_t          runNumber;
   ULong64_t       eventNumber;
   UInt_t          lumiSection;
   UInt_t          bunchCross;
   Float_t         ptHat;
   Float_t         qScale;
   Float_t         evtWeight;
   Float_t         rhoFactor;
   Float_t         rho25Factor;
   Float_t         rhoMuFactor;
   ULong64_t       triggerStatus;
   UInt_t          hltPrescale[64];
   Bool_t          NoiseFilters_isScraping;
   Bool_t          NoiseFilters_isNoiseHcalHBHE;
   Bool_t          NoiseFilters_isNoiseHcalLaser;
   Bool_t          NoiseFilters_isNoiseEcalTP;
   Bool_t          NoiseFilters_isNoiseEcalBE;
   Bool_t          NoiseFilters_isCSCTightHalo;
   Bool_t          NoiseFilters_isCSCLooseHalo;
   Bool_t          NoiseFilters_isNoiseTracking;
   Bool_t          NoiseFilters_isNoiseEEBadSc;
   Bool_t          NoiseFilters_isNoisetrkPOG1;
   Bool_t          NoiseFilters_isNoisetrkPOG2;
   Bool_t          NoiseFilters_isNoisetrkPOG3;

   // List of branches
   TBranch        *b_recoJets;   //!
   //TBranch        *b_recoJPT;   //!
   TBranch        *b_recoElectrons;   //!
   TBranch        *b_recoMuons;   //!
   TBranch        *b_recoPhotons;   //!
   TBranch        *b_recoMET;   //!
   TBranch        *b_triggerObjects;   //!
   TBranch        *b_genJets;   //!
   TBranch        *b_genParticles;   //!
   TBranch        *b_primaryVtx;   //!
   TBranch        *b_beamSpot;   //!
   TBranch        *b_nPUVertices;   //!
   TBranch        *b_nPUVerticesTrue;   //!
   TBranch        *b_isRealData;   //!
   TBranch        *b_runNumber;   //!
   TBranch        *b_eventNumber;   //!
   TBranch        *b_lumiSection;   //!
   TBranch        *b_bunchCross;   //!
   TBranch        *b_ptHat;   //!
   TBranch        *b_qScale;   //!
   TBranch        *b_evtWeight;   //!
   TBranch        *b_rhoFactor;   //!
   TBranch        *b_rho25Factor;   //!
   TBranch        *b_rhoMuFactor;   //!
   TBranch        *b_triggerStatus;   //!
   TBranch        *b_hltPrescale;   //!
   TBranch        *b_NoiseFilters;   //!

   fourLeptons(TTree * /*tree*/ =0) : fChain(0) { }
   virtual ~fourLeptons() { }
   virtual Int_t   Version() const { return 2; }
   virtual void    Begin(TTree *tree);
   virtual void    SlaveBegin(TTree *tree);
   virtual void    Init(TTree *tree);
   virtual Bool_t  Notify();
   virtual Bool_t  Process(Long64_t entry);
   virtual Int_t   GetEntry(Long64_t entry, Int_t getall = 0) { return fChain ? fChain->GetTree()->GetEntry(entry, getall) : 0; }
   virtual void    SetOption(const char *option) { fOption = option; }
   virtual void    SetObject(TObject *obj) { fObject = obj; }
   virtual void    SetInputList(TList *input) { fInput = input; }
   virtual TList  *GetOutputList() const { return fOutput; }
   virtual void    SlaveTerminate();
   virtual void    Terminate();


   virtual void CountEvents(Int_t);

   virtual float CalculateMuonIso(TCMuon *lep);
   virtual float CalculateElectronIso(TCElectron *lep);
   virtual bool PassMuonIdAndIso(TCMuon *l, muIdAndIsoCuts c, TVector3 *pv);
   virtual bool PassElectronIdAndIso(TCElectron *l, elIdAndIsoCuts c, TVector3 *pv);
   virtual bool PassElectronIdAndIsoMVA(TCElectron *l);
   virtual bool PassPhotonIdAndIso(TCPhoton *p, phIdAndIsoCuts c, TVector3 *pv);

   virtual void CalculatePhotonIso(TCPhoton *p, float& chIsoCor, float& nhIsoCor, float& phIsoCor);
   //virtual void FillHistosFull(Int_t n, Double_t w, TCPhysObject , TCPhysObject , TCPhysObject , TCPhysObject , TCPhysObject, string s="");
   virtual void FillHistoCounts(Int_t n, Double_t w);
   //virtual void MakeMuonPlots(TCMuon mu, TVector3 *pv);
   //virtual void MakePhotonPlots(TCPhoton ph);
   //virtual void MakeZeePlots(TCPhoton , TCPhoton );
   virtual void MuonDump(TCMuon mu, TVector3 *pv);
   virtual void PhotonDump(TCPhoton pho,  phIdAndIsoCuts c);
   virtual void ElectronDump(TCElectron ele, elIdAndIsoCuts c, TVector3 *pv);
   //virtual void MakePhotonEnergyCorrPlots(TCPhoton , Float_t , Float_t );

   //virtual void PhotonR9Corrector(TCPhoton& ph);

   TCGenParticle * GetPrimaryAncestor(TCGenParticle *p);

   virtual void DiscoverGeneology(TCGenParticle *p, ULong64_t ev);

   ClassDef(fourLeptons,0);
};

#endif

#ifdef fourLeptons_cxx
void fourLeptons::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   recoJets = 0;
   //recoJPT = 0;
   recoElectrons = 0;
   recoMuons = 0;
   recoPhotons = 0;
   recoMET = 0;
   triggerObjects = 0;
   genJets = 0;
   genParticles = 0;
   primaryVtx = 0;
   beamSpot = 0;
   // Set branch addresses and branch pointers
   totEvents = 0;
   if (!tree) return;
   thisTree    = tree;
   fChain = tree;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("recoJets", &recoJets, &b_recoJets);
   //fChain->SetBranchAddress("recoJPT", &recoJPT, &b_recoJPT);
   fChain->SetBranchAddress("recoElectrons", &recoElectrons, &b_recoElectrons);
   fChain->SetBranchAddress("recoMuons", &recoMuons, &b_recoMuons);
   fChain->SetBranchAddress("recoPhotons", &recoPhotons, &b_recoPhotons);
   fChain->SetBranchAddress("recoMET", &recoMET, &b_recoMET);
   fChain->SetBranchAddress("triggerObjects", &triggerObjects, &b_triggerObjects);
   fChain->SetBranchAddress("genJets", &genJets, &b_genJets);
   fChain->SetBranchAddress("genParticles", &genParticles, &b_genParticles);
   fChain->SetBranchAddress("primaryVtx", &primaryVtx, &b_primaryVtx);
   fChain->SetBranchAddress("beamSpot", &beamSpot, &b_beamSpot);
   fChain->SetBranchAddress("nPUVertices", &nPUVertices, &b_nPUVertices);
   fChain->SetBranchAddress("nPUVerticesTrue", &nPUVerticesTrue, &b_nPUVerticesTrue);
   fChain->SetBranchAddress("isRealData", &isRealData, &b_isRealData);
   fChain->SetBranchAddress("runNumber", &runNumber, &b_runNumber);
   fChain->SetBranchAddress("eventNumber", &eventNumber, &b_eventNumber);
   fChain->SetBranchAddress("lumiSection", &lumiSection, &b_lumiSection);
   fChain->SetBranchAddress("bunchCross", &bunchCross, &b_bunchCross);
   fChain->SetBranchAddress("ptHat", &ptHat, &b_ptHat);
   fChain->SetBranchAddress("qScale", &qScale, &b_qScale);
   fChain->SetBranchAddress("evtWeight", &evtWeight, &b_evtWeight);
   fChain->SetBranchAddress("rhoFactor", &rhoFactor, &b_rhoFactor);
   fChain->SetBranchAddress("rho25Factor", &rho25Factor, &b_rho25Factor);
   fChain->SetBranchAddress("rhoMuFactor", &rhoMuFactor, &b_rhoMuFactor);
   fChain->SetBranchAddress("triggerStatus", &triggerStatus, &b_triggerStatus);
   fChain->SetBranchAddress("hltPrescale", hltPrescale, &b_hltPrescale);
   fChain->SetBranchAddress("NoiseFilters", &NoiseFilters_isScraping, &b_NoiseFilters);
}

Bool_t fourLeptons::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

  UInt_t initEvents;
  TFile   *inFile     = thisTree->GetCurrentFile();
  TTree   *jobTree    = (TTree*)inFile->Get("ntupleProducer/jobTree");
  TBranch *eventsInFile    =  jobTree->GetBranch("nEvents");

  eventsInFile->SetAddress(&initEvents);
  eventsInFile->GetEntry(0);

  totEvents += initEvents;
  cout<<"  Opened file: \n"<<inFile->GetName()<<endl;
  cout<<" Events in file: "<<initEvents<<"  total processed: "<<totEvents<<endl;

  //FillHistosBasic(0, initEvents);


   return kTRUE;
}

#endif // #ifdef fourLeptons_cxx
