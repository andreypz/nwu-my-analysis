#define jpsiGamma_cxx
#include "jpsiGamma.h"

const UInt_t ntrig = 8;
string myTriggers[ntrig] = {
  "HLT_IsoMu24_v",
  "HLT_IsoMu24_eta2p1_v",
  "HLT_Mu13_Mu8_v",
  "HLT_Mu17_Mu8_v",
  "HLT_Mu17_TkMu8_v",
  "HLT_Mu22_TkMu8_v",
  "HLT_Mu22_Photon22_CaloIdL_v",
  "HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v"
};

TString muScleFitParametersFile = "none";

UInt_t nEventsTrig[nC][ntrig];

string  myTrigger = "";
Float_t cut_l1pt  = 23;
Float_t cut_l2pt  = 4;
const Float_t cut_iso_mu1 = 0.4, cut_iso_mu2=0;
Float_t cut_gammapt = 25;
Float_t mllMax = 25;

Bool_t checkTrigger = kTRUE;
//Float_t global_Mll = 0;
//Bool_t applyPhosphor = 0;
Bool_t doRochCorr = 1;
Bool_t doMuScle = 0;
Bool_t doZee = 0;
Bool_t isMugamma = 0;
Bool_t makeApzTree = 1;
bool isDYJets = 0;
Bool_t doJPsiScale = 0;

const UInt_t hisEVTS[] = {9331};
Int_t evSize = sizeof(hisEVTS)/sizeof(int);

bool P4SortCondition(const TLorentzVector& p1, const TLorentzVector& p2) {return (p1.Pt() > p2.Pt());}

void jpsiGamma::Begin(TTree * tree)
{
  cout<<"\n***      Begin the Analyzer      ****"<<endl;
  TString option = GetOption();

  cout<<"option = "<<option.Data()<<endl;
  TObjArray *args = (TObjArray*)option.Tokenize(" ");
  sample    = (string)((TObjString*)args->At(0))->GetString();
  selection = (string)((TObjString*)args->At(1))->GetString();
  trigger   = (string)((TObjString*)args->At(2))->GetString();
  gen       = (string)((TObjString*)args->At(3))->GetString();
  period    = (string)((TObjString*)args->At(4))->GetString();

  const size_t last = string::npos;
  if (sample.find("DYJets")!=last)
    isDYJets = 1;
  cout<<"is DYJets sample !? "<<isDYJets<<endl;

  if (doMuScle){
    if (sample.find("DATA")!=last){
      muScleFitParametersFile = "../data/MuScleFitCorrector_v4_3/MuScleFit_2012ABC_DATA_ReReco_53X.txt";
      if (period.find("2012D")!=last)
        muScleFitParametersFile = "../data/MuScleFitCorrector_v4_3/MuScleFit_2012D_DATA_ReReco_53X.txt";
    }
    else
      muScleFitParametersFile = "../data/MuScleFitCorrector_v4_3/MuScleFit_2012_MC_53X_smearReReco.txt";
  }

  if (selection.find("zee")!=last) {
    doZee = true;
    trigger = "ee";}
  else if (selection.find("mugamma")!=last)
    isMugamma = true;
  //cout<<sample<<selection<<trigger<<gen<<endl;

  if (gen=="true")
    makeGen=true;
  else
    makeGen=false;

  TH1::SetDefaultSumw2(kTRUE);


  vector<string>* triggerNames = 0;
  TFile   *inFile         = tree->GetCurrentFile();
  TTree   *jobTree        = (TTree*)inFile->Get("ntupleProducer/jobTree");
  jobTree->SetBranchAddress("triggerNames", &triggerNames);
  jobTree->GetEntry();

  //cout<<"Printing all the trigger names:"<<endl;
  //for (unsigned i = 0; i < triggerNames->size(); ++i) cout << triggerNames->at(i) << endl;

  histoFile = new TFile(Form("a_%s_higgsHistograms.root", selection.c_str()), "RECREATE");
  histoFile->mkdir("apzTree", "apzTree");

  hists    = new HistManager(histoFile);
  HM       = new HistMaker(hists);
  ObjID    = new ObjectID();
  weighter = new WeightUtils(sample, period, selection, 0);
  roch     = new rochcor2012();
  triggerSelector = new TriggerSelector("", period, *triggerNames);
  myRandom = new TRandom3();

  //if (doMuScle)
  //muScle = new MuScleFitCorrector(muScleFitParametersFile);

  for (Int_t n1=0; n1<nC; n1++){
    nEvents[n1]=0;
    for (UInt_t n2=0; n2<ntrig; n2++)
      nEventsTrig[n1][n2]=0;
  }

  //Angles class:
  ang = new ZGAngles();

  fcuts.open("./out_cutlist.txt", ofstream::out);
  fout.open("./out_synch_.txt",ofstream::out);
  fout.precision(3); fout.setf(ios::fixed, ios::floatfield);

  histoFile->cd();
  histoFile->cd("apzTree");
  if (makeApzTree){
    _apzTree = new TTree("apzTree", "A tree for studying new particles");
    _apzTree->Branch("weight",&apz_w,"weight/D");
    _apzTree->Branch("dr1234",&apz_dr1234,"dr1234/D");
    _apzTree->Branch("dr12",  &apz_dr12,  "dr12/D");
    _apzTree->Branch("dr13",  &apz_dr13,  "dr13/D");
    _apzTree->Branch("dr23",  &apz_dr23,  "dr23/D");
    _apzTree->Branch("dr34",  &apz_dr34,  "dr34/D");
    _apzTree->Branch("pt12",  &apz_pt12,  "pt12/D");
    _apzTree->Branch("pt34",  &apz_pt34,  "pt34/D");
    _apzTree->Branch("m12",   &apz_m12,   "m12/D");
    _apzTree->Branch("m123",  &apz_m123,  "m123/D");
    _apzTree->Branch("m34",   &apz_m34,   "m34/D");
    _apzTree->Branch("m4l",   &apz_m4l,   "m4l/D");
    _apzTree->Branch("pt1",   &apz_pt1,   "pt1/D");
    _apzTree->Branch("pt2",   &apz_pt2,   "pt2/D");
    _apzTree->Branch("pt3",   &apz_pt3,   "pt3/D");
    _apzTree->Branch("pt4",   &apz_pt4,   "pt4/D");

    _apzTree->Branch("eta1234",&apz_eta1234,"eta1234/D");
    _apzTree->Branch("eta12",  &apz_eta12,  "eta12/D");
    _apzTree->Branch("eta34",  &apz_eta34,  "eta12/D");
    _apzTree->Branch("eta1",   &apz_eta1,   "eta1/D");
    _apzTree->Branch("eta2",   &apz_eta2,   "eta2/D");
    _apzTree->Branch("eta3",   &apz_eta3,   "eta3/D");
    _apzTree->Branch("eta4",   &apz_eta4,   "eta4/D");

    _apzTree->Branch("run",  &runNumber,  "run/i");
    _apzTree->Branch("event",&eventNumber,"event/l");
  }

  //----------------------//
  // Selecting triggers   //
  //----------------------//

  if (trigger=="double-mu")
    {
      myTrigger = "HLT_Mu13_Mu8_v";
      //myTrigger = "HLT_Mu17_Mu8_v";
      //cut_l1pt = 15;
      //cut_l2pt = 9;
      //cut_gammapt = 23;
    }
  else if (trigger=="mugamma")
    {
      myTrigger = "HLT_Mu22_Photon22_CaloIdL_v";
      //cut_l1pt = 23;
      //cut_l2pt = 7;
      //cut_gammapt = 25;
    }
  else if (trigger=="single-mu")
    {
      myTrigger = "HLT_IsoMu24_eta2p1_v";
      cut_l1pt = 25;
      cut_l2pt = 7;
      cut_gammapt = 23;
    }
  else if (trigger=="ee")
    {
      myTrigger = "HLT_Ele17_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v";
      cut_l1pt = 25;
      cut_l2pt = 7;
      cut_gammapt = 23;
    }
  else
    checkTrigger = kFALSE;
  //cout<<"Other options are not supported!"<<endl;

}

void jpsiGamma::SlaveBegin(TTree * /*tree*/)
{   TString option = GetOption(); }

Bool_t jpsiGamma::Process(Long64_t entry)
{
  GetEntry(entry);
  CountEvents(0, "Ntuple events",fcuts);
  FillHistoCounts(0, 1);
  if (nEvents[0] % (int)5e4 == 0) cout<<nEvents[8]<<" events passed of "<<nEvents[0]<<" checked!"<<endl;

  if (nEvents[0] == 1) weighter->SetDataBit(isRealData);

  //if (nEvents[0]>20) Abort("enough is enosugh!");

  //////////////////
  //Trigger status//
  //////////////////
  Bool_t triggerPass  = 1;
  Bool_t isFound  = 0;
  Int_t  prescale = 99;
  Float_t eventWeight = 1.0;

  for (UInt_t i =0; i<ntrig; i++)
    {
      triggerSelector->SelectTrigger(myTriggers[i], triggerStatus, hltPrescale, isFound, triggerPass, prescale);
      if(triggerPass) nEventsTrig[0][i]++;
    }


  eventWeight = weighter->PUWeight(nPUVerticesTrue);
  //cout<<" weight="<<eventWeight<<endl;
  ObjID->SetEventInfo(isRealData, runNumber, eventNumber, rhoFactor);
  //cout<<eventNumber<<"  ev rho = "<<rhoFactor<<endl;
  float phoMvaScore;

  nVtx = primaryVtx->GetSize();
  HM->Reset(rhoFactor, nVtx);

  // --- Primary vertex ---//
  if (nVtx<1) return kTRUE;
  TCPrimaryVtx *mainPrimaryVertex = 0; mainPrimaryVertex   = (TCPrimaryVtx*)(primaryVtx->At(0));
  TVector3* pvPosition; pvPosition = mainPrimaryVertex;

  HM->SetVtx(*mainPrimaryVertex);

  // ----------------------//
  // Gen level particles --//
  //-----------------------//
  vector<TCPhysObject> gen_mu, gen_el;
  TCPhysObject gen_gamma, gen_l1, gen_l2, gen_lPt1, gen_lPt2;
  TCPhysObject gen_higgs, gen_gamma_st1;
  vector<TCPhysObject> vetoPhotons;

  Float_t genMll = 0;
  Float_t gendR  = 0;

  if(!isRealData){
    //Int_t ZID = 3000001; //made-up particle that decays to l+l-
    Int_t A = 25;

    if (isDYJets)
      A=23;

    Int_t fsr_mu_count = 0, fsr_el_count=0;
    Int_t ph=0, h=0;

    for (int i = 0; i < genParticles->GetSize(); ++i) {
      TCGenParticle* thisParticle = (TCGenParticle*) genParticles->At(i);

      //if (abs(thisParticle->GetPDGId())==13 && thisParticle->Pt()>2)
      //ObjID->DiscoverGeneology(thisParticle);

      //Higgs himself:
      if (thisParticle->GetPDGId()==25 && (thisParticle->GetStatus()==3 || thisParticle->GetStatus()==62)){
        gen_higgs = *thisParticle;
        hists->fill1DHist(thisParticle->M(), "gen_h_mass",";gen Higgs mass",  200, 124,126, 1,"GEN");
        h++;
      }

      //Z propagator mass:
      if (thisParticle->GetPDGId()==23){
        hists->fill1DHist(thisParticle->M(), "gen_z_mass",";gen Z mass (GeV)",  200, 0,200, 1,"GEN");
      }

      //GEN MUONS
      //This GEN selection is only valid for a sample with LHE from MCFM
      if (abs(thisParticle->GetPDGId()) == 13 && thisParticle->GetStatus()==1 
          && !ObjID->isFSR(thisParticle)
          )
        {
          if (ObjID->GetPrimaryAncestor(thisParticle)->GetPDGId()==A
              //For b -> H -> j/psi gamma (ie ancestor = b)
              || (sample=="hjp" && thisParticle->Mother() && thisParticle->Mother()->GetPDGId() == 443 && abs(ObjID->GetPrimaryAncestor(thisParticle)->GetPDGId())==5)
              )
            {
              //cout<<"   --- found muon --->>>"<<endl;
              hists->fill1DHist(thisParticle->M(), "gen_mu_mass",";gen mu mass",  200, -1,1, 1,"GEN");
              gen_mu.push_back(*thisParticle);
            }
          //this is for the Madgraph case, where there are events with no Higgs in LHE file
          //:(while there are always should be):
          else if (h==0 && thisParticle->Mother() //good boys should have a mother
                   && ObjID->GetPrimaryAncestor(thisParticle)->GetPDGId() == thisParticle->GetPDGId())
            {
              //cout<<"   --- this one --->>>"<<endl;
              //ObjID->DiscoverGeneology(thisParticle);
              //cout<<"   <<--- this one"<<endl;
              hists->fill1DHist(thisParticle->M(), "gen_mu_mass",";gen mu mass",  200, -1,1, 1,"GEN");
              gen_mu.push_back(*thisParticle);
            }
        }

      
      //GEN ELECTRONS
      if (abs(thisParticle->GetPDGId()) == 11 && thisParticle->GetStatus()==1) {
        if (ObjID->GetPrimaryAncestor(thisParticle)->GetPDGId()==A)
          gen_el.push_back(*thisParticle);
        else if (h==0 && thisParticle->Mother()
                 && ObjID->GetPrimaryAncestor(thisParticle)->GetPDGId() == thisParticle->GetPDGId())
          gen_el.push_back(*thisParticle);
      }


      //PHOTON from the Higgs
      if ((sample=="dalitz" || sample=="hjp") && thisParticle->GetPDGId()==22 &&
          (thisParticle->GetStatus()==1 || thisParticle->GetStatus()==23)
          && (ObjID->GetPrimaryAncestor(thisParticle)->GetPDGId()==A
              || (thisParticle->Mother() &&  abs(thisParticle->Mother()->GetPDGId())!=13 && abs(thisParticle->Mother()->GetPDGId())!=11)))
        {
          gen_gamma = *thisParticle;
          ph++;
        }
      else if (isDYJets &&
               thisParticle->GetPDGId()==22 && thisParticle->GetStatus()==1 && ObjID->GetPrimaryAncestor(thisParticle)->GetPDGId()==23)
        gen_gamma = *thisParticle;

      // DYJets sample will be combined with ZGamma, need to remove

      //if (isDYJets && thisParticle->GetPDGId()==22
      //  && thisParticle->GetStatus()==1
      //  && thisParticle->Pt() > 10
      //  )
      //ObjID->DiscoverGeneology(thisParticle);

      // **** Find FSR PHOTONS *** //

      if (thisParticle->GetPDGId()==22 //&& thisParticle->GetStatus()==1
          && thisParticle->Mother()
          && ObjID->GetPrimaryAncestor(thisParticle)->GetPDGId()==23
          && isMugamma && abs(thisParticle->Mother()->GetPDGId())==13
          )
        {
          vetoPhotons.push_back(*thisParticle);

          hists->fill1DHist(thisParticle->Pt(),  "gen_FSR_pho_pt", ";gen FSR photon pt",   200, 0,50, 1,"GEN");
          hists->fill1DHist(thisParticle->Eta(), "gen_FSR_pho_eta",";gen FSR photon eta",  200, -5,5, 1,"GEN");
          // if (ObjID->GetPrimaryAncestor(thisParticle)->GetPDGId()!=A)
          //ObjID->DiscoverGeneology(thisParticle);

          Float_t preFSR_pt = thisParticle->Mother()->Pt();
          for (int j = 0; j < genParticles->GetSize(); ++j) {
            TCGenParticle* fsr = (TCGenParticle*) genParticles->At(j);
            if(fsr->GetPDGId()  == thisParticle->Mother()->GetPDGId()
               && fsr->Mother() == thisParticle->Mother()){

              //cout<<"   0--- this one --->>>"<<endl;
              //ObjID->DiscoverGeneology(fsr, eventNumber);
              //cout<<"   <<---0 this one"<<endl;

              hists->fill1DHist((preFSR_pt - fsr->Pt())/preFSR_pt, "gen_fsr_mu_dPt",
                                ";gen mu (Pt_preFSR - Pt_afterFSR)/pt",  200, -1,1, 1,"GEN");

              if(thisParticle->Pt() > 1)
                hists->fill1DHist((preFSR_pt - fsr->Pt())/preFSR_pt, "gen_fsr_mu_dPt_photonPt1GeV",
                                  ";gen mu (Pt_preFSR - Pt_afterFSR)/pt",  200, -1,1, 1,"GEN");
              fsr_mu_count++;
            }
          }

        }//end of fsr photons loop

      else if (thisParticle->GetPDGId()==22 //&& thisParticle->GetStatus()==1
               && isMugamma
               && !thisParticle->Mother()
               )
        {
          hists->fill1DHist(thisParticle->Pt(),  "gen_ISR_pho_pt", ";gen ISR photon pt",   200, 0,50, 1,"GEN");
          hists->fill1DHist(thisParticle->Eta(), "gen_ISR_pho_eta",";gen ISR photon eta",  200, -5,5, 1,"GEN");
        }
    }// end of genparticles loop


    sort(gen_el.begin(), gen_el.end(), P4SortCondition);
    sort(gen_mu.begin(), gen_mu.end(), P4SortCondition);

    hists->fill1DHist(fsr_mu_count, "gen_mu_fsrcount",";gen mu FSR",  4, 0,4, 1,"GEN");
    hists->fill1DHist(fsr_el_count, "gen_el_fsrcount",";gen el FSR",  4, 0,4, 1,"GEN");



    if(isMugamma){

      if (gen_mu.size()!=2)// return kTRUE;
        Abort(Form("ev #%i NONONO There has to be exactly 2 muons from the Higgs! \n \t\t but there are %i",
                   (int)eventNumber, (int)gen_mu.size()));


      gen_lPt1 = gen_mu[0];
      gen_lPt2 = gen_mu[1];
      // If there are more muons - it's confusing, so let's just ignore them for now.
      // (they may come from ZH -> ZZgamma process)

      if (gen_mu[0].Charge()==1 && gen_mu[1].Charge()==-1){
        gen_l1 = gen_mu[0];
        gen_l2 = gen_mu[1];
      }
      else if (gen_mu[0].Charge()==-1 && gen_mu[1].Charge()==1){
        gen_l1 = gen_mu[1];
        gen_l2 = gen_mu[0];
      }
      else
        Abort("They are the same charge!");


      gendR  = gen_l1.DeltaR(gen_l2);
      genMll = (gen_l1+gen_l2).M();

      //cout<<"\t\t event = "<<eventNumber<<"  "<<endl;
      //cout<<" charge = "<<gen_l1.Charge()<<" pt = "<<gen_l1.Pt()<<" eta="<<gen_l1.Eta()<<" phi="<<gen_l1.Phi()<<endl;
      //cout<<" charge = "<<gen_l2.Charge()<<" pt = "<<gen_l2.Pt()<<" eta="<<gen_l2.Eta()<<" phi="<<gen_l2.Phi()<<endl;


      //if (gen_el.size()!=2 && gen_mu.size()!=2) return kTRUE;
      //Abort(Form("  - - WARNING - -\n ev #%i What's up with that?\n There should be exact two leptons from Higgs. Insteat there %i",
      //(int)eventNumber, (int)(gen_el.size() + gen_mu.size())));

      if (gen_gamma.E()==0 && (sample=="dalitz" || sample=="hjp")) //return kTRUE;
        Abort(Form("event = %i: No gen gamma in an event? that sounds bad",(int)eventNumber));


      //ZGAnlgles:

      if (sample=="dalitz" || sample=="hjp" || sample=="zjp")
        {
          double co1,co2,phi,co3;
          ang->GetAngles(gen_l1, gen_l2, gen_gamma, co1,co2,phi,co3);
          //cout<<eventNumber<<" gen Angles: c1= "<<co1<<"  c2="<<co2<<"   phi="<<phi<<"   coTh="<<co3<<endl;

          double W = 1.;
          if  (sample=="hjp"){
            W = 3*(1+co1*co1)/4;
            eventWeight *= W;
          }
          string label="GEN-ANG1";
          hists->fill1DHist(co1, Form("gen_co1_%s", label.c_str()), ";cos(#vec{l-}, #vec{J/#Psi}) in CM", 100,-1,1, W,label);
          hists->fill1DHist(co2, Form("gen_co2_%s", label.c_str()), ";cos(#vec{l+}, #vec{J/#Psi}) in CM", 100,-1,1, W,label);
          hists->fill1DHist(co3, Form("gen_co3_%s", label.c_str()), ";cos(#Theta)",                 100,-1,1, W,label);
          hists->fill1DHist(phi, Form("gen_phi_%s", label.c_str()), ";#phi(l+)",50, -TMath::Pi(), TMath::Pi(),W,label);
        }


      //if (!(gen_lPt1.Pt() > 23 && gen_lPt1.Pt() > 4 && (gen_lPt1 + gen_lPt2).Pt() > 40 && gen_gamma.Pt() > 40))
      //return kTRUE;

      FillHistoCounts(1, eventWeight);
      CountEvents(1,"Pass Gen acceptance",fcuts);

      if (sample=="dalitz" || sample=="hjp" || sample=="zjp")
        {
          double co1,co2,phi,co3;
          ang->GetAngles(gen_l1, gen_l2, gen_gamma, co1,co2,phi,co3);
          //cout<<eventNumber<<" gen Angles: c1= "<<co1<<"  c2="<<co2<<"   phi="<<phi<<"   coTh="<<co3<<endl;
          double W = 1;
          //if  (sample=="hjp")
          //W = 3*(1+co1*co1)/8;
          string label="GEN-ANG2";
          hists->fill1DHist(co1, Form("gen_co1_%s", label.c_str()), ";cos(#vec{l-}, #vec{J/#Psi}) in CM", 100,-1,1, W,label);
          hists->fill1DHist(co2, Form("gen_co2_%s", label.c_str()), ";cos(#vec{l+}, #vec{J/#Psi}) in CM", 100,-1,1, W,label);
          hists->fill1DHist(co3, Form("gen_co3_%s", label.c_str()), ";cos(#Theta)",                 100,-1,1, W,label);
          hists->fill1DHist(phi, Form("gen_phi_%s", label.c_str()), ";#phi(l+)",50, -TMath::Pi(), TMath::Pi(),W,label);
        }



      hists->fill1DHist(genMll,"gen_Mll",";gen m_{ll} (GeV)",100,0,mllMax, 1,"GEN");

      hists->fill1DHist(genMll,"gen_Mll_0",";gen_Mll",100,0,mllMax, 1,"eff");
      hists->fill1DHist(gendR, "gen_dR_0", ";gen_dR", 50,0,0.3,1,"eff");
      hists->fillProfile(gendR, genMll, "gen_Mll_vs_dR", ";dR(l1,l2);M(l1,l2)", 100, 0, 0.5, 0, 20, 1,"eff");


      //Acceptance study (do not erase!)
      if (sample =="dalitz" && gen_gamma.Pt()>cut_gammapt && fabs(gen_gamma.Eta())<2.5){
        hists->fill1DHist(genMll, "gen_Mll_acc_gamma",";gen_Mll",100,0,mllMax, 1,"eff");
        hists->fill1DHist(gendR,  "gen_dR_acc_gamma", ";gen_dR", 50,0,0.3,1,"eff");

        if(sample=="dalitz" &&
           gen_lPt1.Pt()>cut_l1pt && fabs(gen_lPt1.Eta())<2.4 &&
           gen_lPt2.Pt()>cut_l2pt && fabs(gen_lPt2.Eta())<2.4
           ){
          hists->fill1DHist(genMll,  "gen_Mll_acc_lept",  ";gen_Mll",100,0,mllMax, 1,"eff");
          hists->fill1DHist(gendR,   "gen_dR_acc_lept",   ";gen_dR", 50,0,0.3,     1,"eff");

        }
        else if (sample=="dalitz")
          return kTRUE;
      }
      else if (sample=="dalitz")
        return kTRUE;

      if (sample == "dalitz"){
        hists->fill1DHist(gen_l1.DeltaR(gen_gamma),"gen_l1gamma_deltaR","gen_l1gamma_deltaR",100,0,5, 1,"");
        hists->fill1DHist(gen_l2.DeltaR(gen_gamma),"gen_l2gamma_deltaR","gen_l2gamma_deltaR",100,0,5, 1,"");

        hists->fill1DHist(gen_higgs.Pt(),     "gen_higgs_pt","Pt of higgs",     100, 0,150,  1, "");
        hists->fill1DHist(gen_higgs.M(),      "gen_higgs_mass","Mass of higgs", 100, 50,180,  1, "");
        hists->fill1DHist(gen_gamma.Pt(),     "gen_gamma_pt","Pt of gamma",   50, 0,150,  1, "");
        hists->fill1DHist(gen_gamma.Eta(),    "gen_gamma_eta","Eta of gamma", 50, -3,3,  1, "");
        //hists->fill1DHist(gen_gamma_st1.Pt(), "gen_gamma_st1_pt","Pt of gamma",   50, 0,150,  1, "");
        //hists->fill1DHist(gen_gamma_st1.Eta(),"gen_gamma_st1_eta","Eta of gamma", 50, -3,3,  1, "");
      }

    }
  }


  FillHistoCounts(2, eventWeight);
  CountEvents(2, "Acceptance", fcuts);

  vector<TCElectron> electrons0, electrons;
  vector<TCMuon> muons0, muons;
  vector<TCPhoton> photons0, photonsTight, photonsHZG, photonsMVA, fake_photons;
  TCPhysObject l1,l2, lPt1, lPt2;
  TCPhoton gamma0, gamma,gamma2, ufoton, ufelectron;

  for (Int_t i = 0; i < recoPhotons->GetSize(); ++i) {
    //cout<<"new photon!!!!!!!"<<endl;
    TCPhoton* thisPhoton = (TCPhoton*) recoPhotons->At(i);
    //cout<<"in photon loop event = "<<eventNumber
    //  <<"\n pt="<<thisPhoton->Pt()<<" eta="<<thisPhoton->Eta()<<" phi="<<thisPhoton->Phi()<<" px="<<thisPhoton->Px()<<endl;

    if (isRealData || !makeGen || (makeGen &&gen_lPt1.DeltaR(*thisPhoton) < 0.1 && thisPhoton->Pt()>20))
      fake_photons.push_back(*thisPhoton);

    if (!(fabs(thisPhoton->SCEta()) < 1.5)) continue;

    if(thisPhoton->Pt() > 15){
      if (isRealData || !makeGen || (sample=="dalitz" && makeGen && gen_gamma.DeltaR(*thisPhoton) < 0.1) )
        photons0.push_back(*thisPhoton);

      if(ObjID->PassPhotonIdAndIso(*thisPhoton, "CutBased-MediumWP", phoMvaScore)
         //&& (isRealData || !makeGen || (sample=="dalitz" && makeGen && gen_gamma.DeltaR(*thisPhoton) < 0.2) )
         )
        {

          Double_t corrPhoEnSC   = correctedPhotonEnergy(thisPhoton->SCEnergy(), thisPhoton->SCEta(), thisPhoton->R9(), runNumber,
                                                         0, "Moriond2014", !isRealData, myRandom);
          Double_t corrPhoEnReco = correctedPhotonEnergy(thisPhoton->E(), thisPhoton->SCEta(), thisPhoton->R9(), runNumber,
                                                         0, "Moriond2014", !isRealData, myRandom);

          HM->MakePhotonEnergyCorrPlots(*thisPhoton, corrPhoEnReco, corrPhoEnSC);

          //cout<<runNumber<<"  uncor en="<< thisPhoton->E()<<"  cor en = "<<corrPhoEn<<endl;
          //Double_t scale = 1;
          //Double_t scale = corrPhoEnReco/thisPhoton->E();
          Double_t scale = corrPhoEnSC/thisPhoton->E();

          thisPhoton->SetXYZM(scale*thisPhoton->Px(), scale*thisPhoton->Py(),scale*thisPhoton->Pz(),0);

          //cout<<runNumber<<"  uncor en="<< thisPhoton->E()<<"  cor en = "<<corrPhoEn<<endl;
          //thisPhoton->SetPtEtaPhiM(corrPhoEnSC/cosh(SCEta()));

          thisPhoton->SetIdMap("mvaScore", phoMvaScore);
          photonsHZG.push_back(*thisPhoton);

        }
      if(ObjID->PassPhotonIdAndIso(*thisPhoton, "CutBased-TightWP", phoMvaScore)){
        thisPhoton->SetIdMap("mvaScore", phoMvaScore);
        photonsTight.push_back(*thisPhoton);
      }

      if(ObjID->PassPhotonIdAndIso(*thisPhoton, "MVA", phoMvaScore)){
        thisPhoton->SetIdMap("mvaScore", phoMvaScore);
        photonsMVA.push_back(*thisPhoton);
      }
    }
  }


  sort(photons0.begin(),     photons0.end(),     P4SortCondition);
  sort(photonsTight.begin(), photonsTight.end(), P4SortCondition);
  sort(photonsHZG.begin(),   photonsHZG.end(),   P4SortCondition);
  sort(fake_photons.begin(), fake_photons.end(), P4SortCondition);

  //if (fake_photons.size()>1)
  // Abort("Nah, this is too much.");
  //if (fake_photons.size()>=1)
  //ufoton = fake_photons[0];

  //if (photonsTight.size()<1) return kTRUE;
  //gamma = photonsTight[0];

  if (photonsHZG.size()<1) return kTRUE;
  gamma = photonsHZG[0];

  if (photonsHZG.size()>1)
    gamma2 = photonsHZG[1];

  if (!isRealData)
    eventWeight *= weighter->PhotonSF(gamma);

  //if (photons0.size()<1) return kTRUE;
  //gamma0 = photons0[0];
  //if (gamma0.Pt() < cut_gammapt) return kTRUE;

  for (Int_t i = 0; i <  recoElectrons->GetSize(); ++i) {
    TCElectron* thisElec = (TCElectron*) recoElectrons->At(i);
    if (!(fabs(thisElec->Eta()) < 2.5)) continue;

    if (thisElec->Pt() > 10.0 &&
        thisElec->DeltaR(gamma) > 0.2 ) {

      if(isRealData || !makeGen ||
         ( selection=="el" && makeGen && (gen_l1.DeltaR(*thisElec) < 0.1 || gen_l2.DeltaR(*thisElec)<0.1)  && thisElec->Pt()>10))
        {
          if (ObjID->PassElectronIdAndIsoMVA(*thisElec)){
            thisElec->SetIdMap("mvaScore", 0);
            electrons.push_back(*thisElec);
          }
        }
      if (ObjID->PassElectronIdAndIso(*thisElec, pvPosition, "Loose") &&
          thisElec->Pt() > 15.0){
        thisElec->SetIdMap("mvaScore", 0);
        electrons0.push_back(*thisElec);
      }
    }
  }
  sort(electrons0.begin(), electrons0.end(), P4SortCondition);
  sort(electrons.begin(),  electrons.end(),  P4SortCondition);


  for (Int_t i = 0; i < recoMuons->GetSize(); ++ i) {
    TCMuon* thisMuon = (TCMuon*) recoMuons->At(i);
    //cout<<"event = "<<eventNumber
    //  <<"\n pt="<<thisMuon->Pt()<<" eta="<<thisMuon->Eta()<<" phi="<<thisMuon->Phi()<<" px="<<thisMuon->Px()<<endl;

    if (!(fabs(thisMuon->Eta()) < 2.4)) continue;

    if(thisMuon->Pt() > 4 && ObjID->PassMuonId(*thisMuon, pvPosition, "Soft") ) {
      if (doRochCorr){
        Float_t qter = 1;
        if (isRealData){
          roch->momcor_data(*thisMuon, thisMuon->Charge(), 0, qter);
          if (period=="2012D")
            roch->momcor_data(*thisMuon, thisMuon->Charge(), 1, qter);
        }
        else
          roch->momcor_mc  (*thisMuon, thisMuon->Charge(), 0, qter );
        //cout<<"DBG rochcor. qterr = "<<qter<<endl;
      }

      muons.push_back(*thisMuon);
    }
  }

  sort(muons.begin(), muons.end(), P4SortCondition);

  hists->fill1DHist(muons.size(),     Form("size_mu_cut%i",  1),";Number of muons",    5,0,5, 1, "N");
  hists->fill1DHist(electrons.size(), Form("size_el_cut%i",  1),";Number of electrons (HZZ)",   5,0,5, 1, "N");
  hists->fill1DHist(electrons0.size(),Form("size_el0_cut%i", 1),";Number of electrons (Loose)", 5,0,5, 1, "N");
  hists->fill1DHist(photonsHZG.size(),   Form("size_phHZG_cut%i",  1),";Number of photons (HZG)",   5,0,5, 1, "N");
  hists->fill1DHist(photonsTight.size(), Form("size_phTight_cut%i",1),";Number of photons (Tight)", 5,0,5, 1, "N");
  hists->fill1DHist(photonsMVA.size(),   Form("size_phMVA_cut%i",  1),";Number of photons (MVA)",   5,0,5, 1, "N");

  if(!isRealData && makeGen){
    hists->fill1DHist(genMll,  "gen_Mll_reco_gamma",  ";gen_Mll",100,0,mllMax, 1,"eff");
    hists->fill1DHist(gendR,   "gen_dR_reco_gamma",   ";gen_dR", 50, 0,0.3,    1,"eff");
  }


  if (checkTrigger){
    triggerSelector->SelectTrigger(myTrigger, triggerStatus, hltPrescale, isFound, triggerPass, prescale);
    if (!triggerPass) return kTRUE;
  }

  if (gamma.Pt() < cut_gammapt) return kTRUE;
  if (fabs(gamma.SCEta()) > 1.4442) return kTRUE;

  if(!isRealData && makeGen){
    hists->fill1DHist(genMll,  "gen_Mll_reco_gamma_iso",  ";gen_Mll",100,0,mllMax, 1,"eff");
    hists->fill1DHist(gendR,   "gen_dR_reco_gamma_iso",   ";gen_dR", 50, 0,0.3,    1,"eff");
  }

  FillHistoCounts(3, eventWeight);
  CountEvents(3,"Pass Trigger and Photon reco selection",fcuts);

  if (muons.size()<2) return kTRUE;

  Float_t tmpMll = 99999;
  if (muons.size()==2){
    lPt1 = muons[0];
    lPt2 = muons[1];
  }
  else
    for (UInt_t m1=0; m1 < muons.size(); m1++){
      for (UInt_t m2=m1; m2 < muons.size(); m2++){
        if (muons[m1].Charge()*muons[m2].Charge()==1) continue; //same charge - don't care

        if( (muons[m1]+muons[m2]).M() < tmpMll)
          {
            lPt1 = muons[m1];
            lPt2 = muons[m2];
            tmpMll = (muons[m1]+muons[m2]).M();
          }
      }
    }

  if (lPt1.Charge()==1 && lPt2.Charge()==-1){
    l1 = lPt1;
    l2 = lPt2;
  }
  else if (lPt1.Charge()==-1 && lPt2.Charge()==1){
    l1 = lPt2;
    l2 = lPt1;
  }
  else{
    //cout<<"ch1 = "<<muons[0].Charge()<<"  ch2 = "<<muons[1].Charge()<<endl;
    return kTRUE;//Abort("reco * They are the same charge!");
  }

  Double_t Mll = (l1+l2).M();

  hists->fill1DHist(Mll,  Form("diLep_mass_low_cut%i",  3),";M(ll)", 50, 0,20,  1, "");
  hists->fill1DHist(Mll,  Form("diLep_mass_high_cut%i", 3),";M(ll)", 50, 0,120, 1, "");


  if (ObjID->CalculateMuonIso(muons[0]) > 0.4)
    return kTRUE;
  //if (lPt2.Pt() > 20 && ObjID->CalculateMuonIso(muons[1]) > 0.4)
  //return kTRUE;

  HM->MakePhotonPlots(gamma);

  if (lPt1.Pt() < cut_l1pt || lPt2.Pt() < cut_l2pt)   return kTRUE;

  //if (!isfinite(eventWeight))
  //cout<<"nan/inf "<<eventWeight<<endl;
  //    if (fabs(eventWeight)>50 || fabs(eventWeight)<0.00001)

  if (!isRealData){
    eventWeight *= weighter->MuonSF(lPt1);
    eventWeight *= weighter->MuonSF(lPt2);
  }

  if (!isfinite(eventWeight))
    cout<<"nan after muon sf  "<<eventWeight<<endl;

  if(!isRealData && makeGen){
    hists->fill1DHist(genMll,  "gen_Mll_two_lep_reco", ";gen_Mll",100,0,mllMax, 1,"eff");
    hists->fill1DHist(gendR,   "gen_dR_two_lep_reco",  ";gen_dR", 50, 0,0.3,    1,"eff");
  }

  HM->SetLeptons(lPt1, lPt2);
  HM->SetGamma(gamma);
  if (gamma2.Pt()>3)
    HM->SetGamma2(gamma2);

  HM->FillHistosFull(4, eventWeight);
  FillHistoCounts(4, eventWeight);
  CountEvents(4, "Two muons selected", fcuts);


  //for(Int_t ev=0; ev<evSize;ev++){
  //if (eventNumber==hisEVTS[ev]){cout<<eventNumber<<" Found an event after lept selection "<<endl;
  //  cout<<"Mll = "<<Mll<<endl;
  //  break;}
  //}

  Float_t Mllg = (l1+l2+gamma).M();

  if (Mll > 20) return kTRUE;
  //if (Mll > mllMax) return kTRUE;

  HM->FillHistosFull(5, eventWeight);
  FillHistoCounts(5, eventWeight);
  CountEvents(5, "m(ll) < 20 GeV", fcuts);


  if (lPt1.DeltaR(gamma)<1.0 || lPt2.DeltaR(gamma)<1.0) return kTRUE;
  HM->FillHistosFull(6, eventWeight);
  FillHistoCounts(6, eventWeight);
  CountEvents(6, "dR(l, gamma) < 1", fcuts);

  if (Mll>2.9 && Mll<3.3){
    HM->FillHistosFull(7, eventWeight);
    FillHistoCounts(7, eventWeight);
    CountEvents(7, "Within J/Psi peak", fcuts);
  }

  //if (doJPsiScale && !isRealData)
  //eventWeight *= weighter->JPsiMuMuWeight(Mll);

  if (makeApzTree){
    apz_w = eventWeight;
    apz_pt1 = lPt1.Pt();
    apz_pt2 = lPt2.Pt();
    apz_pt3 = gamma.Pt();
    apz_pt4 = -1;
    if (gamma2.Pt()>3)
      apz_pt4 = gamma2.Pt();
    apz_pt12 = (lPt1+lPt2).Pt();
    apz_pt34 = gamma.Pt();

    apz_dr1234 = (lPt1+lPt2).DeltaR(gamma);
    apz_dr12 = lPt1.DeltaR(lPt2);
    apz_dr13 = lPt1.DeltaR(gamma);
    apz_dr23 = lPt2.DeltaR(gamma);
    apz_dr34 = -1;

    apz_eta1 = lPt1.Eta();
    apz_eta2 = lPt2.Eta();
    apz_eta3 = gamma.SCEta();
    apz_eta4 = -999;

    apz_eta12 = (lPt1+lPt2).Eta();
    apz_eta34 = gamma.SCEta();
    apz_eta1234 = (lPt1+lPt2+gamma).Eta();

    apz_m12 = (lPt1+lPt2).M();
    apz_m34 = gamma.M();

    apz_m123 = (lPt1+lPt2+gamma).M();

    apz_m4l = 0;
    if (gamma2.Pt()>3)
      apz_m4l = (lPt1+lPt2+gamma+gamma2).M();

    _apzTree->Fill();
  }


  if (Mll<2.5 || Mll>3.7) return kTRUE;
  HM->FillHistosFull(8, eventWeight);
  FillHistoCounts(8, eventWeight);
  //CountEvents(8, "no cut", fcuts);
  CountEvents(8, "Loose J/Psi: [2.5, 3.7]", fcuts);

  //if ((l1+l2).Pt()/Mllg < 0.30 || gamma.Pt()/Mllg < 0.30)
  if ((l1+l2).Pt() < 40 || gamma.Pt() < 40)
    return kTRUE;
  HM->FillHistosFull(9, eventWeight);
  FillHistoCounts(9, eventWeight);
  //CountEvents(9, "no cut", fcuts);
  //CountEvents(9, "pT/m(llg) > 0.3", fcuts);
  CountEvents(9, "pT > 40", fcuts);


  if (Mll<2.9 || Mll>3.3) return kTRUE;
  HM->FillHistosFull(10, eventWeight);
  FillHistoCounts(10, eventWeight);
  CountEvents(10, "Tight J/Psi: [2.9, 3.3]", fcuts);

  //global_Mll = Mll;
  HM->MakeMuonPlots(muons[0]);
  HM->MakeMuonPlots(muons[1]);

  if (Mllg>110 && Mllg<150){
    //if (Mllg>76 && Mllg<106){
    HM->FillHistosFull(15, eventWeight);
    FillHistoCounts(15, eventWeight);
    CountEvents(15, "110 < mllg < 150", fcuts);
    //CountEvents(15, "76 < mllg < 106", fcuts);
  }

  if (Mllg>122 && Mllg<128){
    HM->FillHistosFull(16, eventWeight);
    FillHistoCounts(16, eventWeight);
    CountEvents(16, "122 < mllg < 128", fcuts);
  }



  if(!isRealData && makeGen && sample=="hjp"){
    hists->fill1DHist(gen_l1.DeltaR(l1),"reco_gen_l1_deltaR","reco_gen_l1_deltaR",100,0,5, 1,"");
    hists->fill1DHist(gen_l2.DeltaR(l2),"reco_gen_l2_deltaR","reco_gen_l2_deltaR",100,0,5, 1,"");

    hists->fill2DHist(gen_l1.DeltaR(l1), gen_l2.DeltaR(l2),      "reco_gen_2D_ll_deltaR",
                      "reco_gen_2D_ll_deltaR",     100,0,5, 100,0,5, 1,"");
    hists->fill2DHist(gen_l1.DeltaR(l1), gen_gamma.DeltaR(gamma),"reco_gen_2D_l1gamma_deltaR",
                      "reco_gen_2D_l1gamma_deltaR",100,0,5, 100,0,5, 1,"");

    hists->fill1DHist(gen_gamma.DeltaR(gamma),"reco_gen_gamma_deltaR","reco_gen_gamma_deltaR",100,0,5, 1,"");
  }


  /*
    if(!isRealData && makeGen){
    for (Int_t i = 1; i<=6; i++){
    if ((l1+l2).Pt()>20+i*5)
	hists->fill1DHist(genMll,  Form("gen_Mll_%i",i),";gen_Mll", 100,0,mllMax,    1,"eff");
    if (gamma.Pt()>20+i*5)
	hists->fill1DHist(genMll,  Form("gen_Mll_%i",6+i),";gen_Mll", 100,0,mllMax,  1,"eff");
    if (gamma.Pt()/Mllg> 0.15+0.05*i)
	hists->fill1DHist(genMll,  Form("gen_Mll_%i",12+i),";gen_Mll", 100,0,mllMax, 1,"eff");
    if ((l1+l2).Pt()/Mllg> 0.15+0.05*i)
	hists->fill1DHist(genMll,  Form("gen_Mll_%i",18+i),";gen_Mll", 100,0,mllMax, 1,"eff");
    if ((l1+l2).Pt()/Mllg> 0.15+0.05*i   && gamma.Pt()/Mllg> 0.15+0.05*i)
	hists->fill1DHist(genMll,  Form("gen_Mll_%i",24+i),";gen_Mll", 100,0,mllMax, 1,"eff");
    }
    }
  */


  for (UInt_t i =0; i<ntrig; i++){
    triggerSelector->SelectTrigger(myTriggers[i], triggerStatus, hltPrescale, isFound, triggerPass, prescale);
    if(triggerPass) nEventsTrig[10][i]++;

    if (!isFound)
      cout<<"TRG **** Warning ***\n The trigger name "<<myTriggers[i]<<" is not in the list of trigger names"<<endl;
  }

  if (checkTrigger){
    triggerSelector->SelectTrigger(myTrigger, triggerStatus, hltPrescale, isFound, triggerPass, prescale);
    if (!triggerPass) return kTRUE;
    //  else Abort("Event trigger should mu or el");

  }

  HM->FillHistosFull(12, eventWeight);
  FillHistoCounts(12, eventWeight);
  CountEvents(12, "trigger check", fcuts);

  //fout<<" nEvt = "<<nEvents[0]<<" : Run/lumi/event = "<<runNumber<<"/"<<lumiSection<<"/"<<eventNumber<<endl;



  if (Mllg>76 && Mllg<106){
    HM->FillHistosFull(13, eventWeight);
    FillHistoCounts(13, eventWeight);
    CountEvents(13, "76 < mllg < 106", fcuts);
  }

  if (1){
    HM->FillHistosFull(14, eventWeight);
    FillHistoCounts(14, eventWeight);
    CountEvents(14, "no cut", fcuts);
  }


  /*
    for (UInt_t i =0; i<ntrig; i++){
    triggerSelector->SelectTrigger(myTriggers[i], triggerStatus, hltPrescale, isFound, triggerPass, prescale);
    if(triggerPass) nEventsTrig[3][i]++;
    }


    if (Mll < 20){
    for (UInt_t i=0; i<ntrig; i++){
    triggerSelector->SelectTrigger(myTriggers[i], triggerStatus, hltPrescale, isFound, triggerPass, prescale);
    if(triggerPass) nEventsTrig[4][i]++;
    }
    }

    for (UInt_t i =0; i<ntrig; i++){
    triggerSelector->SelectTrigger(myTriggers[i], triggerStatus, hltPrescale, isFound, triggerPass, prescale);
    if(triggerPass) nEventsTrig[5][i]++;

    Bool_t pa  = 1;
    Bool_t fo  = 0;
    Int_t  pr  = 99;
    triggerSelector->SelectTrigger("HLT_Mu22_Photon22_CaloIdL_v", triggerStatus, hltPrescale, fo, pa, pr);

    if(triggerPass || pa) nEventsTrig[6][i]++;
    }
  */
  /* single ele trigger study
     for (UInt_t i =0; i<ntrig; i++)
     {
     triggerSelector->SelectTrigger(myTriggers[i], triggerStatus, hltPrescale, isFound, triggerPass, prescale);

     Bool_t pa  = 1;
     Bool_t fo  = 0;
     Int_t  pr  = 99;
     triggerSelector->SelectTrigger("HLT_Ele27_WP80_v", triggerStatus, hltPrescale, fo, pa, pr);


     //if(nEvents[0]==0)
     //cout<<i<<"   "<<myTriggers[i]<<"   is Found = "<<isFound<<"   ispassed = "<<triggerPass<<"  prescale = "<<prescale<<endl;
     if(triggerPass) nEventsTrig[2][i]++;
     if(triggerPass || pa) nEventsTrig[5][i]++;
     }
  */

  /*
    for (UInt_t i =0; i<ntrig; i++) {
    triggerSelector->SelectTrigger(myTriggers[i], triggerStatus, hltPrescale, isFound, triggerPass, prescale);
    if(triggerPass) nEventsTrig[3][i]++;
    }

  */

  return kTRUE;

}

void jpsiGamma::SlaveTerminate() {}

void jpsiGamma::Terminate()
{
  cout<<" ***  Terminating... **"<<endl;
  fout.close();
  fcuts.close();

  string allCuts[nC];
  string line;
  ifstream myfile("./out_cutlist.txt");
  if (myfile.is_open()){
    while (! myfile.eof() ){
      getline (myfile,line);
      Int_t n = atoi(line.substr(0,2).c_str());
      allCuts[n] = line;
      //cout << n<<"  "<<allCuts[n]<< endl;
    }
    myfile.close();
  }

  cout<<" ** FOR PAS **"<<endl;
  cout<<"n |"<<setw(45)<<" CUT DESCRIPTION \t|"<<" events \t"<< "eff\t|"<<endl;
  for (Int_t n=0; n<nC; n++){
    if (n==0)
      cout<<  "0 |"<<setw(45)<<allCuts[0]<<"\t |"<< nEvents[0]  <<"\t|"<<float(nEvents[0])/nEvents[0]<<"\t|"<<endl;
    else
      cout<<n<<" |"<<setw(45)<<allCuts[n]<<"\t |"<< nEvents[n]  <<"\t|"<<float(nEvents[n])/nEvents[n-1]<<"\t|"<<endl;
  }


  cout<<"\n\n | Trigger efficiency 3              |\t"<<endl;
  for(UInt_t n=0; n<ntrig; n++){
    UInt_t N=10;
    cout<<n<<"  "<<float(nEventsTrig[N][n])/nEvents[N]<<"   "<<myTriggers[n]<<endl;;
  }

  //cout<<"dal = "<<dal<<"   nodal = "<<nodal<<"   tot="<<dal+nodal<<endl;

  hists->fill1DHist(-1, "evt_byCut",";cut #;weighted events", nC+1,-1,nC, totEvents, "Counts");
  hists->fill1DHist(-1, "evt_byCut_raw", ";cut #;events",     nC+1,-1,nC, totEvents, "Counts");

  //gDirectory->Print();
  //gDirectory->FindObject("evt_byCut_raw")->Print();
  histoFile->cd();
  //gDirectory->Print();
  //cout<<"Raw events:       "<<((TH1F*)gDirectory->FindObject("evt_byCut_raw"))<<endl;
  //cout<<"Weighted events:  "<<((TH1F*)histoFile->Get("evt_byCut"))->GetBinContent(1)<<endl;
  //cout<<"weight integral = "<<((TH1F*)histoFile->Get("weight__cut5"))->Integral()<<endl;

  histoFile->Write();
  histoFile->Close();
  cout<<" ** End of Analyzer **"<<endl;
}

void jpsiGamma::CountEvents(Int_t num, string cutName, ofstream& s)
{
  if (nEvents[num]==0)
    s<<num<<" "<<cutName<<endl;
  nEvents[num]++;
}


void jpsiGamma::FillHistoCounts(Int_t num, Double_t weight)
{
  hists->fill1DHist(num, "evt_byCut",";cut;weighted events", nC+1, -1,nC, weight, "Counts");
  hists->fill1DHist(num, "evt_byCut_raw", ";cut;events",     nC+1, -1,nC, 1, "Counts");
}


