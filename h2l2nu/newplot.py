#!/usr/bin/env python
import sys,os

from ROOT import *
import shutil
import datetime

from optparse import OptionParser
parser = OptionParser(usage="usage: %prog [options -e], -c 4], -m] vXX")
parser.add_option("-e", "--ele",   dest="ele", action="store_true", default=False, help="Use electron selection")
parser.add_option("-c", "--cut",   dest="cut", default="2", help="Cut number")
parser.add_option("-p", "--period",dest="period", default="2012", help="Year period; 2011 or 2012")
parser.add_option("-m", "--merge", action="store_true", dest="merge", default=False, help="Do merging?")

import config as c
import makePlots as mp


(options, args) = parser.parse_args()

nargs = len(sys.argv)

print sys.argv[0], "nargs:", nargs
if nargs < 2:
    print "Need to specify the path as v80 for example"
    parser.print_usage()
    exit(1)
            

plotNone = 0

plotSpecial  = 1
plotMVA      = 0
plotMet      = 1
plotJet      = 1
plotLepton   = 1
plotDiLepton = 1
plotMisc     = 1
plotMuons    = 1
plotElectrons= 1


sel = 1

doMerge = options.merge
F0      = options.cut    
ver     = sys.argv[1]
period = options.period
if options.ele:
    sel=2
print 'ver = ', ver, 'cut number = ', F0
    
hPath = '/eos/uscms/store/user/andreypz/batch_output/8TeV/'+ver
print hPath, sel, doMerge

def createDir(dir):
    try:
        os.makedirs(dir)
    except OSError:
        if os.path.isdir(dir):
            pass
        else:
            raise

baseHtmlDir = "/uscms_data/d2/andreypz/hzz2l2nu_html/"
#baseHtmlDir = "./"
subdir = ver+"_cut"+F0+"_"+period
dirNameOut = baseHtmlDir+subdir
selection  = ['muon', 'electron']

plot_types = []
if plotDiLepton:
    plot_types.append('diLepton')
if plotLepton:
    plot_types.append('Lepton')
if plotJet:
    plot_types.append('Jet')
if plotMet:
    plot_types.append('Met')
if plotSpecial:
    plot_types.append('Special')
if plotMuons:
    plot_types.append('Muons')
if plotElectrons:
    plot_types.append('Electrons')
if plotMisc:
    plot_types.append('Misc')
if plotMVA:
    plot_types.append('mvaPresel')

thissel = selection[sel-1]

for x in selection:
    for y in plot_types:
        createDir(dirNameOut+'/'+x+'/'+y)
        
timer = TStopwatch()	
timer.Start()

gROOT.SetBatch()
print "Merging?", doMerge
if doMerge:
    os.system("rm "+hPath+"/m_*"+thissel+"*.root") #removing the old merged files
    os.system("hadd "+hPath+"/m_Data_"    +thissel+"_"+period+".root "+hPath+"/"+thissel+"_"+period+"/hhhh_Double*.root")
    os.system("hadd "+hPath+"/m_ttbar_"   +thissel+"_"+period+".root "+hPath+"/"+thissel+"_"+period+"/hhhh_ttbar_*.root")
    os.system("hadd "+hPath+"/m_DYjets_"  +thissel+"_"+period+".root "+hPath+"/"+thissel+"_"+period+"/hhhh_DYjets_*.root")
    os.system("hadd "+hPath+"/m_DYjets10_"+thissel+"_"+period+".root "+hPath+"/"+thissel+"_"+period+"/hhhh_DYjets10_*.root")
    os.system("hadd "+hPath+"/m_vbfZ_"    +thissel+"_"+period+".root "+hPath+"/"+thissel+"_"+period+"/hhhh_vbfZ_*.root")
                


if plotNone:
    mp.makePlots(sel, dirNameOut, ver, F0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
else:
    mp.makePlots(sel, dirNameOut, ver, F0, plotMuons, plotElectrons, plotSpecial, plotMVA, plotMet, plotJet, plotLepton, plotDiLepton, plotMisc)

print "\n\nDone!"
print "CPU Time : ", timer.CpuTime()
print "RealTime : ", timer.RealTime()  


print "\n\n ******** Now making HTML pages ******** \n"
menu=""

for x in plot_types:
    fname = x+".html"
    imgfile = open(fname,"w")
    imgfile.write("<html><head><title>"+x+"</title></head><body>\n")
    fileList = {}
    for s in selection:
        fileList[s] = os.listdir(dirNameOut+'/'+s+'/'+x)
    #print x,fileList

    if x =="Muons":
        count =1
        mod =1
        for pl in  sorted(fileList["muon"]):
            mod = count % 2
            if mod==1: imgfile.write('<nobr><img src=muon/'+x+'/'+pl+' width=47%>')
            if mod==0: imgfile.write('      <img src=muon/'+x+'/'+pl+' width=47%></nobr>\n')
            count+=1
        if mod==0: imgfile.write("")
        if mod==1: imgfile.write("</nobr>")
    elif x =="Electrons":
        count =1
        mod =1
        for pl in  sorted(fileList["electron"]):
            mod = count % 2
            if mod==1: imgfile.write('<nobr><img src=electron/'+x+'/'+pl+' width=47%>')
            if mod==0: imgfile.write('      <img src=electron/'+x+'/'+pl+' width=47%></nobr>\n')
            count+=1
        if mod==0: imgfile.write("")
        if mod==1: imgfile.write("</nobr>")
    else:
        nmu  = len(fileList["muon"])
        nele = len(fileList["electron"])
        if (nmu!=0 and fileList["muon"]==fileList["electron"]):
            for pl in  sorted(fileList["muon"]):
                imgfile.write('<nobr><img src=muon/'+x+'/'+pl+' width=47%>')
                imgfile.write('    <img src=electron/'+x+'/'+pl+' width=47%></nobr>\n') 
        elif(nmu!=0 and  nele!=0 and fileList["muon"]!=fileList["electron"]):
            print "Something is wrong: muons and electrons are not symmetric!"
        elif(nmu!=0 and nele==0):
            count =1
            mod =1
            for pl in  sorted(fileList["muon"]):
                mod = count % 2
                if mod==1: imgfile.write('<nobr><img src=muon/'+x+'/'+pl+' width=47%>')
                if mod==0: imgfile.write('      <img src=muon/'+x+'/'+pl+' width=47%></nobr>\n')
                count+=1
            if mod==0: imgfile.write("")
            if mod==1: imgfile.write("</nobr>")
        elif(nmu==0):
            print "No plots in", x
        

    imgfile.write("</body></html>")
    imgfile.close()
    os.system("mv "+fname+" "+dirNameOut)
    menu = menu+"<li><a href=\""+x+".html\" target=\"iframe_a\">"+x+"</a></li>"

menu += '<li><a href="yields_muon_2012.html" target="iframe_a">Yields mu</a></li>'
menu += '<li><a href="yields_electron_2012.html" target="iframe_a">Yields ele</a></li>'
#print menu


today = datetime.date.today()
print today

message = '<h2>Comments</h2>\
<ul><li><font color ="dark-blue">Most of the plots are made after cut #<font size="+1"><b>'+F0+'</b></font> from the list of cuts</font></li>\
<li>Top samlpe is a tW + tbarW</li>\
<li>DY samlpe is a combination of DY10_40 and DY_40_inf</li>\
</ul>'

tempfile = open("indextemplate.html","r")
whole_thing = tempfile.read()
whole_thing = whole_thing.replace("{MENU}", menu)
whole_thing = whole_thing.replace("{DATE}", str(today))
whole_thing = whole_thing.replace("{ASIDEMESSAGE}", str(message))
tempfile.close()

ifile = open("index.html","w")
ifile.write(whole_thing)
ifile.close()

print "\n\n *** End of  making HTML pages - all done *** \n"

os.system("mv index.html "+dirNameOut)
os.system("mv yields* "+dirNameOut)
