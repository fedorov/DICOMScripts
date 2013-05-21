import dicom, os, shutil, sys, string
from dicom.tag import Tag

# input: directory with the DICOM files

inputDir = sys.argv[1]
project = sys.argv[2]
subject = sys.argv[3]
outputDir = sys.argv[4]

for r,d,files in os.walk(inputDir):
  for f in files:
    print 'Processing ', f
    inputFile = r+'/'+f
    dcm = dicom.read_file(inputFile)
    outputFile = outputDir+'/'+f

    pcTag = Tag(0x10,0x4000)
    time = string.split(dcm.StudyTime,'.')[0]
    dcm.add_new(pcTag,'LT',"Project: "+project+"; Subject: "+subject+"; Session: "+subject+"_"+dcm.StudyDate+"_"+time+';')

    print dcm.PatientComments

    f = open(outputFile,'wb')
    dicom.write_file(outputFile,dcm)
    # shutil.copyfile(inputFile, outputFile)
