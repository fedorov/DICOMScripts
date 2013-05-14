import dicom, os, shutil, sys

# input: directory with the DICOM files
# output: directory to store files organized by study UID

inputDir = sys.argv[1]
outputDir = sys.argv[2]

for f in os.listdir(inputDir):
  print 'Processing ', f
  inputFile = inputDir+'/'+f
  dcm = dicom.read_file(inputFile)  
  outputSubdir = outputDir+'/'+dcm.StudyInstanceUID
  outputFile = outputSubdir+'/'+f

  try:
    os.mkdir(outputSubdir)    
  except:
    pass

  shutil.copyfile(inputFile, outputFile)
