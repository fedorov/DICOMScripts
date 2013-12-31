import dicom, os, shutil, sys, string
from dicom.tag import Tag

# for each DICOM file in inputDir, set the content of the tagName
# to be the same as in the first file in that dir

if len(sys.argv)<4:
  print 'Usage: ',sys.argv[0],' inputDir tagName outputDir'
  exit

inputDir = sys.argv[1]
inputTag = sys.argv[2]
outputDir = sys.argv[3]

files = os.listdir(inputDir)
f = files[0]

dcm = dicom.read_file(os.path.join(inputDir,f))
dicom.write_file(os.path.join(outputDir,f),dcm)

firstVal = dcm.data_element(inputTag).value

for f in files[1:]:
  dcm = dicom.read_file(os.path.join(inputDir,f))
  dcm.data_element(inputTag).value = firstVal
  dicom.write_file(os.path.join(outputDir,f),dcm)
