#!/usr/bin/env python
import sys
from ROOT import *
gROOT.SetBatch()
#from rooFitBuilder import *
sys.path.append("../zgamma")
import utils as u
import ConfigParser as cp
gROOT.ProcessLine(".L ../tdrstyle.C")
setTDRStyle()

print len(sys.argv), sys.argv

verbose = 0
doExt   = 0

cf = cp.ConfigParser()
cf.read('config.cfg')
subdir = cf.get("path","ver")
yearList   = [a.strip() for a in (cf.get("fits","yearList")).split(',')]
leptonList = [a.strip() for a in (cf.get("fits","leptonList")).split(',')]
catList    = [a.strip() for a in (cf.get("fits","catList")).split(',')]
doBlind    = int(cf.get("fits","blind"))

plotBase = cf.get("path","htmlbase")+"/html/zgamma/dalitz/fits-"+subdir

u.createDir(plotBase)
rooWsFile = TFile(subdir+'/testRooFitOut_Dalitz.root')
myWs    = rooWsFile.Get('ws')
card_ws = RooWorkspace('ws_card')
card_ws.autoImportClassCode(True)

c = TCanvas("c","c",0,0,500,400)
c.cd()
mzg = myWs.var('CMS_hzg_mass')
mzg.setRange('signal',120,130)
mzg.setRange('r1',110,120)
mzg.setRange('r2',130,170)

bkgModel = 'Bern4'
# #######################################
# prep the background and data card    #
# we're going to the extend the bg pdf #
# and rename the parameters to work    #
# with the higgs combination tool      #
# #######################################


def BackgroundNameFixer(fitName, year, lepton, cat, ws, Ext=True):
  dataName      = '_'.join(['data',      lepton,year,'cat'+cat])
  dataNameNew   = '_'.join(['data','obs',lepton,year,'cat'+cat])
  if Ext:
    fitExtName    = '_'.join(['bkgTmp',lepton,year,'cat'+cat])
  else:
    fitExtName = '_'.join(['Bern4',year,lepton,'cat'+cat])

  fitExtNameNew = '_'.join(['bkg',lepton,year,'cat'+cat])

  BernNames = ['Bern3','Bern4','Bern5','Bern6']
  for n in BernNames:
    if n in fitName:
      print "renaming " + fitName
      suffix = '_'.join([year,lepton,'cat'+cat])
      if Ext: normName  = 'norm'+n+'_'+suffix
      p0Name = 'p0'+n+'_'+suffix
      p1Name = 'p1'+n+'_'+suffix
      p2Name = 'p2'+n+'_'+suffix
      p3Name = 'p3'+n+'_'+suffix
      p4Name = 'p4'+n+'_'+suffix

      if Ext: print "Normname from renaming:", normName

      if Ext: normNameNew  = '_'.join(['bkg',lepton,year,'cat'+cat,'norm'])
      p0NameNew = '_'.join(['bkg','p0',lepton,year,'cat'+cat])
      p1NameNew = '_'.join(['bkg','p1',lepton,year,'cat'+cat])
      p2NameNew = '_'.join(['bkg','p2',lepton,year,'cat'+cat])
      p3NameNew = '_'.join(['bkg','p3',lepton,year,'cat'+cat])

      if Ext: ws.factory(normNameNew+'[{0},{1},{2}]'.format(ws.function(normName).getVal(),
                                                            ws.function(normName).getMin(), ws.function(normName).getMax()))
      ws.factory(p0NameNew+'[{0}]'.format(ws.function(p0Name).getVal()))
      ws.factory(p1NameNew+'[{0},{1},{2}]'.format(ws.function(p1Name).getVal(),
                                                  ws.function(p1Name).getMin(),ws.function(p1Name).getMax()))
      ws.factory(p2NameNew+'[{0},{1},{2}]'.format(ws.function(p2Name).getVal(),
                                                  ws.function(p2Name).getMin(),ws.function(p2Name).getMax()))
      ws.factory(p3NameNew+'[{0},{1},{2}]'.format(ws.function(p3Name).getVal(),
                                                  ws.function(p3Name).getMin(),ws.function(p3Name).getMax()))
      if n in ['Bern4','Bern5','Bern6']:
        p4Name = 'p4'+n+'_'+suffix
        p4NameNew = '_'.join(['bkg','p4',lepton,year,'cat'+cat])
        ws.factory(p4NameNew+'[{0},{1},{2}]'.format(ws.function(p4Name).getVal(),
                                                        ws.function(p4Name).getMin(),ws.function(p4Name).getMax()))
      if n in ['Bern5','Bern6']:
        p5Name = 'p5'+n+'_'+suffix
        p5NameNew = '_'.join(['bkg','p5',lepton,year,'cat'+cat])
        ws.factory(p5NameNew+'[{0},{1},{2}]'.format(ws.function(p5Name).getVal(),
                                                    ws.function(p5Name).getMin(),ws.function(p5Name).getMax()))
      if n in ['Bern6']:
        p6Name = 'p6'+n+'_'+suffix
        p6NameNew = '_'.join(['bkg','p6',lepton,year,'cat'+cat])
        ws.factory(p6NameNew+'[{0},{1},{2}]'.format(ws.function(p6Name).getVal(),
                                                          ws.function(p6Name).getMin(),ws.function(p6Name).getMax()))
      if n=='Bern3':
        if Ext:
          ws.factory('EDIT::'+fitExtNameNew+'('+fitExtName+','+normName+'='+normNameNew+','
                     +p0Name+'='+p0NameNew+','+p1Name+'='+p1NameNew+','+p2Name+'='+p2NameNew+','
                     +p3Name+'='+p3NameNew+')')
        else:
          ws.factory('EDIT::'+fitExtNameNew+'('+fitExtName+','
                     +p0Name+'='+p0NameNew+','+p1Name+'='+p1NameNew+','+p2Name+'='+p2NameNew+','
                     +p3Name+'='+p3NameNew+')')
      if n=='Bern4':
        if Ext:
          ws.factory('EDIT::'+fitExtNameNew+'('+fitExtName+','+normName+'='+normNameNew+','
                     +p0Name+'='+p0NameNew+','+p1Name+'='+p1NameNew+','+p2Name+'='+p2NameNew+','
                     +p3Name+'='+p3NameNew+','+p4Name+'='+p4NameNew+')')
        else:
          ws.factory('EDIT::'+fitExtNameNew+'('+fitExtName+','
                     +p0Name+'='+p0NameNew+','+p1Name+'='+p1NameNew+','+p2Name+'='+p2NameNew+','
                     +p3Name+'='+p3NameNew+','+p4Name+'='+p4NameNew+')')

      elif n =='Bern5':
        if Ext:
          ws.factory('EDIT::'+fitExtNameNew+'('+fitExtName+','+normName+'='+normNameNew+','
                     +p0Name+'='+p0NameNew+','+p1Name+'='+p1NameNew+','+p2Name+'='+p2NameNew+','
                     +p3Name+'='+p3NameNew+','+p4Name+'='+p4NameNew+','+p5Name+'='+p5NameNew+')')
        else:
          ws.factory('EDIT::'+fitExtNameNew+'('+fitExtName+','
                     +p0Name+'='+p0NameNew+','+p1Name+'='+p1NameNew+','+p2Name+'='+p2NameNew+','
                     +p3Name+'='+p3NameNew+','+p4Name+'='+p4NameNew+','+p5Name+'='+p5NameNew+')')
      elif n =='Bern6':
        if Ext:
          ws.factory('EDIT::'+fitExtNameNew+'('+fitExtName+','+normName+'='+normNameNew+','
                     +p0Name+'='+p0NameNew+','+p1Name+'='+p1NameNew+','+p2Name+'='+p2NameNew+','
                     +p3Name+'='+p3NameNew+','+p4Name+'='+p4NameNew+','+p5Name+'='+p5NameNew+p6Name+'='+p6NameNew+')')
        else:
          ws.factory('EDIT::'+fitExtNameNew+'('+fitExtName+','
                     +p0Name+'='+p0NameNew+','+p1Name+'='+p1NameNew+','+p2Name+'='+p2NameNew+','
                     +p3Name+'='+p3NameNew+','+p4Name+'='+p4NameNew+','+p5Name+'='+p5NameNew+p6Name+'='+p6NameNew+')')

  BernNames = ['GaussBern4','GaussBern5']
  for n in BernNames:
    if n in fitName:
      suffix = '_'.join([year,lepton,'cat'+cat])
      if Ext: normName  = 'norm'+n+'_'+suffix
      meanName  = 'mean'+n+'_'+suffix
      sigmaName = 'sigma'+n+'_'+suffix
      stepName  = 'step'+n+'_'+suffix
      p0Name = 'p0'+n+'_'+suffix
      p1Name = 'p1'+n+'_'+suffix
      p2Name = 'p2'+n+'_'+suffix
      p3Name = 'p3'+n+'_'+suffix
      p4Name = 'p4'+n+'_'+suffix
      if n=="GaussBern5":
        p5Name = 'p5'+n+'_'+suffix
        if Ext: normNameNew  = '_'.join(['bkg',lepton,year,'cat'+cat,'norm'])
        meanNameNew  = '_'.join(['bkg','mean', lepton,year,'cat'+cat])
        sigmaNameNew = '_'.join(['bkg','sigma',lepton,year,'cat'+cat])
        stepNameNew  = '_'.join(['bkg','step', lepton,year,'cat'+cat])
        p0NameNew = '_'.join(['bkg','p0',lepton,year,'cat'+cat])
        p1NameNew = '_'.join(['bkg','p1',lepton,year,'cat'+cat])
        p2NameNew = '_'.join(['bkg','p2',lepton,year,'cat'+cat])
        p3NameNew = '_'.join(['bkg','p3',lepton,year,'cat'+cat])
        p4NameNew = '_'.join(['bkg','p4',lepton,year,'cat'+cat])
      if n=="GaussBern5":
        p5NameNew = '_'.join(['bkg','p5',lepton,year,'cat'+cat])

        if Ext: ws.factory(normNameNew+'[{0},{1},{2}]'.format(ws.function(normName).getVal(),
                                                      ws.function(normName).getMin(), ws.function(normName).getMax()))
        ws.factory(meanNameNew+'[{0}]'.format(ws.function(meanName).getVal()))
        ws.factory(sigmaNameNew+'[{0},{1},{2}]'.format(ws.function(sigmaName).getVal(),
                                                       ws.function(sigmaName).getMin(),ws.function(sigmaName).getMax()))
        ws.factory(stepNameNew+'[{0},{1},{2}]'.format(ws.function(stepName).getVal(),
                                                      ws.function(stepName).getMin(),ws.function(stepName).getMax()))
        ws.factory(p0NameNew+'[{0}]'.format(ws.function(p0Name).getVal()))
        ws.factory(p1NameNew+'[{0},{1},{2}]'.format(ws.function(p1Name).getVal(),
                                                    ws.function(p1Name).getMin(),ws.function(p1Name).getMax()))
        ws.factory(p2NameNew+'[{0},{1},{2}]'.format(ws.function(p2Name).getVal(),
                                                    ws.function(p2Name).getMin(),ws.function(p2Name).getMax()))
        ws.factory(p3NameNew+'[{0},{1},{2}]'.format(ws.function(p3Name).getVal(),
                                                    ws.function(p3Name).getMin(),ws.function(p3Name).getMax()))
        ws.factory(p4NameNew+'[{0},{1},{2}]'.format(ws.function(p4Name).getVal(),
                                                    ws.function(p4Name).getMin(),ws.function(p4Name).getMax()))
      if n=="GaussBern5":
        ws.factory(p5NameNew+'[{0},{1},{2}]'.format(ws.function(p5Name).getVal(),
                                                    ws.function(p5Name).getMin(),ws.function(p4Name).getMax()))

        if Ext:
          ws.factory('EDIT::'+fitExtNameNew+'('+fitExtName+','+meanName+'='+meanNameNew+','
                     +sigmaName+'='+sigmaNameNew+','+stepName+'='+stepNameNew+','+normName+'='+normNameNew+','
                     +p0Name+'='+p0NameNew+','+p1Name+'='+p1NameNew+','+p2Name+'='+p2NameNew+','
                     +p3Name+'='+p3NameNew+','+p4Name+'='+p4NameNew+','+p5Name+'='+p5NameNew+')')
        else:
          ws.factory('EDIT::'+fitExtNameNew+'('+fitExtName+','+meanName+'='+meanNameNew+','
                     +sigmaName+'='+sigmaNameNew+','+stepName+'='+stepNameNew+','
                     +p0Name+'='+p0NameNew+','+p1Name+'='+p1NameNew+','+p2Name+'='+p2NameNew+','
                     +p3Name+'='+p3NameNew+','+p4Name+'='+p4NameNew+','+p5Name+'='+p5NameNew+')')
      elif n=="GaussBern4":
        if Ext:
          ws.factory('EDIT::'+fitExtNameNew+'('+fitExtName+','+meanName+'='+meanNameNew+','
                     +sigmaName+'='+sigmaNameNew+','+stepName+'='+stepNameNew+','+normName+'='+normNameNew+','
                     +p0Name+'='+p0NameNew+','+p1Name+'='+p1NameNew+','+p2Name+'='+p2NameNew+','
                     +p3Name+'='+p3NameNew+','+p4Name+'='+p4NameNew+')')
        else:
          ws.factory('EDIT::'+fitExtNameNew+'('+fitExtName+','+meanName+'='+meanNameNew+','
                     +sigmaName+'='+sigmaNameNew+','+stepName+'='+stepNameNew+','
                     +p0Name+'='+p0NameNew+','+p1Name+'='+p1NameNew+','+p2Name+'='+p2NameNew+','
                     +p3Name+'='+p3NameNew+','+p4Name+'='+p4NameNew+')')


#myWs.Print()

def doBandsFit(onesigma, twosigma, hmass, cpdf, nomcurve, datanorm, plot, year, lepton):
  print '\n \t \t *** starting bands \n'
  nlim = RooRealVar("nlim","", 0, 0,100)
  print 'total steps needed:', plot.GetXaxis().GetNbins()
  oldhi = oldlo = 9999

  cpdf.Print()
  datanorm.Print()
  nomcurve.Print()

  raw_input('Enter')

  for i in range(1,plot.GetXaxis().GetNbins()+1):
    #r = TRandom(i)
    lowedge = plot.GetXaxis().GetBinLowEdge(i)
    upedge  = plot.GetXaxis().GetBinUpEdge(i)
    center  = plot.GetXaxis().GetBinCenter(i)
    nombkg  = nomcurve.interpolate(center)
    print 'bin number:', i, 'nombkg=', nombkg
    nlim.setVal(nombkg)

    #hmass.removeRange()
    #nlim.removeRange()
    nlim.setRange(nombkg*0.3, nombkg*3.0)
    hmass.setRange("errRange",lowedge,upedge)
    #hmass.Print()
    epdf = RooExtendPdf("epdf","",cpdf,nlim,"errRange")

    cl_one = 1.0 - 2.0*(RooStats.SignificanceToPValue(1.0))
    cl_two = 1.0 - 2.0*(RooStats.SignificanceToPValue(2.0))
    #print 'cl_one', cl_one, 'cl_two', cl_two
    onesigma.SetPoint(i-1,center,nombkg)
    tempi = i

    #nll = epdf.createNLL(datanorm)
    nll = epdf.createNLL(datanorm, RooFit.Extended())
    #nll.Print()
    minim = RooMinimizer(nll)
    minim.setErrorLevel(0.5*pow(ROOT.Math.normal_quantile(1-0.5*(1-cl_one),1.0),2)) #0.5 is because qmu is -2*NLL
    minim.setStrategy(2)
    #minim.setPrintLevel(-1)
    minim.migrad()
    minim.hesse()
    minim.minos(RooArgSet(nlim))
    onelo = -nlim.getErrorLo()
    onehi =  nlim.getErrorHi()
    val = nlim.getVal()

    onesigma.SetPointError(i-1,0.,0.,onelo,onehi)
    if fabs(onelo)<0.01:
      onesigma.SetPointError(i-1,0.,0.,onehi,onehi)
      onelo=onehi
    if fabs(onehi)<0.01:
      onesigma.SetPointError(i-1,0.,0.,onelo,onelo)
      onehi=onelo
    if(fabs(onelo) <0.01 and fabs(onehi)<0.01):
      onesigma.SetPointError(i-1,0.,0.,nlim.getError(),nlim.getError())
      onelo=nlim.getError()
      onehi=nlim.getError()

    print 'val=', val, 'one errHi', onehi, 'one errLo', onelo

    #minim.setErrorLevel(0.5*pow(ROOT.Math.normal_quantile(1-0.5*(1-cltwo),1.0),2)) #0.5 is because qmu is -2*NLL
    # eventually if cl = 0.95 this is the usual 1.92!
    twosigma.SetPoint(i-1,center,nombkg)
    twolo = 1.92*onelo
    twohi = 1.92*onehi
    twosigma.SetPointError(i-1,0.,0.,twolo,twohi)

    print 'two errHi', twohi, 'two errLo', twolo
  onesigma.Print("V")
  twosigma.Print("V")

  raw_input('Enter ')

for year in yearList:
  for lepton in leptonList:
    for cat in catList:
      dataName = '_'.join(['data',lepton,year,'cat'+cat])
      suffix   = '_'.join([year,lepton,'cat'+cat])
      print dataName, suffix

      fitName  = '_'.join([bkgModel,year,lepton,'cat'+cat])
      normName = 'norm'+bkgModel+'_'+suffix

      hPath    = cf.get("path","base")+"/batch_output/zgamma/8TeV/"+subdir
      sigFile_gg   = TFile(hPath+"/mugamma_"+year+"/hhhh_ggH-mad125_1.root", "OPEN")
      sigFile_vbf  = TFile(hPath+"/mugamma_"+year+"/hhhh_vbf-mad125_1.root", "OPEN")
      sigFile_vh   = TFile(hPath+"/mugamma_"+year+"/hhhh_vh-mad125_1.root", "OPEN")
      fsig= [sigFile_gg,sigFile_vbf,sigFile_vh]
      hsig = []
      for i,f in enumerate(fsig):
        Nev = f.Get("Counts/evt_byCut").GetBinContent(2)
        if i==0:
          cro = u.getCS("ggH-125",mySel='mu')
        elif i==1:
          cro = u.getCS("vbfH-125",mySel='mu')
        elif i==2:
          cro = u.getCS("vH-125",mySel='mu')
        lumi = u.getLumi("2012")
        scale = float(lumi*cro)/Nev
        print f.GetName(), cro,Nev,scale

        hsig.append(f.Get("tri_mass__cut10").Clone())
        hsig[-1].Scale(10*scale)
        #hsig[-1].Print("all")

      hsig[0].Add(hsig[1])
      hsig[0].Add(hsig[2])

      print fitName, dataName
      data = myWs.data(dataName)
      fit  = myWs.pdf(fitName)

      ###### Extend the fit (give it a normalization parameter)
      print dataName
      sumEntriesBkg = data.sumEntries()
      sumEntriesSig = data.sumEntries('1','signal')

      if verbose:
        print sumEntriesBkg, sumEntriesSig
        raw_input("sumEntriesBkg and sumEntriesSig")

      dataYieldName = '_'.join(['data','yield',lepton,year,'cat'+cat])
      dataYield     = RooRealVar(dataYieldName,dataYieldName,sumEntriesBkg)
      norm          = RooRealVar(normName,normName,sumEntriesBkg,sumEntriesBkg*0.25,sumEntriesBkg*1.75)

      fitExtName    = '_'.join(['bkgTmp',lepton,year,'cat'+cat])
      fit_ext       = RooExtendPdf(fitExtName,fitExtName, fit,norm)


      if verbose:
        print norm.getVal(), norm.getError()
        raw_input("norm.getVal(), norm.getError()")


      fit_result = RooFitResult(fit_ext.fitTo(data,RooFit.Range('DalitzRegion'), RooFit.Save()))
      # fit_ext.fitTo(data,RooFit.Range('DalitzRegion'), RooFit.Save())
      myBinning = 30
      binWidth = 2.

      testFrame = mzg.frame(RooFit.Range('DalitzRegion'))
      if doBlind:
        data.plotOn(testFrame, RooFit.Binning(myBinning), RooFit.Name('data'), RooFit.CutRange('r1'))
        data.plotOn(testFrame, RooFit.Binning(myBinning), RooFit.Name('data'), RooFit.CutRange('r2'))
      else:
        data.plotOn(testFrame, RooFit.Binning(myBinning), RooFit.Name('data'))


      fit_ext.plotOn(testFrame, RooFit.Name(bkgModel+"2sigma"),
                     RooFit.VisualizeError(fit_result,2), RooFit.FillColor(kCyan-10),RooFit.LineColor(kBlack))
      fit_ext.plotOn(testFrame, RooFit.Name(bkgModel+"1sigma"),
                     RooFit.VisualizeError(fit_result,1), RooFit.FillColor(kCyan-6), RooFit.LineColor(kBlack))
      fit_ext.plotOn(testFrame, RooFit.Name(bkgModel), RooFit.LineColor(kBlue), RooFit.LineWidth(2))
      fit_ext.paramOn(testFrame, RooFit.Layout(0.30,0.99,0.9))
      #fit_ext.statOn(testFrame)


      if verbose:
        print 'have unit norm?? ', sigP.haveUnitNorm()
        chi2 = testFrame.chiSquare(bkgModel,'data')
        chi2_4 = testFrame.chiSquare(4)
        print ' chiSquare=', chi2, chi2_4
        # print "Figuring out norms of PDFs",sigP.getVal(), sigP.analyticalIntegral()
        raw_input("pdf norm / chi2  ")


      '''
      onesigma = TGraphAsymmErrors()
      twosigma = TGraphAsymmErrors()
      tmpCurve = RooCurve(testFrame.findObject(bkgModel))
      doBandsFit(onesigma, twosigma, mzg, fit, tmpCurve, data, testFrame, year, lepton)
      twosigma.SetLineColor(kBlack)
      twosigma.SetFillColor(kCyan-10)
      onesigma.SetLineColor(kBlack)
      onesigma.SetFillColor(kCyan-6)
      twosigma.Draw("L3 same")
      onesigma.Draw("L3 same")
      '''

      if doBlind:
        data.plotOn(testFrame, RooFit.Binning(myBinning), RooFit.Name('data'), RooFit.CutRange('r1'))
        data.plotOn(testFrame, RooFit.Binning(myBinning), RooFit.Name('data'), RooFit.CutRange('r2'))
      else:
        data.plotOn(testFrame, RooFit.Binning(myBinning), RooFit.Name('data'))

      testFrame.SetMaximum(62)
      testFrame.Draw()
      hsig[0].SetAxisRange(115,135,"X")
      hsig[0].SetLineColor(kRed+1)
      hsig[0].SetLineWidth(2)
      hsig[0].Draw('same hist')


      testFrame.SetTitle(";m_{#mu#mu#gamma} (GeV);Events/"+str(binWidth)+" GeV")


      leg  = TLegend(0.53,0.65,0.93,0.87)
      leg.SetFillColor(0)
      leg.SetBorderSize(1)
      leg.AddEntry(testFrame.findObject(bkgModel),"Background Model",'l')
      leg.AddEntry(0,'','')
      leg.AddEntry(0,'','')
      leg.AddEntry(hsig[0],'Expected signal x10','l')
      leg.SetTextSize(0.045)
      #leg.Draw()

      leg2  = TLegend(0.55,0.72,0.91,0.8)
      leg2.SetNColumns(2)
      leg2.SetFillColor(0)
      leg2.SetBorderSize(0)
      leg2.AddEntry(testFrame.findObject(bkgModel+'1sigma'),"#pm 1 #sigma",'f')
      leg2.AddEntry(testFrame.findObject(bkgModel+'2sigma'),"#pm 2 #sigma",'f')
      leg2.SetTextSize(0.045)
      #leg2.Draw()

      prelim = TLatex()
      prelim.SetNDC();
      prelim.SetTextSize(0.045)
      prelim.SetTextFont(62)
      prelim.DrawLatex(0.15,0.95, ("CMS Preliminary"))
      prelim.DrawLatex(0.40,0.95, "#sqrt{s} = 8 TeV,  L = 19.7  fb^{-1}  H#rightarrow#gamma*#gamma#rightarrow#mu#mu#gamma")

      gPad.RedrawAxis()
      for e in ['.png', '.pdf']:
        c.SaveAs(plotBase+'/'+'_'.join(['best_fit',year,lepton,'cat'+cat])+e)

      ###### Import the fit and data, and rename them to the card convention
      dataNameNew = '_'.join(['data','obs',lepton,year,'cat'+cat])

      getattr(card_ws,'import')(data,RooFit.Rename(dataNameNew))
      if doExt:
        getattr(card_ws,'import')(fit_ext)
      else:
        getattr(card_ws,'import')(fit)
        normNameFixed = '_'.join(['bkg',lepton,year,'cat'+cat,'norm'])
        norm.SetName(normNameFixed)
        getattr(card_ws,'import')(norm)

      getattr(card_ws,'import')(dataYield)
      card_ws.commitTransaction()

      fit_ext.Print()
      fit.Print()
      print 'printing the WS before renaming!'
      card_ws.Print()

      #print normName
      BackgroundNameFixer(fitName, year,lepton,cat,card_ws, doExt)

      print 'Now print it After renaming'
      card_ws.Print()


      print "\n * The end * \n"

card_ws.writeToFile(subdir+'/testCardBackground_Dalitz.root')
