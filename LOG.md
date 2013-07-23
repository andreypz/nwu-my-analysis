The log of changes:
==================

2013-Jul-04
  * Ported to Git!
  * Updated the TC classes with the latest version
  * Introduced Zgamma analyzer

2013-May-10
  * Apparently, forgot to commit a TCPhysObject class, doing it now.
  * Tag with V02-16    

2013-Apr-18
  * Tagged with V02-15
    * See previous logs for changes
    
2013-Apr-17
  * Nate's tri-lepton plot is produced
  * Trigger Selector is modified to return: isFound, isPassed and a prescale
  * Modified the Batch master to create a tar.gz before submission and to write output to EOS
  
2012-Dec-06
  * Introduced option parser to run.py script 
  * Synchroization with Nate is more or less succesefull
    * Ulong64 bug in trigger selector is fixed 
    * Covnersion veto for electrons

2012-Nov-13
  * V02-14 tag
    * Pile-up for 2012 samples is included
    * More plots in Muons and electrons
    * Cut on dR(ele, mu) to reject fake electrons
    * Top background estimation scripts are added

2012-Oct-31
  * Made it to run with 2012 and 2011 ntuples using same code (although, the ntuples are diferent)
    * Lepton selection is modified
  * b quarks study and top-background estimation scripts are updated

2012-Oct-07
   * 8 TeV cross section in config file
    
2012-Oct-06
  * V02-13 tag for the latest version of 7TeV analyzer
  * Moving to struct for Mu/Ele isolation and Id.

2012-Sep-29
  * V02-12 tag
    * HistManager added
    * plugins/lib for lineshape library
    * synchronization for 8 TeV
    
2012-Sep-23
  * Adding HistManager class from Andy. Implemented it in higgs analyzer
  * Using N events from Notify to scale the samples to lnmi
  * Removing soucefiles - no use anymore

2012-Sep-21
 * Adding event counts in Notify()
 * Cleaning sourcefiles
 * PU reweighting with fine binning for 2011

2012-Sep-13
 * V02-09 tag
   * k-factors for mH 125 and 200
   * commit before moving to a new ntuple format
   
2012-Sep-06
 * V02-08 tag:
   * MVA for low masses is done (weights are in data). 
   * Added variables for mva trees. 
   * Plotting script improved and more...

2012-Aug-23
 * Recent tags: 
   * V02-07 - Updated MVA cuts, tree maker and training  
   * V02-05 - Workable MVA code 
   * V02-03 - Added rochcor function for correcting muons, nJets histogram for jets in eta<2.5; 
         batch maser is modified to copy the files to a local directory before sendingthem over to batch 

2012-Jul-18
  * V02-02 tag
  * Converted scripts and plotting macros to python
  * Updates in analyzer in order to synchronize with Common analysis:
    * b-tagging
    * jet cuts
    * lepton iso and third lepton veto
    * Met and MT cuts reoptimised
    * etc
    
2012-Jun-14
  * V02-01 tag
  * Lineshape reweighting plugins
  * Updating to the recent TC object classes

2011-Dec-17
  * New version of Weight Utils and reweight files.
      * Fixed k-nlo for ggH samples 
  * Third muon veto updated (closer to Nate/ Pas-like)
  
2011-Dec-14
  * simplified drawing macro (no need to make all stacks - they are produced in drawMulti function)
  
2011-Dec-13
  V01-04 tag
  * Z library class is working

2011-Dec-09
  V01-03 tag
  * Switching to B-master for condor jobs submitions
  * Created plugins directory where all new classes will go
  (moved there weight utils and trigger selector)
  * Starting ZedEvensLibrary class

2011-Dec-05
  V01-02 tag
  * gluglu Higgs reweighting is implemented, kinTree ntuples are reproduced for higgs
  
2011-Dec-04
  V01-01 tag
  * TriggerSelector added (Nate's)
  * Z+jets Library update: more eta-bins
  * Overflow and underflow bins are now added to the last/first bins of all hists
  
2011-Dec-03
  * Weight utils updated: GetPhotonMass moved to Weight Utils
  * Changed the colors for the histograms   

2011-Dec-01 
  * Weighting utils class is implemented (from Nate) 
  * dPhi is changed for 0-jet bin (adding soft jets)
  * WW,WZ,ZZ samples switching to Madgraph (xSec and source files updated)
  * Trigger prescale bug fixed
  
2011-Nov-24
  The following updates are added to the code:
  * Some more histograms added: angle correlationsleptons of leptons, di-lepton, met
  * Z-library implementation
  * Photon+gets reweighting for Z+jets background estimation
  * Ntuples for MVA, in "Anton" directory of a root file
  * The H-mass dependent cuts are changed to new PAS-like cuts
  
2011-Oct-17
 *  VBF signal included

2011-Oct-16
  * V00-08 - for PAS-like yields
  * PAS-like selection restored

2011-Sep-21
*  Created MetDefinitions.h where to put all the Met functions (to share with others)
*  Put a several macros from makeplot to utils - this will be a general place to put such things
*  Deleted merge.C (included in utils.C)
  
2011-Sep-16
*  V00-07 	Fixes, matching Nate's yields; third lepton electron updated
*  V00-06 	typos, broken 

2011-Aug-26
*  tagged with V00-06
*  Moved to higgs7 directory
*  Updated cs and Nev (few things were missed)
*  Mote ttbar samples to run
*  Renamed a banch of files

  
2011-Aug-25
*  V00-05 tagged
*  Removed old analyzer and scripts
*  fixed trigger selection; updated the plotting macros


2011-Aug-23
*  Removed Ntuplizer code
*  Added run.csh that was missing

V00-04 - synchronized with Nate's code

V00-03 - latest version based on old code.
