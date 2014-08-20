#ifndef _HistMaker_H
#define _HistMaker_H

#include <cstring>
#include "HistManager.h"
#include "ZGAngles.h"

#include "../interface/TCPrimaryVtx.h"
#include "../interface/TCPhoton.h"
#include "../interface/TCEGamma.h"
#include "../interface/TCElectron.h"
#include "../interface/TCPhoton.h"
#include "../interface/TCMuon.h"


class HistMaker {
 public:
  HistMaker(HistManager * h);
  virtual ~HistMaker();

   virtual void FillHistosFull(Int_t n, Double_t w, string s="");
   virtual void SetVtx(TCPrimaryVtx v);
   virtual void MakeMuonPlots(const TCMuon& mu, string s="Muons");
   virtual void MakeEGammaCommonPlots(const TCEGamma& e, TString n);
   virtual void MakeElectronPlots(const TCElectron& el, string s="");
   virtual void MakePhotonPlots(const TCPhoton& ph, string s="Photon");
   virtual void MakeZeePlots(const TCPhoton& , const TCPhoton& );
   virtual void MakePhotonEnergyCorrPlots(const TCPhoton& p, Float_t , Float_t );
   virtual void SetLeptons(TCPhysObject l1, TCPhysObject l2);
   virtual void SetGamma(TCPhysObject g);
   virtual void SetGamma2(TCPhysObject g);
   virtual void Reset(float r, UInt_t n);
 private:
  HistManager * hists;

  TCPhysObject _lPt1, _lPt2, _gamma, _gamma2;
  TCPrimaryVtx _pv;
  Bool_t _isVtxSet;
  Bool_t _isLepSet;
  Bool_t _isGammaSet;
  Bool_t _isGamma2Set;
  Float_t _rhoFactor;
  UInt_t _nVtx;
  ZGAngles *angles;
};


#endif
