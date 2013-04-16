#!/bin/csh
source /uscmst1/prod/sw/cms/cshrc prod
scram pro CMSSW CMSSW_4_4_4
cd CMSSW_4_4_4/src
cmsenv 

#### Leave this blank #######

#############################

set outDir    = $1
set count     = $2
set dataName  = $3  #e.g. Photon_Aug05, Run2011B , May10

### Specify addtional arguments here ####
set suffix    = $4  #e.g. DATA. WZ, ZZ etc
set selection = $5
set period    = $6

set dir = ${outDir}/code_dir

echo "Copy all files needed from a working directory" $dir
cd ../
cp -r $dir/* .


cd higgs
mv ../src/input.txt .

#echo 'ls in higgs'
#ls

chmod 755 run.py

#./run.py ${suffix} ${dataName} -p ${period} -b
echo $selection
if ( $selection == "electron" ) then
    echo "Electrons"
    #./run.py ${suffix} ${dataName} --ele -p ${period} -b
else
    echo "Muons"
    ./run.py ${suffix} ${dataName} -p ${period} -b
endif

echo 'ls in higgs'
ls

echo "Done. copying files"
cp hhhh_${dataName}.root $outDir/$selection/hhhh_${dataName}_${count}.root
#cp  events_printout_* $outDir/$selection/printouts/
