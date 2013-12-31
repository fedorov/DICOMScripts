import dicom, os, shutil, sys

# input: directory with the DICOM files
# tag: which DICOM tag to use
# output: directory to store files organized by study UID

inputDir = sys.argv[1]
tag = sys.argv[2]
outputDir = sys.argv[3]

for f in os.listdir(inputDir):
  print 'Processing ', f
  inputFile = inputDir+'/'+f
  dcm = dicom.read_file(inputFile)  
  outputSubdir = outputDir+'/'+str(dcm.data_element(tag).value)
  outputFile = outputSubdir+'/'+f

  try:
    os.mkdir(outputSubdir)
  except:
    pass

  shutil.copyfile(inputFile, outputFile)
